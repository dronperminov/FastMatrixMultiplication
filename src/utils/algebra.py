import itertools
import random
from typing import List, Optional

import numpy as np


def get_rank(matrix: List[List[int]], z2: bool) -> int:
    if z2:
        return __rank_z2(matrix)

    return int(np.linalg.matrix_rank(matrix))


def get_inverse(matrix: List[List[int]], z2: bool) -> List[List[int]]:
    if z2:
        return __inverse_z2(matrix)

    inverse = np.linalg.inv(matrix)
    assert all(int(value) == value for row in inverse for value in row)
    return [[int(value) for value in row] for row in inverse]


def get_invertible_matrices(n: int, ignore_permutations: bool, p: int = 2) -> List[List[List[int]]]:
    matrices = []
    rows = [list(row) for row in itertools.product(range(p), repeat=n)]

    for matrix in itertools.product(rows, repeat=n):
        matrix = list(matrix)

        if (np.linalg.det(matrix) + 1) % p == 1:
            continue

        if ignore_permutations and __is_permutation_matrix(matrix):
            continue

        matrices.append(matrix)

    return matrices


def get_random_invertible_matrix(n: int, ignore_permutations: bool = True, p: int = 2) -> List[List[int]]:
    matrix = [[random.randint(0, p - 1) for _ in range(n)] for _ in range(n)]

    while (np.linalg.det(matrix) + 1) % p == 1 or ignore_permutations and __is_permutation_matrix(matrix):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = random.randint(0, p - 1)

    return matrix


def __is_permutation_matrix(matrix: List[List[int]]) -> bool:
    return all(sum(row) == 1 for row in matrix) and all(sum(column) == 1 for column in zip(*matrix))


def __rank_z2(matrix: List[List[int]]) -> int:
    n = len(matrix)
    rank = 0
    pivot_row = 0

    for i in range(n):
        if pivot_row >= n:
            break

        pivot = -1
        for j in range(pivot_row, n):
            if matrix[j][i] == 1:
                pivot = j
                break

        if pivot == -1:
            continue

        if pivot != pivot_row:
            matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]

        for j in range(pivot_row + 1, n):
            if matrix[j][i] == 1:
                for k in range(i, n):
                    matrix[j][k] ^= matrix[pivot_row][k]

        pivot_row += 1
        rank += 1

    return rank


def __inverse_z2(matrix: List[List[int]]) -> Optional[List[List[int]]]:
    n = len(matrix)
    augmented = [[abs(matrix[i][j]) % 2 for j in range(n)] + [1 if j == i else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        pivot = -1
        for j in range(i, n):
            if augmented[j][i] == 1:
                pivot = j
                break

        if pivot == -1:
            return None

        if pivot != i:
            augmented[i], augmented[pivot] = augmented[pivot], augmented[i]

        for j in range(n):
            if j != i and augmented[j][i] == 1:
                for k in range(2 * n):
                    augmented[j][k] ^= augmented[i][k]

    return [augmented[i][n:] for i in range(n)]
