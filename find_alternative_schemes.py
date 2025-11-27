import argparse
import os.path
import random
import time
from typing import List

from src.entities.tensor_decomposition import TensorDecomposition
from src.schemes.scheme import Scheme
from src.schemes.scheme_bit_packed import SchemeBitPacked
from src.utils.utils import pretty_time


def add_previous_schemes(input_dir: str, scheme: Scheme, schemes: List[Scheme]) -> None:
    filenames = sorted(os.listdir(input_dir))
    for i, filename in enumerate(filenames):
        if not filename.endswith(".json"):
            continue

        previous_scheme = Scheme.from_json(os.path.join(input_dir, filename))
        if previous_scheme.n != scheme.n or previous_scheme.m != scheme.m:
            print(f'Skip scheme "{filename}" (sizes mismatch)')
            continue

        scheme_z2 = previous_scheme.to_z2()
        scheme_z2.sort()
        schemes.append(scheme_z2)
        print(f'Add "{filename}" scheme, now: {len(schemes)} for probable copy')


def flip_scheme(scheme: Scheme, max_iterations: int) -> Scheme:
    scheme_bit = SchemeBitPacked.from_scheme(scheme)

    for i in range(random.randint(1, max_iterations)):
        if not scheme_bit.try_flip():
            break

    return scheme_bit.to_scheme()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-path", help="path to existed scheme", type=str, required=True)
    parser.add_argument("-pu", "--probability-u", help="probability of u-elements copy (default: %(default).2f)", type=float, default=0.8)
    parser.add_argument("-pv", "--probability-v", help="probability of v-elements copy (default: %(default).2f)", type=float, default=0.8)
    parser.add_argument("-pw", "--probability-w", help="probability of w-elements copy (default: %(default).2f)", type=float, default=0.8)
    parser.add_argument("-o", "--output-dir", help="output dir (default: %(default)s)", type=str)
    parser.add_argument("-n", "--max-schemes", help="maximum number of schemes (default: %(default)d)", type=int, default=10000)
    parser.add_argument("-t", "--threads", help="number of sat solver threads (default: %(default)d)", type=int, default=2)
    parser.add_argument("--max-time", help="max sat solver time in seconds (default: %(default)d)", type=int, default=20)
    parser.add_argument("--max-complexity", help="max count of naive additions (default: %(default)d)", type=int, default=0)
    parser.add_argument("-f", "--flip-iterations", help="max number of flip iterations (default: %(default)d)", type=int, default=0)
    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        print(f'Scheme "{args.input_path}" is not exists')
        return

    scheme = Scheme.load(args.input_path).to_z2()

    (n1, n2, n3), m = scheme.n, scheme.m
    print(f"Successfully load scheme ({n1}, {n2}, {n3}, {m})")

    output_dir = os.path.join(args.output_dir, f"{n1}x{n2}x{n3}_m{m}")
    os.makedirs(output_dir, exist_ok=True)

    cnf_path = os.path.join(output_dir, f"{n1}x{n2}x{n3}_m{m}.cnf")
    tensor_decomposition = TensorDecomposition(n1=n1, n2=n2, n3=n3, m=m, max_complexity=args.max_complexity, path=cnf_path)

    schemes = [scheme]
    add_previous_schemes(input_dir=output_dir, scheme=scheme, schemes=schemes)

    for scheme in schemes:
        tensor_decomposition.exclude_scheme(scheme=scheme)

    pu, pv, pw = args.probability_u, args.probability_v, args.probability_w
    print(f"Start finding schemes from {len(schemes)} schemes (p = {pu}, {pv}, {pw}), max complexity: {args.max_complexity}")

    while len(schemes) <= args.max_schemes:
        scheme = random.choice(schemes)

        if args.flip_iterations > 0:
            scheme = flip_scheme(scheme=scheme, max_iterations=args.flip_iterations)

        scheme.sort()
        tensor_decomposition.set_probable_scheme(scheme=scheme, pu=pu, pv=pv, pw=pw)

        while len(schemes) <= args.max_schemes:
            start_time = time.time()
            solution = tensor_decomposition.solve(threads=args.threads, max_time=args.max_time)
            end_time = time.time()

            if not solution:
                print(f"{len(schemes)}. UNSAT ({solution}, elapsed: {pretty_time(end_time - start_time)})")
                break

            u, v, w = solution
            scheme = Scheme(n1=n1, n2=n2, n3=n3, m=m, z2=True, u=u, v=v, w=w)

            filename = f"{n1}x{n2}x{n3}_m{m}_c{scheme.complexity()}_{len(schemes):06d}_Z2.json"
            scheme.save(os.path.join(output_dir, filename))

            print(f'{len(schemes)}. SAT (elapsed: {pretty_time(end_time - start_time)}, saved as "{filename}"')
            schemes.append(scheme)


if __name__ == '__main__':
    main()
