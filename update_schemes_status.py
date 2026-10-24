import json
import math
import os
from collections import defaultdict
from collections.abc import Set
from typing import Dict, List, Optional, Tuple

from src.entities.json_depth_stringifier import JsonDepthStringifier
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
                status[f"{n1}x{n2}x{n3}"] = current_status.get(f"{n1}x{n2}x{n3}", {"ranks": {}, "omegas": {}, "schemes": defaultdict(list)})

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
    data["omegas"] = {}

    for ring, schemes in data["schemes"].items():
        schemes = sorted(schemes, key=lambda info: (info["rank"], info["complexity"], sum(info["buds_count"].values()), not info["source"].startswith("schemes/known/")))
        rank = schemes[0]["rank"]
        omega = schemes[0]["omega"]

        for equal_ring in ring2equal_rings[ring]:
            if equal_ring not in data["ranks"] or rank < data["ranks"][equal_ring]:
                data["ranks"][equal_ring] = rank

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


def get_additions(path: str) -> Tuple[int, int, Tuple[int, int, int], str]:
    with open(path, "r") as f:
        data = json.load(f)

    au = sum(len(expression) - 1 for expression in data["u_fresh"] + data["u"])
    av = sum(len(expression) - 1 for expression in data["v_fresh"] + data["v"])
    aw = sum(len(expression) - 1 for expression in data["w_fresh"] + data["w"])

    return data["complexity"]["reduced"], data["complexity"]["naive"], (au, av, aw), path


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
            scheme = Scheme.load(path=input_path, validate=True)
            scheme.fix_sizes()

            for matrix in [scheme.u, scheme.v, scheme.w]:
                for row in matrix:
                    for value in row:
                        assert not isinstance(value, float)

            ring = scheme.get_ring()
            if ring == "Z2":
                print("Skip Z2 scheme")
                continue

            size = scheme.get_key(sort=False)
            size_key = scheme.get_key(sort=True)
            omega = scheme.omega()
            complexity = scheme.complexity()
            buds = scheme.get_buds()
            buds_count = [sum(1 for p, _, _ in buds if p == target_p) for target_p in range(3)]
            values = scheme.get_unique_values()
            output_path = f"schemes/status/{ring}/{size}_m{scheme.m}_{ring}.json"

            print(f"  - size: {size}")
            print(f"  - rank: {scheme.m}")
            print(f"  - ring: {ring}")
            print(f"  - omega: {omega}")
            print(f"  - complexity: {complexity}")
            print(f"  - values: {values}")
            print(f"  - buds: {sum(buds_count)} ({buds_count[0]} / {buds_count[1]} / {buds_count[2]})")

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

            status[size_key]["schemes"][ring].append({
                "rank": scheme.m,
                "omega": omega,
                "complexity": complexity,
                "values": values,
                "buds_count": {"u": buds_count[0], "v": buds_count[1], "w": buds_count[2]},
                "source": input_path,
                "path": output_path
            })
            scheme.save(output_path)
            print(f'  - saved to "{output_path}"')

        for data in status.values():
            postprocess_size(data=data, ring2equal_rings=ring2equal_rings)

    status = {key: value for key, value in status.items() if value["ranks"]}
    stringifier = JsonDepthStringifier()
    with open("schemes/status.json", "w", encoding="utf-8") as f:
        f.write(stringifier.stringify(status, depth=0, max_depth=5, indent=2))

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
    return f"`{n1}x{n2}x{n3}`"


def get_new_ranks_table(status: Dict[str, dict]) -> List[str]:
    lines = [
        "## New best ranks",
        "",
        "New schemes have been discovered that improve the state-of-the-art for matrix multiplication achieving lower ranks than",
        "previously known.",
        "",
        "|   Format   |   Prev rank   |                            New rank                            |        ω        |",
        "|:----------:|:-------------:|:--------------------------------------------------------------:|:---------------:|"
    ]

    excluded = {
        "2x8x13"
    }

    strassen = math.log(7, 2)

    for size, data in status.items():
        n1, n2, n3 = map(int, size.split("x"))
        min_rank = data["ranks"]["Q"]
        min_known_rank = min(scheme["rank"] for schemes in data["schemes"].values() for scheme in schemes if "known" in scheme["source"])

        if min_rank >= min_known_rank or size in excluded:
            continue

        ring2known_ranks = {ring: [scheme["rank"] for scheme in schemes if "known" in scheme["source"]] for ring, schemes in data["schemes"].items()}
        ring2known_rank = {ring: min(ranks) for ring, ranks in ring2known_ranks.items() if ranks}
        known_rings = [ring for ring in ["ZT", "Z", "Q"] if ring2known_rank.get(ring) == min_known_rank]
        rings = [ring for ring in ["ZT", "Z", "Q"] if ring in data["schemes"] and data["schemes"][ring][0]["rank"] == min_rank]

        prev = f"{min_known_rank} (`{'/'.join(known_rings)}`)"
        curr = f"[{min_rank}](../schemes/results/{rings[0]}/{size}_m{min_rank}_{rings[0]}.json) (`{'/'.join(rings)}`)"
        size = format_size(size)
        omega = 3*math.log(min_rank, n1*n2*n3)
        bold = "**" if omega < strassen else "  "
        lines.append(f"| {size:^10} | {prev:^13} | {curr:^62} | {bold}{omega:.9f}{bold} |")

    return lines


def get_zt_table(status: Dict[str, dict]) -> List[str]:
    lines = [
        "## Rediscovery in the ternary coefficient set (`ZT`)",
        "",
        "The following schemes have been rediscovered in the `ZT` format. Originally known over the rational (`Q`) or integer (`Z`)",
        "fields, implementations with coefficients restricted to the ternary set were previously unknown.",
        "",
        "|   Format   |                          Rank                          | Known ring |",
        "|:----------:|:------------------------------------------------------:|:----------:|"
    ]

    for size, data in status.items():
        ring2known_ranks = {ring: [scheme["rank"] for scheme in schemes if "known" in scheme["source"]] for ring, schemes in data["schemes"].items()}
        ring2known_rank = {ring: min(ranks) for ring, ranks in ring2known_ranks.items() if ranks}
        min_known_rank = min(min(ranks) for ranks in ring2known_ranks.values() if ranks)
        min_rank = data["ranks"]["Q"]

        zt_rank = data["ranks"].get("ZT")
        if zt_rank != min_rank or zt_rank != min_known_rank or zt_rank == ring2known_rank.get("ZT"):
            continue

        rings = [ring for ring in ["Z", "Q"] if ring2known_rank.get(ring) == zt_rank]

        link = f"[{zt_rank}](../schemes/results/ZT/{size}_m{zt_rank}_ZT.json)"
        rings = f"`{'/'.join(rings)}`"
        size = format_size(size)
        lines.append(f"| {size:^10} | {link:^54} | {rings:^10} |")

    return lines


def get_z_table(status: Dict[str, dict]) -> List[str]:
    lines = [
        "## Rediscovery in the integer ring (`Z`)",
        "The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).",
        "Implementations restricted to integer coefficients were previously unknown.",
        "",
        "|   Format   |                         Rank                         |",
        "|:----------:|:----------------------------------------------------:|"
    ]

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
        link = f"[{z_rank}](../schemes/results/Z/{size}_m{z_rank}_Z.json)"
        lines.append(f'| {format_size(size):^10} | {link:^52} |')

    return lines


def get_coefficients_status(status: Dict[str, dict]) -> Tuple[Dict[str, int], int]:
    ring2count = {"ZT": 0, "Z": 0, "Q": 0}
    better_strassen = 0

    for size, data in status.items():
        n1, n2, n3 = map(int, size.split("x"))
        naive_rank = n1*n2*n3
        q = data["ranks"]["Q"]
        z = data["ranks"].get("Z", naive_rank)
        zt = data["ranks"].get("ZT", naive_rank)

        omega = 3*math.log(q) / math.log(naive_rank)

        if zt == q:
            ring2count["ZT"] += 1
        elif z == q:
            ring2count["Z"] += 1
        else:
            ring2count["Q"] += 1

        if omega < math.log(7, 2):
            better_strassen += 1

    return ring2count, better_strassen


def update_results(status: Dict[str, dict]) -> None:
    print("- docs/results.md updating")
    lines = [
        "# Results",
        "",
        *get_new_ranks_table(status=status),
        "",
        *get_zt_table(status=status),
        "",
        *get_z_table(status=status)
    ]

    with open("docs/results.md", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")


def update_additions_table(status: Dict[str, dict]) -> None:
    print("- docs/additions.md updating")

    lines = [
        "# Additions reduction",
        "",
        "The table below compares the number of additions required to evaluate a scheme of each format: `Reduced additions` is the",
        "best count achieved for the scheme with the given rank in the given ring, while `Naive additions` is the count obtained by",
        "straightforward evaluation. `Leading coef` is the leading constant of the arithmetic complexity.",
        "",
        "|   Format   | Rank | Ring |                                     Reduced additions                                     | Naive |     ω     | Leading coef |",
        "|:----------:|:----:|:----:|:-----------------------------------------------------------------------------------------:|:-----:|:---------:|:------------:|"
    ]

    for size, data in status.items():
        n1, n2, n3 = map(int, size.split("x"))

        for ring in ["Q", "Z", "ZT"]:
            rank = data["ranks"][ring]
            schemes_paths = []

            for scheme in data["schemes"].get(ring, []):
                if scheme["rank"] == rank:
                    if scheme["source"].endswith("_reduced.json"):
                        schemes_paths.append(scheme["source"])

                    for source in scheme.get("duplicates", []):
                        if source.endswith("_reduced.json"):
                            schemes_paths.append(source)

            if not schemes_paths:
                continue

            ring = f"`{ring}`"
            reduced, naive, (au, av, aw), source = min(get_additions(scheme_path) for scheme_path in schemes_paths)
            reduced = f"[{reduced}](../{source})"
            omega = 3 * math.log(rank) / math.log(n1*n2*n3)
            bold = "**" if omega < math.log(7, 2) else "  "
            c = 1 + au / (rank - n1 * n2) + av / (rank - n2 * n3) + aw / (rank - n3 * n1)

            lines.append(f"| {format_size(size):^10} | {rank:^4} | {ring:^4} | {reduced:^89} | {naive:^5} | {bold}{omega:.3f}{bold} | {c:^12.2f} |")

        with open("docs/additions.md", "w", encoding="utf-8") as f:
            for line in lines:
                f.write(f"{line}\n")


def update_ranks_table(status: Dict[str, dict], ring2equal_rings: Dict[str, List[str]]) -> None:
    print("- docs/ranks.md updating")

    lines = [
        "# Rank comparison",
        "",
        "The table below summarizes the current state of researched matrix multiplication schemes. It highlights where ternary",
        "schemes (`ZT`) match or approximate the known minimal ranks from other fields. The best ranks of previously known schemes",
        "are given in brackets.",
        "",
        "|   Format   |  `ZT` rank  |   `Z` rank   |   `Q` rank   |        ω        |",
        "|:----------:|:-----------:|:------------:|:------------:|:---------------:|"
    ]

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

        n1, n2, n3 = map(int, size.split("x"))
        omega = 3 * math.log(min_rank, n1 * n2 * n3)
        bold = "**" if omega < math.log(7, 2) else "  "

        lines.append(f'| {format_size(size):^10} | {diff_rank["ZT"]:^11} | {diff_rank["Z"]:^12} | {diff_rank["Q"]:^12} | {bold}{omega:.9f}{bold} |')

    ring2count, better_strassen = get_coefficients_status(status=status)
    total = sum(ring2count.values())

    lines.append("")
    lines.append("## Coefficient set status")
    lines.append(f"* total schemes: {total} ({better_strassen} better Strassen)")
    lines.append(f'* `ZT` schemes: {ring2count["ZT"]} ({ring2count["ZT"] / total:.2%})')
    lines.append(f'* `Z` schemes: {ring2count["Z"]} ({ring2count["Z"] / total:.2%})')
    lines.append(f'* `Q` schemes: {ring2count["Q"]} ({ring2count["Q"] / total:.2%})')

    with open("docs/ranks.md", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")


def main():
    input_dirs = [
        "schemes/known",
        "schemes/results"
    ]

    ring2equal_rings = {"Q": ["Q"], "Z": ["Z", "Q"], "ZT": ["ZT", "Z", "Q"]}
    extensions = [".exp", ".m", "tensor.mpl", "lrp.mpl", ".json"]
    n_max = 16

    status = analyze_schemes(input_dirs=input_dirs, n_max=n_max, extensions=extensions, ring2equal_rings=ring2equal_rings)

    print("\nUpdate docs")
    update_results(status)
    update_additions_table(status)
    update_ranks_table(status, ring2equal_rings=ring2equal_rings)


if __name__ == '__main__':
    main()
