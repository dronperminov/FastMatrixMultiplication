import argparse
import json
import os
import re
import subprocess
import time
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

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


def save_solution(task_path: str, solution: List[int], version: int, unique_ranks: Set[str], show_scheme: bool, save_scheme: bool) -> None:
    model_path = os.path.join(task_path, "model.json")
    solution_path = os.path.join(task_path, f"{version:05d}_solution.json")
    scheme_path = os.path.join(task_path, f"{version:05d}_scheme.json")

    with open(model_path, "r") as f:
        data = json.load(f)

    data["sat"] = solution

    with open(solution_path, "w") as f:
        json.dump(data, f, ensure_ascii=False)

    if data["algorithm"] == "cyclic":
        scheme = SchemeCyclic.from_solution(solution_path)
    else:
        scheme = Scheme.from_solution(solution_path)

    scheme.sort()
    unique_ranks.add(scheme.invariant_rank_pattern())

    if show_scheme:
        scheme.show()

    if save_scheme:
        scheme.save(scheme_path)

    print(f"unique ranks: {len(unique_ranks)}")


def add_solutions_to_cnf(cnf: ConjunctiveNormalForm, solutions: List[List[int]], path: str) -> None:
    for solution in solutions:
        values = {abs(v): v for v in solution}
        ignore = [-values[literal] for literal in cnf.variables.get_real()]
        cnf.add([ignore])

    cnf.save(path)


def get_found_solutions(task_dir: str) -> List[List[int]]:
    solutions = []

    for filename in os.listdir(task_dir):
        if filename.endswith("_solution.json"):
            with open(f"{task_dir}/{filename}", "r") as f:
                solution = json.load(f)
                solutions.append(solution["sat"])

    return solutions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="matrix size (default: %(default)d)", type=int, default=2)
    parser.add_argument("-m", help="number of multiplications (default: %(default)d)", type=int, default=7,)
    parser.add_argument("--mode", help="scheme mode (default: %(default)s)", type=str, choices=["cyclic", "base"], default="base")
    parser.add_argument("-S", help="rank S", type=int, default=2)
    parser.add_argument("-T", help="rank T", type=int, default=7)
    parser.add_argument("--max-time", help="maximum solvation time (unlimited by default)", type=int, default=0)
    parser.add_argument("--threads", help="threads of solver (default: %(default)d)", type=int, default=4)
    parser.add_argument("--seed", help="solver random seed", type=int, default=0)
    parser.add_argument("--retry-on-unsat", help="don't stop when get 'UNSATISFIABLE'", action='store_true', default=False)
    parser.add_argument("--show-scheme", help="show every found scheme", action='store_true', default=False)
    parser.add_argument("--task-name", help="name of the task", type=str, default="task")
    args = parser.parse_args()

    if args.mode == "cyclic" and args.S + 3 * args.T != args.m:
        print(f"Invalid decomposition ranks (S + 3T != m): {args.S} + 3*{args.T} = {args.S + 3 * args.T} != {args.m}")
        return

    save_scheme = True

    if args.mode == "cyclic":
        task_dir = f"tasks/n{args.n}_m{args.m}/{args.mode}_S{args.S}_T{args.T}/{args.task_name}"
    else:
        task_dir = f"tasks/n{args.n}_m{args.m}/{args.mode}/{args.task_name}"

    os.makedirs(task_dir, exist_ok=True)

    print(f"- task dir: {task_dir}")
    print(f"-n: {args.n}")
    print(f"-m: {args.m}")

    if args.max_time > 0:
        print(f"- time limit: {pretty_time(args.max_time)}")

    unique_ranks = set()
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

            equations.generate(task_dir)

            if solutions:
                add_solutions_to_cnf(cnf=equations.cnf, solutions=solutions, path=os.path.join(task_dir, "model.cnf"))

            cmd, stdout, elapsed_time = solve_task(cnf_path=os.path.join(task_dir, "model.cnf"), max_time=args.max_time, seed=args.seed, threads=args.threads)
            times.append(elapsed_time)

            sat, solution = parse_solution(stdout=stdout, real_variables=equations.cnf.variables.get_real())

            print(f"\n{sat} {version}: {pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))}, [{min(times):.3f}...{max(times):.3f}] ({' '.join(cmd)})")

            print("\n=================================================================================================================================================")

            if sat:
                save_solution(task_path=task_dir, solution=solution, version=version, unique_ranks=unique_ranks, show_scheme=True, save_scheme=True)
                break

            if type(sat) is bool and not args.retry_on_unsat:
                return

        while True:
            version += 1
            solutions.append(solution)
            add_solutions_to_cnf(cnf=equations.cnf, solutions=[solution], path=os.path.join(task_dir, "model.cnf"))
            cmd, stdout, elapsed_time = solve_task(cnf_path=os.path.join(task_dir, "model.cnf"), max_time=args.max_time, seed=args.seed, threads=args.threads)
            times.append(elapsed_time)

            sat, solution = parse_solution(stdout=stdout, real_variables=equations.cnf.variables.get_real())

            print(f"\n{sat} {version}: {pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))}, [{min(times):.3f}...{max(times):.3f}] ({' '.join(cmd)})")

            if sat:
                save_solution(task_path=task_dir, solution=solution, version=version, unique_ranks=unique_ranks, show_scheme=args.show_scheme, save_scheme=save_scheme)
                continue

            if type(sat) is bool and not args.retry_on_unsat:
                return

            break


if __name__ == '__main__':
    main()
