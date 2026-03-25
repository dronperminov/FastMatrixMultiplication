import itertools
import json
import math
import random
import re
from fractions import Fraction
from itertools import combinations
from typing import List, Optional, Tuple, Union

from src.schemes.scheme import Scheme
from src.utils.algebra import inverse_fraction_matrix


class FractionalScheme:
    def __init__(self, n1: int, n2: int, n3: int, m: int, u: List[List[Fraction]], v: List[List[Fraction]], w: List[List[Fraction]], validate: bool = True) -> None:
        self.n = [n1, n2, n3]
        self.nn = [n1 * n2, n2 * n3, n3 * n1]
        self.m = m

        assert len(u) == len(v) == len(w) == m
        self.uvw = [
            [[Fraction(u[index][i]) for i in range(self.nn[0])] for index in range(self.m)],
            [[Fraction(v[index][i]) for i in range(self.nn[1])] for index in range(self.m)],
            [[Fraction(w[index][i]) for i in range(self.nn[2])] for index in range(self.m)]
        ]

        if validate:
            self.__validate()

    def copy(self) -> "FractionalScheme":
        n1, n2, n3 = self.n
        uvw = [[[Fraction(self.uvw[i][index][j]) for j in range(self.nn[i])] for index in range(self.m)] for i in range(3)]
        return FractionalScheme(n1=n1, n2=n2, n3=n3, m=self.m, u=uvw[0], v=uvw[1], w=uvw[2], validate=False)

    def try_flip(self) -> bool:
        candidates = self.__find_flip_candidates()
        if not candidates:
            return False

        alpha, pv, pw, index1, index2 = random.choice(candidates)
        if random.random() < 0.5:
            pv, pw = pw, pv

        if random.random() < 0.5:
            index1, index2 = index2, index1
            alpha = 1 / alpha

        beta = Fraction(1)
        self.__flip(pv=pv, pw=pw, index1=index1, index2=index2, alpha=alpha, beta=beta)
        return True

    def can_reduce(self) -> bool:
        return len(self.__find_reduce_candidate()) > 0

    def sandwiching(self, u: List[List[Fraction]], v: List[List[Fraction]], w: List[List[Fraction]]) -> None:
        u1, v1, w1 = inverse_fraction_matrix(u), inverse_fraction_matrix(v), inverse_fraction_matrix(w)
        assert u1 is not None and v1 is not None and w1 is not None

        for index in range(self.m):
            self.__sandwich(index, 0, u, v1)
            self.__sandwich(index, 1, v, w1)
            self.__sandwich(index, 2, w, u1)

    def scale(self, index: int, alpha: Fraction, beta: Fraction, gamma: Fraction) -> None:
        assert alpha * beta * gamma == 1

        for p, scale in enumerate([alpha, beta, gamma]):
            for i in range(self.nn[p]):
                self.uvw[p][index][i] *= scale

    def fractions_count(self) -> int:
        return sum(value.denominator != 1 for p in range(3) for index in range(self.m) for value in self.uvw[p][index])

    def weight(self) -> tuple:
        max_den = max(value.denominator for matrix in self.uvw for row in matrix for value in row)
        f = self.fractions_count()
        w = sum(abs(value.numerator) * value.denominator for matrix in self.uvw for row in matrix for value in row)
        max_value = max(abs(value.numerator) for matrix in self.uvw for row in matrix for value in row if value.denominator == 1)
        count = sum(1 for matrix in self.uvw for row in matrix for value in row if value.denominator == 1 and abs(value.numerator) == max_value)

        return max_den, f, max_value, count, w

    def unique_values(self) -> List[str]:
        unique_values = sorted(set((value.numerator, value.denominator) for matrix in self.uvw for row in matrix for value in row), key=lambda v: v[0] / max(1, v[1]))
        return [f"{num} / {den}" if den > 1 else str(num) for num, den in unique_values]

    def convert_to_ring(self, ring: int = 3) -> Tuple[List[List[int]], List[List[int]], List[List[int]]]:
        u = [[self.__mod(self.uvw[0][index][i], ring) for i in range(self.nn[0])] for index in range(self.m)]
        v = [[self.__mod(self.uvw[1][index][i], ring) for i in range(self.nn[1])] for index in range(self.m)]
        w = [[self.__mod(self.uvw[2][index][i], ring) for i in range(self.nn[2])] for index in range(self.m)]
        return u, v, w

    def to_ring_row(self, ring: int) -> List[int]:
        assert ring in {2, 3}

        u, v, w = self.convert_to_ring(ring=ring)
        row = []
        n1, n2, n3 = self.n

        for index in range(self.m):
            u_low = sum((u[index][i] & 1) << i for i in range(self.nn[0]))
            u_high = sum(((u[index][i] >> 1) & 1) << i for i in range(self.nn[0]))

            v_low = sum((v[index][i] & 1) << i for i in range(self.nn[1]))
            v_high = sum(((v[index][i] >> 1) & 1) << i for i in range(self.nn[1]))

            w_low = sum((w[index][j * n1 + i] & 1) << (i * n3 + j) for i in range(n1) for j in range(n3))
            w_high = sum(((w[index][j * n1 + i] >> 1) & 1) << (i * n3 + j) for i in range(n1) for j in range(n3))

            if ring == 2:
                row.extend([u_low, v_low, w_low])
            else:
                row.extend([u_low, u_high, v_low, v_high, w_low, w_high])

        return row

    def to_scheme(self, validate: bool = True) -> Scheme:
        n1, n2, n3 = self.n
        return Scheme(n1=n1, n2=n2, n3=n3, m=self.m, u=self.uvw[0], v=self.uvw[1], w=self.uvw[2], z2=False, validate=validate)

    @classmethod
    def load(cls, path: str, validate: bool = True) -> "FractionalScheme":
        if path.endswith(".txt"):
            return FractionalScheme.from_txt(path=path, validate=validate)

        return FractionalScheme.from_json(path=path, validate=validate)

    @classmethod
    def from_scheme(cls, scheme: Scheme) -> "FractionalScheme":
        n1, n2, n3 = scheme.n
        u = [[Fraction(value) for value in row] for row in scheme.u]
        v = [[Fraction(value) for value in row] for row in scheme.v]
        w = [[Fraction(value) for value in row] for row in scheme.w]
        return FractionalScheme(n1=n1, n2=n2, n3=n3, m=scheme.m, u=u, v=v, w=w, validate=False)

    @classmethod
    def from_json(cls, path: str, validate: bool = True) -> "FractionalScheme":
        with open(path, "r") as f:
            data = json.load(f)

        n1, n2, n3 = (data["n"], data["n"], data["n"]) if isinstance(data["n"], int) else data["n"]
        m = data["m"]

        u = [[Fraction(value) for value in row] for row in data["u"]]
        v = [[Fraction(value) for value in row] for row in data["v"]]
        w = [[Fraction(value) for value in row] for row in data["w"]]
        return FractionalScheme(n1=n1, n2=n2, n3=n3, m=m, u=u, v=v, w=w, validate=validate)

    @classmethod
    def from_txt(cls, path: str, validate: bool = True) -> "FractionalScheme":
        with open(path) as f:
            text = " ".join([line.strip() for line in f.readlines() if not line.startswith("#")])
            text = map(int, re.split(r"[\s\n]+", text))

        n1, n2, n3, m, *uvw = text
        nn = [n1 * n2, n2 * n3, n3 * n1]

        u_values = uvw[:nn[0] * m * 2]
        v_values = uvw[nn[0]*m*2:(nn[0] + nn[1])*m*2]
        w_values = uvw[(nn[0] + nn[1])*m*2:]

        u = [[Fraction(u_values[(index * nn[0] + i) * 2], u_values[(index * nn[0] + i) * 2 + 1]) for i in range(nn[0])] for index in range(m)]
        v = [[Fraction(v_values[(index * nn[1] + i) * 2], v_values[(index * nn[1] + i) * 2 + 1]) for i in range(nn[1])] for index in range(m)]
        w = [[Fraction(w_values[(index * nn[2] + i) * 2], w_values[(index * nn[2] + i) * 2 + 1]) for i in range(nn[2])] for index in range(m)]
        return FractionalScheme(n1=n1, n2=n2, n3=n3, m=m, u=u, v=v, w=w, validate=validate)

    def save_txt(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(self.to_txt())

    def to_txt(self) -> str:
        lines = []

        for p in range(3):
            line = " ".join(f"{self.uvw[p][index][i].numerator} {self.uvw[p][index][i].denominator}" for index in range(self.m) for i in range(self.nn[p]))
            lines.append(f"{line}\n")

        n1, n2, n3 = self.n
        return f'{n1} {n2} {n3} {self.m}\n{"".join(lines)}'

    def have_fractions(self, index: int) -> bool:
        for i in range(3):
            for v in self.uvw[i][index]:
                if v.denominator > 1:
                    return True

        return False

    def omega(self) -> float:
        return 3 * math.log(self.m) / math.log(self.n[0] * self.n[1] * self.n[2])

    def get_ring(self) -> str:
        integer = False

        for p in range(3):
            for index in range(self.m):
                for value in self.uvw[p][index]:
                    if value.denominator > 1:
                        return "Q"

                    if abs(value.numerator) > 1:
                        integer = True

        return "Z" if integer else "ZT"

    def get_flips(self, with_scales: bool = False) -> List[Union[Tuple[int, int, int], Tuple[int, int, int, int]]]:
        flips = []

        for index1, index2 in combinations(range(self.m), r=2):
            for p in range(3):
                scale = self.__get_linearly_dependent(p, index1, index2)
                if scale is not None:
                    flips.append((p, index1, index2, scale) if with_scales else (p, index1, index2))

        return flips

    def fix_fractions(self) -> None:
        for index in range(self.m):
            lcm = [math.lcm(*[self.uvw[i][index][j].denominator for j in range(self.nn[i])]) for i in range(3)]
            gcd = [math.gcd(*[self.uvw[i][index][j].numerator for j in range(self.nn[i])]) for i in range(3)]

            lcm_p = lcm[0] * lcm[1] * lcm[2]
            gcd_p = gcd[0] * gcd[1] * gcd[2]

            if lcm_p == 1 or gcd_p % lcm_p != 0:
                continue

            alpha = Fraction(lcm[0], math.gcd(lcm_p, gcd[0]))
            beta = Fraction(lcm[1], math.gcd(lcm_p, gcd[1]))
            gamma = Fraction(lcm[2], math.gcd(lcm_p, gcd[2]))

            self.scale(index, alpha, beta, gamma)

    def canonize(self) -> None:
        for index in range(self.m):
            v_lcm = math.lcm(*[v.denominator for v in self.uvw[1][index]])
            w_lcm = math.lcm(*[v.denominator for v in self.uvw[2][index]])
            self.scale(index, Fraction(1, v_lcm * w_lcm), Fraction(v_lcm), Fraction(w_lcm))

    def __validate(self) -> None:
        for i in range(self.nn[0]):
            for j in range(self.nn[1]):
                for k in range(self.nn[2]):
                    assert self.__validate_equation(i, j, k)

    def __validate_equation(self, i: int, j: int, k: int) -> bool:
        i1, i2, j1, j2, k1, k2 = i // self.n[1], i % self.n[1], j // self.n[2], j % self.n[2], k // self.n[0], k % self.n[0]
        target = Fraction((i2 == j1) and (i1 == k2) and (j2 == k1))
        equation = 0

        for index in range(self.m):
            equation += self.uvw[0][index][i] * self.uvw[1][index][j] * self.uvw[2][index][k]

        return equation == target

    def __get_linearly_dependent(self, p: int, index1: int, index2: int) -> Optional[Fraction]:
        k = None

        for v1, v2 in zip(self.uvw[p][index1], self.uvw[p][index2]):
            if (v1 == 0) != (v2 == 0):
                return None

            if v1 == 0:
                continue

            if k is None:
                k = v2 / v1
            elif v2 / v1 != k:
                return None

        return k

    def __find_flip_candidates(self) -> List[Tuple[Fraction, int, int, int, int]]:
        candidates = []

        for p in range(3):
            for index1, index2 in itertools.combinations(range(self.m), r=2):
                alpha = self.__get_linearly_dependent(p=p, index1=index1, index2=index2)
                if alpha is not None:
                    candidates.append((alpha, (p + 1) % 3, (p + 2) % 3, index1, index2))

        return candidates

    def __find_reduce_candidate(self) -> List[Tuple[Fraction, Fraction, int, int, int]]:
        candidates = []

        for index1, index2 in itertools.combinations(range(self.m), r=2):
            ku = self.__get_linearly_dependent(p=0, index1=index1, index2=index2)
            kv = self.__get_linearly_dependent(p=1, index1=index1, index2=index2)
            kw = self.__get_linearly_dependent(p=2, index1=index1, index2=index2)

            if ku and kv:
                candidates.append((ku, kv, 2, index1, index2))

            if ku and kw:
                candidates.append((ku, kw, 2, index1, index2))

            if kv and kw:
                candidates.append((kv, kw, 2, index1, index2))

        return candidates

    def __flip(self, pv: int, pw: int, index1: int, index2: int, alpha: Fraction, beta: Fraction) -> None:
        for i in range(self.nn[pv]):
            self.uvw[pv][index1][i] += alpha * beta * self.uvw[pv][index2][i]

        for i in range(self.nn[pw]):
            self.uvw[pw][index2][i] -= beta * self.uvw[pw][index1][i]

    def __mod(self, value: Fraction, m: int) -> int:
        if value.denominator == 1:
            return value.numerator % m

        a, b = value.numerator, value.denominator
        for c in range(m):
            if (b * c) % m == a % m:
                return c

        raise ValueError("invalid value")

    def __sandwich(self, index: int, p: int, left: List[List[Fraction]], right: List[List[Fraction]]) -> None:
        rows = self.n[p]
        cols = self.n[(p + 1) % 3]

        matrix = [[sum(left[i][k] * self.uvw[p][index][k * cols + j] for k in range(rows)) for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                self.uvw[p][index][i * cols + j] = sum(matrix[i][k] * right[k][j] for k in range(cols))
