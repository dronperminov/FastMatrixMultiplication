import argparse
import os
import random
from dataclasses import dataclass
from fractions import Fraction
from typing import Tuple, List, Callable, Optional

import numpy as np
import torch
import torch.nn.functional as F

from src.schemes.scheme import Scheme


@dataclass
class OptimizationParameters:
    end_part: float
    learning_rate: float
    w_int: Callable[[float], float]
    w_sparse: Callable[[float], float]
    w_magnitude: Callable[[float], float]
    w_balance: Callable[[float], float]


class TrainStrategy:
    def __init__(self, label: str, scales: List[int], p_als: float = 0.0, p_round: float = 0.0, int_type: str = "sin") -> None:
        self.label = label
        self.scales = scales
        self.p_als = p_als
        self.p_round = p_round
        self.int_type = int_type
        self.parameters: List[OptimizationParameters] = []

    def add(self, parameters: OptimizationParameters):
        self.parameters.append(parameters)

    def get(self, step: int, steps: int) -> Optional[Tuple[OptimizationParameters, float]]:
        start_step = 0

        for parameters in self.parameters:
            end_step = int(parameters.end_part * steps)
            if step < end_step:
                t = (step - start_step) / (end_step - start_step)
                return parameters, t

            start_step = end_step

        return None


class GradientDecomposition:
    def __init__(self, n: int, m: int, p: int, rank: int, batch_size: int, device: str, T: torch.Tensor) -> None:
        self.dimension = [n, m, p]
        self.elements = [n * m, m * p, p * n]
        self.rank = rank
        self.batch_size = batch_size
        self.device = torch.device(device)

        self.T = T
        self.norm = self.T.norm().item()

        self.Tu = self.T.reshape(self.elements[0], -1)
        self.Tv = self.T.permute(1, 0, 2).reshape(self.elements[1], -1)
        self.Tw = self.T.permute(2, 0, 1).reshape(self.elements[2], -1)

        self.u = torch.zeros(batch_size, self.elements[0], self.rank, dtype=torch.float64, device=self.device)
        self.v = torch.zeros(batch_size, self.elements[1], self.rank, dtype=torch.float64, device=self.device)
        self.w = torch.zeros(batch_size, self.elements[2], self.rank, dtype=torch.float64, device=self.device)

    def initialize_coefficients(self, methods: List[str]) -> None:
        for i in range(self.batch_size):
            ui, vi, wi = self.__init_coefficients(method=random.choice(methods))
            self.u[i] = ui.detach()
            self.v[i] = vi.detach()
            self.w[i] = wi.detach()

        self.u.requires_grad_(True)
        self.v.requires_grad_(True)
        self.w.requires_grad_(True)

    def clone_coefficients(self, decomposition: "GradientDecomposition") -> None:
        self.u = decomposition.u.detach().clone().requires_grad_(True)
        self.v = decomposition.v.detach().clone().requires_grad_(True)
        self.w = decomposition.w.detach().clone().requires_grad_(True)

    def get_rounded_coefficients(self, scale: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        with torch.no_grad():
            u = torch.round(self.u * scale) / scale
            v = torch.round(self.v * scale) / scale
            w = torch.round(self.w * scale) / scale

        return u, v, w

    def als(self) -> None:
        with torch.no_grad():
            u, v, w = self.__least_squares()
            self.u.data = u
            self.v.data = v
            self.w.data = w

    def round(self, scale: int):
        with torch.no_grad():
            u, v, w = self.get_rounded_coefficients(scale=scale)
            self.u.data = u
            self.v.data = v
            self.w.data = w

    def __init_coefficients(self, method: str) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        if method == "normal":
            u, v, w = self.__init_coefficients_normal()
        elif method == "sparse":
            u, v, w = self.__init_coefficients_sparse()
        elif method == "uniform":
            u, v, w = self.__init_coefficients_uniform()
        else:
            raise ValueError(f"Unknown method {method}")

        return u, v, w

    def __init_coefficients_normal(self) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        scale = 0.3 * (self.norm / self.rank) ** (1 / 3)
        u = torch.randn(self.elements[0], self.rank, dtype=torch.float64, device=self.device) * scale
        v = torch.randn(self.elements[1], self.rank, dtype=torch.float64, device=self.device) * scale
        w = torch.randn(self.elements[2], self.rank, dtype=torch.float64, device=self.device) * scale
        return u, v, w

    def __init_coefficients_sparse(self) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        u = torch.zeros(self.elements[0], self.rank, dtype=torch.float64, device=self.device)
        v = torch.zeros(self.elements[1], self.rank, dtype=torch.float64, device=self.device)
        w = torch.zeros(self.elements[2], self.rank, dtype=torch.float64, device=self.device)

        for index in range(self.rank):
            for matrix, elements in [(u, self.elements[0]), (v, self.elements[1]), (w, self.elements[2])]:
                count = np.random.randint(1, min(4, elements + 1))
                idx = np.random.choice(elements, count, replace=False)
                values = np.random.choice([-1.0, 1.0], count)
                matrix[idx, index] = torch.tensor(values, dtype=torch.float64, device=self.device)

        u += torch.randn_like(u) * 0.1
        v += torch.randn_like(v) * 0.1
        w += torch.randn_like(w) * 0.1
        return u, v, w

    def __init_coefficients_uniform(self) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        u = (torch.rand(self.elements[0], self.rank, dtype=torch.float64, device=self.device) - 0.5) * 4.0
        v = (torch.rand(self.elements[1], self.rank, dtype=torch.float64, device=self.device) - 0.5) * 4.0
        w = (torch.rand(self.elements[2], self.rank, dtype=torch.float64, device=self.device) - 0.5) * 4.0
        return u, v, w

    def __optimize_als_batch(self, v: torch.Tensor, w: torch.Tensor, T: torch.Tensor, lambda_reg: float = 1e-7) -> torch.Tensor:
        vw = torch.einsum('bik,bjk->bijk', v, w).reshape(self.batch_size, -1, self.rank)
        a = torch.einsum('bri,brj->bij', vw, vw)
        b = torch.einsum('ij,bjk->bik', T, vw)
        eye = torch.eye(self.rank, device=self.device).unsqueeze(0)
        u = torch.linalg.solve(a + lambda_reg * eye, b.permute(0, 2, 1))
        return u.permute(0, 2, 1)

    def __least_squares(self) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        variant1 = random.randint(0, 2)
        variant2 = random.randint(0, 1)

        if variant1 == 0:
            u_new = self.__optimize_als_batch(self.v, self.w, self.Tu)

            if variant2 == 0:
                v_new = self.__optimize_als_batch(u_new, self.w, self.Tv)
                w_new = self.__optimize_als_batch(u_new, v_new, self.Tw)
            else:
                w_new = self.__optimize_als_batch(u_new, self.v, self.Tw)
                v_new = self.__optimize_als_batch(u_new, w_new, self.Tv)
        elif variant1 == 1:
            v_new = self.__optimize_als_batch(self.u, self.w, self.Tv)

            if variant2 == 0:
                u_new = self.__optimize_als_batch(v_new, self.w, self.Tu)
                w_new = self.__optimize_als_batch(u_new, v_new, self.Tw)
            else:
                w_new = self.__optimize_als_batch(self.u, v_new, self.Tw)
                u_new = self.__optimize_als_batch(v_new, w_new, self.Tu)
        else:
            w_new = self.__optimize_als_batch(self.u, self.v, self.Tw)

            if variant2 == 0:
                u_new = self.__optimize_als_batch(self.v, w_new, self.Tu)
                v_new = self.__optimize_als_batch(u_new, w_new, self.Tv)
            else:
                v_new = self.__optimize_als_batch(self.u, w_new, self.Tv)
                u_new = self.__optimize_als_batch(v_new, w_new, self.Tu)

        return u_new, v_new, w_new


class GradientDecompositionTrainer:
    def __init__(self, decomposition: GradientDecomposition, strategy: TrainStrategy, learning_rate: float, max_abs_value: float) -> None:
        self.decomposition = decomposition
        self.strategy = strategy
        self.batch_size = decomposition.batch_size
        self.device = decomposition.device
        self.learning_rate = learning_rate
        self.max_abs_value = max_abs_value

        self.optimizer = torch.optim.Adam([decomposition.u, decomposition.v, decomposition.w], lr=learning_rate)
        self.verified = {"ZT": 0, "Z": 0, "Q": 0}
        self.complexities = []
        self.buds = []

        self.best_errors = torch.full((self.batch_size,), float('inf'), dtype=torch.float64, device=self.device)
        self.verified_mask = torch.zeros(self.batch_size, dtype=torch.bool, device=self.device)

    def train(self, step: int, steps: int) -> float:
        self.optimizer.zero_grad()
        step_parameters = self.strategy.get(step=step, steps=steps)
        self.__update_learning_rate(step_parameters[0].learning_rate if step_parameters else self.learning_rate)

        loss = self.__reconstruction_loss(self.decomposition.u, self.decomposition.v, self.decomposition.w)
        if step_parameters:
            loss += self.__get_regularization_loss(parameters=step_parameters[0], t=step_parameters[1])

        loss = loss.sum()
        loss.backward()
        torch.nn.utils.clip_grad_norm_([self.decomposition.u, self.decomposition.v, self.decomposition.w], max_norm=5.0)
        self.optimizer.step()
        return loss.item() / self.batch_size

    def check(self, output_dir: str, p_als: float, p_round: float) -> None:
        for scale in self.strategy.scales:
            self.__check_rationalization(output_dir=output_dir, scale=scale)

        if p_als < self.strategy.p_als:
            self.decomposition.als()

            for scale in self.strategy.scales:
                self.__check_rationalization(output_dir=output_dir, scale=scale)

        if p_round < self.strategy.p_round:
            self.decomposition.round(2)

    def print_status(self, epoch: int, step: int, loss: float) -> None:
        u, v, w = self.decomposition.u, self.decomposition.v, self.decomposition.w
        label = self.strategy.label
        recon_loss = self.__reconstruction_loss(u, v, w).mean().item()
        int_loss = self.__integrality_loss(u, v, w, int_type=self.strategy.int_type).mean().item()
        sparsity_loss = self.__sparsity_loss(u, v, w).mean().item()
        mag_loss = self.__magnitude_loss(u, v, w).mean().item()
        balance_loss = self.__balance_loss(u, v, w).mean().item()
        verified = sum(self.verified.values())

        print(f"| {label:28} | {epoch:5} | {step:6} | {loss:11.6f} | {recon_loss:14.6f} | {int_loss:11.2f} | {sparsity_loss:8.2f} | {mag_loss:9.6f} | {balance_loss:9.6f} | {verified} ({self.verified})")

    def __check_rationalization(self, output_dir: str, scale: int, eps: float = 1e-10) -> None:
        u, v, w = self.decomposition.get_rounded_coefficients(scale=scale)
        errors = self.__reconstruction_loss(u, v, w)

        improved_mask = errors < self.best_errors
        if not improved_mask.any():
            return

        self.best_errors[improved_mask] = errors[improved_mask]
        verify_mask = (self.best_errors < eps) & (~self.verified_mask)

        if verify_mask.any():
            self.__verify(u, v, w, mask=verify_mask, output_dir=output_dir)

    def __verify(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor, mask: torch.Tensor, output_dir: str) -> None:
        for index in mask.nonzero(as_tuple=True)[0]:
            scheme = self.__to_scheme(u[index], v[index], w[index])
            if not scheme.validate():
                mask[index] = 0
                continue

            self.__save_scheme(scheme, output_dir=output_dir)
            self.verified[scheme.get_ring()] += 1
            self.complexities.append(scheme.complexity())
            self.buds.append(len(scheme.get_buds()))

        self.verified_mask |= mask

    def __update_learning_rate(self, learning_rate: float) -> None:
        for g in self.optimizer.param_groups:
            g["lr"] = learning_rate

    def __get_regularization_loss(self, parameters: OptimizationParameters, t: float) -> torch.Tensor:
        loss = 0.0
        u, v, w = self.decomposition.u, self.decomposition.v, self.decomposition.w

        w_int = parameters.w_int(t)
        if w_int != 0:
            loss += w_int * self.__integrality_loss(u, v, w, int_type=self.strategy.int_type)

        w_sparse = parameters.w_sparse(t)
        if w_sparse != 0:
            loss += w_sparse * self.__sparsity_loss(u, v, w)

        w_magnitude = parameters.w_magnitude(t)
        if w_magnitude != 0:
            loss += w_magnitude * self.__magnitude_loss(u, v, w)

        w_balance = parameters.w_balance(t)
        if w_balance != 0:
            loss += w_balance * self.__balance_loss(u, v, w)

        return loss

    def __reconstruction_loss(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        residual = self.decomposition.T.unsqueeze(0) - torch.einsum("bir,bjr,bkr->bijk", u, v, w)
        return (residual ** 2).flatten(start_dim=1).sum(dim=1)

    def __integrality_loss(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor, int_type: str) -> torch.Tensor:
        if int_type == "sin":
            return self.__integrality_loss_sin(u, v, w)

        if int_type == "round":
            return self.__integrality_loss_round(u, v, w)

        if int_type == "ternarization_l1" or int_type == "tern_l1":
            return self.__integrality_loss_ternarization_l1(u, v, w)

        if int_type == "ternarization_l2" or int_type == "tern_l2":
            return self.__integrality_loss_ternarization_l2(u, v, w)

        raise ValueError(f"Unknown integrality loss type ({int_type})")

    def __integrality_loss_sin(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        loss = 0.0
        for matrix in [u, v, w]:
            loss += (torch.sin(np.pi * matrix) ** 2).flatten(start_dim=1).sum(dim=1)

        return loss

    def __integrality_loss_round(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        loss = 0.0
        for matrix in [u, v, w]:
            loss += torch.abs(matrix - torch.round(matrix)).flatten(start_dim=1).sum(dim=1)

        return loss

    def __integrality_loss_ternarization_l1(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        loss = 0.0
        for matrix in [u, v, w]:
            w = torch.abs(matrix)
            wp = torch.abs(matrix - 1)
            wn = torch.abs(matrix + 1)
            loss += (w*wp*wn).flatten(start_dim=1).sum(dim=1)

        return loss

    def __integrality_loss_ternarization_l2(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        loss = 0.0
        for matrix in [u, v, w]:
            w = matrix ** 2
            wp = (matrix - 1) ** 2
            wn = (matrix + 1) ** 2
            loss += (w*wp*wn).flatten(start_dim=1).sum(dim=1)

        return loss

    def __sparsity_loss(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor, eps: float = 1e-4) -> torch.Tensor:
        loss = 0.0
        for matrix in [u, v, w]:
            loss += (torch.sqrt(matrix ** 2 + eps ** 2) - eps).flatten(start_dim=1).sum(dim=1)
        return loss

    def __magnitude_loss(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        loss = 0.0
        for matrix in [u, v, w]:
            loss += (F.relu(matrix.abs() - self.max_abs_value) ** 2).flatten(start_dim=1).sum(dim=1)
        return loss

    def __balance_loss(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
        norm_u = (u ** 2).sum(dim=1)
        norm_v = (v ** 2).sum(dim=1)
        norm_w = (w ** 2).sum(dim=1)
        mean = (norm_u * norm_v * norm_w).clamp(min=1e-8) ** (1 / 3)

        loss = 0.0
        for norm, target in [(norm_u, 1.0), (norm_v, 1.2), (norm_w, 0.9)]:
            loss += ((norm / mean - target) ** 2).sum(dim=1)
        return loss

    def __to_scheme(self, u: torch.Tensor, v: torch.Tensor, w: torch.Tensor) -> Scheme:
        u = [[Fraction(u[i, index].item()) for i in range(self.decomposition.elements[0])] for index in range(self.decomposition.rank)]
        v = [[Fraction(v[i, index].item()) for i in range(self.decomposition.elements[1])] for index in range(self.decomposition.rank)]
        w = [[Fraction(w[i, index].item()) for i in range(self.decomposition.elements[2])] for index in range(self.decomposition.rank)]

        n, m, p = self.decomposition.dimension
        return Scheme(n, m, p, self.decomposition.rank, u=u, v=v, w=w, z2=False, validate=False)

    def __save_scheme(self, scheme: Scheme, output_dir: str) -> None:
        ring = scheme.get_ring()
        buds = scheme.get_buds()
        buds = [sum(1 for p, i, j in buds if p == q) for q in range(3)]
        complexity = scheme.complexity()
        values = ", ".join(f"{int(v)}" if v.denominator == 1 else f"{v.numerator}/{v.denominator}" for v in scheme.get_coefficient_set())
        filename = f"{scheme.n[0]}x{scheme.n[1]}x{scheme.n[2]}_m{scheme.m}_c{complexity}_b{buds[0]}-{buds[1]}-{buds[2]}_{ring}.json"
        print(f"{self.strategy.label}: new verified scheme, {buds} buds, complexity: {complexity}, values: {{{values}}}")
        scheme.save(f"{output_dir}/{filename}")


class GradientDecompositionOptimizer:
    def __init__(self, n: int, m: int, p: int, rank: int, batch_size: int, device: str, output_dir: str, max_abs_value: float):
        self.n = n
        self.m = m
        self.p = p
        self.rank = rank
        self.batch_size = batch_size
        self.device = device
        self.output_dir = output_dir
        self.max_abs_value = max_abs_value

        self.T = self.__get_target_tensor()
        self.strategies = []

    def add_strategy(self, strategy: TrainStrategy) -> None:
        self.strategies.append(strategy)

    def optimize(self, initialization_count: int, learning_rate: float, steps: int, period: int, methods: List[str]) -> None:
        decompositions = self.__init_decompositions(count=initialization_count, methods=methods)
        trainers = self.__init_trainers(decompositions=decompositions, learning_rate=learning_rate)
        epoch = 0

        while True:
            epoch += 1

            print(f"\nStart epoch {epoch}")

            for step in range(steps):
                log_step = step % period == 0 or step == steps - 1

                if log_step:
                    print("\n|           strategy           | epoch |  step  |    total    | reconstruction | integrality | sparsity | magnitude |  balance  | verified")

                p_als, p_round = random.random(), random.random()
                for trainer in trainers:
                    loss = trainer.train(step, steps=steps)
                    trainer.check(output_dir=self.output_dir, p_als=p_als, p_round=p_round)

                    if log_step:
                        if trainer.strategy == self.strategies[0]:
                            print("+------------------------------+-------+--------+-------------+----------------+-------------+----------+-----------+-----------+-----------------------------------")
                        trainer.print_status(epoch, step, loss)

            self.__print_statistics(epoch=epoch, trainers=trainers)

    def __get_target_tensor(self) -> torch.Tensor:
        tensor = torch.zeros((self.n * self.m, self.m * self.p, self.p * self.n), dtype=torch.float64).to(self.device)

        for i in range(self.n):
            for j in range(self.p):
                for k in range(self.m):
                    tensor[i * self.m + k, k * self.p + j, j * self.n + i] = 1.0

        return tensor

    def __init_decompositions(self, count: int, methods: List[str]) -> List[GradientDecomposition]:
        decompositions = [GradientDecomposition(self.n, self.m, self.p, self.rank, self.batch_size, self.device, self.T) for _ in range(count)]

        for decomposition in decompositions:
            decomposition.initialize_coefficients(methods=methods)

        return decompositions

    def __init_trainers(self, decompositions: List[GradientDecomposition], learning_rate: float) -> List[GradientDecompositionTrainer]:
        trainers = []

        for decomposition in decompositions:
            for strategy in self.strategies:
                strategy_decomposition = GradientDecomposition(self.n, self.m, self.p, self.rank, self.batch_size, self.device, self.T)
                strategy_decomposition.clone_coefficients(decomposition)
                trainers.append(GradientDecompositionTrainer(strategy_decomposition, strategy, learning_rate=learning_rate, max_abs_value=self.max_abs_value))

        return trainers

    def __print_statistics(self, epoch: int, trainers: List[GradientDecompositionTrainer]) -> None:
        print(f"\nEpoch {epoch} statistic")
        print("|           strategy           | mean round error | min round error | complexity (mean / min) | buds (mean / max) | verified")
        print("+------------------------------+------------------+-----------------+-------------------------+-------------------+-------------------------")

        for strategy in self.strategies:
            verified = {"ZT": 0, "Z": 0, "Q": 0}
            complexities = []
            buds = []

            sum_error = 0
            min_error = float("+inf")
            count = 0

            for trainer in trainers:
                if trainer.strategy != strategy:
                    continue

                for ring, count in trainer.verified.items():
                    verified[ring] += count

                complexities.extend(trainer.complexities)
                buds.extend(trainer.buds)
                sum_error += trainer.best_errors.sum()
                count += trainer.best_errors.shape[0]

                greater_zero_mask = trainer.best_errors > 0.0
                if greater_zero_mask.any():
                    min_error = min(min_error, trainer.best_errors[greater_zero_mask].min())

            mean_complexity = sum(complexities) / max(len(complexities), 1)
            min_complexity = min(complexities, default=None)
            complexity = f"{mean_complexity:.1f} / {min_complexity}"

            mean_buds = sum(buds) / max(len(buds), 1)
            max_buds = max(buds, default=None)
            buds = f"{mean_buds:.1f} / {max_buds}"

            mean_error = sum_error / count
            verified_count = sum(verified.values())
            print(f"| {strategy.label:28} | {mean_error:16.6f} | {min_error:15.6f} | {complexity:23} | {buds:17} | {verified_count} ({verified})")


def get_strategies(learning_rate: float) -> List[TrainStrategy]:
    strategies = []

    balance_only = OptimizationParameters(
        end_part=0.4,
        learning_rate=learning_rate,
        w_int=lambda t: 0,
        w_sparse=lambda t: 0,
        w_balance=lambda t: 0.01,
        w_magnitude=lambda t: 0
    )

    for p_als in [0.1, 0.4]:
        for p_round in [0.0, 0.01]:
            for int_type in ["sin", "round", "tern_l1", "tern_l2"]:
                strategy = TrainStrategy(label=f"{int_type} (als: {p_als}, r: {p_round})", scales=[1, 2], p_als=p_als, p_round=p_round, int_type=int_type)

                strategy.add(balance_only)
                strategy.add(OptimizationParameters(
                    end_part=1.0,
                    learning_rate=learning_rate,
                    w_int=lambda t: 0.3 * t * t,
                    w_sparse=lambda t: 0.05 * t,
                    w_balance=lambda t: 0.01,
                    w_magnitude=lambda t: 0.1 * t
                ))
                strategies.append(strategy)

    return strategies

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="n", type=int, default=3)
    parser.add_argument("-m", help="m", type=int, default=3)
    parser.add_argument("-p", help="p", type=int, default=3)
    parser.add_argument("--rank", help="decomposition rank", type=int, default=23)
    parser.add_argument("--device", help="torch device", type=str, default="cuda")
    parser.add_argument("--batch-size", help="batch size", type=int, default=256)
    parser.add_argument("--learning-rate", help="learning rate", type=int, default=0.1)
    parser.add_argument("--steps", help="steps per epoch", type=int, default=2000)
    parser.add_argument("--period", help="check period", type=int, default=100)
    parser.add_argument("--initialization-count", help="number of different coefficient initializations", type=int, default=10)
    parser.add_argument("--max-abs-value", help="max absolute value", type=float, default=3.0)
    parser.add_argument("-o", "--output-dir", help="directory for save discovered schemes", type=str, default="data/gradient_schemes")
    args = parser.parse_args()

    n, m, p = args.n, args.m, args.p
    rank = args.rank
    batch_size = args.batch_size
    device = args.device
    initialization_count = args.initialization_count
    learning_rate = args.learning_rate
    steps = args.steps
    period = args.period
    methods = ["normal", "sparse", "uniform"]
    output_dir = f"data/gradient_schemes/{n}x{m}x{p}/rank{rank}"
    max_abs_value = args.max_abs_value
    os.makedirs(output_dir, exist_ok=True)

    optimizer = GradientDecompositionOptimizer(n, m, p, rank, batch_size=batch_size, device=device, output_dir=output_dir, max_abs_value=max_abs_value)

    for strategy in get_strategies(learning_rate=learning_rate):
        optimizer.add_strategy(strategy=strategy)

    optimizer.optimize(initialization_count=initialization_count, learning_rate=learning_rate, steps=steps, period=period, methods=methods)


if __name__ == '__main__':
    main()
