from fractions import Fraction
from typing import Iterable, Union


def format_value(value: Union[int, str, Fraction]) -> str:
    if isinstance(value, Fraction):
        return f'"{value.numerator}/{value.denominator}"'

    return str(value)


def pretty_matrix(matrix: Iterable[Iterable], name: str, indent: str = "") -> str:
    rows = [f'{"," if i > 0 else ""}\n{indent}    [{", ".join(format_value(value) for value in row)}]' for i, row in enumerate(matrix)]
    return f'{name} [{"".join(rows)}\n{indent}]'


def pretty_time(seconds: float) -> str:
    if seconds < 10:
        return f"{seconds:.4f} sec"

    if seconds < 60:
        return f"{seconds:.2f} sec"

    seconds = int(seconds + 0.5)

    if seconds < 3600:
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes} min {seconds} sec"

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours} hours {minutes} mins {seconds} sec"
