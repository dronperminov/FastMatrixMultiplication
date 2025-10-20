import argparse
import os
import time
from typing import List, Optional

from ortools.sat.python.cp_model import CpModel, CpSolver, FEASIBLE, IntVar, OPTIMAL

from src.entities.scheme import Scheme
from src.utils.utils import pretty_time


def add_multiplication_constraints(model: CpModel, n: int, m: int, u: List[List[IntVar]], v: List[List[IntVar]], w: List[List[IntVar]]) -> List[List[List[List[IntVar]]]]:
    uvw = [[[[model.new_int_var(-1, 1, f'uvw{index}_{i}_{j}_{k}') for k in range(n * n)] for j in range(n * n)] for i in range(n * n)] for index in range(m)]

    for index in range(m):
        for i in range(n * n):
            for j in range(n * n):
                for k in range(n * n):
                    model.AddMultiplicationEquality(uvw[index][i][j][k], [u[index][i], v[index][j], w[index][k]])

    return uvw


def add_equation_constraints(model: CpModel, n: int, m: int, uvw: List[List[List[List[IntVar]]]]) -> None:
    for i in range(n * n):
        for j in range(n * n):
            for k in range(n * n):
                i1, i2, j1, j2, k1, k2 = i // n, i % n, j // n, j % n, k // n, k % n
                target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                model.Add(sum(uvw[index][i][j][k] for index in range(m)) == target)


def add_sign_symmetry_constraints(model: CpModel, m: int, u: List[List[IntVar]], w: List[List[IntVar]]) -> None:
    for index in range(m):
        model.add(u[index][0] >= 0)
        model.add(w[index][0] >= 0)


def lift_scheme(scheme: Scheme, workers: int, max_time: int) -> Optional[Scheme]:
    n = scheme.n
    m = scheme.m

    model = CpModel()

    u = [[model.new_int_var(-1, 1, f'u{index}_{i}') if scheme.u[index][i] else 0 for i in range(n * n)] for index in range(m)]
    v = [[model.new_int_var(-1, 1, f'v{index}_{i}') if scheme.v[index][i] else 0 for i in range(n * n)] for index in range(m)]
    w = [[model.new_int_var(-1, 1, f'w{index}_{i}') if scheme.w[index][i] else 0 for i in range(n * n)] for index in range(m)]

    uvw = add_multiplication_constraints(model, n=n, m=m, u=u, v=v, w=w)

    add_equation_constraints(model=model, n=n, m=m, uvw=uvw)
    add_sign_symmetry_constraints(model=model, m=m, u=u, w=w)

    solver = CpSolver()
    solver.parameters.num_search_workers = workers
    solver.parameters.max_time_in_seconds = max_time

    status = solver.solve(model)

    if status != OPTIMAL and status != FEASIBLE:
        return None

    u = [[solver.value(u[index][i]) for i in range(n * n)] for index in range(m)]
    v = [[solver.value(v[index][i]) for i in range(n * n)] for index in range(m)]
    w = [[solver.value(w[index][i]) for i in range(n * n)] for index in range(m)]
    return Scheme(n=n, m=m, u=u, v=v, w=w, z2=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="directory with z2 schemes", type=str, required=True)
    parser.add_argument("-o", "--output-dir", help="directory for save results", type=str, default="lifted")
    parser.add_argument("--workers", help="workers for solvation", type=int, default=8)
    parser.add_argument("--max-time", help="maximum lifting time", type=int, default=20)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for filename in sorted(os.listdir(args.input_dir)):
        if not filename.endswith("_scheme.json"):
            continue

        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, filename)

        if os.path.exists(output_path):
            print(f'Skip lifting scheme "{input_path}" (already lifted)')
            continue

        start_time = time.time()
        scheme = Scheme.load(input_path)
        scheme = lift_scheme(scheme=scheme, workers=args.workers, max_time=args.max_time)
        end_time = time.time()

        if not scheme:
            print(f'Unable to lift scheme "{input_path}" ({pretty_time(end_time - start_time)})')
            continue

        scheme.save(os.path.join(args.output_dir, filename))
        print(f'Successfully lift scheme "{input_path}" ({pretty_time(end_time - start_time)})')


if __name__ == '__main__':
    main()
