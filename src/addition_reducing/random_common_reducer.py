import random
from collections import Counter
from fractions import Fraction
from itertools import combinations
from typing import Dict, List, Set, Tuple, Union


class RandomCommonAdditionReducer:
    def __init__(self, expressions: List[List[Union[int, Fraction]]], real_variables: int, max_size: int = 23) -> None:
        self.expressions = expressions
        self.real_variables = real_variables
        self.max_size = min(max_size, self.real_variables)

    def solve(self, mode: str, loops: int) -> Tuple[List[List[dict]], List[List[dict]], int]:
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

    def __solve_greedy(self) -> Tuple[List[List[dict]], List[List[dict]]]:
        new_vars = []
        expr_indices = [{(i, coefficient) for i, coefficient in enumerate(expression) if coefficient != 0} for expression in self.expressions]

        while True:
            subexpression2score = self.__get_subexpressions(expr_indices=expr_indices + new_vars, max_size=self.max_size)
            best_score = max(subexpression2score.values())

            if best_score == 0:
                return [self.__sort_expression(indices) for indices in expr_indices], [self.__sort_expression(indices) for indices in new_vars]

            sorted_subexpressions = [subexpression for subexpression, score in subexpression2score.items() if score == best_score]
            self.__replace_best_subexpression(expr_indices=expr_indices, new_vars=new_vars, subexpression=set(random.choice(sorted_subexpressions)))

    def __solve_random(self) -> Tuple[List[List[dict]], List[List[dict]]]:
        new_vars = []
        expr_indices = [{(i, coefficient) for i, coefficient in enumerate(expression) if coefficient != 0} for expression in self.expressions]

        while True:
            subexpression2score = self.__get_subexpressions(expr_indices=expr_indices + new_vars, max_size=random.randint(2, self.max_size))
            sorted_subexpressions = sorted([(subexpression, score) for subexpression, score in subexpression2score.items() if score > 0], key=lambda x: -x[1])

            if not sorted_subexpressions:
                return [self.__sort_expression(indices) for indices in expr_indices], [self.__sort_expression(indices) for indices in new_vars]

            subexpression_scores = [score for _, score in sorted_subexpressions]
            best_subexpression, _ = random.choices(sorted_subexpressions, weights=subexpression_scores, k=1)[0]
            self.__replace_best_subexpression(expr_indices=expr_indices, new_vars=new_vars, subexpression=set(best_subexpression))

    def __get_subexpressions(self, expr_indices: List[Set[tuple]], max_size: int) -> Dict[tuple, int]:
        subexpression2count = Counter()

        for indices in expr_indices:
            indices = sorted(indices)

            for subexpression_size in range(2, min(len(indices), max_size) + 1):
                subexpression2count.update(combinations(indices, r=subexpression_size))

        return {subexpression: (len(subexpression) - 1) * (count - 1) for subexpression, count in subexpression2count.items()}

    def __replace_best_subexpression(self, expr_indices: List[Set[tuple]], new_vars: List[Set[tuple]], subexpression: Set[tuple]) -> None:
        inverse_subexpression = {(v, -c) for v, c in subexpression}
        var_index = self.real_variables + len(new_vars)

        for indices in expr_indices + new_vars:
            if subexpression.issubset(indices):
                indices.difference_update(subexpression)
                indices.add((var_index, 1))
            elif inverse_subexpression.issubset(indices):
                indices.difference_update(inverse_subexpression)
                indices.add((var_index, -1))

        new_vars.append(subexpression)

    def __get_cost(self, expr_indices: List[List[dict]], new_vars: List[List[dict]]) -> int:
        return sum(len(expr) - 1 for expr in expr_indices + new_vars)

    def __sort_expression(self, expression: Set[tuple]) -> List[dict]:
        expression = [{"index": index, "value": value} for index, value in expression]
        return sorted(expression, key=lambda variable: variable["index"])
