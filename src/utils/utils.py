from typing import Dict, List, Union


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


def pretty_matrix(matrix: List[List[bool]], name: str, indent: str = "") -> str:
    rows = [f'{"," if i > 0 else ""}\n{indent}    {[int(value) for value in row]}' for i, row in enumerate(matrix)]
    return f'{name} [{"".join(rows)}\n{indent}]'


def parse_value(value: Union[bool, int], literal2value: Dict[int, bool]) -> bool:
    if type(value) is bool:
        return value

    return literal2value[value]


def flatten(matrix: List[list]) -> list:
    return [value for row in matrix for value in row]
