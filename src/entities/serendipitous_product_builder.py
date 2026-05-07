from fractions import Fraction
from typing import List, Set, Tuple

from src.entities.schemes_loader import SchemesLoader
from src.schemes.scheme import Scheme


class SerendipitousProductBuilder:
    def __init__(self, target_ring: str, schemes_directories: List[str]) -> None:
        self.target_ring = target_ring
        self.loader = SchemesLoader(additional_directories=schemes_directories)

    def build(self, s1: Scheme, s2: Scheme, buds: List[Tuple[int, int, int, Fraction]], validate: bool) -> Scheme:
        u_buds, v_buds, w_buds = self.__split_buds(buds)
        product_indices = self.__get_product_indices(s1.m, buds)

        pn1, pn2, pn3 = [s1.n[i] * s2.n[i] for i in range(3)]
        uvw = self.__product_indices(s1=s1, s2=s2, indices=product_indices)

        for group in u_buds:
            for p, matrix in enumerate(self.__add_u_group(s1=s1, s2=s2, group=group)):
                uvw[p].extend(matrix)

        for group in v_buds:
            for p, matrix in enumerate(self.__add_v_group(s1=s1, s2=s2, group=group)):
                uvw[p].extend(matrix)

        for group in w_buds:
            for p, matrix in enumerate(self.__add_w_group(s1=s1, s2=s2, group=group)):
                uvw[p].extend(matrix)

        rank = len(uvw[0])
        count = sum(1 for matrix in uvw for row in matrix for value in row if abs(value) > 1 or Fraction(value).denominator > 1)
        print(f" {pn1}x{pn2}x{pn3}: {rank} non {{-1, 0, 1}}: {count}")

        scheme = Scheme(n1=pn1, n2=pn2, n3=pn3, m=rank, u=uvw[0], v=uvw[1], w=uvw[2], z2=False, validate=validate)
        scheme.remove_zeroes()
        scheme.fix_sizes()
        return scheme

    def __group_buds(self, buds: List[Tuple[int, int, int, Fraction]], target_p: int) -> List[List[Tuple[int, Fraction]]]:
        components = []
        index2component = {}
        ij2scale = {(i, j): scale for p, i, j, scale in buds if p == target_p}

        for p, i, j, scale in buds:
            if p != target_p:
                continue

            if i not in index2component:
                index2component[i] = len(components)
                components.append({i})

            if j not in index2component:
                index2component[j] = len(components)
                components.append({j})

            ci, cj = index2component[i], index2component[j]
            if ci == cj:
                continue

            for k in components[cj]:
                index2component[k] = ci

            components[ci].update(components[cj])
            components[cj] = set()

        groups = []

        for component in components:
            if not component:
                continue

            start = min(component)
            group = [(start, Fraction(1))]

            for end in component:
                if start != end:
                    group.append((end, ij2scale[start, end]))

            groups.append(group)

        return groups

    def __split_buds(self, buds: List[Tuple[int, int, int, Fraction]]) -> Tuple[List[List[Tuple[int, Fraction]]], List[List[Tuple[int, Fraction]]], List[List[Tuple[int, Fraction]]]]:
        u_buds = self.__group_buds(buds, 0)
        v_buds = self.__group_buds(buds, 1)
        w_buds = self.__group_buds(buds, 2)
        return u_buds, v_buds, w_buds

    def __get_product_indices(self, rank: int, buds: List[Tuple[int, int, int, Fraction]]) -> List[int]:
        buds_indices = set()
        for _, i, j, _ in buds:
            buds_indices.add(i)
            buds_indices.add(j)

        return sorted(set(range(rank)).difference(buds_indices))

    def __product_indices(self, s1: Scheme, s2: Scheme, indices: List[int]) -> Tuple[list, list, list]:
        n = [s1.n[i] * s2.n[i] for i in range(3)]
        nn = [n[i] * n[(i + 1) % 3] for i in range(3)]

        uvw = [], [], []
        uvw1 = [s1.u, s1.v, s1.w]
        uvw2 = [s2.u, s2.v, s2.w]

        for index1 in indices:
            for index2 in range(s2.m):
                for p in range(3):
                    p1 = (p + 1) % 3
                    matrix = [0 for _ in range(nn[p])]

                    for i in range(s1.nn[p]):
                        for j in range(s2.nn[p]):
                            row1, col1 = i // s1.n[p1], i % s1.n[p1]
                            row2, col2 = j // s2.n[p1], j % s2.n[p1]

                            row = row1 * s2.n[p] + row2
                            col = col1 * s2.n[p1] + col2
                            matrix[row * n[p1] + col] = uvw1[p][index1][i] * uvw2[p][index2][j]

                    uvw[p].append(matrix)

        return uvw

    def __add_u_flips(self, s1: Scheme, s2: Scheme, s3: Scheme, group: List[Tuple[int, Fraction]], scales: List[Fraction]) -> Tuple[list, list, list]:
        assert s2.n[0] == s3.n[0] and s2.n[1] == s3.n[1] and s2.n[2] * len(group) == s3.n[2]
        assert len(scales) == len(group)

        n = [s1.n[i] * s2.n[i] for i in range(3)]
        nn = [n[0] * n[1], n[1] * n[2], n[2] * n[0]]
        uvw = [], [], []

        for index2 in range(s3.m):
            matrix_u = [0 for _ in range(nn[0])]
            matrix_v = [0 for _ in range(nn[1])]
            matrix_w = [0 for _ in range(nn[2])]

            for i in range(s1.nn[0]):
                for j in range(s2.nn[0]):
                    row1, col1 = i // s1.n[1], i % s1.n[1]
                    row2, col2 = j // s2.n[1], j % s2.n[1]
                    row = row1 * s2.n[0] + row2
                    col = col1 * s2.n[1] + col2
                    matrix_u[row * n[1] + col] = s1.u[group[0][0]][i] * s3.u[index2][j]

            for row1 in range(s1.n[1]):
                for col1 in range(s1.n[2]):
                    for row2 in range(s2.n[1]):
                        for col2 in range(s2.n[2]):
                            i = row1 * s1.n[2] + col1
                            row = row1 * s2.n[1] + row2
                            col = col1 * s2.n[2] + col2

                            for j, (fi, scale) in enumerate(group):
                                matrix_v[row * n[2] + col] += s1.v[fi][i] * s3.v[index2][row2 * s3.n[2] + col2 + j * s2.n[2]] * scale * scales[j]

            for row1 in range(s1.n[2]):
                for col1 in range(s1.n[0]):
                    for row2 in range(s2.n[2]):
                        for col2 in range(s2.n[0]):
                            i = row1 * s1.n[0] + col1
                            row = row1 * s2.n[2] + row2
                            col = col1 * s2.n[0] + col2

                            for j, (fi, _) in enumerate(group):
                                matrix_w[row * n[0] + col] += s1.w[fi][i] * s3.w[index2][(row2 + j * s2.n[2]) * s3.n[0] + col2] / scales[j]

            uvw[0].append(matrix_u)
            uvw[1].append(matrix_v)
            uvw[2].append(matrix_w)

        return uvw

    def __add_v_flips(self, s1: Scheme, s2: Scheme, s3: Scheme, group: List[Tuple[int, Fraction]], scales: List[Fraction]) -> Tuple[list, list, list]:
        assert s2.n[0] * len(group) == s3.n[0] and s2.n[1] == s3.n[1] and s2.n[2] == s3.n[2]
        assert len(scales) == len(group)

        n = [s1.n[i] * s2.n[i] for i in range(3)]
        nn = [n[0] * n[1], n[1] * n[2], n[2] * n[0]]
        uvw = [], [], []

        for index2 in range(s3.m):
            matrix_u = [0 for _ in range(nn[0])]
            matrix_v = [0 for _ in range(nn[1])]
            matrix_w = [0 for _ in range(nn[2])]

            for row1 in range(s1.n[0]):
                for col1 in range(s1.n[1]):
                    for row2 in range(s2.n[0]):
                        for col2 in range(s2.n[1]):
                            i = row1 * s1.n[1] + col1
                            row = row1 * s2.n[0] + row2
                            col = col1 * s2.n[1] + col2

                            for j, (fi, scale) in enumerate(group):
                                matrix_u[row * n[1] + col] += s1.u[fi][i] * s3.u[index2][(row2 + j * s2.n[0]) * s3.n[1] + col2] * scale * scales[j]

            for i in range(s1.nn[1]):
                for j in range(s2.nn[1]):
                    row1, col1 = i // s1.n[2], i % s1.n[2]
                    row2, col2 = j // s2.n[2], j % s2.n[2]
                    row = row1 * s2.n[1] + row2
                    col = col1 * s2.n[2] + col2
                    matrix_v[row * n[2] + col] = s1.v[group[0][0]][i] * s3.v[index2][j]

            for row1 in range(s1.n[2]):
                for col1 in range(s1.n[0]):
                    for row2 in range(s2.n[2]):
                        for col2 in range(s2.n[0]):
                            i = row1 * s1.n[0] + col1
                            row = row1 * s2.n[2] + row2
                            col = col1 * s2.n[0] + col2

                            for j, (fi, _) in enumerate(group):
                                matrix_w[row * n[0] + col] += s1.w[fi][i] * s3.w[index2][row2 * s3.n[0] + col2 + j * s2.n[0]] / scales[j]

            uvw[0].append(matrix_u)
            uvw[1].append(matrix_v)
            uvw[2].append(matrix_w)

        return uvw

    def __add_w_flips(self, s1: Scheme, s2: Scheme, s3: Scheme, group: List[Tuple[int, Fraction]], scales: List[Fraction]) -> Tuple[list, list, list]:
        assert s2.n[0] == s3.n[0] and s2.n[1] * len(group) == s3.n[1] and s2.n[2] == s3.n[2]
        assert len(scales) == len(group)

        n = [s1.n[i] * s2.n[i] for i in range(3)]
        nn = [n[0] * n[1], n[1] * n[2], n[2] * n[0]]
        uvw = [], [], []

        for index2 in range(s3.m):
            matrix_u = [0 for _ in range(nn[0])]
            matrix_v = [0 for _ in range(nn[1])]
            matrix_w = [0 for _ in range(nn[2])]

            for row1 in range(s1.n[0]):
                for col1 in range(s1.n[1]):
                    for row2 in range(s2.n[0]):
                        for col2 in range(s2.n[1]):
                            i = row1 * s1.n[1] + col1
                            row = row1 * s2.n[0] + row2
                            col = col1 * s2.n[1] + col2

                            for j, (fi, scale) in enumerate(group):
                                matrix_u[row * n[1] + col] += s1.u[fi][i] * s3.u[index2][row2 * s3.n[1] + col2 + j * s2.n[1]] * scale * scales[j]

            for row1 in range(s1.n[1]):
                for col1 in range(s1.n[2]):
                    for row2 in range(s2.n[1]):
                        for col2 in range(s2.n[2]):
                            i = row1 * s1.n[2] + col1
                            row = row1 * s2.n[1] + row2
                            col = col1 * s2.n[2] + col2

                            for j, (fi, _) in enumerate(group):
                                matrix_v[row * n[2] + col] += s1.v[fi][i] * s3.v[index2][(row2 + j * s2.n[1]) * s3.n[2] + col2] / scales[j]

            for i in range(s1.nn[2]):
                for j in range(s2.nn[2]):
                    row1, col1 = i // s1.n[0], i % s1.n[0]
                    row2, col2 = j // s2.n[0], j % s2.n[0]
                    row = row1 * s2.n[2] + row2
                    col = col1 * s2.n[0] + col2
                    matrix_w[row * n[0] + col] = s1.w[group[0][0]][i] * s3.w[index2][j]

            uvw[0].append(matrix_u)
            uvw[1].append(matrix_v)
            uvw[2].append(matrix_w)

        return uvw

    def __add_u_group(self, s1: Scheme, s2: Scheme, group: List[Tuple[int, Fraction]]) -> Tuple[list, list, list]:
        s3s = self.loader.load(s2.n[0], s2.n[1], s2.n[2] * len(group), target_ring=self.target_ring)
        group_scales = self.__get_combinations(n=len(group))

        if s3s[0].m == s2.m * len(group):
            return self.__product_indices(s1=s1, s2=s2, indices=[index for index, _ in group])

        best_uvw, best_weight = None, None
        for s3 in s3s:
            for scales in group_scales:
                uvw = self.__add_u_flips(s1=s1, s2=s2, s3=s3, group=group, scales=scales)
                weight = self.__get_weight(uvw)

                if weight[0] == 1 and weight[1] == 1:
                    print(f"  {self.__weight2str(weight):2} u ({s3s[0].n}: {s3s[0].m}) -> {weight}")
                    return uvw

                if best_weight is None or weight < best_weight:
                    best_uvw, best_weight = uvw, weight

        print(f"  {self.__weight2str(best_weight):2} u ({s3s[0].n}: {s3s[0].m}) -> {best_weight}")
        return best_uvw

    def __add_v_group(self, s1: Scheme, s2: Scheme, group: List[Tuple[int, Fraction]]) -> Tuple[list, list, list]:
        s3s = self.loader.load(s2.n[0] * len(group), s2.n[1], s2.n[2], target_ring=self.target_ring)
        group_scales = self.__get_combinations(n=len(group))

        if s3s[0].m == s2.m * len(group):
            return self.__product_indices(s1=s1, s2=s2, indices=[index for index, _ in group])

        best_uvw, best_weight = None, None
        for s3 in s3s:
            for scales in group_scales:
                uvw = self.__add_v_flips(s1=s1, s2=s2, s3=s3, group=group, scales=scales)
                weight = self.__get_weight(uvw)

                if weight[0] == 1 and weight[1] == 1:
                    print(f"  {self.__weight2str(weight):2} v ({s3s[0].n}: {s3s[0].m}) -> {weight}")
                    return uvw

                if best_weight is None or weight < best_weight:
                    best_uvw, best_weight = uvw, weight

        print(f"  {self.__weight2str(best_weight):2} v ({s3s[0].n}: {s3s[0].m}) -> {best_weight}")
        return best_uvw

    def __add_w_group(self, s1: Scheme, s2: Scheme, group: List[Tuple[int, Fraction]]) -> Tuple[list, list, list]:
        s3s = self.loader.load(s2.n[0], s2.n[1] * len(group), s2.n[2], target_ring=self.target_ring)
        group_scales = self.__get_combinations(n=len(group))

        if s3s[0].m == s2.m * len(group):
            return self.__product_indices(s1=s1, s2=s2, indices=[index for index, _ in group])

        best_uvw, best_weight = None, None
        for s3 in s3s:
            for scales in group_scales:
                uvw = self.__add_w_flips(s1=s1, s2=s2, s3=s3, group=group, scales=scales)
                weight = self.__get_weight(uvw)

                if weight[0] == 1 and weight[1] == 1:
                    print(f"  {self.__weight2str(weight):2} w ({s3s[0].n}: {s3s[0].m}) -> {weight}")
                    return uvw

                if best_weight is None or weight < best_weight:
                    best_uvw, best_weight = uvw, weight

        print(f"  {self.__weight2str(best_weight):2} w ({s3s[0].n}: {s3s[0].m}) -> {best_weight}")
        return best_uvw

    def __get_combinations(self, n: int) -> List[List[Fraction]]:
        combinations = []

        for i in range(1 << (n - 1)):
            combinations.append([Fraction(1), *[Fraction(-1 if (i >> j) & 1 == 0 else 1) for j in range(n - 1)]])

        return combinations

    def __get_weight(self, values: Tuple[list, list, list]) -> tuple:
        fractions = [Fraction(value) for matrix in values for row in matrix for value in row]
        max_den = max(value.denominator for value in fractions)
        max_abs_num = max(abs(value.numerator) for value in fractions)
        max_abs_count = sum(1 for value in fractions if abs(value.numerator) == max_abs_num)
        score = sum(abs(value.numerator) * value.denominator for value in fractions)
        return max_den, max_abs_num, max_abs_count, score

    def __weight2str(self, weight: tuple) -> str:
        max_den, max_abs, max_abs_count, w = weight
        if max_den > 1:
            return "Q"

        if max_abs > 1:
            return "Z"

        return "ZT"
