import argparse
import os
import time

from src.entities.scheme import Scheme
from src.utils.algebra import get_random_invertible_matrix
from src.utils.utils import pretty_time


def probability_minimization(scheme: Scheme, max_iterations: int) -> Scheme:
    best_scheme = scheme.copy()
    best_complexity = scheme.complexity()

    for _ in range(max_iterations):
        u = get_random_invertible_matrix(n=scheme.n, ignore_permutations=False)
        v = get_random_invertible_matrix(n=scheme.n, ignore_permutations=False)
        w = get_random_invertible_matrix(n=scheme.n, ignore_permutations=False)
        scheme.sandwiching(u=u, v=v, w=w)

        complexity = scheme.complexity()

        if complexity < best_complexity:
            best_complexity = complexity
            best_scheme = scheme.copy()

    return best_scheme


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="directory with schemes", type=str, required=True)
    parser.add_argument("-o", "--output-dir", help="directory for save results", type=str, default="minimized")
    parser.add_argument("--max-iterations", help="maximum sandwiching operations", type=int, default=500)
    parser.add_argument("-f", "--force", help="force retry minimization existed scheme", action="store_true", default=False)
    parser.add_argument("--skip", help="number of files for skip", type=int, default=0)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    filenames = sorted([filename for filename in os.listdir(args.input_dir) if filename.endswith("_scheme.json")])[args.skip:]

    if not filenames:
        print("There are no schemes for minimization")
        return

    print(f"Start minimizing {len(filenames)} schemes")
    print(f"- input directory: {args.input_dir}")
    print(f"- output directory: {args.output_dir}")
    print(f"- max iterations: {args.max_iterations}\n")

    minimized = 0
    skipped = 0
    unable = 0
    total = len(filenames)
    times = []

    for filename in filenames:
        input_path = os.path.join(args.input_dir, filename)

        if not args.force and os.path.exists(os.path.join(args.output_dir, filename)):
            skipped += 1
            print(f'Skip minimization the scheme "{input_path}" (already minimized)')
            continue

        scheme = Scheme.load(input_path)
        initial_complexity = scheme.complexity()

        start_time = time.time()
        minimized_scheme = probability_minimization(scheme=scheme, max_iterations=args.max_iterations)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        minimized_complexity = minimized_scheme.complexity()
        minimized_scheme.sort()
        minimized_scheme.save(os.path.join(args.output_dir, filename))

        if minimized_complexity == initial_complexity:
            unable += 1
            print(f'Unable to minimize the scheme "{input_path}" from {initial_complexity} ({pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))})')
            continue

        minimized += 1
        print(f'Successfully minimize the scheme "{input_path}" from {initial_complexity} to {minimized_complexity} ({pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))})')

    print(f"\nTotal input schemes: {total}")
    print(f"- Minimized: {minimized} schemes ({minimized / total:.2%})")
    print(f"- Skipped: {skipped} schemes ({skipped / total:.2%})")
    print(f"- Unable to minimize: {unable} schemes ({unable / total:.2%})")


if __name__ == '__main__':
    main()
