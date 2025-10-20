import json
from typing import List

from src.entities.cnf import ConjunctiveNormalForm
from src.utils.formulas import and_encoding, at_least_k_matrix, lex_chain, lex_order, xor_chain


class BrentEquationsCyclic:
    def __init__(self, n: int, m: int, rank_s: int, rank_t: int) -> None:
        self.n = n
        self.m = m
        self.rank_s = rank_s
        self.rank_t = rank_t

        assert rank_s >= 0
        assert rank_t >= 0
        assert m == rank_s + 3 * rank_t

        self.nn = n * n

        self.cnf = ConjunctiveNormalForm(f"n: {self.n}, m: {self.m} (S: {self.rank_s}, T: {self.rank_t})")

        self.a = [[self.cnf.variables.get(f'a^{index + 1}_{i + 1}') for i in range(self.nn)] for index in range(rank_s)]
        self.b = [[self.cnf.variables.get(f'b^{index + 1}_{i + 1}') for i in range(self.nn)] for index in range(rank_t)]
        self.c = [[self.cnf.variables.get(f'c^{index + 1}_{i + 1}') for i in range(self.nn)] for index in range(rank_t)]
        self.d = [[self.cnf.variables.get(f'd^{index + 1}_{i + 1}') for i in range(self.nn)] for index in range(rank_t)]

        self.ands = {}

    def generate(self, path: str) -> None:
        self.__encode_equations()
        self.__encode_constraints()
        self.__encode_ordering()

        self.cnf.statistic()
        self.cnf.save(f"{path}.cnf")

        with open(f"{path}.json", "w", encoding="utf-8") as f:
            json.dump({
                "algorithm": "abcd",
                "n": self.n, "m": self.m, "s": self.rank_s, "t": self.rank_t,
                "a": self.a, "b": self.b, "c": self.c, "d": self.d
            }, f, ensure_ascii=False, indent=2)

    def __encode_equations(self) -> None:
        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
                    target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                    self.cnf.add(self.__encode_equation(i, j, k, target), f"equation {i1 + 1} {i2 + 1} {j1 + 1} {j2 + 1} {k1 + 1} {k2 + 1} = {target}")

    def __encode_equation(self, i: int, j: int, k: int, target: bool) -> List[List[int]]:
        clauses = []
        x = []

        for index in range(self.m):
            if index < self.rank_s:
                mults = [self.a[index][i], self.a[index][j], self.a[index][k]]
            elif index < self.rank_s + self.rank_t:
                offset = index - self.rank_s
                mults = [self.b[offset][i], self.d[offset][j], self.c[offset][k]]
            elif index < self.rank_s + 2 * self.rank_t:
                offset = index - self.rank_s - self.rank_t
                mults = [self.c[offset][i], self.b[offset][j], self.d[offset][k]]
            else:
                offset = index - self.rank_s - 2 * self.rank_t
                mults = [self.d[offset][i], self.c[offset][j], self.b[offset][k]]

            mults = sorted(set(mults))
            if len(mults) == 1:
                t = mults[0]
            elif len(mults) == 2:
                t = self.__encode_and(mults[0], mults[1], clauses)
            else:
                s = self.__encode_and(mults[0], mults[1], clauses)
                t = self.__encode_and(s, mults[2], clauses)

            x.append(t)

        clauses.extend(xor_chain(x if target else [-x[0], *x[1:]], variables=self.cnf.variables))
        return clauses

    def __encode_ordering(self) -> None:
        self.cnf.add(lex_chain(self.a, self.cnf.variables, strict=False), f"a ordering")

        bcd = [self.b[index] + self.c[index] + self.d[index] for index in range(self.rank_t)]
        self.cnf.add(lex_chain(bcd, self.cnf.variables, strict=False), f"bcd ordering")

        for index in range(self.rank_t):
            bcd = self.b[index] + self.c[index] + self.d[index]
            dbc = self.d[index] + self.b[index] + self.c[index]
            cdb = self.c[index] + self.d[index] + self.b[index]
            self.cnf.add(lex_order(bcd, dbc, self.cnf.variables, strict=False))
            self.cnf.add(lex_order(bcd, cdb, self.cnf.variables, strict=False))

    def __encode_constraints(self) -> None:
        matrix = self.a + self.b + self.c + self.d
        self.cnf.add(at_least_k_matrix(matrix=matrix, k_row=1, k_column=self.n, variables=self.cnf.variables))

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
