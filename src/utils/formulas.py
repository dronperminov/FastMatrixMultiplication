from typing import List, Tuple

from src.entities.variable_storage import VariableStorage


def and_equality(target: int, variables: List[int]) -> List[List[int]]:
    clauses = []

    for v in variables:
        clauses.append([-target, v])

    clauses.append([target] + [-variable for variable in variables])
    return clauses


def xor_chain(x: List[int], variables: VariableStorage, k: int = 7) -> List[List[int]]:
    if len(x) <= k:
        return [x]

    clauses = []
    v = variables.get()
    first, last = x[:k], x[k:]
    clauses.append([*first, -v])
    clauses.extend(xor_chain([v, *last], variables=variables, k=k))
    return clauses


def at_least_k(x: List[int], k: int, variables: VariableStorage) -> List[List[int]]:
    assert k >= 0

    if k == 0:
        return []

    if k > len(x):
        return [[x[0]], [-x[0]]]  # unsatisfiable

    if k == len(x):
        return [[xi] for xi in x]

    s, clauses = __counter_constraints(x=x, count=k, variables=variables)
    clauses.append([s[k - 1]])
    return clauses


def at_most_k(x: List[int], k: int, variables: VariableStorage) -> List[List[int]]:
    assert k >= 0

    if k >= len(x):
        return []

    if k == 0:
        return [[-xi] for xi in x]

    s, clauses = __counter_constraints(x=x, count=k + 1, variables=variables)
    clauses.append([-s[k]])
    return clauses


def between_k(x: List[int], k1: int, k2: int, variables: VariableStorage) -> List[List[int]]:
    assert k1 >= 0
    assert k1 <= k2

    if k2 > len(x):
        k2 = len(x)

    if k1 == 0 and k2 == len(x):
        return []

    s, clauses = __counter_constraints(x=x, count=k2 + 1, variables=variables)

    if k1 > 0:
        clauses.append([s[k1 - 1]])

    if k2 < len(x):
        clauses.append([-s[k2]])

    return clauses


def lex_order(a: List[int], b: List[int], variables: VariableStorage, strict: bool) -> List[List[int]]:
    assert len(a) == len(b)

    if not a:
        return []

    clauses = []
    prev_eq = None

    for i, (ai, bi) in enumerate(zip(a, b)):
        eq = variables.get()

        clauses.append([-eq, -ai, bi])
        clauses.append([-eq, ai, -bi])

        if i == 0:
            clauses.append([-ai, bi])
            clauses.append([-ai, -bi, eq])
            clauses.append([ai, bi, eq])
        else:
            clauses.append([-prev_eq, -ai, bi])
            clauses.append([-eq, prev_eq])
            clauses.append([-prev_eq, -ai, -bi, eq])
            clauses.append([-prev_eq, ai, bi, eq])

        prev_eq = eq

    if strict:
        clauses.append([-prev_eq])

    return clauses


def lex_chain(values: List[List[int]], variables: VariableStorage, strict: bool) -> List[List[int]]:
    clauses = []

    for i in range(1, len(values)):
        clauses.extend(lex_order(values[i - 1], values[i], variables=variables, strict=strict))

    return clauses


def __counter_constraints(x: List[int], count: int, variables: VariableStorage) -> Tuple[List[int], List[List[int]]]:
    clauses = []
    prev_s = None

    for index, xi in enumerate(x):
        curr_s = [variables.get() for _ in range(min(index + 1, count))]

        for k in range(min(index + 1, count)):
            if index == 0 and k == 0:
                clauses.append([-curr_s[0], xi])
                clauses.append([-xi, curr_s[0]])
            else:
                if k == 0:
                    clauses.append([-curr_s[0], xi, prev_s[0]])
                    clauses.append([-xi, curr_s[0]])
                    clauses.append([-prev_s[0], curr_s[0]])
                else:
                    if index == k:
                        clauses.append([-curr_s[k], xi])
                        clauses.append([-curr_s[k], prev_s[k - 1]])
                    else:
                        clauses.append([-curr_s[k], xi, prev_s[k]])
                        clauses.append([-curr_s[k], prev_s[k - 1], prev_s[k]])
                        clauses.append([-prev_s[k], curr_s[k]])

                    clauses.append([-xi, -prev_s[k - 1], curr_s[k]])

        prev_s = curr_s

    return prev_s, clauses
