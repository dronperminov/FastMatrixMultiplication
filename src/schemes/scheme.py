import itertools
import json
import random
import re
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from typing import Dict, List, Tuple, Union

from src.entities.addition_minimization import AdditionMinimization
from src.utils.algebra import rank_z2
from src.utils.utils import pretty_matrix


class Scheme:
    def __init__(self, n1: int, n2: int, n3: int, m: int, u: List[List[Union[int, Fraction]]], v: List[List[Union[int, Fraction]]], w: List[List[Union[int, Fraction]]], z2: bool, validate: bool = True) -> None:
        self.n = [n1, n2, n3]
        self.nn = [n1 * n2, n2 * n3, n3 * n1]
        self.m = m
        self.z2 = z2

        assert len(u) == len(v) == len(w) == m
        self.u = [[abs(u[index][i]) % 2 if z2 else u[index][i] for i in range(self.nn[0])] for index in range(self.m)]
        self.v = [[abs(v[index][i]) % 2 if z2 else v[index][i] for i in range(self.nn[1])] for index in range(self.m)]
        self.w = [[abs(w[index][i]) % 2 if z2 else w[index][i] for i in range(self.nn[2])] for index in range(self.m)]

        if validate:
            self.__validate()

    @classmethod
    def naive(cls, n1: int, n2: int, n3: int, z2: bool) -> "Scheme":
        m = n1 * n2 * n3
        u = [[0 for _ in range(n1 * n2)] for _ in range(m)]
        v = [[0 for _ in range(n2 * n3)] for _ in range(m)]
        w = [[0 for _ in range(n3 * n1)] for _ in range(m)]

        for i in range(n1):
            for j in range(n3):
                for k in range(n2):
                    index = (i * n3 + j) * n2 + k
                    u[index][i * n2 + k] = 1
                    v[index][k * n3 + j] = 1
                    w[index][j * n1 + i] = 1

        return Scheme(n1=n1, n2=n2, n3=n3, m=m, u=u, v=v, w=w, z2=z2, validate=False)

    def copy(self) -> "Scheme":
        u = [[self.u[index][i] for i in range(self.nn[0])] for index in range(self.m)]
        v = [[self.v[index][i] for i in range(self.nn[1])] for index in range(self.m)]
        w = [[self.w[index][i] for i in range(self.nn[2])] for index in range(self.m)]
        return Scheme(n1=self.n[0], n2=self.n[1], n3=self.n[2], m=self.m,u=u, v=v, w=w, z2=self.z2, validate=False)

    def save(self, path: str) -> None:
        multiplications = "".join(f'{"," if i > 0 else ""}\n        "{multiplication}"' for i, multiplication in enumerate(self.__get_multiplications()))
        elements = "".join(f'{"," if i > 0 else ""}\n        "{element}"' for i, element in enumerate(self.__get_elements()))

        u = pretty_matrix(self.u, '"u":', "    ")
        v = pretty_matrix(self.v, '"v":', "    ")
        w = pretty_matrix(self.w, '"w":', "    ")

        with open(path, "w", encoding="utf-8") as f:
            f.write("{\n")
            f.write(f'    "n": {self.n},\n')
            f.write(f'    "m": {self.m},\n')
            f.write(f'    "z2": {"true" if self.z2 else "false"},\n')
            f.write(f'    "multiplications": [{multiplications}\n')
            f.write(f'    ],\n')
            f.write(f'    "elements": [{elements}\n')
            f.write(f'    ],\n')
            f.write(f'    {u},\n')
            f.write(f'    {v},\n')
            f.write(f'    {w}')

            if self.z2:
                f.write(",\n")
                f.write(f'    "invariant_f": "{self.invariant_f()}",\n')
                f.write(f'    "invariant_g": "{self.invariant_g()}",\n')
                f.write(f'    "type": "{self.invariant_type()}"')

            f.write("\n")
            f.write("}\n")

    @classmethod
    def load(cls, path: str, validate: bool = True) -> "Scheme":
        lower_path = path.lower()

        if lower_path.endswith(".exp"):
            return Scheme.from_exp(path, validate=validate)

        if lower_path.endswith(".m"):
            return Scheme.from_m(path, validate=validate)

        if lower_path.endswith("lrp.mpl"):
            return Scheme.from_lrp_mpl(path, validate=validate)

        if lower_path.endswith("tensor.mpl"):
            return Scheme.from_tensor_mpl(path, validate=validate)

        if lower_path.endswith(".json"):
            return Scheme.from_json(path, validate=validate)

        raise ValueError(f'Invalid extension "{path}"')

    @classmethod
    def from_json(cls, path: str, validate: bool = True) -> "Scheme":
        with open(path, "r") as f:
            data = json.load(f)

        n1, n2, n3 = data["n"]
        m = data["m"]
        z2 = data.get("z2", False)

        u = [[cls.__parse_value(value) for value in row] for row in data["u"]]
        v = [[cls.__parse_value(value) for value in row] for row in data["v"]]
        w = [[cls.__parse_value(value) for value in row] for row in data["w"]]
        return Scheme(n1=n1, n2=n2, n3=n3, m=m, z2=z2, u=u, v=v, w=w, validate=validate)

    @classmethod
    def from_lrp_mpl(cls, path: str, validate: bool = True) -> "Scheme":
        match = re.search(r"(?P<n1>\d+)x(?P<n2>\d+)x(?P<n3>\d+)_LRP.mpl", path)
        n1 = int(match.group("n1"))
        n2 = int(match.group("n2"))
        n3 = int(match.group("n3"))

        with open(path, "r") as f:
            text = f.read()

        mu, mv, mw = re.findall(r"\[\[.*?]]", text)
        u, v, w = json.loads(mu), json.loads(mv), json.loads(mw)
        m = len(u)
        z2 = all(value == 0 or value == 1 for matrix in [u, v, w] for row in matrix for value in row)

        u = [[u[index][j * n1 + i] for i in range(n1) for j in range(n2)] for index in range(m)]
        v = [[v[index][j * n2 + i] for i in range(n2) for j in range(n3)] for index in range(m)]
        w = [[w[j * n3 + i][index] for i in range(n3) for j in range(n1)] for index in range(m)]
        return Scheme(n1=n1, n2=n2, n3=n3, m=m, z2=z2, u=u, v=v, w=w, validate=validate)

    @classmethod
    def from_tensor_mpl(cls, path: str, validate: bool = True) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            text = f.read()

        a = re.search(r"A:=Matrix\((?P<rows>\d+), (?P<columns>\d+)", text)
        b = re.search(r"B:=Matrix\((?P<rows>\d+), (?P<columns>\d+)", text)
        c = re.search(r"C:=Matrix\((?P<rows>\d+), (?P<columns>\d+)", text)

        triads = re.findall(r"Triad\(\[Matrix\(.+?\), Matrix\(.+?\), Matrix\(.+?\)]\)", text)
        m = len(triads)
        n1, n2, n3 = int(a.group("rows")), int(b.group("rows")), int(c.group("rows"))

        u = [[0 for _ in range(n1 * n2)] for _ in range(m)]
        v = [[0 for _ in range(n2 * n3)] for _ in range(m)]
        w = [[0 for _ in range(n3 * n1)] for _ in range(m)]

        for index, triad in enumerate(triads):
            triad = re.sub(r"(-?\d+/\d+)", r'Fraction("\1")', triad)
            a, b, c = [eval(matrix) for matrix in re.findall(r"Matrix\(\d+, \d+, (?P<values>\[.+?])\)", triad)]

            for i in range(n1):
                for j in range(n2):
                    u[index][i * n2 + j] = a[i][j]

            for i in range(n2):
                for j in range(n3):
                    v[index][i * n3 + j] = b[i][j]

            for i in range(n3):
                for j in range(n1):
                    w[index][i * n1 + j] = c[i][j]

        return Scheme(n1=n1, n2=n2, n3=n3, m=m, u=u, v=v, w=w, z2=False, validate=validate)

    @classmethod
    def from_exp(cls, path: str, validate: bool = True) -> "Scheme":
        # TODO: fractions
        with open(path, "r") as f:
            text = f.read()
            z2 = re.search(r"-[abc]", text) is None
            lines = [line.replace(" ", "") for line in text.splitlines() if line.strip()]

        m = len(lines)
        n1, n2, n3 = 0, 0, 0
        u = [{} for _ in range(m)]
        v = [{} for _ in range(m)]
        w = [{} for _ in range(m)]

        for index, line in enumerate(lines):
            for sign, matrix, row, column in re.findall(r"(?P<sign>[-+]?\d*)?\*?(?P<matrix>[abc])(?P<row>\d)(?P<column>\d)", line):
                row, column = int(row), int(column)
                sign = {"": 1, "+": 1, "-": -1}[sign] if sign in {"", "+", "-"} else int(sign)

                if matrix == "a":
                    u[index][(row - 1, column - 1)] = abs(sign) % 2 if z2 else sign
                    n1 = max(n1, row)
                    n2 = max(n2, column)
                elif matrix == "b":
                    v[index][(row - 1, column - 1)] = abs(sign) % 2 if z2 else sign
                    n2 = max(n2, row)
                    n3 = max(n3, column)
                else:
                    w[index][(row - 1, column - 1)] = abs(sign) % 2 if z2 else sign
                    n1 = max(n1, column)
                    n3 = max(n3, row)

        u = [[u[index].get((i, j), 0) for i in range(n1) for j in range(n2)] for index in range(m)]
        v = [[v[index].get((i, j), 0) for i in range(n2) for j in range(n3)] for index in range(m)]
        w = [[w[index].get((i, j), 0) for i in range(n3) for j in range(n1)] for index in range(m)]

        return Scheme(n1=n1, n2=n2, n3=n3, m=m, u=u, v=v, w=w, z2=z2, validate=validate)

    @classmethod
    def from_m(cls, path: str, validate: bool = True) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            text = f.read().replace("{", "[").replace("}", "]")

        text = re.sub(r"(-?\d+/\d+)", r'Fraction("\1")', text)
        data = eval(text)

        a, b, c = data[0]
        n1 = len(a)
        n2 = len(b)
        n3 = len(b[0])
        z2 = all(value == 0 or value == 1 for data_row in data for matrix in data_row for row in matrix for value in row)

        u, v, w = [], [], []
        for index, row in enumerate(data):
            u.append([abs(row[0][i][j]) if z2 else row[0][i][j] for i in range(n1) for j in range(n2)])
            v.append([abs(row[1][i][j]) if z2 else row[1][i][j] for i in range(n2) for j in range(n3)])
            w.append([abs(row[2][i][j]) if z2 else row[2][i][j] for i in range(n3) for j in range(n1)])

        return Scheme(n1=n1, n2=n2, n3=n3, m=len(data), u=u, v=v, w=w, z2=z2, validate=validate)

    def to_z2(self) -> "Scheme":
        u = [[abs(self.u[index][i]) % 2 for i in range(self.nn[0])] for index in range(self.m)]
        v = [[abs(self.v[index][i]) % 2 for i in range(self.nn[1])] for index in range(self.m)]
        w = [[abs(self.w[index][i]) % 2 for i in range(self.nn[2])] for index in range(self.m)]
        return Scheme(n1=self.n[0], n2=self.n[1], n3=self.n[2], m=self.m, u=u, v=v, w=w, z2=True)

    def show(self) -> None:
        print(f"n: {self.n[0]}{self.n[1]}{self.n[2]}, m: {self.m}")
        print("\n".join(self.__get_multiplications()))
        print("\n".join(self.__get_elements()))

    def show_tensors(self) -> None:
        print("\n".join(self.__get_tensors()))

    def to_cpp(self, den: int = 1) -> str:
        u = " ".join(f'{" ".join(str(int(self.u[index][i] * den)) for i in range(self.nn[0]))}' for index in range(self.m))
        v = " ".join(f'{" ".join(str(int(self.v[index][i] * den)) for i in range(self.nn[1]))}' for index in range(self.m))
        w = " ".join(f'{" ".join(str(int(self.w[index][i] * den)) for i in range(self.nn[2]))}' for index in range(self.m))
        n1, n2, n3 = self.n
        return f"{n1} {n2} {n3} {self.m}\n{u}\n{v}\n{w}"

    def invariant_f(self) -> str:
        ranks: Dict[tuple, int] = defaultdict(int)

        for index in range(self.m):
            rank_a = self.__get_rank(self.u[index], self.n[0], self.n[1])
            rank_b = self.__get_rank(self.v[index], self.n[1], self.n[2])
            rank_c = self.__get_rank(self.w[index], self.n[2], self.n[0])

            for (a, b, c) in permutations([rank_a, rank_b, rank_c], r=3):
                ranks[(a, b, c)] += 1

        sorted_ranks = sorted(ranks.items(), key=lambda v: (sum(v[0]), sum(v[0][:2]), v[0]), reverse=True)
        coefficients = [f'{self.__pc(count)}{self.__pp("x", rank_a)}{self.__pp("y", rank_b)}{self.__pp("z", rank_c)}' for (rank_a, rank_b, rank_c), count in sorted_ranks]
        return " + ".join(coefficients)

    def invariant_g(self) -> str:
        ranks: Dict[int, int] = defaultdict(int)

        ranks[sum(self.__get_rank(self.u[index], self.n[0], self.n[1]) for index in range(self.m))] += 1
        ranks[sum(self.__get_rank(self.v[index], self.n[1], self.n[2]) for index in range(self.m))] += 1
        ranks[sum(self.__get_rank(self.w[index], self.n[2], self.n[0]) for index in range(self.m))] += 1

        sorted_ranks = sorted(ranks.items(), key=lambda v: v[0], reverse=True)
        coefficients = [f'{self.__pc(count)}{self.__pp("w", rank)}' for rank, count in sorted_ranks]
        return " + ".join(coefficients)

    def invariant_type(self) -> str:
        ranks = []

        for index in range(self.m):
            u = self.__get_rank(self.u[index], self.n[0], self.n[1])
            v = self.__get_rank(self.v[index], self.n[1], self.n[2])
            w = self.__get_rank(self.w[index], self.n[2], self.n[0])
            ranks.append((u, v, w))

        powers: Dict[tuple, int] = defaultdict(int)

        for a, b, c in sorted(ranks):
            powers[(a, b, c)] += 1

        sorted_ranks = sorted(powers.items(), key=lambda v: (sum(v[0]), sum(v[0][:2]), v[0]), reverse=True)
        coefficients = [f'{self.__pc(count)}{self.__pp("X", rank_a)}{self.__pp("Y", rank_b)}{self.__pp("Z", rank_c)}' for (rank_a, rank_b, rank_c), count in sorted_ranks]
        return " + ".join(coefficients)

    def complexity(self) -> int:
        u_ones = sum(bool(value) for row in self.u for value in row)
        v_ones = sum(bool(value) for row in self.v for value in row)
        w_ones = sum(bool(value) for row in self.w for value in row)
        return u_ones + v_ones + w_ones - self.m * 2 - self.nn[2]

    def get_key(self, sort: bool) -> str:
        n = sorted(self.n) if sort else self.n
        return f"{n[0]}x{n[1]}x{n[2]}"

    def swap_basis_rows(self, i1: int, i2: int) -> None:
        if i1 == i2:
            return

        i_map = {i1: i2, i2: i1}
        self.u = [[self.u[index][i_map.get(i, i) * self.n[1] + j] for i in range(self.n[0]) for j in range(self.n[1])] for index in range(self.m)]
        self.w = [[self.w[index][i * self.n[0] + i_map.get(j, j)] for i in range(self.n[2]) for j in range(self.n[0])] for index in range(self.m)]

    def swap_basis_columns(self, j1: int, j2: int) -> None:
        if j1 == j2:
            return

        j_map = {j1: j2, j2: j1}
        self.v = [[self.v[index][i * self.n[2] + j_map.get(j, j)] for i in range(self.n[1]) for j in range(self.n[2])] for index in range(self.m)]
        self.w = [[self.w[index][j_map.get(i, i) * self.n[0] + j] for i in range(self.n[2]) for j in range(self.n[0])] for index in range(self.m)]

    def multiply_row(self, index, alpha: Union[int, Fraction], beta: Union[int, Fraction], gamma: Union[int, Fraction]) -> None:
        if alpha * beta * gamma != 1:
            raise ValueError(f'Invalid row multiplication coefficients')

        for i in range(self.nn[0]):
            self.u[index][i] *= alpha

        for i in range(self.nn[1]):
            self.v[index][i] *= beta

        for i in range(self.nn[2]):
            self.w[index][i] *= gamma

        self.__validate()

    def minimize_additions(self) -> int:
        greedy = True

        max_size = 5
        uv_max_size = min(max_size, self.m)
        w_max_size = min(max_size, self.nn[2])
        loops = 25

        u_minimization = AdditionMinimization(self.u, name="u", var_names=[f"a{i + 1}{j + 1}" for i in range(self.n[0]) for j in range(self.n[1])], max_size=uv_max_size)
        v_minimization = AdditionMinimization(self.v, name="v", var_names=[f"b{i + 1}{j + 1}" for i in range(self.n[1]) for j in range(self.n[2])], max_size=uv_max_size)
        w_minimization = AdditionMinimization([[self.w[index][i] for index in range(self.m)] for i in range(self.nn[2])], name="w", var_names=[f"m{i + 1}" for i in range(self.m)], max_size=w_max_size)

        u_indices, u_vars, u_additions = u_minimization.solve(greedy, loops=loops)
        v_indices, v_vars, v_additions = v_minimization.solve(greedy, loops=loops)
        w_indices, w_vars, w_additions = w_minimization.solve(greedy, loops=loops)
        complexity = u_additions + v_additions + w_additions

        # self.show()
        # u_minimization.show(u_vars, u_indices)
        # print("---------------------------------------")
        # v_minimization.show(v_vars, v_indices)
        # print("---------------------------------------")
        # w_minimization.show(w_vars, w_indices)
        # print(f"{self.complexity()} vs {complexity}")
        return complexity

    def sort(self) -> None:
        while not self.__check_ordering():
            if random.random() < 0.5:
                i1 = random.randint(0, self.n[0] - 1)
                i2 = random.randint(0, self.n[0] - 1)
                self.swap_basis_rows(i1, i2)

            if random.random() < 0.5:
                j1 = random.randint(0, self.n[2] - 1)
                j2 = random.randint(0, self.n[2] - 1)
                self.swap_basis_columns(j1, j2)

            self.sort_multiplications()

    def sort_multiplications(self) -> None:
        indices = sorted(range(self.m), key=lambda index: self.u[index] + self.v[index] + self.w[index])

        self.u = [self.u[index] for index in indices]
        self.v = [self.v[index] for index in indices]
        self.w = [self.w[index] for index in indices]

    def is_ternary(self) -> bool:
        if self.z2 or self.is_rational():
            return False

        values = [value for row in self.u + self.v + self.w for value in row]
        return min(values) == -1 and max(values) == 1

    def is_rational(self) -> bool:
        if self.z2:
            return False

        values = [value for row in self.u + self.v + self.w for value in row]
        return any(isinstance(value, Fraction) and value.denominator != 1 for value in values)

    def get_ring(self) -> str:
        if self.z2:
            return "Z2"

        values = [value for row in self.u + self.v + self.w for value in row]

        if any(isinstance(value, Fraction) and value.denominator != 1 for value in values):
            return "Q"

        if min(values) == -1 and max(values) == 1:
            return "ZT"

        return "Z"

    def double(self, p: int) -> None:
        n = [self.n[0], self.n[1], self.n[2]]
        n[p] *= 2

        nn = [n[0] * n[1], n[1] * n[2], n[2] * n[0]]
        m = self.m * 2

        u = [[0 for _ in range(nn[0])] for _ in range(m)]
        v = [[0 for _ in range(nn[1])] for _ in range(m)]
        w = [[0 for _ in range(nn[2])] for _ in range(m)]

        d0 = self.n[0] if p == 0 else 0
        d1 = self.n[1] if p == 1 else 0
        d2 = self.n[2] if p == 2 else 0

        for index in range(self.m):
            for i in range(self.n[0]):
                for j in range(self.n[1]):
                    u[index][i * n[1] + j] = self.u[index][i * self.n[1] + j]
                    u[self.m + index][(i + d0) * n[1] + j + d1] = self.u[index][i * self.n[1] + j]

            for i in range(self.n[1]):
                for j in range(self.n[2]):
                    v[index][i * n[2] + j] = self.v[index][i * self.n[2] + j]
                    v[self.m + index][(i + d1) * n[2] + j + d2] = self.v[index][i * self.n[2] + j]

            for i in range(self.n[2]):
                for j in range(self.n[0]):
                    w[index][i * n[0] + j] = self.w[index][i * self.n[0] + j]
                    w[self.m + index][(i + d2) * n[0] + j + d0] = self.w[index][i * self.n[0] + j]

        self.n = n
        self.nn = nn
        self.m = m

        self.u = u
        self.v = v
        self.w = w
        # self.__validate()

    def can_merge(self, scheme: "Scheme", p: int) -> bool:
        return all(self.n[i] == scheme.n[i] for i in range(3) if i != p)

    def merge(self, scheme: "Scheme", p: int) -> "Scheme":
        for i in range(3):
            if i != p:
                assert self.n[i] == scheme.n[i]

        n = [self.n[i] if i != p else self.n[i] + scheme.n[i] for i in range(3)]
        nn = [n[0] * n[1], n[1] * n[2], n[2] * n[0]]
        m = self.m + scheme.m

        u = [[0 for _ in range(nn[0])] for _ in range(m)]
        v = [[0 for _ in range(nn[1])] for _ in range(m)]
        w = [[0 for _ in range(nn[2])] for _ in range(m)]

        d0 = self.n[0] if p == 0 else 0
        d1 = self.n[1] if p == 1 else 0
        d2 = self.n[2] if p == 2 else 0

        for index in range(self.m):
            for i in range(self.n[0]):
                for j in range(self.n[1]):
                    u[index][i * n[1] + j] = self.u[index][i * self.n[1] + j]

            for i in range(self.n[1]):
                for j in range(self.n[2]):
                    v[index][i * n[2] + j] = self.v[index][i * self.n[2] + j]

            for i in range(self.n[2]):
                for j in range(self.n[0]):
                    w[index][i * n[0] + j] = self.w[index][i * self.n[0] + j]

        for index in range(scheme.m):
            for i in range(scheme.n[0]):
                for j in range(scheme.n[1]):
                    u[self.m + index][(i + d0) * n[1] + j + d1] = scheme.u[index][i * scheme.n[1] + j]

            for i in range(scheme.n[1]):
                for j in range(scheme.n[2]):
                    v[self.m + index][(i + d1) * n[2] + j + d2] = scheme.v[index][i * scheme.n[2] + j]

            for i in range(scheme.n[2]):
                for j in range(scheme.n[0]):
                    w[self.m + index][(i + d2) * n[0] + j + d0] = scheme.w[index][i * scheme.n[0] + j]

        return Scheme(n1=n[0], n2=n[1], n3=n[2], m=m, u=u, v=v, w=w, z2=self.z2, validate=False)

    def product(self, scheme: "Scheme") -> "Scheme":
        if self.z2 != scheme.z2:
            raise ValueError("only one of schemes in z2")

        n = [self.n[i] * scheme.n[i] for i in range(3)]
        nn = [n[i] * n[(i + 1) % 3] for i in range(3)]
        m = self.m * scheme.m

        u = [[0 for _ in range(nn[0])] for _ in range(m)]
        v = [[0 for _ in range(nn[1])] for _ in range(m)]
        w = [[0 for _ in range(nn[2])] for _ in range(m)]
        uvw = [u, v, w]
        uvw1 = [self.u, self.v, self.w]
        uvw2 = [scheme.u, scheme.v, scheme.w]

        for index1 in range(self.m):
            for index2 in range(scheme.m):
                index = index1 * scheme.m + index2

                for p in range(3):
                    p1 = (p + 1) % 3

                    for i in range(self.nn[p]):
                        for j in range(scheme.nn[p]):
                            row1, col1 = i // self.n[p1], i % self.n[p1]
                            row2, col2 = j // scheme.n[p1], j % scheme.n[p1]

                            row = row1 * scheme.n[p] + row2
                            col = col1 * scheme.n[p1] + col2
                            uvw[p][index][row * n[p1] + col] = uvw1[p][index1][i] * uvw2[p][index2][j]

        return Scheme(n1=n[0], n2=n[1], n3=n[2], m=m, u=uvw[0], v=uvw[1], w=uvw[2], z2=self.z2)

    def project(self, p: int, q: int) -> None:
        self.__exclude_row(p, q)
        self.__exclude_column((p + 2) % 3, q)
        self.n[p] -= 1

        for i in range(3):
            self.nn[i] = self.n[i] * self.n[(i + 1) % 3]

        self.__remove_zeroes()

    def extend(self, p: int) -> None:
        n = [self.n[i] for i in range(3)]
        n[p] += 1
        nn = [n[i] * n[(i + 1) % 3] for i in range(3)]

        if p == 0:
            self.__add_row(0)
            self.__add_column(2)

            for i in range(self.n[2]):
                for j in range(self.n[1]):
                    self.__add_triplet(0, 1, 2, self.__one_hot(nn[0], self.n[0] * self.n[1] + j), self.__one_hot(nn[1], j * self.n[2] + i), self.__one_hot(nn[2], i * (self.n[0] + 1) + self.n[0]))
        elif p == 1:
            self.__add_row(1)
            self.__add_column(0)

            for i in range(self.n[0]):
                for j in range(self.n[2]):
                    self.__add_triplet(0, 1, 2, self.__one_hot(nn[0], i * (self.n[1] + 1) + self.n[1]), self.__one_hot(nn[1], self.n[1] * self.n[2] + j), self.__one_hot(nn[2], j * self.n[0] + i))
        elif p == 2:
            self.__add_row(2)
            self.__add_column(1)

            for i in range(self.n[0]):
                for j in range(self.n[1]):
                    self.__add_triplet(0, 1, 2, self.__one_hot(nn[0], i * self.n[1] + j), self.__one_hot(nn[1], j * (self.n[2] + 1) + self.n[2]), self.__one_hot(nn[2], self.n[2] * self.n[0] + i))

        self.n[p] += 1

        for i in range(3):
            self.nn[i] = self.n[i] * self.n[(i + 1) % 3]

        # self.__validate()

    def swap(self, p1: int, p2: int) -> None:
        if p1 > p2:
            p1, p2 = p2, p1

        if p1 == 0 and p2 == 1:
            uvw = [self.u, self.w, self.v]
            n = [self.n[1], self.n[0], self.n[2]]
        elif p1 == 0 and p2 == 2:
            uvw = [self.v, self.u, self.w]
            n = [self.n[2], self.n[1], self.n[0]]
        else:
            uvw = [self.w, self.v, self.u]
            n = [self.n[0], self.n[2], self.n[1]]

        u = [[uvw[0][index][j * n[0] + i] for i in range(n[0]) for j in range(n[1])] for index in range(self.m)]
        v = [[uvw[1][index][j * n[1] + i] for i in range(n[1]) for j in range(n[2])] for index in range(self.m)]
        w = [[uvw[2][index][j * n[2] + i] for i in range(n[2]) for j in range(n[0])] for index in range(self.m)]
        self.u, self.v, self.w = u, v, w
        self.n = n
        self.nn = [n[i] * n[(i + 1) % 3] for i in range(3)]

    def fix_sizes(self) -> None:
        if self.n[0] > self.n[1]:
            self.swap(0, 1)

        if self.n[1] > self.n[2]:
            self.swap(1, 2)

        if self.n[0] > self.n[1]:
            self.swap(0, 1)

        assert sorted(self.n) == self.n

    def set_sizes(self, n1: int, n2: int, n3: int) -> None:
        if self.n == [n1, n3, n2]:
            self.swap(1, 2)
        elif self.n == [n2, n1, n3]:
            self.swap(0, 1)
        elif self.n == [n2, n3, n1]:
            self.swap(0, 1)
            self.swap(0, 2)
        elif self.n == [n3, n1, n2]:
            self.swap(0, 1)
            self.swap(1, 2)
        elif self.n == [n3, n2, n1]:
            self.swap(0, 2)

        assert self.n == [n1, n2, n3]

    def modify_to_sizes(self, n1: int, n2: int, n3: int) -> None:
        n = [n1, n2, n3]

        while self.n != n:
            p = random.choice([i for i in range(3) if self.n[i] != n[i]])

            if self.n[p] > n[p]:
                self.project(p, q=random.randint(0, self.n[p] - 1))
            elif random.random() < 0.5:
                self.double(p)
            else:
                self.extend(p)

    def flip(self, i: int, j: int, k: int, index1: int, index2: int) -> None:
        uvw = [self.u, self.v, self.w]
        assert uvw[i][index1] == uvw[i][index2]

        for index in range(self.nn[j]):
            uvw[j][index1][index] += uvw[j][index2][index]

        for index in range(self.nn[k]):
            uvw[k][index2][index] -= uvw[k][index1][index]

        self.__remove_zeroes()

    def try_flip(self) -> bool:
        candidates = []

        for index1, index2 in itertools.combinations(range(self.m), r=2):
            if self.u[index1] == self.u[index2]:
                if self.___ternary_add(self.v[index1], self.v[index2]) and self.___ternary_sub(self.w[index2], self.w[index1]):
                    candidates.append((0, 1, 2, index1, index2))
                elif self.___ternary_add(self.w[index1], self.w[index2]) and self.___ternary_sub(self.v[index2], self.v[index1]):
                    candidates.append((0, 2, 1, index1, index2))
            elif self.v[index1] == self.v[index2]:
                if self.___ternary_add(self.u[index1], self.u[index2]) and self.___ternary_sub(self.w[index2], self.w[index1]):
                    candidates.append((1, 0, 2, index1, index2))
                elif self.___ternary_add(self.w[index1], self.w[index2]) and self.___ternary_sub(self.u[index2], self.u[index1]):
                    candidates.append((1, 2, 0, index1, index2))
            elif self.w[index1] == self.w[index2]:
                if self.___ternary_add(self.u[index1], self.u[index2]) and self.___ternary_sub(self.v[index2], self.v[index1]):
                    candidates.append((2, 0, 1, index1, index2))
                elif self.___ternary_add(self.v[index1], self.v[index2]) and self.___ternary_sub(self.u[index2], self.u[index1]):
                    candidates.append((2, 1, 0, index1, index2))

        if not candidates:
            return False

        i, j, k, index1, index2 = random.choice(candidates)
        if random.random() < 0.5:
            index1, index2 = index2, index1

        self.flip(i, j, k, index1, index2)
        return True

    def ___ternary_add(self, a: List[int], b: List[int]) -> bool:
        for ai, bi in zip(a, b):
            if not (-1 <= ai + bi <= 1):
                return False

        return True

    def ___ternary_sub(self, a: List[int], b: List[int]) -> bool:
        for ai, bi in zip(a, b):
            if not (-1 <= ai - bi <= 1):
                return False

        return True

    def __eq__(self, scheme: "Scheme") -> bool:
        if self.n != scheme.n or self.m != scheme.m:
            return False

        for index in range(self.m):
            if self.u[index] != scheme.u[index]:
                return False

            if self.v[index] != scheme.v[index]:
                return False

            if self.w[index] != scheme.w[index]:
                return False

        return True

    def __validate(self) -> None:
        for i in range(self.nn[0]):
            for j in range(self.nn[1]):
                for k in range(self.nn[2]):
                    assert self.__validate_equation(i, j, k)

    def __validate_equation(self, i: int, j: int, k: int) -> bool:
        i1, i2, j1, j2, k1, k2 = i // self.n[1], i % self.n[1], j // self.n[2], j % self.n[2], k // self.n[0], k % self.n[0]
        target = (i2 == j1) and (i1 == k2) and (j2 == k1)
        equation = 0

        for index in range(self.m):
            equation += self.u[index][i] * self.v[index][j] * self.w[index][k]

        if self.z2:
            equation = abs(equation) % 2

        return equation == target

    @staticmethod
    def __parse_value(value: Union[str, int]) -> Union[int, Fraction]:
        if isinstance(value, str):
            value = Fraction(value)
            if value.denominator == 1:
                value = int(value)

        return value

    def __remove_zeroes(self) -> None:
        non_zero_indices = [index for index in range(self.m) if any(self.u[index]) and any(self.v[index]) and any(self.w[index])]
        self.u = [self.u[index] for index in non_zero_indices]
        self.v = [self.v[index] for index in non_zero_indices]
        self.w = [self.w[index] for index in non_zero_indices]
        self.m = len(non_zero_indices)

    def __add_triplet(self, i: int, j: int, k: int, u: List[int], v: List[int], w: List[int]) -> None:
        uvw = [self.u, self.v, self.w]
        uvw[i].append(u)
        uvw[j].append(v)
        uvw[k].append(w)
        self.m = len(self.u)

    def __exclude_column(self, matrix: int, column: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]
        old_columns = [j for j in range(n2) if j != column]
        uvw = [self.u, self.v, self.w]

        for index in range(self.m):
            uvw[matrix][index] = [uvw[matrix][index][i * n2 + old_j] for i in range(n1) for j, old_j in enumerate(old_columns)]

    def __exclude_row(self, matrix: int, row: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]
        old_rows = [i for i in range(n1) if i != row]
        uvw = [self.u, self.v, self.w]

        for index in range(self.m):
            uvw[matrix][index] = [uvw[matrix][index][old_i * n2 + j] for i, old_i in enumerate(old_rows) for j in range(n2)]

    def __add_column(self, matrix: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]
        uvw = [self.u, self.v, self.w]

        for index in range(self.m):
            values = []
            for i in range(n1):
                for j in range(n2):
                    values.append(uvw[matrix][index][i * n2 + j])

                values.append(0)

            uvw[matrix][index] = values

    def __add_row(self, matrix: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]
        uvw = [self.u, self.v, self.w]

        for index in range(self.m):
            values = []
            for i in range(n1):
                for j in range(n2):
                    values.append(uvw[matrix][index][i * n2 + j])

            for j in range(n2):
                values.append(0)

            uvw[matrix][index] = values

    def __one_hot(self, nn: int, index: int) -> List[int]:
        matrix = [0 for _ in range(nn)]
        matrix[index] = 1
        return matrix

    def __get_rank(self, matrix: List[int], n1: int, n2: int) -> int:
        matrix = [[abs(matrix[i * n2 + j]) % 2 for j in range(n2)] for i in range(n1)]
        return rank_z2(matrix)

    def __get_tensors(self) -> List[str]:
        return [self.__get_tensor(index) for index in range(self.m)]

    def __get_multiplications(self) -> List[str]:
        return [self.__get_multiplication(index) for index in range(self.m)]

    def __get_elements(self) -> List[str]:
        return [self.__get_element(i, j) for i in range(self.n[0]) for j in range(self.n[2])]

    def __get_tensor(self, index: int) -> str:
        u = self.__get_addition([(self.u[index][i], f"a{i // self.n[1] + 1}{i % self.n[1] + 1}") for i in range(self.nn[0])])
        v = self.__get_addition([(self.v[index][i], f"b{i // self.n[2] + 1}{i % self.n[2] + 1}") for i in range(self.nn[1])])
        w = self.__get_addition([(self.w[index][i], f"c{i % self.n[0] + 1}{i // self.n[0] + 1}") for i in range(self.nn[2])])
        return f"({u})×({v})×({w})"

    def __get_multiplication(self, index: int) -> str:
        product = "∧" if self.z2 else "*"
        alpha = self.__get_addition([(self.u[index][i * self.n[1] + j], f"a{i + 1}{j + 1}") for i in range(self.n[0]) for j in range(self.n[1])])
        beta = self.__get_addition([(self.v[index][i * self.n[2] + j], f"b{i + 1}{j + 1}") for i in range(self.n[1]) for j in range(self.n[2])])
        return f"m{index + 1} = ({alpha}) {product} ({beta})"

    def __get_element(self, i: int, j: int) -> str:
        element = self.__get_addition([(self.w[index][j * self.n[0] + i], f"m{index + 1}") for index in range(self.m)])
        return f"c{i + 1}{j + 1} = {element}"

    def __get_addition(self, values: List[Tuple[int, str]]) -> str:
        if self.z2:
            return " ⊕ ".join(name for value, name in values if value)

        addition = []

        for value, name in values:
            if not value:
                continue

            coefficient = "" if abs(value) == 1 else f"{abs(value)}"

            if not addition:
                addition.append(f"{coefficient}{name}" if value > 0 else f"-{coefficient}{name}")
            else:
                addition.append(f"+ {coefficient}{name}" if value > 0 else f"- {coefficient}{name}")

        return " ".join(addition)

    def __pp(self, name: str, power: int) -> str:
        if power == 0:
            return ""

        if power == 1:
            return name

        return f"{name}^{power}"

    def __pc(self, count: int) -> str:
        if count == 1:
            return ""

        return str(count)

    def __check_ordering(self) -> bool:
        return self.__check_basis_ordering() and self.__check_multiplications_ordering()

    def __check_multiplications_ordering(self) -> bool:
        rows = [self.u[index] + self.v[index] + self.w[index] for index in range(self.m)]

        for index in range(1, self.m):
            if rows[index - 1] >= rows[index]:
                return False

        return True

    def __check_basis_ordering(self) -> bool:
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

        for i in range(1, self.n[0]):
            if rows[i - 1] > rows[i]:
                return False

        for i in range(1, self.n[2]):
            if columns[i - 1] > columns[i]:
                return False

        return True

    def __get_row(self, matrix: List[List[int]], index: int, row: int, n1: int, n2: int) -> List[int]:
        return [matrix[index][row * n2 + j] for j in range(n2)]

    def __get_column(self, matrix: List[List[int]], index: int, column: int, n1: int, n2: int) -> List[int]:
        return [matrix[index][i * n2 + column] for i in range(n1)]
