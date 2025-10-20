import json
from typing import List

from src.models.model import Model
from src.utils.utils import parse_value, pretty_matrix


class ModelCyclic(Model):
    def __init__(self, n: int, m: int, a: List[List[int]], b: List[List[int]], c: List[List[int]], d: List[List[int]]):
        self.rank_s = len(a)
        self.rank_t = len(b)

        assert len(b) == len(c) == len(d)
        assert m == self.rank_s + self.rank_t * 3

        self.a = [[value != 0 for value in row] for row in a]
        self.b = [[value != 0 for value in row] for row in b]
        self.c = [[value != 0 for value in row] for row in c]
        self.d = [[value != 0 for value in row] for row in d]

        super().__init__(n=n, m=m, u=self.a + self.b + self.c + self.d, v=self.a + self.d + self.b + self.c, w=self.a + self.c + self.d + self.b)
        self.__validate()

    @classmethod
    def from_solution(cls, path: str) -> "ModelCyclic":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        n, m = data["n"], data["m"]
        rank_s, rank_t = data["s"], data["t"]

        literal2value = {abs(int(literal)): int(literal) > 0 for literal in data["sat"]}

        a = [[parse_value(data["a"][index][i], literal2value) for i in range(n * n)] for index in range(rank_s)]
        b = [[parse_value(data["b"][index][i], literal2value) for i in range(n * n)] for index in range(rank_t)]
        c = [[parse_value(data["c"][index][i], literal2value) for i in range(n * n)] for index in range(rank_t)]
        d = [[parse_value(data["d"][index][i], literal2value) for i in range(n * n)] for index in range(rank_t)]
        return ModelCyclic(n=n, m=m, a=a, b=b, c=c, d=d)

    def show_matrices(self) -> None:
        print(pretty_matrix(self.a, "A"))
        print(pretty_matrix(self.b, "B"))
        print(pretty_matrix(self.c, "C"))
        print(pretty_matrix(self.d, "D"))
        print("")
        print(pretty_matrix(self.u, "U"))
        print(pretty_matrix(self.v, "V"))
        print(pretty_matrix(self.w, "W"))

    def shift_bcd(self, index: int) -> None:
        for i in range(self.nn):
            self.b[index], self.c[index], self.d[index] = self.d[index], self.b[index], self.c[index]

        self.__update()
        self.__validate()

    def __validate(self) -> None:
        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    assert self.__validate_equation(i, j, k)

    def __validate_equation(self, i: int, j: int, k: int) -> bool:
        i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
        target = (i2 == j1) and (i1 == k2) and (j2 == k1)
        equation = False

        for index in range(self.m):
            if index < self.rank_s:
                equation ^= self.a[index][i] and self.a[index][j] and self.a[index][k]
            elif index < self.rank_s + self.rank_t:
                offset = index - self.rank_s
                equation ^= self.b[offset][i] and self.d[offset][j] and self.c[offset][k]
            elif index < self.rank_s + 2 * self.rank_t:
                offset = index - self.rank_s - self.rank_t
                equation ^= self.c[offset][i] and self.b[offset][j] and self.d[offset][k]
            else:
                offset = index - self.rank_s - 2 * self.rank_t
                equation ^= self.d[offset][i] and self.c[offset][j] and self.b[offset][k]

        return equation == target

    def __update(self) -> None:
        self.u = self.a + self.b + self.c + self.d
        self.v = self.a + self.d + self.b + self.c
        self.w = self.a + self.c + self.d + self.b
