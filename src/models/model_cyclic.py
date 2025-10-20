import json
from typing import List

from src.models.model import Model
from src.utils.utils import parse_value, pretty_matrix


class ModelCyclic(Model):
    def __init__(self, n: int, m: int, a: List[List[int]], b: List[List[int]], c: List[List[int]], d: List[List[int]], z2: bool = True):
        self.rank_s = len(a)
        self.rank_t = len(b)

        assert len(b) == len(c) == len(d)
        assert m == self.rank_s + self.rank_t * 3

        value_type = bool if z2 else int
        self.a = [[value_type(value) for value in row] for row in a]
        self.b = [[value_type(value) for value in row] for row in b]
        self.c = [[value_type(value) for value in row] for row in c]
        self.d = [[value_type(value) for value in row] for row in d]

        super().__init__(n=n, m=m, u=self.a + self.b + self.c + self.d, v=self.a + self.d + self.b + self.c, w=self.a + self.c + self.d + self.b, z2=z2)
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
        return ModelCyclic(n=n, m=m, a=a, b=b, c=c, d=d, z2=True)

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

    def save(self, path: str) -> None:
        a = pretty_matrix(self.a, '"a":', "    ")
        b = pretty_matrix(self.b, '"b":', "    ")
        c = pretty_matrix(self.c, '"c":', "    ")
        d = pretty_matrix(self.d, '"d":', "    ")

        u = pretty_matrix(self.u, '"u":', "    ")
        v = pretty_matrix(self.v, '"v":', "    ")
        w = pretty_matrix(self.w, '"w":', "    ")

        multiplications = []
        for i, multiplication in enumerate(self.get_multiplications()):
            multiplications.append(f'{"," if i > 0 else ""}\n        "{multiplication}"')

        elements = []
        for i, row in enumerate(self.get_elements()):
            for j, element in enumerate(row):
                elements.append(f'{"," if i > 0 or j > 0 else ""}\n        "{element}"')

        u_ones, v_ones, w_ones = self.ones()

        with open(path, "w", encoding="utf-8") as f:
            f.write("{\n")
            f.write(f'    "n": {self.n},\n')
            f.write(f'    "m": {self.m},\n')
            f.write(f'    "z2": {"true" if self.z2 else "false"},\n')
            f.write(f'    "type": "cyclic",\n')
            f.write(f'    "multiplications": [{"".join(multiplications)}\n')
            f.write(f'    ],\n')
            f.write(f'    "elements": [{"".join(elements)}\n')
            f.write(f'    ],\n')
            f.write(f'    {u},\n')
            f.write(f'    {v},\n')
            f.write(f'    {w},\n')
            f.write(f'    {a},\n')
            f.write(f'    {b},\n')
            f.write(f'    {c},\n')
            f.write(f'    {d},\n')
            f.write(f'    "invariant_f": "{self.invariant_f()}",\n')
            f.write(f'    "invariant_g": "{self.invariant_g()}",\n')
            f.write(f'    "invariant_h": "{self.invariant_h()}",\n')
            f.write(f'    "weight": {self.weight()},\n'),
            f.write(f'    "complexity": {self.complexity()},\n')
            f.write(f'    "u_ones": {u_ones},\n')
            f.write(f'    "v_ones": {v_ones},\n')
            f.write(f'    "w_ones": {w_ones}\n')
            f.write("}\n")

    def __validate(self) -> None:
        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    assert self.__validate_equation(i, j, k)

    def __validate_equation(self, i: int, j: int, k: int) -> bool:
        i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
        target = (i2 == j1) and (i1 == k2) and (j2 == k1)
        equation = 0

        for index in range(self.m):
            if index < self.rank_s:
                equation += int(self.a[index][i]) * int(self.a[index][j]) * int(self.a[index][k])
            elif index < self.rank_s + self.rank_t:
                offset = index - self.rank_s
                equation += int(self.b[offset][i]) * int(self.d[offset][j]) * int(self.c[offset][k])
            elif index < self.rank_s + 2 * self.rank_t:
                offset = index - self.rank_s - self.rank_t
                equation += int(self.c[offset][i]) * int(self.b[offset][j]) * int(self.d[offset][k])
            else:
                offset = index - self.rank_s - 2 * self.rank_t
                equation += int(self.d[offset][i]) * int(self.c[offset][j]) * int(self.b[offset][k])

        if self.z2:
            equation %= 2

        return equation == target

    def __update(self) -> None:
        self.u = self.a + self.b + self.c + self.d
        self.v = self.a + self.d + self.b + self.c
        self.w = self.a + self.c + self.d + self.b
