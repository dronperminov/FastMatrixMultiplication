import itertools
import random
from typing import List

import numpy as np

from src.utils.utils import flatten


def get_rank(matrix: List[List[bool]]) -> int:
    n = len(matrix)
    matrix = [[int(value) for value in row] for row in matrix]

    if n == 2:
        return rank2x2(matrix)

    if n == 3:
        return rank3x3(matrix)

    return int(np.linalg.matrix_rank(matrix))


def rank2x2(matrix: List[List[int]]) -> int:
    if det2x2(matrix) != 0:
        return 2

    if any([value != 0 for row in matrix for value in row]):
        return 1

    return 0


def rank3x3(matrix: List[List[int]]) -> int:
    if det3x3(matrix) != 0:
        return 3

    for row in range(3):
        for column in range(3):
            m2x2 = [[matrix[i][j] for j in range(3) if j != column] for i in range(3) if i != row]
            if det2x2(m2x2) != 0:
                return 2

    if any([value != 0 for row in matrix for value in row]):
        return 1

    return 0


def get_det(matrix: List[List[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return det2x2(matrix)

    if len(matrix) == 3:
        return det3x3(matrix)

    return np.linalg.det(matrix)


def det2x2(matrix: List[List[int]]) -> int:
    a, b, c, d = flatten(matrix)
    return a * d - b * c


def det3x3(matrix: List[List[int]]) -> int:
    a, b, c, d, e, f, g, h, i = flatten(matrix)
    return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h


def get_inverse(matrix: List[List[int]], z2: bool) -> List[List[int]]:
    if len(matrix) == 1:
        inverse = [[1 // matrix[0][0]]]
    elif len(matrix) == 2:
        inverse = inverse2x2(matrix)
    elif len(matrix) == 3:
        inverse = inverse3x3(matrix)
    else:
        inverse = np.linalg.inv(matrix)

    inverse = [[abs(int(value)) % 2 if z2 else int(value) for value in row] for row in inverse]
    return inverse


def inverse3x3(matrix: List[List[int]]) -> List[List[int]]:
    a, b, c, d, e, f, g, h, i = flatten(matrix)
    det = det3x3(matrix)
    adj = [
        [e * i - f * h, c * h - b * i, b * f - c * e],
        [f * g - d * i, a * i - c * g, c * d - a * f],
        [d * h - e * g, b * g - a * h, a * e - b * d]
    ]

    assert all(abs(v) % abs(det) == 0 for v in flatten(adj))
    return [[value // det for value in row] for row in adj]


def inverse2x2(matrix: List[List[int]]) -> List[List[int]]:
    a, b, c, d = flatten(matrix)
    det = det2x2(matrix)
    assert all(abs(v) % abs(det) == 0 for v in flatten(matrix))

    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]


def get_invertible_matrices(n: int, ignore_permutations: bool, p: int = 2) -> List[List[List[int]]]:
    matrices = []
    rows = [list(row) for row in itertools.product(range(p), repeat=n)]

    for matrix in itertools.product(rows, repeat=n):
        matrix = list(matrix)
        det = get_det(matrix)

        if (det + 1) % p == 1:
            continue

        if ignore_permutations and __is_permutation_matrix(matrix):
            continue

        matrices.append(matrix)

    return matrices


def get_random_invertible_matrix(n: int, ignore_permutations: bool = True, p: int = 2) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    while (get_det(matrix) + 1) % p == 1 or ignore_permutations and __is_permutation_matrix(matrix):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = random.randint(0, p - 1)

    return matrix


def __is_permutation_matrix(matrix: List[List[int]]) -> bool:
    return all(sum(row) == 1 for row in matrix) and all(sum(column) == 1 for column in zip(*matrix))
