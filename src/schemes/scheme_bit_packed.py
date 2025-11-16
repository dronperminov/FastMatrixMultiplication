import itertools
import random
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from src.schemes.scheme import Scheme


class SchemeBitPacked:
    def __init__(self, n1: int, n2: int, n3: int, u: List[int], v: List[int], w: List[int], validate: bool = True) -> None:
        self.n = [n1, n2, n3]
        self.nn = [n1*n2, n2*n3, n1*n3]
        self.m = len(u)

        self.uvw = [[ui for ui in u], [vi for vi in v], [wi for wi in w]]

        if validate:
            self.__validate()

    @classmethod
    def from_scheme(cls, scheme: Scheme, validate: bool = True) -> "SchemeBitPacked":
        u = [sum(((abs(scheme.u[index][i]) % 2) << i) for i in range(scheme.nn[0])) for index in range(scheme.m)]
        v = [sum(((abs(scheme.v[index][i]) % 2) << i) for i in range(scheme.nn[1])) for index in range(scheme.m)]
        w = [sum(((abs(scheme.w[index][i]) % 2) << i) for i in range(scheme.nn[2])) for index in range(scheme.m)]
        n1, n2, n3 = scheme.n
        return SchemeBitPacked(n1=n1, n2=n2, n3=n3, u=u, v=v, w=w, validate=validate)

    def to_scheme(self) -> "Scheme":
        u = [[(self.uvw[0][index] >> i) & 1 for i in range(self.nn[0])] for index in range(self.m)]
        v = [[(self.uvw[1][index] >> i) & 1 for i in range(self.nn[1])] for index in range(self.m)]
        w = [[(self.uvw[2][index] >> i) & 1 for i in range(self.nn[2])] for index in range(self.m)]
        n1, n2, n3 = self.n
        return Scheme(n1=n1, n2=n2, n3=n3, m=self.m, z2=True, u=u, v=v, w=w)

    def to_cpp(self) -> str:
        u = " ".join(str(self.uvw[0][index]) for index in range(self.m))
        v = " ".join(str(self.uvw[1][index]) for index in range(self.m))
        w = " ".join(str(self.uvw[2][index]) for index in range(self.m))
        n1, n2, n3 = self.n
        return f"{n1} {n2} {n3} {self.m}\n{u}\n{v}\n{w}"

    def try_flip(self) -> bool:
        possible_flip = self.__get_flip_candidate()
        if not possible_flip:
            return False

        self.__flip(*possible_flip)
        return True

    def expand(self, count: int) -> None:
        for _ in range(count):
            v = random.randint(0, 1)
            if v == 0:
                self.__try_plus()
            elif v == 1:
                self.__try_split()

    def try_reduce(self) -> bool:
        possible_reduce = self.__get_reduce_candidate()
        if not possible_reduce:
            return False

        self.__reduce(*possible_reduce)
        return True

    def try_project(self, min_n: Tuple[int, int, int]) -> bool:
        indices = []
        if self.n[0] - 1 > min_n[0] and self.n[1] >= min_n[1] and self.n[2] >= min_n[2]:
            indices.append(0)

        if self.n[0] >= min_n[0] and self.n[1] - 1 > min_n[1] and self.n[2] >= min_n[2]:
            indices.append(1)

        if self.n[0] >= min_n[0] and self.n[1] >= min_n[1] and self.n[2] - 1 > min_n[2]:
            indices.append(2)

        if not indices:
            return False

        p = random.choice(indices)
        q = random.randint(0, self.n[p] - 1)
        self.project(p, q)

        while self.try_reduce():
            pass
        return True

    def try_extend(self, max_n: Tuple[int, int, int]) -> bool:
        indices = []

        if self.n[0] + 1 < max_n[0] and self.n[1] <= max_n[1] and self.n[2] <= max_n[2]:
            indices.append(0)

        if self.n[0] <= max_n[0] and self.n[1] + 1 < max_n[1] and self.n[2] <= max_n[2]:
            indices.append(1)

        if self.n[0] <= max_n[0] and self.n[1] <= max_n[1] and self.n[2] + 1 < max_n[2]:
            indices.append(2)

        if not indices:
            return False

        self.extend(random.choice(indices))
        while self.try_reduce():
            pass

        return True

    def project(self, p: int, q: int) -> None:
        self.__exclude_row(p, q)
        self.__exclude_column((p + 2) % 3, q)
        self.n[p] -= 1

        for i in range(3):
            self.nn[i] = self.n[i] * self.n[(i + 1) % 3]

        self.__remove_zeroes()
        self.__validate()

    def extend(self, p: int) -> None:
        if p == 0:
            self.__add_row(0)
            self.__add_column(2)

            for i in range(self.n[2]):
                for j in range(self.n[1]):
                    self.__add_triplet(0, 1, 2, 1 << (self.n[0] * self.n[1] + j), 1 << (j * self.n[2] + i), 1 << (i * (self.n[0] + 1) + self.n[0]))
        elif p == 1:
            self.__add_row(1)
            self.__add_column(0)

            for i in range(self.n[0]):
                for j in range(self.n[2]):
                    self.__add_triplet(0, 1, 2, 1 << (i * (self.n[1] + 1) + self.n[1]), 1 << (self.n[1] * self.n[2] + j), 1 << (j * self.n[0] + i))
        elif p == 2:
            self.__add_row(2)
            self.__add_column(1)

            for i in range(self.n[0]):
                for j in range(self.n[1]):
                    self.__add_triplet(0, 1, 2, 1 << (i * self.n[1] + j), 1 << (j * (self.n[2] + 1) + self.n[2]), 1 << (self.n[2] * self.n[0] + i))

        self.n[p] += 1

        for i in range(3):
            self.nn[i] = self.n[i] * self.n[(i + 1) % 3]

        self.__validate()

    def __validate(self) -> None:
        for i in range(self.nn[0]):
            for j in range(self.nn[1]):
                for k in range(self.nn[2]):
                    assert self.__validate_equation(i, j, k)

    def __validate_equation(self, i: int, j: int, k: int) -> bool:
        i1, i2, j1, j2, k1, k2 = i // self.n[1], i % self.n[1], j // self.n[2], j % self.n[2], k // self.n[0], k % self.n[0]
        target = (i2 == j1) and (i1 == k2) and (j2 == k1)
        equation = False

        for index in range(self.m):
            equation ^= ((self.uvw[0][index] >> i) & 1) and ((self.uvw[1][index] >> j) & 1) and ((self.uvw[2][index] >> k) & 1)

        return equation == target

    def __remove_zeroes(self) -> None:
        non_zero_indices = [index for index in range(self.m) if self.uvw[0][index] and self.uvw[1][index] and self.uvw[2][index]]
        self.uvw[0] = [self.uvw[0][index] for index in non_zero_indices]
        self.uvw[1] = [self.uvw[1][index] for index in non_zero_indices]
        self.uvw[2] = [self.uvw[2][index] for index in non_zero_indices]
        self.m = len(non_zero_indices)

    def __remove_at(self, index: int) -> None:
        self.m -= 1
        self.uvw[0].pop(index)
        self.uvw[1].pop(index)
        self.uvw[2].pop(index)

    def __exclude_column(self, matrix: int, column: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]
        old_columns = [j for j in range(n2) if j != column]

        for index in range(self.m):
            self.uvw[matrix][index] = sum(((self.uvw[matrix][index] >> (i * n2 + old_j)) & 1) << (i * (n2 - 1) + j) for i in range(n1) for j, old_j in enumerate(old_columns))

    def __exclude_row(self, matrix: int, row: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]
        old_rows = [i for i in range(n1) if i != row]

        for index in range(self.m):
            self.uvw[matrix][index] = sum(((self.uvw[matrix][index] >> (old_i * n2 + j)) & 1) << (i * n2 + j) for i, old_i in enumerate(old_rows) for j in range(n2))

    def __add_column(self, matrix: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]

        for index in range(self.m):
            self.uvw[matrix][index] = sum(((self.uvw[matrix][index] >> (i * n2 + j)) & 1) << (i * (n2 + 1) + j) for i in range(n1) for j in range(n2))

    def __add_row(self, matrix: int) -> None:
        n1, n2 = self.n[matrix], self.n[(matrix + 1) % 3]

        for index in range(self.m):
            self.uvw[matrix][index] = sum(((self.uvw[matrix][index] >> (i * n2 + j)) & 1) << (i * n2 + j) for i in range(n1) for j in range(n2))

    def __add_triplet(self, i: int, j: int, k: int, u: int, v: int, w: int) -> None:
        self.uvw[i].append(u)
        self.uvw[j].append(v)
        self.uvw[k].append(w)
        self.m += 1

    def __get_flip_candidate(self) -> Optional[Tuple[int, int, int, int]]:
        permutation = [0, 1, 2]
        indices = [index for index in range(self.m)]

        random.shuffle(permutation)
        random.shuffle(indices)

        for p in range(3):
            i, j, k = permutation[p], permutation[(p + 1) % 3], permutation[(p + 2) % 3]
            for index1, index2 in itertools.combinations(indices, r=2):
                if self.uvw[i][index1] == self.uvw[i][index2]:
                    return j, k, index1, index2

        return None

    def __flip(self, i: int, j: int, index1: int, index2: int) -> None:
        self.uvw[i][index1] ^= self.uvw[i][index2]
        self.uvw[j][index2] ^= self.uvw[j][index1]

        if not self.uvw[i][index1] or not self.uvw[j][index2]:
            self.__remove_zeroes()

    def __plus(self, i: int, j: int, k: int, index1: int, index2: int) -> None:
        a1 = self.uvw[i][index1]
        b1 = self.uvw[j][index1]
        c1 = self.uvw[k][index1]

        a2 = self.uvw[i][index2]
        b2 = self.uvw[j][index2]
        c2 = self.uvw[k][index2]

        a = a1 ^ a2
        b = b1 ^ b2
        c = c1 ^ c2
        variant = random.randint(0, 2)

        if variant == 0:
            self.uvw[j][index1] = b
            self.uvw[i][index2] = a
            self.__add_triplet(i, j, k, a1, b2, c)
        elif variant == 1:
            self.uvw[k][index1] = c
            self.uvw[j][index2] = b
            self.__add_triplet(i, j, k, a, b1, c2)
        else:
            self.uvw[i][index1] = a
            self.uvw[k][index2] = c
            self.__add_triplet(i, j, k, a2, b, c1)

        if not (a and b and c):
            self.__remove_zeroes()

    def __split(self, i: int, j: int, k: int, index: int, value: int) -> None:
        u = self.uvw[i][index] ^ value
        self.uvw[i][index] = value
        self.__add_triplet(i, j, k, u, self.uvw[j][index], self.uvw[k][index])

    def __reduce(self, i: int, index1: int, index2: int) -> None:
        self.uvw[i][index1] ^= self.uvw[i][index2]
        is_zero = not self.uvw[i][index1]

        self.__remove_at(index2)

        if is_zero:
            self.__remove_zeroes()

    def __try_plus(self) -> bool:
        if self.m >= self.n[0] * self.n[1] * self.n[2]:
            return False

        index1 = random.randint(0, self.m - 1)
        index2 = random.randint(0, self.m - 1)

        while index1 == index2:
            index2 = random.randint(0, self.m - 1)

        permutation = [0, 1, 2]
        random.shuffle(permutation)
        i, j, k = permutation

        self.__plus(i, j, k, index1, index2)
        return True

    def __try_split(self) -> bool:
        if self.m >= self.n[0] * self.n[1] * self.n[2]:
            return False

        index = random.randint(0, self.m - 1)

        permutation = [0, 1, 2]
        random.shuffle(permutation)
        i, j, k = permutation

        value = random.randint(1, 1 << self.nn[i])

        while value == self.uvw[i][index]:
            value = random.randint(1, 1 << self.nn[i])

        self.__split(i, j, k, index, value)
        return True

    def __get_reduce_candidate(self) -> Optional[Tuple[int, int, int]]:
        permutation = [0, 1, 2]
        random.shuffle(permutation)

        for p in range(3):
            i, j, k = permutation[p], permutation[(p + 1) % 3], permutation[(p + 2) % 3]
            uvw2indices: Dict[int, List[int]] = defaultdict(list)

            for index in range(self.m):
                uvw2indices[self.uvw[i][index]].append(index)

            for indices in uvw2indices.values():
                if len(indices) < 2:
                    continue

                for index1, index2 in itertools.combinations(indices, r=2):
                    if self.uvw[j][index1] == self.uvw[j][index2]:
                        return k, index1, index2

                    if self.uvw[k][index1] == self.uvw[k][index2]:
                        return j, index1, index2

        return None
