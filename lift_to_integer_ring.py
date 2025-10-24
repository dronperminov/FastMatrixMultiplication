import argparse
import os
import time

from src.entities.scheme import Scheme
from src.lifting.ring_solver_ortools import RingSolverOrtools
from src.lifting.ternary_solver import TernarySolver
from src.utils.utils import pretty_time


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
    parser.add_argument("--skip", help="number of files for skip", type=int, default=0)
    args = parser.parse_args()

    if args.min_coef >= 0:
        print(f"Min coef must be less than zero")
        return

    if args.max_coef <= 0:
        print(f"Max coef must be greater than zero")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    filenames = sorted([filename for filename in os.listdir(args.input_dir) if filename.endswith("_scheme.json")])[args.skip:]

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

        if not args.force and os.path.exists(os.path.join(args.output_dir, filename)):
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already lifted)')
            continue

        scheme = Scheme.load(input_path)
        if not scheme.z2:
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already Z field)')
            continue

        if args.min_coef == -1 and args.max_coef == 1:
            solver = TernarySolver(scheme=scheme)
        else:
            solver = RingSolverOrtools(scheme=scheme, min_coef=args.min_coef, max_coef=args.max_coef)

        start_time = time.time()
        lifted_schemes = solver.lift(max_time=args.max_time, max_solutions=args.max_solutions)
        elapsed_time = time.time() - start_time

        if not lifted_schemes:
            unable += 1
            print(f'Unable to lift the scheme "{input_path}" ({pretty_time(elapsed_time)})')
            continue

        lifted += 1
        total_integer += len(lifted_schemes)

        for i, lifted_scheme in enumerate(lifted_schemes):
            if args.sort_scheme:
                lifted_scheme.sort()

            lifted_filename = filename if i == 0 else filename.replace("_scheme.json", f"_v{i + 1}_scheme.json")
            lifted_scheme.save(os.path.join(args.output_dir, lifted_filename))

        print(f'Successfully lift the scheme "{input_path}" ({pretty_time(elapsed_time)}, solutions: {len(lifted_schemes)})')

    print(f"\nTotal input schemes: {total}")
    print(f"- Lifted: {lifted} schemes ({lifted / total:.2%}), got {total_integer} schemes")
    print(f"- Skipped: {skipped} schemes ({skipped / total:.2%})")
    print(f"- Unable to lift: {unable} schemes ({unable / total:.2%})")


if __name__ == '__main__':
    main()
