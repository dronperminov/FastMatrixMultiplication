from typing import List, Tuple

from ortools.sat.python.cp_model import CpModel, CpSolver, FEASIBLE, IntVar, OPTIMAL

from src.entities.scheme import Scheme
from src.entities.solution_collector import SolutionCollector


class RingSolverOrtools:
    def __init__(self, scheme: Scheme, min_coef: int, max_coef: int) -> None:
        self.scheme = scheme
        self.model = CpModel()
        self.min_coef = min_coef
        self.max_coef = max_coef

        self.n = scheme.n
        self.m = scheme.m
        self.nn = scheme.nn

        self.ring_values = list(range(self.min_coef, self.max_coef + 1))
        self.max_values = {bool(mod): max(value for value in self.ring_values if value % 2 == mod) for mod in [0, 1]}
        self.min_values = {bool(mod): min(value for value in self.ring_values if value % 2 == mod) for mod in [0, 1]}
        self.max_abs = max(abs(self.min_coef), abs(self.max_coef))

        self.u = [[self.model.new_int_var(self.min_values[scheme.u[index][i]], self.max_values[scheme.u[index][i]], f'u{index}_{i}') for i in range(self.nn)] for index in range(self.m)]
        self.v = [[self.model.new_int_var(self.min_values[scheme.v[index][i]], self.max_values[scheme.v[index][i]], f'v{index}_{i}') for i in range(self.nn)] for index in range(self.m)]
        self.w = [[self.model.new_int_var(self.min_values[scheme.w[index][i]], self.max_values[scheme.w[index][i]], f'w{index}_{i}') for i in range(self.nn)] for index in range(self.m)]

        self.__add_values_constraints()

        self.uv = self.__init_uv_constraints()
        self.uvw = self.__init_uvw_constraints()
        self.__add_equation_constraints()

        self.u_abs, self.w_abs = self.__init_abs_constraints()
        self.__add_sign_symmetry_constraints()

    def lift(self, max_time: int, max_solutions: int) -> List[Scheme]:
        solver = CpSolver()

        if max_time > 0:
            solver.parameters.max_time_in_seconds = max_time

        solution_collector = SolutionCollector(self.u, self.v, self.w, max_solutions=max_solutions)
        status = solver.SearchForAllSolutions(self.model, solution_collector)

        if status != OPTIMAL and status != FEASIBLE:
            return []

        return [Scheme(n=self.n, m=self.m, u=u, v=v, w=w, z2=False) for u, v, w in solution_collector.solutions]

    def __add_equation_constraints(self) -> None:
        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
                    target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                    self.model.Add(sum(self.uvw[index][i][j][k] for index in range(self.m)) == target)

    def __add_values_constraints(self) -> None:
        bool2invalid_values = {
            True: [value for value in range(self.min_coef, self.max_coef + 1) if abs(value) % 2 == 0],
            False: [value for value in range(self.min_coef, self.max_coef + 1) if abs(value) % 2 == 1]
        }

        for index in range(self.m):
            for i in range(self.nn):
                for value in bool2invalid_values[self.scheme.u[index][i]]:
                    self.model.add(self.u[index][i] != value)

                for value in bool2invalid_values[self.scheme.v[index][i]]:
                    self.model.add(self.v[index][i] != value)

                for value in bool2invalid_values[self.scheme.w[index][i]]:
                    self.model.add(self.w[index][i] != value)

    def __init_abs_constraints(self) -> Tuple[List[List[IntVar]], List[List[IntVar]]]:
        u_abs = [[self.model.new_int_var(0, self.max_abs, f"|u_{index}_{i}|") for i in range(self.nn)] for index in range(self.m)]
        w_abs = [[self.model.new_int_var(0, self.max_abs, f"|w_{index}_{i}|") for i in range(self.nn)] for index in range(self.m)]

        for index in range(self.m):
            for i in range(self.nn):
                self.model.add_abs_equality(u_abs[index][i], self.u[index][i])
                self.model.add_abs_equality(w_abs[index][i], self.w[index][i])

        return u_abs, w_abs

    def __init_uv_constraints(self) -> List[List[List[IntVar]]]:
        max_prod = self.max_abs ** 2
        uv = [[[0 for _ in range(self.scheme.nn)] for _ in range(self.nn)] for _ in range(self.m)]

        for index in range(self.m):
            for i in range(self.nn):
                for j in range(self.nn):
                    uv[index][i][j] = self.model.new_int_var(-max_prod, max_prod, f"uv{index}_{i}_{j}")
                    self.model.AddMultiplicationEquality(uv[index][i][j], self.u[index][i], self.v[index][j])

        return uv

    def __init_uvw_constraints(self) -> List[List[List[List[IntVar]]]]:
        max_prod = self.max_abs ** 3
        uvw = [[[[0 for _ in range(self.scheme.nn)] for _ in range(self.scheme.nn)] for _ in range(self.nn)] for _ in range(self.m)]

        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    for index in range(self.m):
                        uvw[index][i][j][k] = self.model.new_int_var(-max_prod, max_prod, f"uvw{index}_{i}_{j}_{k}")
                        self.model.AddMultiplicationEquality(uvw[index][i][j][k], self.uv[index][i][j], self.w[index][k])

        return uvw

    def __add_sign_symmetry_constraints(self) -> None:
        for index in range(self.m):
            for i in range(self.nn):
                self.model.add(-self.u[index][i] <= sum(self.u_abs[index][j] for j in range(i)))
                self.model.add(-self.w[index][i] <= sum(self.w_abs[index][j] for j in range(i)))
