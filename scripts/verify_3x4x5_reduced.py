#!/usr/bin/env python3
"""Check the 47-product integer 3x4x5 circuits by exact coefficient expansion.

Python standard library only. Aliases and unary negation are free; every
binary addition/subtraction in fresh and final rows is counted.
"""
import copy
import json
from pathlib import Path

def require(value, message):
    if not value:
        raise ValueError(message)

def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        require(key not in obj, f'duplicate JSON key: {key}')
        obj[key] = value
    return obj

def read(path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)

def linear(row, pool, width, where):
    require(type(row) is list, f'{where}: row is not list')
    out = [0] * width
    for pos, term in enumerate(row):
        require(type(term) is dict and set(term) == {'index', 'value'}, f'{where}/{pos}: term schema')
        idx, sign = term['index'], term['value']
        require(type(idx) is int and 0 <= idx < len(pool), f'{where}/{pos}: unavailable index {idx}')
        require(type(sign) is int and sign in (-1, 1), f'{where}/{pos}: coefficient {sign}')
        for k in range(width):
            out[k] += sign * pool[idx][k]
    return out

def expand(group, size, obj):
    pool = [[int(i == k) for k in range(size)] for i in range(size)]
    require(type(obj[group + '_fresh']) is list, 'fresh rows are not list')
    for i, row in enumerate(obj[group + '_fresh']):
        pool.append(linear(row, pool, size, f'{group}_fresh/{i}'))
    return [linear(row, pool, size, f'{group}/{i}') for i, row in enumerate(obj[group])]

def verify(obj, expected_additions):
    require(set(obj) == {'n', 'm', 'z2', 'complexity', 'u_fresh', 'v_fresh', 'w_fresh', 'u', 'v', 'w'}, 'top-level schema')
    require(obj['n'] == [3, 4, 5] and all(type(x) is int for x in obj['n']), 'dimensions')
    require(type(obj['m']) is int and obj['m'] == 47 and obj['z2'] is False, 'rank or field')
    for group, length in [('u', 47), ('v', 47), ('w', 15)]:
        require(type(obj[group]) is list and len(obj[group]) == length, f'{group}: output count')
    u, v = expand('u', 12, obj), expand('v', 20, obj)
    # Every product has a 240-entry exact coefficient vector indexed by a*20+b.
    products = [[u[r][a] * v[r][b] for a in range(12) for b in range(20)] for r in range(47)]
    require(all(any(t) for t in products), 'zero bilinear product')
    pool = list(products)
    require(type(obj['w_fresh']) is list, 'w fresh rows are not list')
    for k, row in enumerate(obj['w_fresh']):
        pool.append(linear(row, pool, 240, f'w_fresh/{k}'))
    mismatch = []
    for k, row in enumerate(obj['w']):
        actual = linear(row, pool, 240, f'w/{k}')
        i, col = k % 3, k // 3
        desired = [0] * 240
        for j in range(4):
            desired[(4*i+j)*20 + 5*j+col] = 1
        for pos, (got, want) in enumerate(zip(actual, desired)):
            if got != want:
                mismatch.append({'output': k, 'a': pos//20, 'b': pos%20, 'got': got, 'want': want})
    require(not mismatch, f'{len(mismatch)} coefficient mismatches; first={mismatch[:3]}')
    costs = {group: sum(max(len(row)-1, 0) for row in obj[group]) for group in ['u_fresh', 'u', 'v_fresh', 'v', 'w_fresh', 'w']}
    total = sum(costs.values())
    require(total == expected_additions, f'addition count {total} != {expected_additions}')
    require(obj['complexity']['reduced'] == total, 'reduced metadata disagrees')
    return {'bilinear_products': len(products), 'coefficient_equalities_checked': 3600, 'additions': total, 'addition_breakdown': costs, 'fresh_counts': {g: len(obj[g+'_fresh']) for g in ['u','v','w']}, 'nonzero_output_coefficients': 60}


def main():
    root = Path(__file__).resolve().parents[1] / "schemes/results/addition_reduced_ZT"
    for additions in (161, 160):
        path = root / f"3x4x5_m47_cr{additions}_cn277_ZT_reduced.json"
        scheme = read(path)
        result = verify(scheme, additions)
        print(f"{path.name}: {result}")
        bad = copy.deepcopy(scheme)
        bad["u"][0][0]["value"] *= -1
        try:
            verify(bad, additions)
        except ValueError:
            pass
        else:
            raise RuntimeError("Sign-corrupted negative control was accepted")
    print("PASS: both exact circuits; corrupted controls rejected")


if __name__ == "__main__":
    main()
