import argparse
import os
import time

from src.lifting.ternary_solver import TernarySolver
from src.schemes.scheme import Scheme
from src.utils.utils import pretty_time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="directory with Z2 schemes", type=str)
    parser.add_argument("-o", "--output-dir", help="directory for save lifted schemes", type=str, default="lifted")
    parser.add_argument("--max-time", help="maximum lifting time", type=int, default=0)
    parser.add_argument("--max-solutions", help="maximum number of lifted solutions", type=int, default=1)
    parser.add_argument("--sort-scheme", help="sort lifted scheme", action="store_true", default=False)
    parser.add_argument("-f", "--force", help="force retry lifting existed scheme", action="store_true", default=False)
    parser.add_argument("--skip", help="number of files for skip", type=int, default=0)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    extensions = (".json", ".exp", ".m", "tensor.mpl", "lrp.mpl")
    filenames = sorted(filename for filename in os.listdir(args.input_dir) if filename.lower().endswith(extensions) and "solution" not in filename)[args.skip:]

    if not filenames:
        print("There are no schemes for lifting")
        return

    print(f"Start lifting {len(filenames)} schemes from Z2 ring to ZT coefficient set")
    print(f"- input directory: {args.input_dir}")
    print(f"- output directory: {args.output_dir}")
    print(f"- time limit: {args.max_time}")

    lifted = 0
    skipped = 0
    unable = 0
    total = len(filenames)
    total_integer = 0
    times = []

    for filename in filenames:
        input_path = os.path.join(args.input_dir, filename)
        name, extension = filename.rsplit(".", maxsplit=1)
        output_path = os.path.join(args.output_dir, f"{name}_ZT.{extension}")

        if not args.force and os.path.exists(output_path):
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already lifted)')
            continue

        scheme = Scheme.load(input_path, validate=False)
        if not scheme.z2:
            skipped += 1
            print(f'Skip lifting the scheme "{input_path}" (already ZT coefficient set)')
            continue

        solver = TernarySolver(scheme=scheme)
        start_time = time.time()
        lifted_schemes = solver.lift(max_time=args.max_time, max_solutions=args.max_solutions)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        if not lifted_schemes:
            unable += 1
            print(f'Unable to lift the scheme "{input_path}" ({pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))})')
            continue

        lifted += 1
        total_integer += len(lifted_schemes)

        name, extension = filename.rsplit(".", maxsplit=1)

        for i, lifted_scheme in enumerate(lifted_schemes):
            if args.sort_scheme:
                lifted_scheme.sort()

            lifted_name = (name if i == 0 else f"{name}_v{i + 1}")
            lifted_scheme.save(os.path.join(args.output_dir, f"{lifted_name}_ZT.json"))

        print(f'Successfully lift the scheme "{input_path}" ({pretty_time(elapsed_time)}, mean: {pretty_time(sum(times) / len(times))}, solutions: {len(lifted_schemes)})')

    print(f"\nTotal input schemes: {total}")
    print(f"- Lifted: {lifted} schemes ({lifted / total:.2%}), got {total_integer} schemes")
    print(f"- Skipped: {skipped} schemes ({skipped / total:.2%})")
    print(f"- Unable to lift: {unable} schemes ({unable / total:.2%})")


if __name__ == '__main__':
    main()
