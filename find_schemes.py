import argparse
import json
import os
import re
import subprocess
import time
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from src.brent_equations.brent_equations_base import BrentEquationsBase
from src.brent_equations.brent_equations_cyclic import BrentEquationsCyclic
from src.entities.cnf import ConjunctiveNormalForm
from src.entities.scheme import Scheme
from src.entities.scheme_cyclic import SchemeCyclic
from src.utils.utils import pretty_time


def get_cryptominisat_args(cnf_path: str, max_time: int, rnd_polar: bool, threads: int, seed: int) -> List[str]:
    args = ["cryptominisat5", "--verb", "0"]

    if max_time > 0:
        args.extend(["--maxtime", f"{max_time}"])

    if seed > 0:
        args.extend(["-r", f"{seed + 1}"])

    if rnd_polar:
        args.extend(["--polar", "rnd"])

    args.extend(["--threads", f"{threads}"])
    args.append(cnf_path)
    return args


def solve_task(cnf_path: str, max_time: int, seed: int, threads: int) -> Tuple[List[str], str, float]:
    start_time = time.time()
    cmd = get_cryptominisat_args(cnf_path=cnf_path, max_time=max_time, rnd_polar=False, threads=threads, seed=seed)
    stdout = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    end_time = time.time()
    return cmd, stdout, end_time - start_time


def parse_solution(stdout: str, real_variables: List[int]) -> Tuple[Optional[bool], List[int]]:
    text2sat = {"SATISFIABLE": True, "UNSATISFIABLE": False}

    lines = stdout.strip().split("\n")
    sat = [line[2:].strip() for line in lines if line.startswith("s ")]
    sat = None if not sat else text2sat.get(sat[0], None)

    if not sat:
        return sat, []

    real_variables = set(real_variables)
    solution = " ".join([line[2:].strip() for line in lines if line.startswith("v ")])
    literals = [int(literal) for literal in re.split(r" +", solution) if literal != "0"]
    literals = [literal for literal in literals if abs(literal) in real_variables]
    return sat, literals


def save_solution(task_path: str, solution: List[int], version: int, complexities: Dict[int, int], show_scheme: bool, save_scheme: bool) -> None:
    solution_path = f"{task_path}{version:05d}_solution.json"
    scheme_path = f"{task_path}{version:05d}_scheme.json"

    with open(f"{task_path}.json", "r") as f:
        data = json.load(f)

    data["sat"] = solution

    with open(solution_path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    if data["algorithm"] == "cyclic":
        scheme = SchemeCyclic.from_solution(solution_path)
    else:
        scheme = Scheme.from_solution(solution_path)

    scheme.sort()

    complexities[scheme.complexity()] += 1

    if show_scheme:
        scheme.show()

    if save_scheme:
        scheme.save(scheme_path)

    sorted_complexities = {key: complexities[key] for key in sorted(complexities)}
    print(f"complexities: {sorted_complexities}")


def add_solutions_to_cnf(cnf: ConjunctiveNormalForm, solutions: List[List[int]], path: str) -> None:
    for solution in solutions:
        values = {abs(v): v for v in solution}
        ignore = [-values[literal] for literal in cnf.variables.get_real()]
        cnf.add([ignore])

    cnf.save(path)


def get_found_solutions(task_dir: str) -> List[List[int]]:
    solutions = []

    for filename in os.listdir(task_dir):
        if "_solution" not in filename:
            continue

        with open(f"{task_dir}/{filename}", "r") as f:
            solution = json.load(f)

        solutions.append(solution["sat"])

    return solutions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="matrix size", type=int, default=2)
    parser.add_argument("-m", help="number of multiplications", type=int, default=7)
    parser.add_argument("--mode", help="scheme mode", type=str, choices=["cyclic", "base"], default="base")
    parser.add_argument("-S", help="rank S", type=int, default=2)
    parser.add_argument("-T", help="rank T", type=int, default=7)
    parser.add_argument("--max-time", help="maximum solvation time", type=int, default=0)
    parser.add_argument("--threads", help="threads of solver", type=int, default=4)
    parser.add_argument("--seed", help="solver random seed", type=int, default=0)
    parser.add_argument("--retry-on-unsat", help="don't stop when get 'UNSATISFIABLE'", action='store_true', default=False)
    parser.add_argument("--show-scheme", help="show every found scheme", action='store_true', default=False)
    args = parser.parse_args()

    save_scheme = True

    if args.mode == "cyclic":
        task_dir = f"tasks/n{args.n}_m{args.m}/{args.mode}_S{args.S}_T{args.T}"
    else:
        task_dir = f"tasks/n{args.n}_m{args.m}/{args.mode}"

    task_path = f"{task_dir}/task"
    os.makedirs(task_dir, exist_ok=True)

    print(f"- task dir: {task_dir}")
    print(f"-n: {args.n}")
    print(f"-m: {args.m}")

    if args.max_time > 0:
        print(f"- time limit: {pretty_time(args.max_time)}")

    complexity2count = defaultdict(int)
    times = []

    solutions = get_found_solutions(task_dir=task_dir)
    if solutions:
        version = len(solutions) + 1
        print(f"\nSuccessfully loaded {len(solutions)} already founded solutions")
    else:
        version = 1

    print(f"Start finding solution {version}\n")

    while True:
        while True:
            if args.mode == "cyclic":
                equations = BrentEquationsCyclic(n=args.n, m=args.m, rank_s=args.S, rank_t=args.T)
            elif args.mode == "base":
                equations = BrentEquationsBase(n=args.n, m=args.m)
            else:
                raise ValueError(f'Unknown mode "{args.mode}"')

            equations.generate(task_path)

            if solutions:
                add_solutions_to_cnf(cnf=equations.cnf, solutions=solutions, path=f"{task_path}.cnf")

            cmd, stdout, elapsed_time = solve_task(cnf_path=f"{task_path}.cnf", max_time=args.max_time, seed=args.seed, threads=args.threads)
            times.append(elapsed_time)

            sat, solution = parse_solution(stdout=stdout, real_variables=equations.cnf.variables.get_real())

            print(f"\n{sat} {version}: {pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))}, [{min(times):.3f}...{max(times):.3f}] ({' '.join(cmd)})")

            print("\n=================================================================================================================================================")

            if sat:
                save_solution(task_path=task_path, solution=solution, version=version, complexities=complexity2count, show_scheme=True, save_scheme=True)
                break

            if type(sat) is bool and not args.retry_on_unsat:
                return

        while True:
            version += 1
            solutions.append(solution)
            add_solutions_to_cnf(cnf=equations.cnf, solutions=[solution], path=f"{task_path}.cnf")
            cmd, stdout, elapsed_time = solve_task(cnf_path=f"{task_path}.cnf", max_time=args.max_time, seed=args.seed, threads=args.threads)
            times.append(elapsed_time)

            sat, solution = parse_solution(stdout=stdout, real_variables=equations.cnf.variables.get_real())

            print(f"\n{sat} {version}: {pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))}, [{min(times):.3f}...{max(times):.3f}] ({' '.join(cmd)})")

            if sat:
                save_solution(task_path=task_path, solution=solution, version=version, complexities=complexity2count, show_scheme=args.show_scheme, save_scheme=save_scheme)
                continue

            if type(sat) is bool and not args.retry_on_unsat:
                return

            break


if __name__ == '__main__':
    main()
