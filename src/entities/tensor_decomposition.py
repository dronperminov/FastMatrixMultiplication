import random
from typing import List, Optional, Tuple

from src.entities.cnf import ConjunctiveNormalForm
from src.schemes.scheme_bit_packed import Scheme


class TensorDecomposition:
    def __init__(self, n1: int, n2: int, n3: int, m: int, path: str) -> None:
        self.n = [n1, n2, n3]
        self.nn = [n1 * n2, n2 * n3, n3 * n1]
        self.m = m
        self.path = path

        self.cnf = ConjunctiveNormalForm()
        self.u = [[self.cnf.add_var(f"u[{index}][{i}]") for i in range(self.nn[0])] for index in range(self.m)]
        self.v = [[self.cnf.add_var(f"v[{index}][{i}]") for i in range(self.nn[1])] for index in range(self.m)]
        self.w = [[self.cnf.add_var(f"w[{index}][{i}]") for i in range(self.nn[2])] for index in range(self.m)]

        self.__encode_decomposition()
        self.__encode_multiplications_ordering()
        self.__encode_cycle_shift_ordering()
        self.__encode_basis_ordering()
        self.__encode_constraints()

    def set_probable_scheme(self, scheme: Scheme, pu: float, pv: float, pw: float) -> None:
        if scheme.n != self.n or scheme.m != self.m:
            return

        self.cnf.clear_values()

        for index in range(self.m):
            for i in range(self.nn[0]):
                if random.random() < pu:
                    self.cnf.set_value(self.u[index][i], bool(scheme.u[index][i]))

            for i in range(self.nn[1]):
                if random.random() < pv:
                    self.cnf.set_value(self.v[index][i], bool(scheme.v[index][i]))

            for i in range(self.nn[2]):
                if random.random() < pw:
                    self.cnf.set_value(self.w[index][i], bool(scheme.w[index][i]))

    def solve(self, threads: int = 2, max_time: int = 0) -> Optional[Tuple[List[List[bool]], List[List[bool]], List[List[bool]]]]:
        result = self.cnf.solve(self.path, threads=threads, max_time=max_time)
        if not result:
            return result

        u = [[self.cnf[self.u[index][i]] for i in range(self.nn[0])] for index in range(self.m)]
        v = [[self.cnf[self.v[index][i]] for i in range(self.nn[1])] for index in range(self.m)]
        w = [[self.cnf[self.w[index][i]] for i in range(self.nn[2])] for index in range(self.m)]
        return u, v, w

    def exclude_scheme(self, scheme: Scheme) -> None:
        variables = {}

        for index in range(self.m):
            for i in range(self.nn[0]):
                variables[self.u[index][i]] = scheme.u[index][i]

            for i in range(self.nn[1]):
                variables[self.v[index][i]] = scheme.v[index][i]

            for i in range(self.nn[2]):
                variables[self.w[index][i]] = scheme.w[index][i]

        self.cnf.exclude_solution(variables=variables)

    def __set_value(self, index: int, i: int, value: bool) -> None:
        if i < self.nn[0]:
            self.cnf.set_value(self.u[index][i], value)
        elif i < self.nn[0] + self.nn[1]:
            self.cnf.set_value(self.v[index][i - self.nn[0]], value)
        else:
            self.cnf.set_value(self.w[index][i - self.nn[0] - self.nn[1]], value)

    def __encode_decomposition(self) -> None:
        for i in range(self.nn[0]):
            for j in range(self.nn[1]):
                for k in range(self.nn[2]):
                    i1, i2, j1, j2, k1, k2 = i // self.n[1], i % self.n[1], j // self.n[2], j % self.n[2], k // self.n[0], k % self.n[0]
                    target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                    self.cnf.add_xor([self.cnf.add_and_var([self.u[index][i], self.v[index][j], self.w[index][k]]) for index in range(self.m)], target)

    def __encode_multiplications_ordering(self) -> None:
        self.cnf.add_lex_chain([self.u[index] + self.v[index] + self.w[index] for index in range(self.m)], strict=True)

    def __encode_cycle_shift_ordering(self) -> None:
        if self.n[0] != self.n[1] or self.n[1] != self.n[2]:
            return

        uvw = [value for row in self.u + self.v + self.w for value in row]
        wuv = [value for row in self.w + self.u + self.v for value in row]
        vwu = [value for row in self.v + self.w + self.u for value in row]

        self.cnf.add_lex_order(uvw, wuv, strict=False, comment="cycle shift uvw <= wuv")
        self.cnf.add_lex_order(uvw, vwu, strict=False, comment="cycle shift uvw <= vwu")

    def __encode_basis_ordering(self) -> None:
        rows = []
        columns = []

        for i in range(self.n[0]):
            row_u, column_w = [], []

            for index in range(self.m):
                row_u.extend(self.__get_row(self.u, index, row=i, n1=self.n[0], n2=self.n[1]))
                column_w.extend(self.__get_column(self.w, index, column=i, n1=self.n[2], n2=self.n[0]))

            rows.append(row_u + column_w)

        for i in range(self.n[2]):
            column_v, row_w = [], []

            for index in range(self.m):
                column_v.extend(self.__get_column(self.v, index, column=i, n1=self.n[1], n2=self.n[2]))
                row_w.extend(self.__get_row(self.w, index, row=i, n1=self.n[2], n2=self.n[0]))

            columns.append(column_v + row_w)

        self.cnf.add_lex_chain(rows, strict=False, comment=f"basis rows ordering")
        self.cnf.add_lex_chain(columns, strict=False, comment=f"basis columns ordering")

    def __encode_constraints(self) -> None:
        for index in range(self.m):
            self.cnf.add_at_least_k(self.u[index], k=1)
            self.cnf.add_at_least_k(self.v[index], k=1)
            self.cnf.add_at_least_k(self.w[index], k=1)

        for i in range(self.nn[0]):
            self.cnf.add_at_least_k([self.u[index][i] for index in range(self.m)], k=self.n[2])

        for i in range(self.nn[1]):
            self.cnf.add_at_least_k([self.v[index][i] for index in range(self.m)], k=self.n[0])

        for i in range(self.nn[2]):
            self.cnf.add_at_least_k([self.w[index][i] for index in range(self.m)], k=1)

    def __get_row(self, matrix: List[List[int]], index: int, row: int, n1: int, n2: int) -> List[int]:
        return [matrix[index][row * n2 + j] for j in range(n2)]

    def __get_column(self, matrix: List[List[int]], index: int, column: int, n1: int, n2: int) -> List[int]:
        return [matrix[index][i * n2 + column] for i in range(n1)]
