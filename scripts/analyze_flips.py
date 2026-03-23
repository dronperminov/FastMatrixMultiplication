import json
import os
from typing import List

from src.omega_optimization.flip_structure_optimizer import FlipStructureOptimizer
from src.omega_optimization.structure_depth_optimizer import StructureDepthOptimizer
from src.schemes.fractional_scheme import FractionalScheme
from src.schemes.scheme import Scheme


def analyze_scheme(path: str, depths: List[int], max_iterations: int, eps: float) -> dict:
    scheme = FractionalScheme.from_scheme(Scheme.load(path, validate=False))
    scheme_omega = scheme.omega()
    n1, n2, n3 = scheme.n
    ring = scheme.get_ring()

    flips = scheme.get_flips()
    structure_optimizer = FlipStructureOptimizer(n=n1, m=n2, p=n3, rank=scheme.m, flips=flips)
    structure_omega, structure = structure_optimizer.optimize(iterations=max_iterations, eps=eps)

    depth_optimizer = StructureDepthOptimizer(n=n1, m=n2, p=n3, structure=structure, eps=eps)
    omegas = {depth: depth_optimizer.optimize(depth=depth) for depth in depths}

    size = f"{scheme.n[0]}x{scheme.n[1]}x{scheme.n[2]}"
    print(f"| {size:8} | {scheme.m:4} | {scheme_omega:18.15f} | {structure_omega:17.15f} | {omegas[depths[-1]]:17.15f} | {len(flips):5} | {ring:>4} | {structure}")

    return {
        "path": path,
        "size": [n1, n2, n3],
        "rank": scheme.m,
        "ring": ring,
        "omega": scheme_omega,
        "flips": len(flips),
        "structure": structure,
        "structure_omega": structure_omega,
        "w1": depth_optimizer.w1,
        "w2": depth_optimizer.w2,
        "w3": depth_optimizer.w3,
        "depth2omega": omegas
    }


def analyze_schemes(paths: List[str], filename: str, depths: List[int]) -> None:
    results = []

    print(f"|   size   | rank |    scheme omega    |  structure omega  |    omega depth    | flips | ring | structure ")

    for path in paths:
        result = analyze_scheme(path, depths=depths, max_iterations=250, eps=1e-15)
        results.append(result)

        with open(filename, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)


def get_status_paths() -> List[str]:
    with open("../schemes/status.json") as f:
        status = json.load(f)

    paths = []
    for size, data in status.items():
        n1, n2, n3 = map(int, size.split("x"))
        if n1 < 3:
            continue

        for ring in ["Q", "Z", "ZT"]:
            for scheme_data in data["schemes"].get(ring, []):
                if scheme_data["rank"] == data["ranks"]["Q"]:
                    paths.append(f'../{scheme_data["source"]}')

    return paths


def get_directory_paths(directory: str) -> List[str]:
    extensions = "m", ".exp", "tensor.mpl",  ".txt", "lrp.mpl", ".json"
    paths = []

    for path, _, filenames in os.walk(directory):
        for filename in sorted(filenames):
            if filename.endswith(extensions):
                paths.append(os.path.join(path, filename).replace("\\", "/"))

    return paths


def main():
    paths = get_status_paths()
    # paths = get_directory_paths("../schemes/known")
    analyze_schemes(paths=paths, filename="status_results.json", depths=[1, 2, 3, 4, 8])


if __name__ == '__main__':
    main()
