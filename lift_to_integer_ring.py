import argparse
import os
import time
from typing import List, Optional

from ortools.sat.python.cp_model import CpModel, CpSolver, FEASIBLE, IntVar, OPTIMAL

from src.entities.scheme import Scheme
from src.utils.utils import pretty_time


def add_non_zero_constrains(model: CpModel, n: int, m: int, u: List[List[IntVar]], v: List[List[IntVar]], w: List[List[IntVar]]) -> None:
    for index in range(m):
        for i in range(n * n):
            if type(u[index][i]) is IntVar:
                model.add(u[index][i] != 0)

            if type(v[index][i]) is IntVar:
                model.add(v[index][i] != 0)

            if type(w[index][i]) is IntVar:
                model.add(w[index][i] != 0)


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


def add_sign_symmetry_constraints(model: CpModel, n: int, m: int, u: List[List[IntVar]], w: List[List[IntVar]]) -> None:
    u_abs = [[model.new_int_var(0, 1, f'|u{index}_{i}|') for i in range(n * n)] for index in range(m)]
    w_abs = [[model.new_int_var(0, 1, f'|w{index}_{i}|') for i in range(n * n)] for index in range(m)]

    for index in range(m):
        model.add(u[index][0] >= 0)

        for i in range(n * n):
            model.add(-u[index][i] <= sum(u_abs[index][j] for j in range(i)))

        model.add(w[index][0] >= 0)

        for i in range(n * n):
            model.add(-w[index][i] <= sum(w_abs[index][j] for j in range(i)))


def lift_scheme(scheme: Scheme, workers: int, max_time: int) -> Optional[Scheme]:
    n = scheme.n
    m = scheme.m

    model = CpModel()

    u = [[model.new_int_var(-1, 1, f'u{index}_{i}') if scheme.u[index][i] else 0 for i in range(n * n)] for index in range(m)]
    v = [[model.new_int_var(-1, 1, f'v{index}_{i}') if scheme.v[index][i] else 0 for i in range(n * n)] for index in range(m)]
    w = [[model.new_int_var(-1, 1, f'w{index}_{i}') if scheme.w[index][i] else 0 for i in range(n * n)] for index in range(m)]

    uvw = add_multiplication_constraints(model, n=n, m=m, u=u, v=v, w=w)

    add_non_zero_constrains(model=model, n=n, m=m, u=u, v=v, w=w)
    add_equation_constraints(model=model, n=n, m=m, uvw=uvw)
    add_sign_symmetry_constraints(model=model, n=n, m=m, u=u, w=w)

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
    filenames = sorted([filename for filename in os.listdir(args.input_dir) if filename.endswith("_scheme.json")])

    lifted = 0
    skipped = 0
    unable = 0
    total = len(filenames)

    for filename in filenames:
        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, filename)

        if os.path.exists(output_path):
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already lifted)')
            continue

        scheme = Scheme.load(input_path)
        if not scheme.z2:
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already Z field)')
            continue

        start_time = time.time()
        scheme = lift_scheme(scheme=scheme, workers=args.workers, max_time=args.max_time)
        end_time = time.time()

        if not scheme:
            unable += 1
            print(f'Unable to lift the scheme "{input_path}" ({pretty_time(end_time - start_time)})')
            continue

        lifted += 1
        scheme.sort()
        scheme.save(os.path.join(args.output_dir, filename))
        print(f'Successfully lift the scheme "{input_path}" ({pretty_time(end_time - start_time)})')

    print(f"\nTotal schemes: {total}")
    print(f"- Lifted: {lifted} schemes ({lifted / total:.2%})")
    print(f"- Skipped: {skipped} schemes ({skipped / total:.2%})")
    print(f"- Unable to lift: {unable} schemes ({unable / total:.2%})")


if __name__ == '__main__':
    main()
