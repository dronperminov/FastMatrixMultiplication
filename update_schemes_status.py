import json
import math
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
                status[f"{n1}x{n2}x{n3}"] = current_status.get(f"{n1}x{n2}x{n3}", {"ranks": {}, "omegas": {}, "complexities": {}, "schemes": defaultdict(list)})

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
    data["omegas"] = {}

    for ring, schemes in data["schemes"].items():
        schemes = sorted(schemes, key=lambda info: (info["rank"], info["complexity"], not info["source"].startswith("schemes/known/")))
        rank = schemes[0]["rank"]
        complexity = schemes[0]["complexity"]
        omega = schemes[0]["omega"]

        for equal_ring in ring2equal_rings[ring]:
            if equal_ring not in data["ranks"] or rank < data["ranks"][equal_ring]:
                data["ranks"][equal_ring] = rank

            if equal_ring not in data["complexities"] or complexity < data["complexities"][equal_ring]:
                data["complexities"][equal_ring] = complexity

            if equal_ring not in data["omegas"] or omega < data["omegas"][equal_ring]:
                data["omegas"][equal_ring] = omega

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

            for matrix in [scheme.u, scheme.v, scheme.w]:
                for row in matrix:
                    for value in row:
                        assert not isinstance(value, float)

            ring = scheme.get_ring()
            size = scheme.get_key(sort=False)
            size_key = scheme.get_key(sort=True)
            omega = scheme.omega()
            complexity = scheme.complexity()
            output_path = f"schemes/status/{ring}/{size}_m{scheme.m}_{ring}.json"

            print(f"  - size: {size}")
            print(f"  - rank: {scheme.m}")
            print(f"  - ring: {ring}")
            print(f"  - omega: {omega}")
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

            status[size_key]["schemes"][ring].append({"rank": scheme.m, "omega": omega, "complexity": complexity, "source": input_path, "path": output_path})
            scheme.save(output_path)
            print(f'  - saved to "{output_path}"')

        for data in status.values():
            postprocess_size(data=data, ring2equal_rings=ring2equal_rings)

        status = {key: value for key, value in status.items() if value["ranks"]}

        with open("schemes/status.json", "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False, sort_keys=False)

    for data in status.values():
        for scheme_datas in data["schemes"].values():
            for scheme_data in scheme_datas:
                if not os.path.exists(scheme_data["path"]):
                    scheme = Scheme.load(scheme_data["source"], validate=False)
                    scheme.save(scheme_data["path"])
                    print(f'Detected missed scheme "{scheme_data["path"]}" (reload from "{scheme_data["source"]}")')

    return status


def format_value(ring2value: Dict[str, int], ring: str, min_value: int, unique_value: bool) -> str:
    return "?" if ring not in ring2value else f"{ring2value[ring]}"


def format_size(size: str) -> str:
    n1, n2, n3 = map(int, size.split("x"))
    return f"`{n1}×{n2}×{n3}`"


def plot_full_table(status: Dict[str, dict], ring2equal_rings: Dict[str, List[str]]) -> None:
    print("## Ranks")
    print("|   Format   |  `ZT` rank  |   `Z` rank   |   `Q` rank   |  `Z2` rank  |")
    print("|:----------:|:-----------:|:------------:|:------------:|:-----------:|")

    for size, data in status.items():
        known_ranks = {}

        for ring, schemes in data["schemes"].items():
            known_schemes = sorted([scheme for scheme in schemes if "known" in scheme["source"]], key=lambda s: (s["rank"], s["complexity"]))
            if not known_schemes:
                continue

            rank = known_schemes[0]["rank"]

            for equal_ring in ring2equal_rings[ring]:
                if equal_ring not in known_ranks or rank < known_ranks[equal_ring]:
                    known_ranks[equal_ring] = rank

        current_ranks = data["ranks"]
        min_rank = min([current_ranks[ring] for ring in ["Q", "Z", "ZT"] if ring in current_ranks], default=None)
        unique_ranks = len(set(current_ranks[ring] for ring in ["Q", "Z", "ZT"] if ring in current_ranks)) == 1
        diff_rank = {}

        for ring in ring2equal_rings:
            rank_curr = format_value(current_ranks, ring=ring, min_value=min_rank, unique_value=unique_ranks)
            rank_known = format_value(known_ranks, ring=ring, min_value=min_rank, unique_value=unique_ranks)
            diff_rank[ring] = rank_curr if rank_curr == rank_known else f"{rank_curr} ({rank_known})"

        print(f'| {format_size(size):^10} | {diff_rank["ZT"]:^11} | {diff_rank["Z"]:^12} | {diff_rank["Q"]:^12} | {diff_rank["Z2"]:^11} |')


def plot_new_ranks_table(status: Dict[str, dict]) -> None:
    print("\n\n### New best ranks")
    print("New schemes have been discovered that improve the state-of-the-art for matrix multiplication achieving lower ranks than previously known.\n")
    print("|   Format   |  Prev rank  |                          New rank                          |")
    print("|:----------:|:-----------:|:----------------------------------------------------------:|")

    for size, data in status.items():
        min_rank = min(rank for ring, rank in data["ranks"].items() if ring != "Z2")
        min_known_rank = min(scheme["rank"] for ring, schemes in data["schemes"].items() for scheme in schemes if ring != "Z2" and "known" in scheme["source"])

        if min_rank >= min_known_rank:
            continue

        ring2known_ranks = {ring: [scheme["rank"] for scheme in schemes if "known" in scheme["source"]] for ring, schemes in data["schemes"].items() if ring != "Z2"}
        ring2known_rank = {ring: min(ranks) for ring, ranks in ring2known_ranks.items() if ranks}
        known_rings = [ring for ring in ["ZT", "Z", "Q"] if ring2known_rank.get(ring) == min_known_rank]
        rings = [ring for ring in ["ZT", "Z", "Q"] if ring in data["schemes"] and data["schemes"][ring][0]["rank"] == min_rank]

        prev = f"{min_known_rank} (`{'/'.join(known_rings)}`)"
        curr = f"[{min_rank}](schemes/results/{rings[0]}/{size}_m{min_rank}_{rings[0]}.json) (`{'/'.join(rings)}`)"
        size = format_size(size)
        print(f"| {size:^10} | {prev:^11} | {curr:^58} |")


def plot_zt_table(status: Dict[str, dict]) -> None:
    print("\n\n### Rediscovery in the ternary coefficient set (`ZT`)")
    print("The following schemes have been rediscovered in the `ZT` format. Originally known over the rational (`Q`) or integer (`Z`) fields, implementations")
    print("with coefficients restricted to the ternary set were previously unknown.\n")
    print("|   Format   |                        Rank                        | Known ring |")
    print("|:----------:|:--------------------------------------------------:|:----------:|")

    for size, data in status.items():
        ring2known_ranks = {ring: [scheme["rank"] for scheme in schemes if "known" in scheme["source"]] for ring, schemes in data["schemes"].items() if ring != "Z2"}
        ring2known_rank = {ring: min(ranks) for ring, ranks in ring2known_ranks.items() if ranks}
        min_known_rank = min(min(ranks) for ranks in ring2known_ranks.values() if ranks)
        min_rank = min(rank for ring, rank in data["ranks"].items() if ring != "Z2")

        zt_rank = data["ranks"].get("ZT")
        if zt_rank != min_rank or zt_rank != min_known_rank or zt_rank == ring2known_rank.get("ZT"):
            continue

        rings = [ring for ring in ["Z", "Q"] if ring2known_rank.get(ring) == zt_rank]

        link = f"[{zt_rank}](schemes/results/ZT/{size}_m{zt_rank}_ZT.json)"
        rings = f"`{'/'.join(rings)}`"
        size = format_size(size)
        print(f"| {size:^10} | {link:^50} | {rings:^10} |")


def plot_z_table(status: Dict[str, dict]) -> None:
    print("\n\n### Rediscovery in the integer ring (`Z`)")
    print("The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).")
    print("Implementations restricted to integer coefficients were previously unknown.\n")
    print("|   Format   |                       Rank                       |")
    print("|:----------:|:------------------------------------------------:|")

    for size, data in status.items():
        ring2known_rank = {}

        for ring, schemes in data["schemes"].items():
            known_schemes = [scheme for scheme in schemes if "known" in scheme["source"]]
            if known_schemes:
                ring2known_rank[ring] = known_schemes[0]["rank"]

        min_known_rank = min(ring2known_rank.values())
        if "Z" in ring2known_rank and ring2known_rank["Z"] == min_known_rank:
            continue

        if "ZT" in data["ranks"] and data["ranks"]["ZT"] == min_known_rank:
            continue

        if data["ranks"].get("Z") != min_known_rank:
            continue

        z_rank = data["ranks"]["Z"]
        link = f"[{z_rank}](schemes/results/Z/{size}_m{z_rank}_Z.json)"
        print(f'| {format_size(size):^10} | {link:^48} |')


def print_coefficients_status(status: Dict[str, dict]) -> None:
    zt_count = 0
    z_count = 0
    q_count = 0
    total = 0
    better_strassen = 0

    for size, data in status.items():
        n1, n2, n3 = map(int, size.split("x"))
        naive_rank = n1*n2*n3
        q = data["ranks"]["Q"]
        z = data["ranks"].get("Z", naive_rank)
        zt = data["ranks"].get("ZT", naive_rank)

        omega = 3*math.log(q) / math.log(naive_rank)

        if zt == q:
            zt_count += 1
        elif z == q:
            z_count += 1
        else:
            q_count += 1

        if omega < math.log(7, 2):
            better_strassen += 1

        total += 1

    print("\n### Coefficient set status")
    print(f"* total schemes: {total} ({better_strassen} better Strassen)")
    print(f"* `ZT` schemes: {zt_count} ({zt_count / total:.2%})")
    print(f"* `Z` schemes: {z_count} ({z_count / total:.2%})")
    print(f"* `Q` schemes: {q_count} ({q_count / total:.2%})\n")


def main():
    input_dirs = [
        "schemes/known",
        "schemes/results"
    ]

    ring2equal_rings = {"Q": ["Q"], "Z2": ["Z2"], "Z": ["Z", "Z2", "Q"], "ZT": ["ZT", "Z", "Z2", "Q"]}
    extensions = [".exp", ".m", "tensor.mpl", "lrp.mpl", ".json"]
    n_max = 16

    status = analyze_schemes(input_dirs=input_dirs, n_max=n_max, extensions=extensions, ring2equal_rings=ring2equal_rings)
    plot_new_ranks_table(status)
    plot_zt_table(status)
    plot_z_table(status)
    plot_full_table(status, ring2equal_rings=ring2equal_rings)
    print_coefficients_status(status)


if __name__ == '__main__':
    main()
