from typing import Callable, Tuple


def find_root_newton(func: Callable[[float], Tuple[float, float]], x0: float, eps: float) -> float:
    while True:
        fx, df = func(x0)
        if fx == 0:
            return x0

        x1 = x0 - fx / df
        if abs(x1 - x0) < eps:
            return x1

        x0 = x1


def find_root_bisection(func: Callable[[float], float], a: float, b: float, eps: float) -> float:
    fa = func(a)

    while b - a > eps:
        x = (a + b) / 2
        fx = func(x)

        if fa * fx < 0:
            b = x
        else:
            a, fa = x, fx

    return (a + b) / 2
