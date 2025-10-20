import json
from collections import defaultdict
from itertools import combinations, permutations
from typing import Dict, List, Set, Tuple

from src.utils.algebra import get_rank
from src.utils.utils import parse_value, pretty_matrix


class Model:
    def __init__(self, n: int, m: int, u: List[List[bool]], v: List[List[bool]], w: List[List[bool]]) -> None:
        self.n = n
        self.m = m
        self.nn = self.n * self.n

        self.u = u
        self.v = v
        self.w = w

        assert len(u) == len(v) == len(w) == self.m
        assert len(u[0]) == len(v[0]) == len(w[0]) == self.nn

        self.__validate()

    @classmethod
    def from_solution(cls, path: str) -> "Model":
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

        return Model(n=n, m=m, u=u, v=v, w=w)

    @classmethod
    def from_exp(cls, path: str) -> "Model":
        n = 3
        m = 23

        with open(path, encoding="utf-8") as f:
            lines = f.read().strip().replace("-", "+").replace("(+", "(").replace(" ", "").splitlines()

        assert len(lines) == m

        u = [[False for _ in range(n * n)] for _ in range(m)]
        v = [[False for _ in range(n * n)] for _ in range(m)]
        w = [[False for _ in range(n * n)] for _ in range(m)]

        for index in range(m):
            alpha, beta, gamma = [v[1:-1].split("+") for v in lines[index].split("*")]

            for a, i, j in alpha:
                u[index][(int(i) - 1) * n + int(j) - 1] = True

            for b, i, j in beta:
                v[index][(int(i) - 1) * n + int(j) - 1] = True

            for c, i, j in gamma:
                w[index][(int(i) - 1) * n + int(j) - 1] = True

        return Model(n=n, m=m, u=u, v=v, w=w)

    @classmethod
    def load(cls, path: str) -> "Model":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        u = [[value != 0 for value in row] for row in data["u"]]
        v = [[value != 0 for value in row] for row in data["v"]]
        w = [[value != 0 for value in row] for row in data["w"]]
        model = Model(n=data["n"], m=data["m"], u=u, v=v, w=w)
        return model

    def save(self, path: str) -> None:
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
            f.write(f'    {u},\n')
            f.write(f'    {v},\n')
            f.write(f'    {w},\n')
            f.write(f'    "invariant_f": "{self.invariant_f()}",\n')
            f.write(f'    "invariant_g": "{self.invariant_g()}",\n')
            f.write(f'    "invariant_h": "{self.invariant_h()}",\n')
            f.write(f'    "weight": {self.weight()},\n'),
            f.write(f'    "complexity": {self.complexity()},\n')
            f.write(f'    "u_ones": {u_ones},\n')
            f.write(f'    "v_ones": {v_ones},\n')
            f.write(f'    "w_ones": {w_ones},\n')
            f.write(f'    "multiplications": [{"".join(multiplications)}\n')
            f.write(f'    ],\n')
            f.write(f'    "elements": [{"".join(elements)}\n')
            f.write(f'    ]\n')
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

    def show_params(self) -> None:
        print(f"- ones: {self.ones()}")
        print(f"- weight: {self.weight()}")
        print(f"- complexity: {self.complexity()}")

    def sort(self) -> None:
        for i1 in range(self.n):
            for i2 in range(self.n):
                for j1 in range(self.n):
                    for j2 in range(self.n):
                        self.swap_basis_rows(i1, i2)
                        self.swap_basis_columns(j1, j2)
                        self.sort_cycle_shift()
                        self.sort_multiplications()

                        if self.__check_ordering():
                            # self.__show_ordering()
                            return

        # self.__show_ordering()
        assert self.__check_ordering()

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

    def sort_cycle_shift(self) -> None:
        uvw = self.__flatten(self.u + self.v + self.w)
        wuv = self.__flatten(self.w + self.u + self.v)
        vwu = self.__flatten(self.v + self.w + self.u)

        if wuv <= uvw and wuv <= vwu:
            self.u, self.v, self.w = self.w, self.u, self.v
        elif vwu <= uvw and vwu <= wuv:
            self.u, self.v, self.w = self.v, self.w, self.u

    def sort_multiplications(self) -> None:
        indices = sorted(range(self.m), key=lambda index: self.__get_order(index))

        self.u = [self.u[index] for index in indices]
        self.v = [self.v[index] for index in indices]
        self.w = [self.w[index] for index in indices]

    def addition_statistics(self) -> dict:
        u_indices = [{i for i in range(self.nn) if self.u[index][i]} for index in range(self.m)]
        v_indices = [{i for i in range(self.nn) if self.v[index][i]} for index in range(self.m)]
        w_indices = [{index for index in range(self.m) if self.w[index][i]} for i in range(self.nn)]

        return {
            "u": self.__addition_analytics(u_indices),
            "v": self.__addition_analytics(v_indices),
            "w": self.__addition_analytics(w_indices)
        }

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

        sorted_ranks = sorted(ranks.items(), key=lambda v: (sum(v[0]), *v[0]), reverse=True)
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
                        terms[term_power] += int(self.u[index][i] and self.v[index][j] and self.w[index][k])

        coefficients = [f'{self.__pc(terms[rank])}{self.__pp("t", rank)}' for rank in range(3, -1, -1)]
        return f'{" + ".join(coefficients)} ({sum(terms)})'

    def weight(self) -> int:
        terms = 0

        for i in range(self.nn):
            for j in range(self.nn):
                for k in range(self.nn):
                    for index in range(self.m):
                        terms += int(self.u[index][i] and self.v[index][j] and self.w[index][k])

        return terms

    def ones(self) -> Tuple[int, int, int]:
        u_ones = sum(self.__flatten(self.u))
        v_ones = sum(self.__flatten(self.v))
        w_ones = sum(self.__flatten(self.w))
        return u_ones, v_ones, w_ones

    def complexity(self) -> int:
        u_ones, v_ones, w_ones = self.ones()
        return u_ones + v_ones + w_ones - self.m * 2 - self.nn

    def column_ones(self) -> Tuple[List[int], List[int], List[int]]:
        u_ones = [sum(self.u[index][i] for index in range(self.m)) for i in range(self.nn)]
        v_ones = [sum(self.v[index][i] for index in range(self.m)) for i in range(self.nn)]
        w_ones = [sum(self.w[index][i] for index in range(self.m)) for i in range(self.nn)]
        return u_ones, v_ones, w_ones

    def __get_multiplication(self, index: int) -> str:
        alpha = " ⊕ ".join([f"a{i + 1}{j + 1}" for i in range(self.n) for j in range(self.n) if self.u[index][i * self.n + j]])
        beta = " ⊕ ".join([f"b{i + 1}{j + 1}" for i in range(self.n) for j in range(self.n) if self.v[index][i * self.n + j]])
        return f"m{index + 1} = ({alpha}) ∧ ({beta})"

    def __get_element(self, i: int, j: int) -> str:
        element_expression = self.__get_element_expression(i, j)
        element = " ⊕ ".join([f"m{index + 1}" for index in range(self.m) if self.w[index][j * self.n + i]])
        return f"c{i + 1}{j + 1} = {element_expression} = {element}"

    def __get_element_expression(self, ci: int, cj: int) -> str:
        used_element = [[False for _ in range(self.nn)] for _ in range(self.nn)]

        for index in range(self.m):
            if not self.w[index][cj * self.n + ci]:
                continue

            for i in range(self.nn):
                for j in range(self.nn):
                    used_element[i][j] ^= self.u[index][i] and self.v[index][j]

        elements = []

        for i in range(self.nn):
            for j in range(self.nn):
                if used_element[i][j]:
                    elements.append(f"a{i // self.n + 1}{i % self.n + 1} ∧ b{j // self.n + 1}{j % self.n + 1}")

        return " ⊕ ".join(elements)

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
            equation ^= self.u[index][i] and self.v[index][j] and self.w[index][k]

        return equation == target

    def __get_rank(self, matrix: List[bool]) -> int:
        matrix = [[matrix[i * self.n + j] for j in range(self.n)] for i in range(self.n)]
        return get_rank(matrix)

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

    def __flatten(self, matrix: List[List[bool]]) -> List[int]:
        return [value for row in matrix for value in row]

    def __get_row(self, matrix: List[List[bool]], index: int, row: int) -> List[int]:
        return [matrix[index][row * self.n + j] for j in range(self.n)]

    def __get_column(self, matrix: List[List[bool]], index: int, column: int) -> List[int]:
        return [matrix[index][i * self.n + column] for i in range(self.n)]

    def __get_order(self, index: int) -> List[int]:
        return self.u[index] + self.v[index]

    def __show_ordering(self) -> None:
        print("ordering:")
        print(f"- multiplications: {self.__check_multiplications_ordering()}")
        print(f"- basis: {self.__check_basis_ordering()}")
        print(f"- cycle shift: {self.__check_cycle_shift_ordering()}")
        print(f"- transpose: {self.__check_transpose_ordering()}")

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
        uvw = self.__flatten(self.u + self.v + self.w)
        wuv = self.__flatten(self.w + self.u + self.v)
        vwu = self.__flatten(self.v + self.w + self.u)
        return uvw <= wuv and uvw <= vwu

    def __check_transpose_ordering(self) -> bool:
        ut = [[self.u[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        vt = [[self.v[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]
        wt = [[self.w[index][j * self.n + i] for i in range(self.n) for j in range(self.n)] for index in range(self.m)]

        uvw = self.__flatten(self.u + self.v + self.w)
        vuw_t = self.__flatten(vt + ut + wt)
        return uvw <= vuw_t

    def __addition_analytics(self, addition_indices: List[Set[int]], max_size: int = 5) -> dict:
        size2count = {size: defaultdict(int) for size in range(2, max_size + 1)}

        for indices in addition_indices:
            for size in range(2, max_size + 1):
                for d in combinations(sorted(indices), r=size):
                    size2count[size][tuple(d)] += 1

        size2count = {size: {d: count for d, count in size2count[size].items() if count > 1} for size in range(2, max_size + 1)}
        size2safe = {}

        for size in range(2, max_size + 1):
            d2safe = {d: (count - 1) * (size - 1) for d, count in size2count[size].items()}
            size2safe[size] = list(dict(sorted(d2safe.items(), key=lambda item: -item[1])[:3]).values())

        return {size: size2safe[size] for size in range(2, max_size + 1)}
