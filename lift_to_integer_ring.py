import argparse
import os
import time
from typing import List

from ortools.sat.python.cp_model import CpModel, CpSolver, FEASIBLE, IntVar, OPTIMAL

from src.entities.scheme import Scheme
from src.entities.solution_collector import SolutionCollector
from src.utils.utils import pretty_time


def add_values_constrains(model: CpModel, scheme: Scheme, u: List[List[IntVar]], v: List[List[IntVar]], w: List[List[IntVar]], min_coef: int, max_coef: int) -> None:
    bool2values = {
        True: [value for value in range(min_coef, max_coef + 1) if abs(value) % 2 == 0],
        False: [value for value in range(min_coef, max_coef + 1) if abs(value) % 2 == 1]
    }

    for index in range(scheme.m):
        for i in range(scheme.n * scheme.n):
            for value in bool2values[scheme.u[index][i]]:
                model.add(u[index][i] != value)

            for value in bool2values[scheme.v[index][i]]:
                model.add(v[index][i] != value)

            for value in bool2values[scheme.w[index][i]]:
                model.add(w[index][i] != value)


def add_equation_constraints(model: CpModel, scheme: Scheme, u: List[List[IntVar]], v: List[List[IntVar]], w: List[List[IntVar]], min_coef: int, max_coef: int) -> None:
    max_prod2 = max(-min_coef, max_coef) ** 2
    max_prod = max(-min_coef, max_coef) ** 3

    uv = [[[model.new_int_var(-max_prod2, max_prod2, f"uv_{index}_{i}_{j}") for j in range(scheme.nn)] for i in range(scheme.nn)] for index in range(scheme.m)]

    for index in range(scheme.m):
        for i in range(scheme.nn):
            for j in range(scheme.nn):
                model.AddMultiplicationEquality(uv[index][i][j], u[index][i], v[index][j])

    for i in range(scheme.nn):
        for j in range(scheme.nn):
            for k in range(scheme.nn):
                i1, i2, j1, j2, k1, k2 = i // scheme.n, i % scheme.n, j // scheme.n, j % scheme.n, k // scheme.n, k % scheme.n
                target = (i2 == j1) and (i1 == k2) and (j2 == k1)

                terms = []

                for index in range(scheme.m):
                    uvw = model.new_int_var(-max_prod, max_prod, f"uvw{index}_{i}_{j}_{k}")
                    model.AddMultiplicationEquality(uvw, uv[index][i][j], w[index][k])
                    terms.append(uvw)

                model.Add(sum(terms) == target)


def add_sign_symmetry_constraints(model: CpModel, n: int, m: int, u: List[List[IntVar]], w: List[List[IntVar]], min_coef: int, max_coef: int) -> None:
    max_abs = max(-min_coef, max_coef)

    for index in range(m):
        u_abs = [model.new_int_var(0, max_abs, f"|u_{index}_{i}|") for i in range(n * n)]
        w_abs = [model.new_int_var(0, max_abs, f"|w_{index}_{i}|") for i in range(n * n)]

        for i in range(n * n):
            model.add_abs_equality(u_abs[i], u[index][i])
            model.add_abs_equality(w_abs[i], w[index][i])

            model.add(-u[index][i] <= sum(u_abs[j] for j in range(i)))
            model.add(-w[index][i] <= sum(w_abs[j] for j in range(i)))


def lift_scheme(scheme: Scheme, max_time: int, min_coef: int, max_coef: int, max_solutions: int) -> List[Scheme]:
    n = scheme.n
    m = scheme.m

    model = CpModel()

    u = [[model.new_int_var(min_coef, max_coef, f'u{index}_{i}') for i in range(n * n)] for index in range(m)]
    v = [[model.new_int_var(min_coef, max_coef, f'v{index}_{i}') for i in range(n * n)] for index in range(m)]
    w = [[model.new_int_var(min_coef, max_coef, f'w{index}_{i}') for i in range(n * n)] for index in range(m)]

    add_values_constrains(model=model, scheme=scheme, u=u, v=v, w=w, min_coef=min_coef, max_coef=max_coef)
    add_equation_constraints(model=model, scheme=scheme, u=u, v=v, w=w, min_coef=min_coef, max_coef=max_coef)
    add_sign_symmetry_constraints(model=model, n=n, m=m, u=u, w=w, min_coef=min_coef, max_coef=max_coef)

    solver = CpSolver()

    if max_time > 0:
        solver.parameters.max_time_in_seconds = max_time

    solution_collector = SolutionCollector(u, v, w, max_solutions=max_solutions)
    status = solver.SearchForAllSolutions(model, solution_collector)

    if status != OPTIMAL and status != FEASIBLE:
        return []

    return [Scheme(n=n, m=m, u=u, v=v, w=w, z2=False) for u, v, w in solution_collector.solutions]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="directory with z2 schemes", type=str, default="tasks/n4_m47/base/basic")
    parser.add_argument("-o", "--output-dir", help="directory for save results", type=str, default="lifted")
    parser.add_argument("--max-time", help="maximum lifting time", type=int, default=0)
    parser.add_argument("--max-solutions", help="maximum number of lifted solutions", type=int, default=1)
    parser.add_argument("--min-coef", help="maximum ring coefficient", type=int, default=-1)
    parser.add_argument("--max-coef", help="maximum ring coefficient", type=int, default=1)
    parser.add_argument("--sort-scheme", help="sort lifted scheme", action="store_true", default=False)
    parser.add_argument("-f", "--force", help="force retry lifting existed scheme", action="store_true", default=False)
    args = parser.parse_args()

    if args.min_coef >= 0:
        print(f"Min coef must be less than zero")
        return

    if args.max_coef <= 0:
        print(f"Max coef must be greater than zero")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    filenames = sorted([filename for filename in os.listdir(args.input_dir) if filename.endswith("_scheme.json")])

    if not filenames:
        print("There are no schemes for lifting")
        return

    print(f"Start lifting {len(filenames)} schemes from Z2 to Z ring")
    print(f"- input directory: {args.input_dir}")
    print(f"- output directory: {args.output_dir}")
    print(f"- time limit: {args.max_time}")
    print(f"- ring coefficients: {list(range(args.min_coef, args.max_coef + 1))}")

    lifted = 0
    skipped = 0
    unable = 0
    total = len(filenames)
    total_integer = 0

    for filename in filenames:
        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, filename[:-5])

        if not args.force and os.path.exists(output_path):
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already lifted)')
            continue

        scheme = Scheme.load(input_path)
        if not scheme.z2:
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already Z field)')
            continue

        start_time = time.time()
        lifted_schemes = lift_scheme(scheme=scheme, max_time=args.max_time, min_coef=args.min_coef, max_coef=args.max_coef, max_solutions=args.max_solutions)
        end_time = time.time()

        if not lifted_schemes:
            unable += 1
            print(f'Unable to lift the scheme "{input_path}" ({pretty_time(end_time - start_time)})')
            continue

        lifted += 1
        total_integer += len(lifted_schemes)
        os.makedirs(output_path, exist_ok=True)

        for i, lifted_scheme in enumerate(lifted_schemes):
            if args.sort_scheme:
                lifted_scheme.sort()

            lifted_scheme.save(os.path.join(output_path, f"{filename[:-5]}_v{i + 1}.json"))

        print(f'Successfully lift the scheme "{input_path}" ({pretty_time(end_time - start_time)}, integer solutions: {len(lifted_schemes)})')

    print(f"\nTotal input schemes: {total}")
    print(f"- Lifted: {lifted} schemes ({lifted / total:.2%}), got {total_integer} schemes")
    print(f"- Skipped: {skipped} schemes ({skipped / total:.2%})")
    print(f"- Unable to lift: {unable} schemes ({unable / total:.2%})")


if __name__ == '__main__':
    main()
