import itertools
import json
import random
import re
from collections import defaultdict
from itertools import permutations
from typing import Dict, List, Tuple, Union

from src.utils.algebra import get_inverse, get_rank
from src.utils.utils import flatten, parse_value, pretty_matrix


class Scheme:
    def __init__(self, n: int, m: int, u: List[List[Union[bool, int]]], v: List[List[Union[bool, int]]], w: List[List[Union[bool, int]]], z2: bool = True) -> None:
        self.n = n
        self.m = m
        self.nn = self.n * self.n
        self.z2 = z2

        self.u = [[u[index][i] for i in range(self.nn)] for index in range(self.m)]
        self.v = [[v[index][i] for i in range(self.nn)] for index in range(self.m)]
        self.w = [[w[index][i] for i in range(self.nn)] for index in range(self.m)]

        assert len(u) == len(v) == len(w) == self.m
        assert len(u[0]) == len(v[0]) == len(w[0]) == self.nn

        self.__validate()

    @classmethod
    def from_solution(cls, path: str) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        n: int = data["n"]
        m: int = data["m"]

        literal2value = {abs(int(literal)): int(literal) > 0 for literal in data["sat"]}

        if data.get("algorithm") == "abcd":
            rank_s, rank_t = data["s"], data["t"]

            a = [[parse_value(data["a"][index][i], literal2value) for i in range(n * n)] for index in range(rank_s)]
            b = [[parse_value(data["b"][index][i], literal2value) for i in range(n * n)] for index in range(rank_t)]
            c = [[parse_value(data["c"][index][i], literal2value) for i in range(n * n)] for index in range(rank_t)]
            d = [[parse_value(data["d"][index][i], literal2value) for i in range(n * n)] for index in range(rank_t)]

            u = a + b + c + d
            v = a + d + b + c
            w = a + c + d + b
        else:
            u = [[parse_value(data["u"][index][i], literal2value) for i in range(n * n)] for index in range(m)]
            v = [[parse_value(data["v"][index][i], literal2value) for i in range(n * n)] for index in range(m)]
            w = [[parse_value(data["w"][index][i], literal2value) for i in range(n * n)] for index in range(m)]

        return Scheme(n=n, m=m, u=u, v=v, w=w, z2=True)

    @classmethod
    def from_exp(cls, path: str, n: int, z2: bool = True) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            lines = f.read().strip().replace("(a", "(+a").replace("(b", "(+b").replace("(c", "(+c").replace(" ", "").splitlines()

        m = len(lines)

        u = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]
        v = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]
        w = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]

        for index, line in enumerate(lines):
            alpha, beta, gamma = [re.findall(r"[-+]\d?\*?[abc]\d\d", v[1:-1]) for v in re.findall(rf"\(.*?\)", lines[index])]

            for alpha_i in alpha:
                i, j, value = cls.__parse_exp_row(alpha_i, z2)
                u[index][i * n + j] = value

            for beta_i in beta:
                i, j, value = cls.__parse_exp_row(beta_i, z2)
                v[index][i * n + j] = value

            for gamma_i in gamma:
                i, j, value = cls.__parse_exp_row(gamma_i, z2)
                w[index][i * n + j] = value

        return Scheme(n=n, m=m, u=u, v=v, w=w, z2=z2)

    @staticmethod
    def __parse_exp_row(element: str, z2: bool) -> Tuple[int, int, Union[bool, int]]:
        if len(element) == 6:
            sign, value, _, a, i, j = element
        else:
            sign, a, i, j = element
            value = 1

        sign2value = {"+": 1, "-": -1}

        return int(i) - 1, int(j) - 1, abs(int(value)) %2 != 0 if z2 else sign2value[sign] * int(value)

    @classmethod
    def from_m(cls, path: str, z2: bool = True) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            text = f.read().replace("{", "[").replace("}", "]")

        data = json.loads(text)
        m = len(data)
        n = len(data[0][0])

        u = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]
        v = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]
        w = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]

        for index, row in enumerate(data):
            for i in range(n):
                for j in range(n):
                    u[index][i * n + j] = abs(row[0][i][j]) % 2 != 0 if z2 else row[0][i][j]
                    v[index][i * n + j] = abs(row[1][i][j]) % 2 != 0 if z2 else row[1][i][j]
                    w[index][i * n + j] = abs(row[2][i][j]) % 2 != 0 if z2 else row[2][i][j]

        return Scheme(n=n, m=m, u=u, v=v, w=w, z2=z2)

    @classmethod
    def from_plain_text(cls, path: str, n: int, m: int, z2: bool) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            lines = f.read().strip().replace("(a", "(+a").replace("(b", "(+b").splitlines()

        u = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]
        v = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]
        w = [[False if z2 else 0 for _ in range(n * n)] for _ in range(m)]

        for line in lines:
            match = re.match(r"^P(?P<index>\d\d)\s*:=\s*\((?P<a>[^)]+)\)\s*\*\s*\((?P<b>[^)]+)\)", line)
            if match:
                index = int(match.group("index")) - 1
                a, b = match.group("a"), match.group("b")

                for element in re.findall(r"[-+]\d?\*?[abc]\d\d", match.group("a")):
                    i, j, value = cls.__parse_exp_row(element, z2)
                    u[index][i * n + j] = value

                for element in re.findall(r"[-+]\d?\*?[abc]\d\d", match.group("b")):
                    i, j, value = cls.__parse_exp_row(element, z2)
                    v[index][i * n + j] = value

                continue

            match = re.match(r"^c(?P<i>\d)(?P<j>\d)\s*:=\s*(?P<multiplications>.+);", line)
            if match:
                i, j = int(match.group("i")) - 1, int(match.group("j")) - 1
                for multiplication in re.findall(r"[+-]?P\d+", match.group("multiplications")):
                    if multiplication.startswith("P"):
                        sign = 1
                        index = int(multiplication[1:]) - 1
                    else:
                        sign = 1 if multiplication[0] == "+" else -1
                        index = int(multiplication[2:]) - 1

                    w[index][j * n + i] = abs(sign) % 2 != 0 if z2 else sign

        return Scheme(n=n, m=m, u=u, v=v, w=w, z2=z2)

    @classmethod
    def load(cls, path: str) -> "Scheme":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        z2 = data.get("z2", True)
        value_type = bool if z2 else int
        u = [[value_type(value) for value in row] for row in data["u"]]
        v = [[value_type(value) for value in row] for row in data["v"]]
        w = [[value_type(value) for value in row] for row in data["w"]]
        return Scheme(n=data["n"], m=data["m"], u=u, v=v, w=w, z2=z2)

    def to_z2(self) -> "Scheme":
        u = [[abs(self.u[index][i]) % 2 != 0 for i in range(self.nn)] for index in range(self.m)]
        v = [[abs(self.v[index][i]) % 2 != 0 for i in range(self.nn)] for index in range(self.m)]
        w = [[abs(self.w[index][i]) % 2 != 0 for i in range(self.nn)] for index in range(self.m)]
        return Scheme(n=self.n, m=self.m, u=u, v=v, w=w, z2=True)

    def copy(self) -> "Scheme":
        return Scheme(n=self.n, m=self.m, u=self.u, v=self.v, w=self.w, z2=self.z2)

    def save(self, path: str) -> None:
        u = pretty_matrix(self.u, '"u":', "    ")
        v = pretty_matrix(self.v, '"v":', "    ")
        w = pretty_matrix(self.w, '"w":', "    ")
        ranks = pretty_matrix(self.ranks(), '"ranks":', "    ")

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
            f.write(f'    "type": "base",\n')
            f.write(f'    "multiplications": [{"".join(multiplications)}\n')
            f.write(f'    ],\n')
            f.write(f'    "elements": [{"".join(elements)}\n')
            f.write(f'    ],\n')
            f.write(f'    {u},\n')
            f.write(f'    {v},\n')
            f.write(f'    {w},\n')
            f.write(f'    "invariant_f": "{self.invariant_f()}",\n')
            f.write(f'    "invariant_g": "{self.invariant_g()}",\n')
            f.write(f'    "invariant_h": "{self.invariant_h()}",\n')
            f.write(f'    "rank_pattern": "{self.invariant_rank_pattern()}",\n')
            f.write(f'    "weight": {self.weight()},\n'),
            f.write(f'    "complexity": {self.complexity()},\n')
            f.write(f'    {ranks},\n')
            f.write(f'    "u_ones": {u_ones},\n')
            f.write(f'    "v_ones": {v_ones},\n')
            f.write(f'    "w_ones": {w_ones}\n')
            f.write("}\n")

    def show(self, matrices: bool = False, invariants: bool = True, params: bool = True) -> None:
        print(f"n: {self.n}, m: {self.m}")

        if matrices:
            self.show_matrices()

        print("\n".join(self.get_multiplications()))
        print("\n".join([element for row in self.get_elements() for element in row]))

        if invariants:
            self.show_invariants()

        if params:
            self.show_params()

        print("")

    def show_matrices(self) -> None:
        print(pretty_matrix(self.u, "u = "))
        print(pretty_matrix(self.v, "v = "))
        print(pretty_matrix(self.w, "w = "))

    def show_invariants(self) -> None:
        print(f"- f(x,y,z): {self.invariant_f()}")
        print(f"- g(w): {self.invariant_g()}")
        print(f"- h(t): {self.invariant_h()}")
        print(f"- rank pattern: {self.invariant_rank_pattern()}")

    def show_params(self) -> None:
        print(f"- ones: {self.ones()}")
        print(f"- weight: {self.weight()}")
        print(f"- complexity: {self.complexity()}")

    def show_tab(self) -> None:
        for index in range(self.m):
            for i in range(self.n):
                u = " ".join(f"{self.u[index][i * self.n + j]:2d}" for j in range(self.n))
                v = " ".join(f"{self.v[index][i * self.n + j]:2d}" for j in range(self.n))
                w = " ".join(f"{self.w[index][i * self.n + j]:2d}" for j in range(self.n))
                print(f"{u} |{v} |{w}")

            print("+".join(["---" * self.n] * 3))

    def sort(self) -> None:
        while not self.__check_ordering():
            if random.random() < 0.5:
                i1 = random.randint(0, self.n - 1)
                i2 = random.randint(0, self.n - 1)
                self.swap_basis_rows(i1, i2)

            if random.random() < 0.5:
                j1 = random.randint(0, self.n - 1)
                j2 = random.randint(0, self.n - 1)
                self.swap_basis_columns(j1, j2)

            if random.random() < 0.5:
                self.cycle_shift()

            self.sort_multiplications()

    def transpose(self) -> None:
        ut = [[self.u[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        vt = [[self.v[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        wt = [[self.w[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]

        self.u = vt
        self.v = ut
        self.w = wt

    def cycle_shift(self) -> None:
        self.u, self.v, self.w = self.v, self.w, self.u

    def swap_basis_rows(self, i1: int, i2: int) -> None:
        if i1 == i2:
            return

        i_map = {i1: i2, i2: i1}
        self.u = [[self.u[index][i_map.get(i, i) * self.n + j] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        self.w = [[self.w[index][i * self.n + i_map.get(j, j)] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]

    def swap_basis_columns(self, j1: int, j2: int) -> None:
        if j1 == j2:
            return

        j_map = {j1: j2, j2: j1}
        self.v = [[self.v[index][i * self.n + j_map.get(j, j)] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        self.w = [[self.w[index][j_map.get(i, i) * self.n + j] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]

    def scale_multiplication(self, index: int, alpha: int, beta: int, gamma: int) -> None:
        if self.z2:
            raise ValueError(f"scale method is not allowed in Z2")

        if alpha * beta * gamma != 1:
            raise ValueError(f"alpha * beta * gamma != 1")

        for i in range(self.nn):
            self.u[index][i] *= alpha
            self.v[index][i] *= beta
            self.w[index][i] *= gamma

        self.__validate()

    def sandwiching(self, u: List[List[int]], v: List[List[int]], w: List[List[int]]) -> None:
        u1 = get_inverse(u, z2=self.z2)
        v1 = get_inverse(v, z2=self.z2)
        w1 = get_inverse(w, z2=self.z2)

        if all(value == 0 for value in flatten(u1)) or all(value == 0 for value in flatten(v1)) or all(value == 0 for value in flatten(w1)):
            print("Invalid inverse matrix")
            return

        for index in range(self.m):
            self.u[index] = self._matmul(self.u[index], u, v1)
            self.v[index] = self._matmul(self.v[index], v, w1)
            self.w[index] = self._matmul(self.w[index], w, u1)

        self.__validate()

    def _matmul(self, matrix: List[Union[bool, int]], left: List[List[int]], right: List[List[int]]) -> List[Union[bool, int]]:
        matrix = [[int(matrix[i * self.n + j]) for j in range(self.n)] for i in range(self.n)]
        result = [[sum(left[i][k] * matrix[k][j] for k in range(self.n)) for j in range(self.n)] for i in range(self.n)]
        result = [[sum(result[i][k] * right[k][j] for k in range(self.n)) for j in range(self.n)] for i in range(self.n)]

        if self.z2:
            result = [abs(value) % 2 != 0 for row in result for value in row]
        else:
            result = [value for row in result for value in row]

        return result

    def sort_cycle_shift(self) -> None:
        uvw = flatten(self.u + self.v + self.w)
        wuv = flatten(self.w + self.u + self.v)
        vwu = flatten(self.v + self.w + self.u)

        if wuv <= uvw and wuv <= vwu:
            self.u, self.v, self.w = self.w, self.u, self.v
        elif vwu <= uvw and vwu <= wuv:
            self.u, self.v, self.w = self.v, self.w, self.u

    def sort_multiplications(self) -> None:
        indices = sorted(range(self.m), key=lambda index: self.__get_order(index))

        self.u = [self.u[index] for index in indices]
        self.v = [self.v[index] for index in indices]
        self.w = [self.w[index] for index in indices]

    def sort_multiplications_by_ranks(self) -> None:
        indices = sorted(range(self.m), key=lambda index: (self.__get_rank(self.u[index]), self.__get_rank(self.v[index]), self.__get_rank(self.w[index])))

        self.u = [self.u[index] for index in indices]
        self.v = [self.v[index] for index in indices]
        self.w = [self.w[index] for index in indices]

    def get_multiplications(self) -> List[str]:
        return [self.__get_multiplication(index) for index in range(self.m)]

    def get_elements(self) -> List[List[str]]:
        return [[self.__get_element(i, j) for j in range(self.n)] for i in range(self.n)]

    def invariant_g(self) -> str:
        ranks: Dict[int, int] = defaultdict(int)

        for matrices in [self.u, self.v, self.w]:
            ranks[sum(self.__get_rank(matrices[index]) for index in range(self.m))] += 1

        sorted_ranks = sorted(ranks.items(), key=lambda v: v[0], reverse=True)
        coefficients = [f'{self.__pc(count)}{self.__pp("w", rank)}' for rank, count in sorted_ranks]
        return " + ".join(coefficients)

    def invariant_f(self) -> str:
        ranks: Dict[tuple, int] = defaultdict(int)

        for index in range(self.m):
            rank_a = self.__get_rank(self.u[index])
            rank_b = self.__get_rank(self.v[index])
            rank_c = self.__get_rank(self.w[index])

            for (a, b, c) in permutations([rank_a, rank_b, rank_c], r=3):
                ranks[(a, b, c)] += 1

        sorted_ranks = sorted(ranks.items(), key=lambda v: (sum(v[0]), sum(v[0][:2]), v[0]), reverse=True)
        coefficients = [f'{self.__pc(count)}{self.__pp("x", rank_a)}{self.__pp("y", rank_b)}{self.__pp("z", rank_c)}' for (rank_a, rank_b, rank_c), count in sorted_ranks]
        return " + ".join(coefficients)

    def invariant_h(self) -> str:
        terms = [0, 0, 0, 0]

        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    i1, i2, j1, j2, k1, k2 = i // self.n, i % self.n, j // self.n, j % self.n, k // self.n, k % self.n
                    term_power = sum([i2 == j1, i1 == k2, j2 == k1])

                    for index in range(self.m):
                        terms[term_power] += int(bool(self.u[index][i]) and bool(self.v[index][j]) and bool(self.w[index][k]))

        coefficients = [f'{self.__pc(terms[rank])}{self.__pp("t", rank)}' for rank in range(3, -1, -1)]
        return f'{" + ".join(coefficients)} ({sum(terms)})'

    def invariant_rank_pattern(self) -> str:
        scheme_ranks = self.ranks()
        permuted_ranks = [sorted((ranks[i], ranks[j], ranks[k]) for ranks in scheme_ranks) for i, j, k in permutations(range(3), r=3)]
        sorted_ranks = max(permuted_ranks, key=lambda ranks: self.__sorted_count(ranks))

        if self.n > 3:
            return str(hash(tuple(sorted_ranks)))

        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ranks2letter = {rank: letters[i] for i, rank in enumerate(itertools.product(range(1, self.n + 1), repeat=3))}

        pattern = "".join(ranks2letter[ranks] for ranks in sorted_ranks)
        matches = [match.group() for match in re.finditer(r"(.)\1+|\w", pattern)]
        return "".join(f'{len(match) if len(match) > 1 else ""}{match[0]}' for match in matches)

    def ranks(self) -> List[Tuple[int, int, int]]:
        return [(self.__get_rank(self.u[index]), self.__get_rank(self.v[index]), self.__get_rank(self.w[index])) for index in range(self.m)]

    def weight(self) -> int:
        terms = 0

        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    for index in range(self.m):
                        terms += int(bool(self.u[index][i]) and bool(self.v[index][j]) and bool(self.w[index][k]))

        return terms

    def ones(self) -> Tuple[int, int, int]:
        u_ones = sum(bool(value) for row in self.u for value in row)
        v_ones = sum(bool(value) for row in self.v for value in row)
        w_ones = sum(bool(value) for row in self.w for value in row)
        return u_ones, v_ones, w_ones

    def complexity(self) -> int:
        u_ones, v_ones, w_ones = self.ones()
        return u_ones + v_ones + w_ones - self.m * 2 - self.nn

    def column_ones(self) -> Tuple[List[int], List[int], List[int]]:
        u_ones = [sum(bool(self.u[index][i]) for index in range(self.m)) for i in range(self.nn)]
        v_ones = [sum(bool(self.v[index][i]) for index in range(self.m)) for i in range(self.nn)]
        w_ones = [sum(bool(self.w[index][i]) for index in range(self.m)) for i in range(self.nn)]
        return u_ones, v_ones, w_ones

    def __hash__(self) -> int:
        elements = "\n".join("\n".join(row) for row in self.get_elements())
        multiplications = "\n".join(self.get_multiplications())
        return hash(f"{elements}\n{multiplications}")

    def __get_multiplication(self, index: int) -> str:
        product = "∧" if self.z2 else "*"
        alpha = self.__get_addition([(self.u[index][i * self.n + j], f"a{i + 1}{j + 1}") for i in range(self.n) for j in range(self.n)])
        beta = self.__get_addition([(self.v[index][i * self.n + j], f"b{i + 1}{j + 1}") for i in range(self.n) for j in range(self.n)])
        return f"m{index + 1} = ({alpha}) {product} ({beta})"

    def __get_element(self, i: int, j: int) -> str:
        element_expression = self.__get_element_expression(i, j)
        element = self.__get_addition([(self.w[index][j * self.n + i], f"m{index + 1}") for index in range(self.m)])
        return f"c{i + 1}{j + 1} = {element_expression} = {element}"

    def __get_element_expression(self, ci: int, cj: int) -> str:
        used_element = [[0 for _ in range(self.nn)] for _ in range(self.nn)]

        for index in range(self.m):
            for i in range(self.nn):
                for j in range(self.nn):
                    used_element[i][j] += self.u[index][i] * self.v[index][j] * self.w[index][cj * self.n + ci]

        elements = []
        product = "∧" if self.z2 else "*"

        for i in range(self.nn):
            for j in range(self.nn):
                if self.z2:
                    used_element[i][j] = abs(used_element[i][j]) % 2

                elements.append((used_element[i][j], f"a{i // self.n + 1}{i % self.n + 1} {product} b{j // self.n + 1}{j % self.n + 1}"))

        return self.__get_addition(elements)

    def __get_addition(self, values: List[Tuple[Union[bool, int], str]]) -> str:
        if self.z2:
            return " ⊕ ".join(name for value, name in values if value)

        addition = []

        for value, name in values:
            if not value:
                continue

            coefficient = "" if abs(value) <= 1 else f"{abs(value)}"

            if not addition:
                addition.append(f"{coefficient}{name}" if value > 0 else f"-{coefficient}{name}")
            else:
                addition.append(f"+ {coefficient}{name}" if value > 0 else f"- {coefficient}{name}")

        return " ".join(addition)

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
            equation += int(self.u[index][i]) * int(self.v[index][j]) * int(self.w[index][k])

        if self.z2:
            equation %= 2

        return equation == target

    def __get_rank(self, matrix: List[bool]) -> int:
        matrix = [[int(matrix[i * self.n + j]) for j in range(self.n)] for i in range(self.n)]
        return get_rank(matrix, z2=self.z2)

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

    def __get_row(self, matrix: List[List[bool]], index: int, row: int) -> List[Union[bool, int]]:
        return [matrix[index][row * self.n + j] for j in range(self.n)]

    def __get_column(self, matrix: List[List[bool]], index: int, column: int) -> List[Union[bool, int]]:
        return [matrix[index][i * self.n + column] for i in range(self.n)]

    def __get_order(self, index: int) -> List[Union[int, bool]]:
        return self.u[index] + self.v[index]

    def __sorted_count(self, ranks: List[Tuple[int, int, int]]) -> tuple:
        ranks = flatten(ranks)
        return tuple(ranks)

    def __check_ordering(self) -> bool:
        checks = [
            self.__check_multiplications_ordering(),
            self.__check_basis_ordering(),
            self.__check_cycle_shift_ordering(),
            self.__check_transpose_ordering()
        ]

        return all(checks)

    def __check_multiplications_ordering(self) -> bool:
        rows = [self.__get_order(index) for index in range(self.m)]

        for index in range(1, self.m):
            if rows[index - 1] >= rows[index]:
                return False

        return True

    def __check_basis_ordering(self) -> bool:
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

        for i in range(1, self.n):
            if rows[i - 1] > rows[i]:
                return False

            if columns[i - 1] > columns[i]:
                return False

        return True

    def __check_cycle_shift_ordering(self) -> bool:
        uvw = flatten(self.u + self.v + self.w)
        wuv = flatten(self.w + self.u + self.v)
        vwu = flatten(self.v + self.w + self.u)
        return uvw <= wuv and uvw <= vwu

    def __check_transpose_ordering(self) -> bool:
        ut = [[self.u[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        vt = [[self.v[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        wt = [[self.w[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]

        uvw = flatten(self.u + self.v + self.w)
        vuw_t = flatten(vt + ut + wt)
        return uvw <= vuw_t
