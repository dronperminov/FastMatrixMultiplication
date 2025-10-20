import json
from typing import List

from src.entities.cnf import ConjunctiveNormalForm
from src.utils.formulas import and_encoding, at_least_k_matrix, lex_chain, lex_order, xor_chain
from src.utils.utils import flatten


class BrentEquationsBase:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.nn = n * n

        self.cnf = ConjunctiveNormalForm(f"n: {self.n}, m: {self.m}")

        self.u = [[self.cnf.variables.get(f"u^{index + 1}_{i + 1}") for i in range(self.nn)] for index in range(self.m)]
        self.v = [[self.cnf.variables.get(f"v^{index + 1}_{i + 1}") for i in range(self.nn)] for index in range(self.m)]
        self.w = [[self.cnf.variables.get(f"w^{index + 1}_{i + 1}") for i in range(self.nn)] for index in range(self.m)]

        self.ands = {}

    def generate(self, path: str) -> None:
        self.__encode_equations()
        self.__encode_constraints()
        self.__encode_ordering()

        self.cnf.statistic()
        self.cnf.save(f"{path}.cnf")

        with open(f"{path}.json", "w", encoding="utf-8") as f:
            json.dump({
                "algorithm": "base",
                "n": self.n, "m": self.m,
                "u": self.u, "v": self.v, "w": self.w
            }, f, ensure_ascii=False, indent=2)

    def __encode_equations(self) -> None:
        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
                    target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                    self.cnf.add(self.__encode_equation(i, j, k, target), f"equation {i + 1} {j + 1} {k + 1} = {target}")

    def __encode_equation(self, i: int, j: int, k: int, target: bool) -> List[List[int]]:
        x = []
        clauses = []

        for index in range(self.m):
            mults = sorted([self.u[index][i], self.v[index][j], self.w[index][k]])
            s = self.__encode_and(mults[0], mults[1], clauses)
            t = self.__encode_and(s, mults[2], clauses)
            x.append(t)

        clauses.extend(xor_chain(x if target else [-x[0], *x[1:]], variables=self.cnf.variables))
        return clauses

    def __encode_ordering(self) -> None:
        self.__encode_multiplications_ordering()  # m!
        self.__encode_cycle_shift_ordering()  # 3: UVW -> WUV -> VWU
        self.__encode_basis_ordering()  # n!

    def __encode_multiplications_ordering(self) -> None:
        rows = [self.u[index] + self.v[index] for index in range(self.m)]
        self.cnf.add(lex_chain(rows, variables=self.cnf.variables, strict=True), f"multiplications ordering")

    def __encode_cycle_shift_ordering(self) -> None:
        uvw = flatten(self.u + self.v + self.w)
        wuv = flatten(self.w + self.u + self.v)
        vwu = flatten(self.v + self.w + self.u)

        self.cnf.add(lex_order(uvw, wuv, self.cnf.variables, strict=False), "cycle shift uvw <= wuv")
        self.cnf.add(lex_order(uvw, vwu, self.cnf.variables, strict=False), "cycle shift uvw <= vwu")

    def __encode_basis_ordering(self) -> None:
        rows = []
        columns = []

        for i in range(self.n):
            row_u, column_w = [], []
            column_v, row_w = [], []

            for index in range(self.m):
                row_u.extend(self.__get_row(self.u, index, row=i))
                column_w.extend(self.__get_column(self.w, index, column=i))

                column_v.extend(self.__get_column(self.v, index, column=i))
                row_w.extend(self.__get_row(self.w, index, row=i))

            rows.append(row_u + column_w)
            columns.append(column_v + row_w)

        self.cnf.add(lex_chain(rows, self.cnf.variables, strict=False), f"basis rows ordering")
        self.cnf.add(lex_chain(columns, self.cnf.variables, strict=False), f"basis columns ordering")

    def __encode_constraints(self) -> None:
        self.cnf.add(at_least_k_matrix(self.u, k_row=1, k_column=self.n, variables=self.cnf.variables), f"at_least u (1 in rows, {self.n} in columns)")
        self.cnf.add(at_least_k_matrix(self.v, k_row=1, k_column=self.n, variables=self.cnf.variables), f"at_least v (1 in rows, {self.n} in columns)")
        self.cnf.add(at_least_k_matrix(self.w, k_row=1, k_column=self.n, variables=self.cnf.variables), f"at_least w (1 in rows, {self.n} in columns)")

    def __encode_and(self, a: int, b: int, clauses: List[List[int]]) -> int:
        if a == b:
            return a

        if a > b:
            a, b = b, a

        key = (a, b)

        if key not in self.ands:
            t = self.cnf.variables.get()
            clauses.extend(and_encoding(t, [a, b]))
            self.ands[key] = t

        return self.ands[key]

    def __get_row(self, matrix: List[List[int]], index: int, row: int) -> List[int]:
        return [matrix[index][row * self.n + j] for j in range(self.n)]

    def __get_column(self, matrix: List[List[int]], index: int, column: int) -> List[int]:
        return [matrix[index][i * self.n + column] for i in range(self.n)]
