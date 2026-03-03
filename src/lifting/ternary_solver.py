from typing import List, Union

from ortools.sat.python.cp_model import CpModel, CpSolver, FEASIBLE, IntVar, OPTIMAL

from src.entities.solution_collector import SolutionCollector
from src.schemes.scheme import Scheme


class TernarySolver:
    def __init__(self, scheme: Scheme) -> None:
        self.scheme = scheme
        self.model = CpModel()

        self.n = scheme.n
        self.m = scheme.m
        self.nn = scheme.nn

        self.u = [[self.model.new_int_var(0, 1, f'u{index}_{i}') if scheme.u[index][i] else 0 for i in range(self.nn[0])] for index in range(self.m)]
        self.v = [[self.model.new_int_var(0, 1, f'v{index}_{i}') if scheme.v[index][i] else 0 for i in range(self.nn[1])] for index in range(self.m)]
        self.w = [[self.model.new_int_var(0, 1, f'w{index}_{i}') if scheme.w[index][i] else 0 for i in range(self.nn[2])] for index in range(self.m)]

        self.__add_equation_constraints()
        self.__add_sign_symmetry_constraints()

    def lift(self, max_time: int = 20, max_solutions: int = 1) -> List[Scheme]:
        solver = CpSolver()

        if max_time > 0:
            solver.parameters.max_time_in_seconds = max_time

        solution_collector = SolutionCollector(self.u, self.v, self.w, max_solutions=max_solutions)
        status = solver.SearchForAllSolutions(self.model, solution_collector)

        if status != OPTIMAL and status != FEASIBLE:
            return []

        return [self.__parse_solution(u, v, w) for u, v, w in solution_collector.solutions]

    def __parse_solution(self, u: List[List[int]], v: List[List[int]], w: List[List[int]]) -> Scheme:
        n1, n2, n3 = self.n
        u_solution = [[u[index][i] * 2 - 1 if self.scheme.u[index][i] else 0 for i in range(self.nn[0])] for index in range(self.m)]
        v_solution = [[v[index][i] * 2 - 1 if self.scheme.v[index][i] else 0 for i in range(self.nn[1])] for index in range(self.m)]
        w_solution = [[w[index][i] * 2 - 1 if self.scheme.w[index][i] else 0 for i in range(self.nn[2])] for index in range(self.m)]
        return Scheme(n1=n1, n2=n2, n3=n3, m=self.m, u=u_solution, v=v_solution, w=w_solution, z2=False)

    def __add_equation_constraints(self) -> None:
        for i in range(self.nn[0]):
            for j in range(self.nn[1]):
                uv = [self.__multiply_uv(index=index, i=i, j=j) for index in range(self.m)]

                for k in range(self.nn[2]):
                    uvw = [self.__multiply_uvw(uv=uv[index], index=index, i=i, j=j, k=k) for index in range(self.m)]

                    i1, i2, j1, j2, k1, k2 = i // self.n[1], i % self.n[1], j // self.n[2], j % self.n[2], k // self.n[0], k % self.n[0]
                    target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                    self.model.Add(sum(uvw[index] for index in range(self.m)) == target)

    def __multiply_uv(self, index: int, i: int, j: int) -> Union[IntVar, int]:
        if type(self.u[index][i]) is not IntVar or type(self.v[index][j]) is not IntVar:
            return 0

        uv = self.model.new_int_var(-1, 1, f"uv{index}_{i}_{j}")
        self.model.AddMultiplicationEquality(uv, self.u[index][i] * 2 - 1, self.v[index][j] * 2 - 1)
        return uv

    def __multiply_uvw(self, uv: Union[IntVar, int], index: int, i: int, j: int, k: int) -> Union[IntVar, int]:
        if type(uv) is not IntVar or type(self.w[index][k]) is not IntVar:
            return 0

        uvw = self.model.new_int_var(-1, 1, f"uvw{index}_{i}_{j}_{k}")
        self.model.AddMultiplicationEquality(uvw, uv, self.w[index][k] * 2 - 1)
        return uvw

    def __add_sign_symmetry_constraints(self) -> None:
        for index in range(self.m):
            u_value = [self.u[index][i] * 2 - 1 if type(self.u[index][i]) is IntVar else 0 for i in range(self.nn[0])]
            w_value = [self.w[index][i] * 2 - 1 if type(self.w[index][i]) is IntVar else 0 for i in range(self.nn[2])]

            u_abs = [1 if type(self.u[index][i]) is IntVar else 0 for i in range(self.nn[0])]
            w_abs = [1 if type(self.w[index][i]) is IntVar else 0 for i in range(self.nn[2])]

            for i in range(self.nn[0]):
                self.model.add(-u_value[i] <= sum(u_abs[j] for j in range(i)))

            for i in range(self.nn[2]):
                self.model.add(-w_value[i] <= sum(w_abs[j] for j in range(i)))
