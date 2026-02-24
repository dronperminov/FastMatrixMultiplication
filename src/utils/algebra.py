from fractions import Fraction
from typing import List, Optional


def rank_z2(matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    rank = 0
    pivot_row = 0

    for i in range(cols):
        if pivot_row >= rows:
            break

        pivot = -1
        for j in range(pivot_row, rows):
            if matrix[j][i] == 1:
                pivot = j
                break

        if pivot == -1:
            continue

        if pivot != pivot_row:
            matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]

        for j in range(pivot_row + 1, rows):
            if matrix[j][i] == 1:
                for k in range(i, cols):
                    matrix[j][k] ^= matrix[pivot_row][k]

        pivot_row += 1
        rank += 1

    return rank


def inverse_fraction_matrix(matrix: List[List[Fraction]]) -> Optional[List[List[Fraction]]]:
    assert len(matrix) == len(matrix[0])
    n = len(matrix)
    augmented = [[Fraction(value) for value in row] + [Fraction(i == j) for j in range(n)] for i, row in enumerate(matrix)]

    for col in range(n):
        pivot_row = col
        for row in range(col + 1, n):
            if abs(augmented[row][col]) > abs(augmented[pivot_row][col]):
                pivot_row = row

        if pivot_row != col:
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]

        if augmented[col][col] == 0:
            return None

        pivot = augmented[col][col]
        for j in range(2 * n):
            augmented[col][j] /= pivot

        for i in range(n):
            if i != col:
                factor = augmented[i][col]
                for j in range(2 * n):
                    augmented[i][j] -= factor * augmented[col][j]

    return [row[n:] for row in augmented]
