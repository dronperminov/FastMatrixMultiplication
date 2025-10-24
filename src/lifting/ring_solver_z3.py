from typing import List

from z3 import And, Int, Or, Solver, sat, set_option

from src.entities.scheme import Scheme


class RingSolverZ3:
    def __init__(self, scheme: Scheme, min_coef: int, max_coef: int) -> None:
        self.scheme = scheme
        self.solver = Solver()
        self.min_coef = min_coef
        self.max_coef = max_coef

        self.n = scheme.n
        self.m = scheme.m
        self.nn = scheme.nn

        self.ring_values = list(range(self.min_coef, self.max_coef + 1))
        self.max_values = {bool(mod): max(value for value in self.ring_values if value % 2 == mod) for mod in [0, 1]}
        self.min_values = {bool(mod): min(value for value in self.ring_values if value % 2 == mod) for mod in [0, 1]}

        self.u = [[Int(f'u{index}{i}') for i in range(self.nn)] for index in range(self.m)]
        self.v = [[Int(f'v{index}{i}') for i in range(self.nn)] for index in range(self.m)]
        self.w = [[Int(f'w{index}{i}') for i in range(self.nn)] for index in range(self.m)]

        self.__add_values_constraints()
        self.__add_equation_constraints()
        self.__add_sign_symmetry_constraints()

    def lift(self, max_time: int, max_solutions: int) -> List[Scheme]:
        if max_time > 0:
            set_option("solver.timeout", max_time * 1000)

        return self.__get_solutions(max_solutions=max_solutions)

    def __add_equation_constraints(self) -> None:
        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
                    target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                    self.solver.add(sum(self.u[index][i] * self.v[index][j] * self.w[index][k] for index in range(self.m)) == target)

    def __add_values_constraints(self) -> None:
        for index in range(self.m):
            for i in range(self.nn):
                self.solver.add(self.u[index][i] >= self.min_values[self.scheme.u[index][i]])
                self.solver.add(self.u[index][i] <= self.max_values[self.scheme.u[index][i]])

                self.solver.add(self.v[index][i] >= self.min_values[self.scheme.v[index][i]])
                self.solver.add(self.v[index][i] <= self.max_values[self.scheme.v[index][i]])

                self.solver.add(self.w[index][i] >= self.min_values[self.scheme.w[index][i]])
                self.solver.add(self.w[index][i] <= self.max_values[self.scheme.w[index][i]])

                self.solver.add(self.u[index][i] % 2 == int(self.scheme.u[index][i]))
                self.solver.add(self.v[index][i] % 2 == int(self.scheme.v[index][i]))
                self.solver.add(self.w[index][i] % 2 == int(self.scheme.w[index][i]))

    def __add_sign_symmetry_constraints(self) -> None:
        for index in range(self.m):
            self.__positive_first_non_zero(self.u[index])
            self.__positive_first_non_zero(self.v[index])

    def __positive_first_non_zero(self, values: List[Int]) -> None:
        conditions = []
        for i in range(self.nn):
            prev_zero = And(values[j] == 0 for j in range(i))
            conditions.append(And(prev_zero, values[i] > 0))

        self.solver.add(Or(conditions))

    def __get_solutions(self, max_solutions: int) -> List[Scheme]:
        schemes = []

        for _ in range(max_solutions):
            if self.solver.check() != sat:
                break

            model = self.solver.model()

            u = [[model[self.u[index][i]].as_long() for i in range(self.nn)] for index in range(self.m)]
            v = [[model[self.v[index][i]].as_long() for i in range(self.nn)] for index in range(self.m)]
            w = [[model[self.w[index][i]].as_long() for i in range(self.nn)] for index in range(self.m)]
            schemes.append(Scheme(n=self.n, m=self.m, u=u, v=v, w=w, z2=False))

            solution = [variable() != model[variable] for variable in model]
            self.solver.add(Or(solution))

        return schemes
