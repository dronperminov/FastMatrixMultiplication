import random
from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Set, Tuple


class AdditionMinimization:
    def __init__(self, expressions: List[List[int]], name: str, var_names: List[str], max_size: int = 23) -> None:
        self.expressions = expressions
        self.max_size = max_size
        self.name = name
        self.var_names = var_names
        self.real_variables = max(len(expression) for expression in expressions)

    def solve(self, greedy: bool = False, loops: int = 10) -> Tuple[List[Set[int]], Dict[int, Set[int]], int]:
        best_score = float("inf")
        solution = None

        for _ in range(loops):
            if greedy:
                indices, new_vars = self.solve_greedy()
            else:
                indices, new_vars = self.solve_random()

            cost = self.__get_cost(indices, new_vars)

            if cost < best_score:
                best_score = cost
                solution = (indices, new_vars, cost)

        return solution

    def solve_greedy(self) -> Tuple[List[Set[int]], Dict[int, Set[int]]]:
        new_vars = {}
        expr_indices = [{(i + 1) * coefficient for i, coefficient in enumerate(expression) if coefficient != 0} for expression in self.expressions]

        while True:
            combination2count: Dict[tuple, int] = defaultdict(int)

            for indices in expr_indices + list(new_vars.values()):
                for d in range(2, self.max_size + 1):
                    for combination in combinations(sorted(indices), r=d):
                        combination2count[tuple(combination)] += 1

            combination2score = {combination: (len(combination) - 1) * (count - 1) for combination, count in combination2count.items()}
            sorted_combinations = sorted(combination2score.items(), key=lambda x: -x[1])
            best_score = sorted_combinations[0][1]
            best_combination = random.choice([combination for combination, score in sorted_combinations if score == best_score])

            if best_score == 0:
                return expr_indices, new_vars

            var_index = self.real_variables + len(new_vars) + 1
            inverse_best_combination = {-v for v in best_combination}

            for indices in expr_indices:
                if set(best_combination).issubset(indices):
                    for index in best_combination:
                        indices.remove(index)

                    indices.add(var_index)
                elif inverse_best_combination.issubset(indices):
                    for index in inverse_best_combination:
                        indices.remove(index)

                    indices.add(-var_index)

            for indices in new_vars.values():
                if set(best_combination).issubset(indices):
                    for index in best_combination:
                        indices.remove(index)

                    indices.add(var_index)
                elif inverse_best_combination.issubset(indices):
                    for index in inverse_best_combination:
                        indices.remove(index)

                    indices.add(-var_index)

            new_vars[var_index] = set(best_combination)

    def solve_random(self) -> Tuple[List[Set[int]], Dict[int, Set[int]]]:
        new_vars = {}
        expr_indices = [{i for i, used in enumerate(expression) if used} for expression in self.expressions]

        while True:
            combination2count: Dict[tuple, int] = defaultdict(int)

            for indices in expr_indices:
                for combination in combinations(sorted(indices), r=2):
                    combination2count[tuple(combination)] += 1

            combination2score = {combination: (len(combination) - 1) * (count - 1) for combination, count in combination2count.items()}
            sorted_combinations = sorted([(combination, score) for combination, score in combination2score.items() if score > 0], key=lambda x: -x[1])

            if not sorted_combinations:
                return expr_indices, new_vars

            best_combination, best_score = sorted_combinations[0] if random.random() < 0.7 else random.choice(sorted_combinations)
            var_index = -len(new_vars) - 1

            for indices in expr_indices:
                if set(best_combination).issubset(indices):
                    for index in best_combination:
                        indices.remove(index)

                    indices.add(var_index)

            new_vars[var_index] = set(best_combination)

    def __get_cost(self, expr_indices: List[Set[int]], new_vars: Dict[int, Set[int]]) -> int:
        return sum(len(expr) - 1 for expr in expr_indices) + sum(len(var_values) - 1 for var_values in new_vars.values())

    def show_vars(self, new_vars: Dict[int, Set[int]]) -> None:
        for var_index, combination in new_vars.items():
            names = " ".join([self.__get_name(i) for i in sorted(combination, key=lambda i: abs(i))]).lstrip("+ ")
            print(f"{self.name}{var_index - self.real_variables} = {names}")

    def show_expressions(self, expr_indices: List[Set[int]]) -> None:
        for index, indices in enumerate(expr_indices):
            names = " ".join([self.__get_name(i) for i in sorted(indices, key=lambda i: abs(i))]).lstrip("+ ")
            print(f'{index + 1}. {names}')

    def show(self, new_vars: Dict[int, Set[int]], indices: List[Set[int]]) -> None:
        self.show_vars(new_vars)
        self.show_expressions(indices)

    def __show_combination(self, sorted_combinations: List[Tuple[tuple, int]]) -> None:
        names = [f'{" + ".join(self.__get_name(i) for i in combination)}: {score}' for combination, score in sorted_combinations]
        print(", ".join(names))

    def __get_name(self, index: int) -> str:
        sign = "+" if index > 0 else "-"
        assert index != 0

        if abs(index) > self.real_variables:
            return f"{sign} {self.name}{abs(index) - self.real_variables}"

        return f"{sign} {self.var_names[abs(index) - 1]}"
