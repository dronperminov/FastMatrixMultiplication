import json
import os
from collections import defaultdict
from collections.abc import Set
from typing import Dict, List, Optional

from src.schemes.scheme import Scheme


def init_status(n_max: int) -> dict:
    if os.path.exists("schemes/status.json"):
        with open("schemes/status.json", encoding="utf-8") as f:
            current_status = json.load(f)
    else:
        current_status = {}

    status = {}

    for n1 in range(2, n_max + 1):
        for n2 in range(n1, n_max + 1):
            for n3 in range(n2, n_max + 1):
                if n1 * n2 <= 64 and n2 * n3 <= 64 and n1 * n3 <= 64:
                    status[f"{n1}x{n2}x{n3}"] = current_status.get(f"{n1}x{n2}x{n3}", {"ranks": {}, "complexities": {}, "schemes": defaultdict(list)})

    return status


def find_duplicate(data: List[dict], scheme: Scheme) -> Optional[dict]:
    for row in data:
        if row["rank"] != scheme.m:
            continue

        if Scheme.load(row["path"], validate=False) == scheme:
            return row

    return None


def postprocess_size(data: dict, ring2equal_rings: Dict[str, List[str]]) -> None:
    data["ranks"] = {}
    data["complexities"] = {}

    for ring, schemes in data["schemes"].items():
        schemes = sorted(schemes, key=lambda info: (info["rank"], info["complexity"], not info["source"].startswith("schemes/known/")))
        rank = schemes[0]["rank"]
        complexity = schemes[0]["complexity"]

        for equal_ring in ring2equal_rings[ring]:
            if equal_ring not in data["ranks"] or rank < data["ranks"][equal_ring]:
                data["ranks"][equal_ring] = rank

            if equal_ring not in data["complexities"] or complexity < data["complexities"][equal_ring]:
                data["complexities"][equal_ring] = complexity

        data["schemes"][ring] = schemes


def get_scheme_paths(input_dir: str, scheme_extensions: List[str]) -> List[str]:
    scheme_filenames = []

    for path, _, filenames in os.walk(input_dir):
        for filename in sorted(filenames):
            if filename.endswith(tuple(scheme_extensions)):
                scheme_filenames.append(os.path.join(path, filename).replace("\\", "/"))

    return scheme_filenames


def get_checked_paths(status: Dict[str, dict]) -> Set[str]:
    checked_paths = set()

    for data in status.values():
        for schemes in data["schemes"].values():
            for scheme in schemes:
                checked_paths.add(scheme["source"])

                for duplicate_path in scheme.get("duplicates", []):
                    checked_paths.add(duplicate_path)

    return checked_paths


def analyze_schemes(input_dirs: List[str], n_max: int, extensions: List[str], ring2equal_rings: Dict[str, List[str]]) -> dict:
    for ring in ring2equal_rings:
        os.makedirs(f"schemes/status/{ring}", exist_ok=True)

    status = init_status(n_max=n_max)
    checked_paths = get_checked_paths(status=status)

    for input_dir in input_dirs:
        input_paths = get_scheme_paths(input_dir=input_dir, scheme_extensions=extensions)
        print(f"Analyze '{input_dir}': {len(input_paths)} scheme files")

        for input_path in input_paths:
            if input_path in checked_paths:
                continue

            print(f'- load "{input_path}"')
            scheme = Scheme.load(path=input_path, validate=False)
            scheme.fix_sizes()

            ring = scheme.get_ring()
            size = scheme.get_key(sort=False)
            size_key = scheme.get_key(sort=True)
            complexity = scheme.complexity()
            output_path = f"schemes/status/{ring}/{size}_m{scheme.m}_{ring}.json"

            print(f"  - size: {size}")
            print(f"  - rank: {scheme.m}")
            print(f"  - ring: {ring}")
            print(f"  - complexity: {complexity}")

            if os.path.exists(output_path):
                count = sum(1 for data in status[size_key]["schemes"][ring] if data["rank"] == scheme.m)
                duplicate = find_duplicate(status[size_key]["schemes"][ring], scheme)
                if duplicate:
                    print(f'  - skip duplicate ("{output_path}" already exists)')

                    if "duplicates" not in duplicate:
                        duplicate["duplicates"] = []
                    duplicate["duplicates"].append(input_path)
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


def format_value(ring2value: Dict[str, int], ring: str, min_value: int, unique_value: bool) -> str:
    return "?" if ring not in ring2value else f"{ring2value[ring]}"


def format_size(size: str) -> str:
    n1, n2, n3 = map(int, size.split("x"))
    return f"`({n1}, {n2}, {n3})`"


def plot_full_table(status: Dict[str, dict], ring2equal_rings: Dict[str, List[str]]) -> None:
    print("## Ranks and complexities")
    print("|    size     | rank in `ZT`  | rank in `Z` | rank in `Q` |  rank in `Z2`   | complexity in `ZT` | complexity in `Z` | complexity in `Q` |")
    print("|:-----------:|:-------------:|:-----------:|:-----------:|:---------------:|:------------------:|:-----------------:|:-----------------:|")

    for size, data in status.items():
        known_ranks, known_complexities = {}, {}

        for ring, schemes in data["schemes"].items():
            known_schemes = sorted([scheme for scheme in schemes if "known" in scheme["source"]], key=lambda s: (s["rank"], s["complexity"]))
            if not known_schemes:
                continue

            rank = known_schemes[0]["rank"]
            complexity = known_schemes[0]["complexity"]

            for equal_ring in ring2equal_rings[ring]:
                if equal_ring not in known_ranks or rank < known_ranks[equal_ring]:
                    known_ranks[equal_ring] = rank

                if equal_ring not in known_complexities or complexity < known_complexities[equal_ring]:
                    known_complexities[equal_ring] = complexity

        current_ranks, current_complexities = data["ranks"], data["complexities"]
        min_rank = min([current_ranks[ring] for ring in ["Q", "Z", "ZT"] if ring in current_ranks], default=None)
        min_complexity = min([current_complexities[ring] for ring in ["Q", "Z", "ZT"] if ring in current_complexities], default=None)

        unique_ranks = len(set(current_ranks[ring] for ring in ["Q", "Z", "ZT"] if ring in current_ranks)) == 1
        unique_complexities = len(set(current_complexities[ring] for ring in ["Q", "Z", "ZT"] if ring in current_complexities)) == 1

        diff_rank = {}
        diff_complexity = {}

        for ring in ring2equal_rings:
            rank_curr = format_value(current_ranks, ring=ring, min_value=min_rank, unique_value=unique_ranks)
            rank_known = format_value(known_ranks, ring=ring, min_value=min_rank, unique_value=unique_ranks)
            diff_rank[ring] = rank_curr if rank_curr == rank_known else f"{rank_curr} ({rank_known})"

            if unique_ranks:
                complexity_curr = format_value(current_complexities, ring=ring, min_value=min_complexity, unique_value=unique_complexities)
                complexity_known = format_value(known_complexities, ring=ring, min_value=min_complexity, unique_value=unique_complexities)
                diff_complexity[ring] = complexity_curr if complexity_curr == complexity_known else f"{complexity_curr} ({complexity_known})"
            else:
                diff_complexity[ring] = "-"

        n1, n2, n3 = size.split("x")
        size = f"`({n1}, {n2}, {n3})`"
        print(f'| {size:^11} | {diff_rank["ZT"]:^13} | {diff_rank["Z"]:^11} | {diff_rank["Q"]:^11} | {diff_rank["Z2"]:^15} | {diff_complexity["ZT"]:^18} | {diff_complexity["Z"]:^17} | {diff_complexity["Q"]:^17} |')


def plot_new_ranks_table(status: Dict[str, dict]) -> None:
    print("\n\n### New best ranks in ternary field (ZT)")
    print("New schemes have been discovered that improve the state-of-the-art for matrix multiplication in the ternary field, achieving lower ranks than previously known.\n")
    print("|    Format    | Prev rank | New rank |")
    print("|:------------:|:---------:|:--------:|")

    for size, data in status.items():
        ring2known_ranks = {ring: [scheme["rank"] for scheme in schemes if "known" in scheme["source"]] for ring, schemes in data["schemes"].items() if ring != "Z2"}
        min_known_rank = min(scheme["rank"] for ring, schemes in data["schemes"].items() for scheme in schemes if ring != "Z2" and "known" in scheme["source"])
        min_rank = min(rank for ring, rank in data["ranks"].items() if ring != "Z2")
        if min_rank >= min_known_rank:
            continue

        ring2known_rank = {ring: min(ranks) for ring, ranks in ring2known_ranks.items() if ranks}
        known_rings = [ring for ring in ["Z", "Q"] if ring2known_rank.get(ring) == min_known_rank]
        size = format_size(size)
        prev = f"{min_known_rank} (`{'/'.join(known_rings)}`)"
        print(f"| {size:^12} | {prev:^9} | {min_rank:^8} |")


def plot_zt_table(status: Dict[str, dict]) -> None:
    print("\n\n### Conversions to ternary field (`ZT`)")
    print("The following schemes have been converted to the `ZT` field, having been previously known over rational (`Q`) or integer (`Z`) fields but lacking known")
    print("ternary implementations:\n")
    print("|    Format    | Rank | Known ring |")
    print("|:------------:|:----:|:----------:|")

    for size, data in status.items():
        ring2known_scheme = {}

        for ring, schemes in data["schemes"].items():
            known_schemes = [scheme for scheme in schemes if "known" in scheme["source"]]
            if known_schemes:
                ring2known_scheme[ring] = known_schemes[0]

        min_known_rank = min(scheme["rank"] for ring, scheme in ring2known_scheme.items())
        if "ZT" in ring2known_scheme and ring2known_scheme["ZT"]["rank"] == min_known_rank or "ZT" not in data["ranks"] or data["ranks"]["ZT"] != min_known_rank:
            continue

        rank = data["ranks"]["ZT"]
        rings = [ring for ring in ["Z", "Q"] if ring in data["schemes"] and data["schemes"][ring][0]["rank"] == min_known_rank]

        size = format_size(size)
        rings = f"`{'/'.join(rings)}`"
        print(f"| {size:^12} | {rank:^4} | {rings:^10} |")


def plot_new_ranks_z2_table(status: Dict[str, dict]) -> None:
    print("\n\n### New discoveries in binary field (`Z2`)")
    print("New schemes have been discovered that improve the state-of-the-art for matrix multiplication in the binary field (`Z2`),")
    print("achieving lower ranks than previously known.\n")
    print("|    Format    | Prev rank | New rank | Note              |")
    print("|:------------:|:---------:|:--------:|:------------------|")

    for size, data in status.items():
        min_known_rank = min(scheme["rank"] for ring, schemes in data["schemes"].items() for scheme in schemes if "known" in scheme["source"])
        min_rank = data["ranks"]["Z2"]
        if min_rank < min_known_rank:
            print(f"| {format_size(size):^12} | {min_known_rank:^9} | {min_rank:^8} |                   |")
        elif min_rank == data["ranks"]["Q"] and data["ranks"]["Q"] < data["ranks"]["Z"]:
            prev_rank = min([scheme["rank"] for ring, schemes in data["schemes"].items() for scheme in schemes if ring != "Q" and "known" in scheme["source"]], default="?")
            print(f"| {format_size(size):^12} | {prev_rank:^9} | {min_rank:^8} | equal to `Q` ring |")


def main():
    input_dirs = [
        "schemes/known/tensor",
        "schemes/known/jakobmoosbauer_flips",
        "schemes/known/alpha_evolve",
        "schemes/known/fmm_add_reduction",
        "schemes/known/meta_flip_graph",
        "schemes/new/FlipGraphGPU",
        "schemes/new/FlipGraphGPU_Z",
        "schemes/new/FlipGraphGPU_Z2",
        "schemes/new/FlipGraphGPU_merge",
    ]

    ring2equal_rings = {"Q": ["Q"], "Z2": ["Z2"], "Z": ["Z", "Z2", "Q"], "ZT": ["ZT", "Z", "Z2", "Q"]}
    extensions = [".exp", ".m", "tensor.mpl", "lrp.mpl", ".json"]
    n_max = 16

    status = analyze_schemes(input_dirs=input_dirs, n_max=n_max, extensions=extensions, ring2equal_rings=ring2equal_rings)
    plot_new_ranks_table(status)
    plot_zt_table(status)
    plot_new_ranks_z2_table(status)
    plot_full_table(status, ring2equal_rings=ring2equal_rings)


if __name__ == '__main__':
    main()
