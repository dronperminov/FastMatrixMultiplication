import argparse
import os
import time
from typing import List

from ortools.sat.python.cp_model import CpModel, CpSolver, FEASIBLE, IntVar, OPTIMAL

from src.entities.scheme import Scheme
from src.entities.solution_collector import SolutionCollector
from src.utils.utils import pretty_time


def add_equation_constraints(model: CpModel, scheme: Scheme, u: List[List[IntVar]], v: List[List[IntVar]], w: List[List[IntVar]]) -> None:
    uv = [[[0 for _ in range(scheme.nn)] for _ in range(scheme.nn)] for _ in range(scheme.m)]

    for index in range(scheme.m):
        for i in range(scheme.nn):
            for j in range(scheme.nn):
                if type(u[index][i]) is IntVar and type(v[index][j]) is IntVar:
                    uv[index][i][j] = model.new_int_var(-1, 1, f"uv{index}_{i}_{j}")
                    model.AddMultiplicationEquality(uv[index][i][j], u[index][i] * 2 - 1, v[index][j] * 2 - 1)

    for i in range(scheme.nn):
        for j in range(scheme.nn):
            for k in range(scheme.nn):
                i1, i2, j1, j2, k1, k2 = i // scheme.n, i % scheme.n, j // scheme.n, j % scheme.n, k // scheme.n, k % scheme.n
                target = (i2 == j1) and (i1 == k2) and (j2 == k1)
                terms = []

                for index in range(scheme.m):
                    if type(uv[index][i][j]) is IntVar and type(w[index][k]) is IntVar:
                        uvw = model.new_int_var(-1, 1, f"uvw{index}_{i}_{j}_{k}")
                        model.AddMultiplicationEquality(uvw, uv[index][i][j], w[index][k] * 2 - 1)
                        terms.append(uvw)

                model.Add(sum(terms) == target)


def add_sign_symmetry_constraints(model: CpModel, n: int, m: int, u: List[List[IntVar]], w: List[List[IntVar]]) -> None:
    for index in range(m):
        u_value = [u[index][i] * 2 - 1 if type(u[index][i]) is IntVar else 0 for i in range(n * n)]
        w_value = [w[index][i] * 2 - 1 if type(w[index][i]) is IntVar else 0 for i in range(n * n)]

        u_abs = [1 if type(u[index][i]) is IntVar else 0 for i in range(n * n)]
        w_abs = [1 if type(w[index][i]) is IntVar else 0 for i in range(n * n)]

        for i in range(n * n):
            model.add(-u_value[i] <= sum(u_abs[j] for j in range(i)))
            model.add(-w_value[i] <= sum(w_abs[j] for j in range(i)))


def lift_scheme(scheme: Scheme, max_time: int, max_solutions: int) -> List[Scheme]:
    model = CpModel()

    u = [[model.new_int_var(0, 1, f'u{index}_{i}') if scheme.u[index][i] else 0 for i in range(scheme.nn)] for index in range(scheme.m)]
    v = [[model.new_int_var(0, 1, f'v{index}_{i}') if scheme.v[index][i] else 0 for i in range(scheme.nn)] for index in range(scheme.m)]
    w = [[model.new_int_var(0, 1, f'w{index}_{i}') if scheme.w[index][i] else 0 for i in range(scheme.nn)] for index in range(scheme.m)]

    add_equation_constraints(model=model, scheme=scheme, u=u, v=v, w=w)
    add_sign_symmetry_constraints(model=model, n=scheme.n, m=scheme.m, u=u, w=w)

    solver = CpSolver()

    if max_time > 0:
        solver.parameters.max_time_in_seconds = max_time

    solution_collector = SolutionCollector(u, v, w, max_solutions=max_solutions)
    status = solver.SearchForAllSolutions(model, solution_collector)

    if status != OPTIMAL and status != FEASIBLE:
        return []

    schemes = []

    for u_value, v_value, w_value in solution_collector.solutions:
        u_solution = [[u_value[index][i] * 2 - 1 if scheme.u[index][i] else 0 for i in range(scheme.nn)] for index in range(scheme.m)]
        v_solution = [[v_value[index][i] * 2 - 1 if scheme.v[index][i] else 0 for i in range(scheme.nn)] for index in range(scheme.m)]
        w_solution = [[w_value[index][i] * 2 - 1 if scheme.w[index][i] else 0 for i in range(scheme.nn)] for index in range(scheme.m)]

        schemes.append(Scheme(n=scheme.n, m=scheme.m, u=u_solution, v=v_solution, w=w_solution, z2=False))

    return schemes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="directory with z2 schemes", type=str, default="tasks/n4_m47/base/basic")
    parser.add_argument("-o", "--output-dir", help="directory for save results", type=str, default="lifted")
    parser.add_argument("--max-time", help="maximum lifting time", type=int, default=0)
    parser.add_argument("--max-solutions", help="maximum number of lifted solutions", type=int, default=1)
    parser.add_argument("--sort-scheme", help="sort lifted scheme", action="store_true", default=False)
    parser.add_argument("-f", "--force", help="force retry lifting existed scheme", action="store_true", default=False)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    filenames = sorted([filename for filename in os.listdir(args.input_dir) if filename.endswith("_scheme.json")])

    if not filenames:
        print("There are no schemes for lifting")
        return

    print(f"Start lifting {len(filenames)} schemes from Z2 to Z ring")
    print(f"- input directory: {args.input_dir}")
    print(f"- output directory: {args.output_dir}")
    print(f"- time limit: {args.max_time}")
    print("- ring coefficients: {-1, 0, 1}")

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
        lifted_schemes = lift_scheme(scheme=scheme, max_time=args.max_time, max_solutions=args.max_solutions)
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
