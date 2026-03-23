import math
import random
from collections import defaultdict
from typing import List, Set, Tuple

from src.utils.find_root import find_root_bisection


class FlipStructureOptimizer:
    def __init__(self, n: int, m: int, p: int, rank: int, flips: List[Tuple[int, int, int]]) -> None:
        self.n = n
        self.m = m
        self.p = p
        self.rank = rank
        self.flips = flips

    def optimize(self, iterations: int = 250, eps: float = 1e-15) -> Tuple[float, List[Tuple[int, Tuple[int, int, int]]]]:
        best_omega = 3
        best_structure = []

        for _ in range(iterations):
            structure = self.__select_random_structure()
            omega = find_root_bisection(func=lambda x: self.__f(x, structure), a=2.5, b=3.0, eps=eps)
            if omega < best_omega:
                best_omega, best_structure = omega, structure

        return best_omega, best_structure

    def __select_random_flips(self) -> List[Tuple[int, int, int]]:
        available = [(p, i, j) for p, i, j in self.flips]
        ignored = [set(), set(), set()]
        selected = []

        while available:
            p, i, j = random.choice(available)
            selected.append((p, i, j))

            for q in range(3):
                if p != q:
                    ignored[q].add(i)
                    ignored[q].add(j)

            available = [(p1, i1, j1) for p1, i1, j1 in available if i1 not in ignored[p1] and j1 not in ignored[p1] and (p, i, j) != (p1, i1, j1)]

        return selected

    def __group_flips(self, flips: List[Tuple[int, int, int]], target_p: int) -> List[Set[int]]:
        components = []
        index2component = {}

        for p, i, j in flips:
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

        return [component for component in components if component]

    def __count_sizes(self, sizes: List[Tuple[int, int, int]]) -> List[Tuple[int, Tuple[int, int, int]]]:
        size2count = defaultdict(int)
        for size in sizes:
            size2count[size] += 1

        return sorted((count, size) for size, count in size2count.items())

    def __select_random_structure(self) -> List[Tuple[int, Tuple[int, int, int]]]:
        flips = self.__select_random_flips()

        u_sizes = [(1, 1, len(group)) for group in self.__group_flips(flips, 0)]
        v_sizes = [(len(group), 1, 1) for group in self.__group_flips(flips, 1)]
        w_sizes = [(1, len(group), 1) for group in self.__group_flips(flips, 2)]

        structure = self.__count_sizes(u_sizes) + self.__count_sizes(v_sizes) + self.__count_sizes(w_sizes)
        one_count = self.rank - sum(s * n * m * p for s, (n, m, p) in structure)
        if one_count:
            structure.append((one_count, (1, 1, 1)))

        return structure

    def __f(self, omega: float, structure: List[Tuple[int, Tuple[int, int, int]]]) -> float:
        score = -math.pow(self.n * self.m * self.p, omega)

        for s_a, (n_a, m_a, p_a) in structure:
            for s_b, (n_b, m_b, p_b) in structure:
                for s_c, (n_c, m_c, p_c) in structure:
                    score += s_a * s_b * s_c * math.pow(n_a * m_b * p_c, omega - 2) * n_b * n_c * m_a * m_c * p_a * p_b

        return score
