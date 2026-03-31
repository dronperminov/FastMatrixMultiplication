import itertools
import math
from functools import lru_cache
from typing import List, Tuple

from src.utils.find_root import find_root_bisection, find_root_newton


class StructureDepthOptimizer:
    def __init__(self, n: int, m: int, p: int, structure: List[Tuple[int, Tuple[int, int, int]]], eps: float = 1e-15) -> None:
        self.n = n
        self.m = m
        self.p = p
        self.structure = structure
        self.structure_normalized = [(si, (ni / n, mi / m, pi / p)) for si, (ni, mi, pi) in self.structure]
        self.eps = eps
        self.T = lru_cache(maxsize=None)(self.__T)
        self.get_heuristic = lru_cache(maxsize=None)(self.__get_heuristic)

        self.rank = sum(si * ni * mi * pi for si, (ni, mi, pi) in structure)
        self.omega = 3*math.log(self.rank) / math.log(n*m*p)
        self.structure_omega = find_root_bisection(self.f0, 2.5, 3.0, eps=eps)
        self.limit_omega = find_root_bisection(self.f_inf, 2.0, 3.0, eps=eps)
        self.w1, self.w2, self.w3 = self.__get_exponents()

    def show(self) -> None:
        print(f"- dimension: {self.n}x{self.m}x{self.p}")
        print(f"- structure: {self.structure}")
        print(f"- rank: {self.rank}")
        print(f"- omega (rank): {self.omega:.15f}")
        print(f"- omega (structure): {self.structure_omega:.15f}")
        print(f"- omega (limit): {self.limit_omega:.15f}")
        print(f"- eps: {self.eps}")
        print(f"- w1: {self.w1}")
        print(f"- w2: {self.w2}")
        print(f"- w3: {self.w3}")
        print("")

    def optimize(self, depth: int, x0: float = 2.8) -> float:
        return find_root_newton(lambda w: self.f(w, depth=depth), x0=x0, eps=self.eps)

    def __T(self, a: float, b: float, c: float, w: float, depth: int) -> Tuple[float, float]:
        if depth == 0:
            fx = a ** (w - 2) * b * c + a * b ** (w - 2) * c + a * b * c ** (w - 2)
            df = math.log(a) * a ** (w - 2) * b * c + a * math.log(b) * b ** (w - 2) * c + a * b * math.log(c) * c ** (w - 2)
            return fx, df

        if a == b == c and a < 1:
            return 3 * a ** w, 3 * math.log(a) * a ** w

        best_i = self.get_heuristic(a=a, b=b, c=c)
        v_fx, v_df = 0, 0
        for si, (ni, mi, pi) in self.structure_normalized:
            n, m, p = list(itertools.permutations([ni, mi, pi], r=3))[best_i]
            args = sorted([a * n, b * m, c * p])
            fx, df = self.T(a=args[0], b=args[1], c=args[2], w=w, depth=depth - 1)
            v_fx += si * fx
            v_df += si * df

        return v_fx, v_df

    def f(self, w: float, depth: int) -> Tuple[float, float]:
        fx, df = self.T(1.0, 1.0, 1.0, w=w, depth=depth)
        return fx - 3, df

    def f0(self, omega: float) -> float:
        score = -math.pow(self.n * self.m * self.p, omega)

        for s_a, (n_a, m_a, p_a) in self.structure:
            for s_b, (n_b, m_b, p_b) in self.structure:
                for s_c, (n_c, m_c, p_c) in self.structure:
                    score += s_a * s_b * s_c * math.pow(n_a * m_b * p_c, omega - 2) * n_b * n_c * m_a * m_c * p_a * p_b

        return score

    def f_inf(self, omega: float) -> float:
        score = math.pow(self.n * self.m * self.p, omega / 3)

        for si, (ni, mi, pi) in self.structure:
            score -= si * math.pow(ni * mi * pi, omega / 3)

        return score

    def f1(self, w: float) -> float:
        return sum(si * (ni / self.n) ** (w - 2) * (mi / self.m) * (pi / self.p) for si, (ni, mi, pi) in self.structure) - 1

    def f2(self, w: float) -> float:
        return sum(si * (ni / self.n) * (mi / self.m) ** (w - 2) * (pi / self.p) for si, (ni, mi, pi) in self.structure) - 1

    def f3(self, w: float) -> float:
        return sum(si * (ni / self.n) * (mi / self.m) * (pi / self.p) ** (w - 2) for si, (ni, mi, pi) in self.structure) - 1

    def __get_heuristic(self, a: float, b: float, c: float) -> int:
        heuristic_v = [0.0 for _ in range(6)]

        for si, (ni, mi, pi) in self.structure_normalized:
            for i, (n, m, p) in enumerate(itertools.permutations([ni, mi, pi], r=3)):
                heuristic_v[i] += si * float(a * n + b * m + c * p)

        return heuristic_v.index(min(heuristic_v))

    def __get_exponents(self) -> Tuple[float, float, float]:
        w1 = find_root_bisection(self.f1, a=2, b=3, eps=self.eps)
        w2 = find_root_bisection(self.f2, a=2, b=3, eps=self.eps)
        w3 = find_root_bisection(self.f3, a=2, b=3, eps=self.eps)
        return w1, w2, w3
