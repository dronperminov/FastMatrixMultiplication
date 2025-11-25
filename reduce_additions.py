import json
import os

from src.entities.addition_reducer import AdditionReducer
from src.schemes.scheme import Scheme
from src.utils.utils import pretty_matrix


def save_reduced_scheme(reduced: dict, path: str) -> None:
    n1, n2, n3 = reduced["n"]
    m = reduced["m"]
    z2 = reduced["z2"]

    u_fresh = pretty_matrix(reduced["u_fresh"], '"u_fresh":', "    ")
    v_fresh = pretty_matrix(reduced["v_fresh"], '"v_fresh":', "    ")
    w_fresh = pretty_matrix(reduced["w_fresh"], '"w_fresh":', "    ")

    u = pretty_matrix(reduced["u"], '"u":', "    ")
    v = pretty_matrix(reduced["v"], '"v":', "    ")
    w = pretty_matrix(reduced["w"], '"w":', "    ")

    with open(path, "w", encoding="utf-8") as f:
        f.write("{\n")
        f.write(f'    "n": [{n1}, {n2}, {n3}],\n')
        f.write(f'    "m": {m},\n')
        f.write(f'    "z2": {"true" if z2 else "false"},\n')
        f.write(f'    "complexity": {{"naive": {reduced["complexity"]["naive"]}, "reduced": {reduced["complexity"]["reduced"]}}},\n')
        f.write(f'    {u_fresh},\n')
        f.write(f'    {v_fresh},\n')
        f.write(f'    {w_fresh},\n')
        f.write(f'    {u},\n')
        f.write(f'    {v},\n')
        f.write(f'    {w}\n')
        f.write("}\n")


def reduce_scheme_additions(scheme: Scheme, addition_reducer: AdditionReducer, max_flips: int) -> dict:
    best = addition_reducer.reduce(scheme=scheme, mode="hybrid")

    for _ in range(max_flips):
        if not scheme.try_flip():
            break

        reduced = addition_reducer.reduce(scheme=scheme, mode="hybrid")
        if reduced["complexity"]["reduced"] < best["complexity"]["reduced"]:
            best = reduced

    return best


def main():
    output_dir = "schemes/reduced"
    max_loops = 50
    max_size = 10
    max_flips = 100

    with open("schemes/status.json") as f:
        status = json.load(f)

    addition_reducer = AdditionReducer(max_loops=max_loops, max_size=max_size)

    for size, data in status.items():
        scheme = Scheme.load(data["schemes"]["ZT"][0]["path"], validate=False)
        reduced = reduce_scheme_additions(scheme=scheme, addition_reducer=addition_reducer, max_flips=max_flips)
        reduced_complexity = reduced["complexity"]["reduced"]

        print(f"{size}: {scheme.m}, initial complexity: {scheme.complexity()}, reduced: {reduced_complexity}")

        path = os.path.join(output_dir, f"{scheme.n[0]}x{scheme.n[1]}x{scheme.n[2]}_m{scheme.m}_c{reduced_complexity}_reduced.json")
        save_reduced_scheme(reduced, path)
        Scheme.load(path)


if __name__ == '__main__':
    main()
