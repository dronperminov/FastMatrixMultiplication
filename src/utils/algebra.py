from typing import List


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
