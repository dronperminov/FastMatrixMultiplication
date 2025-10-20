from typing import List


def get_rank(matrix: List[List[bool]]) -> int:
    n = len(matrix)
    matrix = [[int(value) for value in row] for row in matrix]

    if n == 2:
        return rank2x2(matrix)

    if n == 3:
        return rank3x3(matrix)

    raise ValueError("invalid matrix size")


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


def det2x2(matrix: List[List[int]]) -> int:
    [[a, b], [c, d]] = matrix
    return a * d - b * c


def det3x3(matrix: List[List[int]]) -> int:
    [[a, b, c], [d, e, f], [g, h, i]] = matrix
    return a * det2x2([[e, f], [h, i]]) - b * det2x2([[d, f], [g, i]]) + c * det2x2([[d, e], [g, h]])
