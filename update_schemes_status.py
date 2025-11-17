import json
import os
from collections import defaultdict
from typing import Dict, List

from src.schemes.scheme import Scheme


def init_status(n_max: int = 9) -> dict:
    if os.path.exists("schemes/status.json"):
        with open("schemes/status.json", encoding="utf-8") as f:
            return json.load(f)

    status = {}

    for n1 in range(2, n_max + 1):
        for n2 in range(n1, n_max + 1):
            for n3 in range(n2, n_max + 1):
                status[f"{n1}{n2}{n3}"] = {"ranks": {}, "schemes": defaultdict(list)}

    return status


def is_duplicate(data: List[dict], scheme: Scheme) -> bool:
    for row in data:
        if row["rank"] != scheme.m:
            continue

        if Scheme.load(row["path"], validate=False) == scheme:
            return True

    return False


def postprocess_size(data: dict, ring2equal_rings: Dict[str, List[str]]) -> None:
    data["ranks"] = {}

    for ring, schemes in data["schemes"].items():
        schemes = sorted(schemes, key=lambda info: (info["rank"], info["complexity"], not info["source"].startswith("schemes/known/")))
        rank = schemes[0]["rank"]

        for equal_ring in ring2equal_rings[ring]:
            if equal_ring not in data["ranks"] or rank < data["ranks"][equal_ring]:
                data["ranks"][equal_ring] = rank

        data["schemes"][ring] = schemes


def get_scheme_paths(input_dir: str, scheme_extensions: List[str]) -> List[str]:
    scheme_filenames = []

    for path, _, filenames in os.walk(input_dir):
        for filename in sorted(filenames):
            if filename.endswith(tuple(scheme_extensions)):
                scheme_filenames.append(os.path.join(path, filename).replace("\\", "/"))

    return scheme_filenames


def analyze_schemes(input_dirs: List[str], n_max: int, max_count: int, extensions: List[str], ring2equal_rings: Dict[str, List[str]]) -> dict:
    for ring in ring2equal_rings:
        os.makedirs(f"schemes/status/{ring}", exist_ok=True)

    status = init_status(n_max=n_max)
    checked_paths = {scheme["source"] for data in status.values() for schemes in data["schemes"].values() for scheme in schemes}

    for input_dir in input_dirs:
        input_paths = get_scheme_paths(input_dir=input_dir, scheme_extensions=extensions)
        print(f"Analyze '{input_dir}': {len(input_paths)} scheme files")

        for input_path in input_paths:
            filename = os.path.basename(input_path)

            if filename in {"2x4x6_tensor.mpl"}:
                continue

            if input_path in checked_paths:
                continue

            print(f'- load "{input_path}"')
            scheme = Scheme.load(path=input_path, validate=False)
            ring = scheme.get_ring()
            size = f"{scheme.n[0]}{scheme.n[1]}{scheme.n[2]}"
            size_key = scheme.get_key()
            complexity = scheme.complexity()
            output_path = f"schemes/status/{ring}/{size}_m{scheme.m}_{ring}.json"

            print(f"  - size: {size}")
            print(f"  - rank: {scheme.m}")
            print(f"  - ring: {ring}")
            print(f"  - complexity: {complexity}")

            if os.path.exists(output_path):
                count = sum(1 for data in status[size_key]["schemes"][ring] if data["rank"] == scheme.m)

                if count > max_count or is_duplicate(status[size_key]["schemes"][ring], scheme):
                    print(f'  - skip ("{output_path}" already exists)')
                    continue

                output_path = output_path.replace(".json", f"_v{count + 1}.json")

            if ring not in status[size_key]["schemes"]:
                status[size_key]["schemes"][ring] = []

            status[size_key]["schemes"][ring].append({"rank": scheme.m, "complexity": complexity, "source": input_path, "path": output_path})
            scheme.save(output_path)
            print(f'  - saved to "{output_path}"')

        for size, data in status.items():
            postprocess_size(data=data, ring2equal_rings=ring2equal_rings)

        with open("schemes/status.json", "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False, sort_keys=False)

    return status


def format_rank(ring2rank: Dict[str, int], ring: str, min_rank: int, unique_rank: bool) -> str:
    if ring not in ring2rank:
        return "?"

    rank = ring2rank[ring]
    if min_rank is None or unique_rank or rank > min_rank:
        return str(rank)

    return f"**{rank}**"


def plot_table(status: Dict[str, dict], ring2equal_rings: Dict[str, List[str]]) -> None:
    print("|    size     | rank in `ZT`  | rank in `Z` | rank in `Q` |  rank in `Z2`   |")
    print("|:-----------:|:-------------:|:-----------:|:-----------:|:---------------:|")

    for size, data in status.items():
        known_ranks = {}
        for ring, schemes in data["schemes"].items():
            schemes = sorted([scheme for scheme in schemes if "known" in scheme["source"]], key=lambda s: s["rank"])
            if not schemes:
                continue

            rank = schemes[0]["rank"]

            for equal_ring in ring2equal_rings[ring]:
                if equal_ring not in known_ranks or rank < known_ranks[equal_ring]:
                    known_ranks[equal_ring] = rank

        current_ranks = data["ranks"]
        min_rank = min([current_ranks[ring] for ring in ["Q", "Z", "ZT"] if ring in current_ranks], default=None)
        diff = {}

        for ring in ring2equal_rings:
            rank_curr = format_rank(current_ranks, ring=ring, min_rank=min_rank, unique_rank=len(set(current_ranks.values())) == 1)
            rank_known = format_rank(known_ranks, ring=ring, min_rank=min_rank, unique_rank=len(set(current_ranks.values())) == 1)
            diff[ring] = rank_curr if rank_curr == rank_known else f"{rank_curr} ({rank_known})"

        size = f"`({size[0]}, {size[1]}, {size[2]})`"
        print(f'| {size:^11} | {diff["ZT"]:^13} | {diff["Z"]:^11} | {diff["Q"]:^11} | {diff["Z2"]:^15} |')


def main():
    input_dirs = [
        "schemes/known/tensor",
        "schemes/known/jakobmoosbauer_flips",
        "schemes/known/alpha_evolve",
        "schemes/known/fmm_add_reduction",
        "schemes/known/meta_flip_graph",
        "schemes/new/FlipGraphGPU",
        "schemes/new/FlipGraphGPU_Z",
        "schemes/new/FlipGraphGPU_Z2"
    ]

    ring2equal_rings = {"Q": ["Q"], "Z2": ["Z2"], "Z": ["Z", "Z2", "Q"], "ZT": ["ZT", "Z", "Z2", "Q"]}
    extensions = [".exp", ".m", "tensor.mpl", "lrp.mpl", ".json"]
    n_max = 8
    max_count = 200

    status = analyze_schemes(input_dirs=input_dirs, n_max=n_max, max_count=max_count, extensions=extensions, ring2equal_rings=ring2equal_rings)
    plot_table(status, ring2equal_rings=ring2equal_rings)


if __name__ == '__main__':
    main()
