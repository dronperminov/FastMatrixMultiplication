import itertools
import json
import math
import random
from fractions import Fraction
from typing import List, Optional, Tuple


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

        self.den = math.lcm(*[value.denominator for p in range(3) for index in range(self.m) for value in self.uvw[p][index]])

        if validate:
            self.__validate()

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

    def fractions_count(self) -> int:
        return sum(value.denominator != 1 for p in range(3) for index in range(self.m) for value in self.uvw[p][index])

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
        if self.uvw[p][index1] == self.uvw[p][index2]:
            return Fraction(1)

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
