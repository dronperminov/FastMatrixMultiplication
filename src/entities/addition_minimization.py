import random
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from typing import Dict, List, Set, Tuple, Union


class AdditionMinimization:
    def __init__(self, expressions: List[List[Union[int, Fraction]]], real_variables: int, max_size: int = 23) -> None:
        self.expressions = expressions
        self.real_variables = real_variables
        self.max_size = min(max_size, self.real_variables)

    def solve(self, mode: str, loops: int) -> Tuple[List[List[int]], List[List[int]], int]:
        best_score = float("inf")
        solution = None

        for _ in range(loops):
            if mode == "greedy":
                indices, new_vars = self.__solve_greedy()
            elif mode == "random":
                indices, new_vars = self.__solve_random()
            else:
                indices, new_vars = self.__solve_random() if random.random() < 0.5 else self.__solve_greedy()

            cost = self.__get_cost(indices, new_vars)

            if cost < best_score:
                best_score = cost
                solution = (indices, new_vars, cost)

        return solution

    def __solve_greedy(self) -> Tuple[List[List[int]], List[List[int]]]:
        new_vars = []
        expr_indices = [{(i + 1) * coefficient for i, coefficient in enumerate(expression) if coefficient != 0} for expression in self.expressions]

        while True:
            combination2score = self.__get_combinations(expr_indices=expr_indices + new_vars, max_size=self.max_size)
            sorted_combinations = sorted(combination2score.items(), key=lambda x: -x[1])
            best_score = sorted_combinations[0][1]

            if best_score == 0:
                return [self.__sort_combination(indices) for indices in expr_indices], [self.__sort_combination(indices) for indices in new_vars]

            best_combination = random.choice([combination for combination, score in sorted_combinations if score == best_score])
            self.__replace_best_combination(expr_indices=expr_indices, new_vars=new_vars, combination=set(best_combination))

    def __solve_random(self) -> Tuple[List[List[int]], List[List[int]]]:
        new_vars = []
        expr_indices = [{(i + 1) * coefficient for i, coefficient in enumerate(expression) if coefficient != 0} for expression in self.expressions]

        while True:
            combination2score = self.__get_combinations(expr_indices=expr_indices + new_vars, max_size=2)
            sorted_combinations = sorted([(combination, score) for combination, score in combination2score.items() if score > 0], key=lambda x: -x[1])

            if not sorted_combinations:
                return [self.__sort_combination(indices) for indices in expr_indices], [self.__sort_combination(indices) for indices in new_vars]

            best_combination, _ = sorted_combinations[0] if random.random() < 0.5 else random.choice(sorted_combinations)
            self.__replace_best_combination(expr_indices=expr_indices, new_vars=new_vars, combination=set(best_combination))

    def __get_combinations(self, expr_indices: List[Set[int]], max_size: int) -> Dict[tuple, int]:
        combination2count: Dict[tuple, int] = defaultdict(int)

        for indices in expr_indices:
            for combination_size in range(2, max_size + 1):
                for combination in combinations(sorted(indices), r=combination_size):
                    combination2count[tuple(combination)] += 1

        return {combination: (len(combination) - 1) * (count - 1) for combination, count in combination2count.items()}

    def __replace_best_combination(self, expr_indices: List[Set[int]], new_vars: List[Set[int]], combination: Set[int]) -> None:
        inverse_combination = {-v for v in combination}
        var_index = self.real_variables + len(new_vars) + 1

        for indices in expr_indices + new_vars:
            if combination.issubset(indices):
                indices.difference_update(combination)
                indices.add(var_index)
            elif inverse_combination.issubset(indices):
                indices.difference_update(inverse_combination)
                indices.add(-var_index)

        new_vars.append(combination)

    def __get_cost(self, expr_indices: List[List[int]], new_vars: List[List[int]]) -> int:
        return sum(len(expr) - 1 for expr in expr_indices + new_vars)

    def __sort_combination(self, combination: Set[int]) -> List[int]:
        return sorted(combination, key=lambda variable: abs(variable))
