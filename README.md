# FastMatrixMultiplication

[![arXiv:2511.20317](https://img.shields.io/badge/arXiv-2511.20317-b31b1b.svg)](https://arxiv.org/abs/2511.20317)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.13365-b31b1b.svg)](https://arxiv.org/abs/2512.13365)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.21980-b31b1b.svg)](https://arxiv.org/abs/2512.21980)

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `(2, 2, 2)` to `(11, 11, 11)`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`, focusing on all tensor shapes satisfying `max(n₁n₂, n₂n₃, n₃n₁) ≤ 128` and `max(n₁, n₂, n₃) ≤ 16`.

## Overview
This repository documents the search for fast matrix multiplication (FMM) schemes using a custom meta flip graph method. The search focuses on schemes that use only the
coefficients `-1`, `0`, and `1`, denoted as `ZT`. This constraint is significant for practical implementations where computational complexity and hardware efficiency are critical.

Key insight: several known optimal schemes originally found over the rationals (`Q`) or integers (`Z`) have been successfully rediscovered with minimal, ternary
coefficients. This can lead to more efficient and hardware-friendly implementations.

## Latest progress

For a detailed history of discoveries and improvements, see the [CHANGELOG.md](CHANGELOG.md).

## Publications

* [Fast Matrix Multiplication via Ternary Meta Flip Graphs](https://arxiv.org/abs/2511.20317) (arxiv)
* [Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication](https://arxiv.org/abs/2512.13365) (arxiv)
* [A 58-Addition, Rank-23 Scheme for General 3x3 Matrix Multiplication](https://arxiv.org/abs/2512.21980) (arxiv)

## Key results

### New best ranks
New schemes have been discovered that improve the state-of-the-art for matrix multiplication achieving lower ranks than previously known.

|     Format     |  Prev rank  |  New rank  |
|:--------------:|:-----------:|:----------:|
|  `(2, 8, 13)`  |  164 (`Q`)  | 163 (`Z`)  |
|  `(4, 4, 10)`  |  120 (`Q`)  | 115 (`ZT`) |
|  `(4, 4, 12)`  |  142 (`Q`)  | 141 (`ZT`) |
|  `(4, 4, 14)`  |  165 (`Q`)  | 163 (`Q`)  |
|  `(4, 4, 15)`  |  177 (`Q`)  | 176 (`ZT`) |
|  `(4, 4, 16)`  |  189 (`Q`)  | 188 (`ZT`) |
|  `(4, 5, 9)`   |  136 (`Q`)  | 132 (`ZT`) |
|  `(4, 5, 10)`  |  151 (`Z`)  | 146 (`ZT`) |
|  `(4, 5, 11)`  |  165 (`Z`)  | 160 (`ZT`) |
|  `(4, 5, 12)`  |  180 (`Z`)  | 175 (`ZT`) |
|  `(4, 5, 13)`  |  194 (`Z`)  | 192 (`ZT`) |
|  `(4, 5, 14)`  |  208 (`Z`)  | 207 (`ZT`) |
|  `(4, 5, 15)`  |  226 (`Z`)  | 221 (`ZT`) |
|  `(4, 5, 16)`  |  240 (`Q`)  | 236 (`ZT`) |
|  `(4, 7, 11)`  |  227 (`Z`)  | 226 (`ZT`) |
|  `(4, 9, 11)`  | 280 (`ZT`)  | 279 (`ZT`) |
|  `(5, 5, 9)`   |  167 (`Z`)  | 163 (`ZT`) |
|  `(5, 6, 10)`  |  218 (`Z`)  | 217 (`ZT`) |
|  `(5, 7, 8)`   |  205 (`Q`)  | 204 (`ZT`) |
|  `(6, 7, 7)`   | 215 (`ZT`)  | 212 (`ZT`) |
|  `(6, 7, 8)`   | 239 (`ZT`)  | 238 (`ZT`) |
|  `(6, 7, 9)`   | 270 (`ZT`)  | 268 (`ZT`) |
|  `(6, 7, 10)`  |  296 (`Z`)  | 293 (`Q`)  |
|  `(7, 7, 10)`  |  346 (`Z`)  | 345 (`Q`)  |
|  `(7, 8, 15)`  |  571 (`Q`)  | 570 (`Q`)  |
|  `(8, 8, 16)`  |  672 (`Q`)  | 671 (`Q`)  |
|  `(8, 9, 14)`  |  669 (`Z`)  | 666 (`ZT`) |
| `(9, 10, 10)`  |  600 (`Z`)  | 599 (`ZT`) |
| `(9, 11, 11)`  |  725 (`Q`)  | 715 (`Q`)  |


### Rediscovery in the ternary coefficient set (`ZT`)
The following schemes have been rediscovered in the `ZT` format. Originally known over the rational (`Q`) or integer (`Z`) fields, implementations
with coefficients restricted to the ternary set were previously unknown.

|     Format     | Rank | Known ring |
|:--------------:|:----:|:----------:|
|  `(2, 3, 10)`  |  50  |    `Z`     |
|  `(2, 3, 13)`  |  65  |    `Z`     |
|  `(2, 3, 15)`  |  75  |    `Z`     |
|  `(2, 4, 6)`   |  39  |    `Z`     |
|  `(2, 4, 11)`  |  71  |    `Q`     |
|  `(2, 4, 12)`  |  77  |    `Q`     |
|  `(2, 4, 15)`  |  96  |    `Q`     |
|  `(2, 5, 9)`   |  72  |    `Q`     |
|  `(2, 6, 9)`   |  86  |    `Z`     |
|  `(2, 7, 8)`   |  88  |    `Z`     |
|  `(2, 8, 15)`  | 188  |    `Z`     |
|  `(3, 3, 7)`   |  49  |    `Q`     |
|  `(3, 3, 9)`   |  63  |    `Q`     |
|  `(3, 4, 5)`   |  47  |    `Z`     |
|  `(3, 4, 6)`   |  54  |   `Z/Q`    |
|  `(3, 4, 9)`   |  83  |    `Q`     |
|  `(3, 4, 10)`  |  92  |    `Q`     |
|  `(3, 4, 11)`  | 101  |    `Q`     |
|  `(3, 4, 12)`  | 108  |    `Q`     |
|  `(3, 4, 16)`  | 146  |    `Q`     |
|  `(3, 5, 10)`  | 115  |    `Z`     |
|  `(3, 6, 8)`   | 108  |   `Z/Q`    |
|  `(3, 8, 12)`  | 216  |    `Q`     |
|  `(4, 4, 6)`   |  73  |   `Z/Q`    |
|  `(4, 4, 8)`   |  96  |    `Q`     |
|  `(4, 4, 11)`  | 130  |    `Q`     |
|  `(4, 5, 6)`   |  90  |    `Z`     |
|  `(4, 5, 7)`   | 104  |   `Z/Q`    |
|  `(4, 5, 8)`   | 118  |   `Z/Q`    |
|  `(4, 6, 7)`   | 123  |   `Z/Q`    |
|  `(4, 6, 9)`   | 159  |    `Q`     |
|  `(4, 6, 10)`  | 175  |    `Z`     |
|  `(4, 6, 11)`  | 194  |    `Q`     |
|  `(4, 6, 13)`  | 228  |    `Z`     |
|  `(4, 6, 15)`  | 263  |    `Z`     |
|  `(4, 7, 7)`   | 144  |   `Z/Q`    |
|  `(4, 7, 12)`  | 246  |    `Z`     |
|  `(4, 7, 15)`  | 307  |    `Q`     |
|  `(4, 8, 13)`  | 297  |    `Z`     |
|  `(4, 9, 14)`  | 355  |    `Z`     |
|  `(5, 5, 6)`   | 110  |   `Z/Q`    |
|  `(5, 5, 7)`   | 127  |   `Z/Q`    |
|  `(5, 5, 8)`   | 144  |   `Z/Q`    |
|  `(5, 5, 10)`  | 184  |    `Q`     |
|  `(5, 5, 11)`  | 202  |    `Q`     |
|  `(5, 5, 12)`  | 220  |    `Z`     |
|  `(5, 5, 13)`  | 237  |    `Z`     |
|  `(5, 5, 14)`  | 254  |    `Z`     |
|  `(5, 5, 15)`  | 271  |    `Q`     |
|  `(5, 5, 16)`  | 288  |    `Q`     |
|  `(5, 6, 6)`   | 130  |   `Z/Q`    |
|  `(5, 6, 7)`   | 150  |   `Z/Q`    |
|  `(5, 6, 8)`   | 170  |   `Z/Q`    |
|  `(5, 6, 9)`   | 197  |    `Z`     |
|  `(5, 6, 16)`  | 340  |    `Q`     |
|  `(5, 7, 7)`   | 176  |   `Z/Q`    |
|  `(5, 7, 10)`  | 254  |    `Z`     |
|  `(5, 7, 11)`  | 277  |    `Z`     |
|  `(5, 8, 12)`  | 333  |    `Q`     |
|  `(6, 6, 7)`   | 183  |   `Z/Q`    |
|  `(6, 8, 10)`  | 329  |    `Z`     |
|  `(6, 8, 11)`  | 357  |    `Q`     |
|  `(6, 8, 12)`  | 378  |    `Q`     |
|  `(6, 9, 9)`   | 342  |    `Z`     |
|  `(6, 9, 10)`  | 373  |    `Z`     |
|  `(7, 8, 10)`  | 385  |    `Z`     |
|  `(7, 8, 11)`  | 423  |    `Q`     |
|  `(7, 8, 12)`  | 454  |    `Q`     |
|  `(7, 9, 10)`  | 437  |    `Z`     |
|  `(8, 8, 11)`  | 475  |    `Q`     |
|  `(8, 8, 13)`  | 559  |    `Q`     |
|  `(8, 9, 11)`  | 533  |    `Q`     |
|  `(8, 9, 13)`  | 624  |    `Z`     |
| `(8, 10, 11)`  | 588  |    `Z`     |
| `(8, 10, 12)`  | 630  |    `Z`     |
| `(10, 10, 10)` | 651  |    `Z`     |
| `(10, 10, 11)` | 719  |    `Z`     |
| `(10, 10, 12)` | 770  |    `Z`     |
| `(10, 11, 11)` | 793  |    `Z`     |
| `(11, 11, 11)` | 873  |    `Z`     |


### Rediscovery in the integer ring (`Z`)
The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).
Implementations restricted to integer coefficients were previously unknown.

|     Format     | Rank |
|:--------------:|:----:|
|  `(2, 5, 7)`   |  55  |
|  `(2, 5, 8)`   |  63  |
|  `(2, 5, 13)`  | 102  |
|  `(2, 5, 14)`  | 110  |
|  `(2, 5, 15)`  | 118  |
|  `(2, 5, 16)`  | 126  |
|  `(2, 6, 8)`   |  75  |
|  `(2, 6, 13)`  | 122  |
|  `(2, 6, 14)`  | 131  |
|  `(2, 7, 7)`   |  76  |
|  `(2, 7, 12)`  | 131  |
|  `(2, 7, 13)`  | 142  |
|  `(2, 7, 14)`  | 152  |
|  `(2, 7, 15)`  | 164  |
|  `(2, 8, 14)`  | 175  |
|  `(3, 4, 8)`   |  73  |
|  `(3, 5, 7)`   |  79  |
|  `(3, 5, 13)`  | 147  |
|  `(3, 5, 14)`  | 158  |
|  `(3, 5, 15)`  | 169  |
|  `(3, 7, 7)`   | 111  |
|  `(3, 8, 9)`   | 163  |
|  `(3, 8, 11)`  | 198  |
|  `(3, 8, 16)`  | 288  |
|  `(5, 7, 9)`   | 229  |
|  `(5, 8, 9)`   | 260  |
|  `(5, 8, 16)`  | 445  |
|  `(5, 9, 11)`  | 353  |
|  `(5, 9, 12)`  | 377  |
|  `(6, 8, 16)`  | 511  |
|  `(6, 9, 11)`  | 407  |
|  `(6, 9, 12)`  | 434  |
|  `(7, 8, 16)`  | 603  |
|  `(7, 9, 11)`  | 480  |

## Methodology & instruments
The research employs a multi-stage approach using custom-built tools:

### [ternary_flip_graph](https://github.com/dronperminov/ternary_flip_graph): core flip graph exploration toolkit
A comprehensive CPU-based toolkit for discovering fast matrix multiplication algorithms using flip graph techniques. Supports multiple coefficient sets
(`{0, 1}`, `{0, 1, 2}`, `{-1, 0, 1}`) and provides tools for rank minimization, complexity optimization, alternative scheme discovery, and meta operations
for transforming schemes between dimensions.

### [ternary_addition_reducer](https://github.com/dronperminov/ternary_addition_reducer): addition reduction tool
A high-performance tool for optimizing the number of arithmetic additions in fast matrix multiplication algorithms with ternary coefficients. It implements multiple
heuristic strategies to find near-optimal computation schemes, significantly reducing the additive cost of matrix multiplications schemes.

### Alternative scheme finding
This script starts from an existing binary (`Z2`) scheme and discovers new, non-identical schemes for the same dimensions. It works by:
* Randomly preserving coefficients from the original `U`, `V`, `W` matrices with configurable probabilities;
* Solving the resulting Brent equations using the CryptoMiniSat SAT solver;
* Exploring the solution space around known schemes.

```bash
python find_alternative_schemes.py -i <input_scheme_path> -o <output_dir> [options]
```

#### Options:
* `-pu`, `-pv`, `-pw` - probability thresholds for preserving `U`, `V`, `W` coefficients (default: `0.8`)
* `--max-time` - sat solver timeout in seconds (default: `20`)
* `-f` - maximum flip iterations for more effective search
* `-t` - number of sat solver threads

### Ternary coefficient Lifting
This script lifts binary (`Z2`) schemes to the ternary integer coefficient set (`ZT`, coefficients `{-1, 0, 1}`)
using OR-Tools SAT solver.

```bash
python lift_schemes.py -i <input_dir> -o <output_dir> [options]
```

#### Options:
* `--max-time` - maximum lifting time per scheme in seconds
* `--max-solutions` - maximum number of ternary solutions to find
* `--sort-scheme` - output schemes in "canonical" form
* `-f` - force re-lifting of existing schemes

## Analyzed Schemes & Data Sources
This research consolidates and analyzes schemes from several leading sources in the field:

| Source               | Description                                                                                                                                                                                      |
|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FMM catalogue        | The central repository for known fast matrix multiplication algorithms ([fmm.univ-lille.fr](https://fmm.univ-lille.fr)).                                                                         |
| Alpha Tensor         | Schemes from DeepMind's AlphaTensor project ([https://github.com/google-deepmind/alphatensor/tree/main/algorithms](https://github.com/google-deepmind/alphatensor/tree/main/algorithms)).        |
| Alpha Evolve         | Schemes from DeepMind's AlphaEvolve project ([mathematical_results.ipynb](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)). |
| Original Flip Graph  | Foundational work by Jakob Moosbauer ([flips](https://github.com/jakobmoosbauer/flips/tree/main/solutions)).                                                                                     |
| Adaptive flip graph  | Improved flip graph approach ([adap](https://github.com/Yamato-Arai/adap)).                                                                                                                      |
| Symmetric flip graph | Flip graphs with symmetry ([symmetric-flips](https://github.com/jakobmoosbauer/symmetric-flips)).                                                                                                |
| Meta Flip Graph      | Advanced flip graph techniques by M. Kauers et al. ([matrix-multiplication](https://github.com/mkauers/matrix-multiplication)).                                                                  |
| FMM Add Reduction    | Work on additive reductions by @werekorren ([fmm_add_reduction](https://github.com/werekorren/fmm_add_reduction/tree/main/algorithms)).                                                          |

## Scheme File Formats
This repository uses two JSON formats for storing matrix-multiplication schemes:
* Full scheme format (`.json`) - complete description with human-readable bilinear products and the matrices `U`, `V`, `W`;
* Reduced scheme format (`_reduced.json`) - compact representation used after additive-complexity reduction.

Both formats are described below.

### Full scheme format
This is the primary format used in the repository.
Each file describes a bilinear algorithm for multiplying an `n₁×n₂` by `n₂×n₃` using `m`multiplications.

#### Top level structure
```
{
    "n": [n₁, n₂, n₃],
    "m": rank,
    "z2": false,
    "u": [...],
    "v": [...],
    "w": [...],
    "multiplications": [...],
    "elements": [...]
}
```

#### Fields
* `n` - array `[n₁, n₂, n₃]` describing the dimensions (`A` is `n₁ × n₂`, `B` is `n₂ × n₃`);
* `m` - number of bilinear multiplications (rank);
* `z2` - whether coefficients are in Z2 field (`true`) or in any other (`false`);
* `multiplications` (human-readable) - list of expressions `m_k = (linear form in A) * (linear form in B)`;
* `elements` (human-readable) - expressions for each entry `c_{ij}` as linear combination of the `m_k`;
* `u` (machine-readable) - matrix encoding the linear form of `A`, size `m × (n₁·n₂)`;
* `v` (machine-readable) - matrix encoding the linear form of `B`, size `m × (n₂·n₃)`;
* `w` (machine-readable) - matrix encoding the linear form of `Cᵀ`, size `m × (n₃·n₁)`;

This format is intended for reproducibility and human and machine readability.

#### Example
Scheme `(2, 2, 2: 7)`:

```json
{
    "n": [2, 2, 2],
    "m": 7,
    "z2": false,
    "multiplications": [
        "m1 = (a11 + a22) * (b11 + b22)",
        "m2 = (a12 - a22) * (b21 + b22)",
        "m3 = (-a11 + a21) * (b11 + b12)",
        "m4 = (a11 + a12) * (b22)",
        "m5 = (a11) * (b12 - b22)",
        "m6 = (a22) * (-b11 + b21)",
        "m7 = (a21 + a22) * (b11)"
    ],
    "elements": [
        "c11 = m1 + m2 - m4 + m6",
        "c12 = m4 + m5",
        "c21 = m6 + m7",
        "c22 = m1 + m3 + m5 - m7"
    ],
    "u": [
        [1, 0, 0, 1],
        [0, 1, 0, -1],
        [-1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ],
    "v": [
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, -1],
        [-1, 0, 1, 0],
        [1, 0, 0, 0]
    ],
    "w": [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [-1, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, -1]
    ]
}
```

### Reduced scheme format
The reduced scheme format is used to store bilinear algorithms after additive-complexity reduction.
It contains both the "fresh-variable" representation (used during common-subexpression elimination) and the final reduced linear forms.

#### Top-level structure
```
{
    "n": [n₁, n₂, n₃],
    "m": rank,
    "z2": false,
    "complexity": {"naive": x, "reduced": y},
    "u_fresh": [...],
    "v_fresh": [...],
    "w_fresh": [...],
    "u": [...],
    "v": [...],
    "w": [...]
}
```

#### Fields
* `n`, `m`, `z2` - these fields have the same meaning as in the full scheme format (matrix dimensions, number of bilinear multiplications and binary field flag);

##### Complexity:
* `naive` - total number of additions before any reduction;
* `reduced` - number of additions after elimination of common subexpressions and simplification.

##### Fresh-variable representation
The reducer may introduce fresh intermediate variables to eliminate repeated subexpressions.
These are stored in three arrays: `u_fresh`, `v_fresh` and `w_fresh`.

Each array contains sparse linear forms written as:

```
[{ "index": i, "value": c }, ...]
```

###### Important indexing rule
Fresh-variable indices are allocated in consecutive blocks:
* For `U`: original indices: `0 ... n₁·n₂ - 1`, fresh indices start from: n1·n2;
* For `V`: original indices: `0 ... n₂·n₃ - 1`, fresh indices start from: n2·n3;
* For `W`: original indices: `0 ... m - 1`, fresh indices start from: m.

Thus the reducer’s intermediate variables do not collide with original matrix entries.
Each list entry corresponds to one intermediate expression introduced during reduction.

#### Reduced linear forms
After performing additive-complexity minimization, the reducer outputs the final optimized linear forms in `u`, `v` and `w`.
`u` and `v` arrays have exactly `m` rows each, `w` have `n₃·n₁` rows, and each row represents a sparse linear form:

```
[{ "index": i, "value": c }, ...]
```

#### Example
Reduces `(2, 2, 2: 7)` from 24 to 15 additions:
```json
{
    "n": [2, 2, 2],
    "m": 7,
    "z2": true,
    "complexity": {"naive": 24, "reduced": 15},
    "u_fresh": [
        [{"index": 2, "value": 1}, {"index": 3, "value": 1}],
        [{"index": 1, "value": 1}, {"index": 4, "value": 1}]
    ],
    "v_fresh": [
        [{"index": 2, "value": 1}, {"index": 3, "value": 1}],
        [{"index": 1, "value": 1}, {"index": 4, "value": 1}]
    ],
    "w_fresh": [
        [{"index": 2, "value": 1}, {"index": 3, "value": 1}],
        [{"index": 0, "value": 1}, {"index": 7, "value": 1}]
    ],
    "u": [
        [{"index": 4, "value": 1}],
        [{"index": 2, "value": 1}],
        [{"index": 1, "value": 1}],
        [{"index": 5, "value": 1}],
        [{"index": 0, "value": 1}],
        [{"index": 0, "value": 1}, {"index": 5, "value": 1}],
        [{"index": 1, "value": 1}, {"index": 3, "value": 1}]
    ],
    "v": [
        [{"index": 4, "value": 1}],
        [{"index": 0, "value": 1}, {"index": 5, "value": 1}],
        [{"index": 2, "value": 1}],
        [{"index": 5, "value": 1}],
        [{"index": 0, "value": 1}],
        [{"index": 1, "value": 1}],
        [{"index": 1, "value": 1}, {"index": 3, "value": 1}]
    ],
    "w": [
        [{"index": 2, "value": 1}, {"index": 4, "value": 1}],
        [{"index": 1, "value": 1}, {"index": 6, "value": 1}, {"index": 7, "value": 1}],
        [{"index": 5, "value": 1}, {"index": 8, "value": 1}],
        [{"index": 6, "value": 1}, {"index": 8, "value": 1}]
    ]
}
```

## Loading Schemes

The repository provides a Scheme class with a load method that supports all scheme formats used here:
* Full scheme format (`.json`);
* Addition-reduced scheme format (`reduced.json`);
* Maple format (`.m`)
* Plain text expressions (`.exp`)
* Maple tensor representation (`.tensor.mpl`)

This allows seamless integration of schemes produced by different tools and sources.

### Example usage

```python
from src.schemes.scheme import Scheme

scheme = Scheme.load("scheme.json")
scheme.show()  # print the scheme in human-readable format
scheme.show_tensors()  # print the scheme in (a)×(b)×(c) format

# scheme saving
scheme.save("scheme.json")  # save in json format
scheme.save_maple("scheme.m")  # save in maple format
scheme.save_txt("scheme.txt")  # save in txt format
```


## Research Findings & Status

The table below summarizes the current state of researched matrix multiplication schemes. It highlights where ternary schemes (ZT) match or approximate the known minimal ranks
from other fields. The best ranks of previously known schemes are given in brackets.

| Format<br/>`(n, m, p)` | rank<br/>in `ZT` | rank<br/>in `Z` | rank<br/>in `Q` | rank<br/>in `Z2` | complexity<br/>in `ZT` | complexity<br/>in `Z` | complexity<br/>in `Q` |
|:----------------------:|:----------------:|:---------------:|:---------------:|:----------------:|:----------------------:|:---------------------:|:---------------------:|
|      `(2, 2, 2)`       |        7         |        7        |        7        |        7         |           18           |          18           |          18           |
|      `(2, 2, 3)`       |        11        |       11        |       11        |        11        |           20           |          20           |          20           |
|      `(2, 2, 4)`       |        14        |       14        |       14        |        14        |           36           |          36           |          36           |
|      `(2, 2, 5)`       |        18        |       18        |       18        |        18        |           38           |          38           |          38           |
|      `(2, 2, 6)`       |        21        |       21        |       21        |        21        |           54           |          54           |          54           |
|      `(2, 2, 7)`       |        25        |       25        |       25        |        25        |           56           |          56           |          56           |
|      `(2, 2, 8)`       |        28        |       28        |       28        |        28        |           72           |          72           |          72           |
|      `(2, 2, 9)`       |        32        |       32        |       32        |        32        |           74           |          74           |          74           |
|      `(2, 2, 10)`      |        35        |       35        |       35        |        35        |           90           |          90           |          90           |
|      `(2, 2, 11)`      |        39        |       39        |       39        |        39        |           92           |          92           |          92           |
|      `(2, 2, 12)`      |        42        |       42        |       42        |        42        |          108           |          108          |          108          |
|      `(2, 2, 13)`      |        46        |       46        |       46        |        46        |          110           |          110          |          110          |
|      `(2, 2, 14)`      |        49        |       49        |       49        |        49        |          126           |          126          |          126          |
|      `(2, 2, 15)`      |        53        |       53        |       53        |        53        |          128           |          128          |          128          |
|      `(2, 2, 16)`      |        56        |       56        |       56        |        56        |          144           |          144          |          144          |
|      `(2, 3, 3)`       |        15        |       15        |       15        |        15        |           58           |          58           |          58           |
|      `(2, 3, 4)`       |        20        |       20        |       20        |        20        |           82           |          82           |          82           |
|      `(2, 3, 5)`       |        25        |       25        |       25        |        25        |       106 (113)        |       106 (108)       |       106 (108)       |
|      `(2, 3, 6)`       |        30        |       30        |       30        |        30        |          116           |          116          |          116          |
|      `(2, 3, 7)`       |        35        |       35        |       35        |        35        |          140           |          140          |          140          |
|      `(2, 3, 8)`       |        40        |       40        |       40        |        40        |          164           |          164          |          164          |
|      `(2, 3, 9)`       |        45        |       45        |       45        |        45        |          174           |          174          |          174          |
|      `(2, 3, 10)`      |      50 (?)      |       50        |       50        |        50        |        198 (?)         |       198 (254)       |       198 (254)       |
|      `(2, 3, 11)`      |        55        |       55        |       55        |        55        |          222           |          222          |          222          |
|      `(2, 3, 12)`      |        60        |       60        |       60        |        60        |          232           |          232          |          232          |
|      `(2, 3, 13)`      |      65 (?)      |       65        |       65        |        65        |        256 (?)         |       256 (312)       |       256 (312)       |
|      `(2, 3, 14)`      |        70        |       70        |       70        |        70        |          280           |          280          |          280          |
|      `(2, 3, 15)`      |      75 (?)      |       75        |       75        |        75        |        307 (?)         |       307 (381)       |       307 (381)       |
|      `(2, 3, 16)`      |        80        |       80        |       80        |        80        |          328           |          328          |          328          |
|      `(2, 4, 4)`       |        26        |       26        |       26        |        26        |          122           |          122          |          122          |
|      `(2, 4, 5)`       |      33 (?)      |       33        |       32        |        33        |           -            |           -           |           -           |
|      `(2, 4, 6)`       |      39 (?)      |       39        |       39        |        39        |        202 (?)         |       202 (329)       |       202 (329)       |
|      `(2, 4, 7)`       |        45        |       45        |       45        |        45        |          308           |          308          |          308          |
|      `(2, 4, 8)`       |        51        |       51        |       51        |        51        |          354           |          354          |          354          |
|      `(2, 4, 9)`       |      59 (?)      |     59 (?)      |       58        |      59 (?)      |           -            |           -           |           -           |
|      `(2, 4, 10)`      |      65 (?)      |     65 (?)      |       64        |      65 (?)      |           -            |           -           |           -           |
|      `(2, 4, 11)`      |      71 (?)      |     71 (?)      |       71        |      71 (?)      |        430 (?)         |        430 (?)        |       430 (749)       |
|      `(2, 4, 12)`      |      77 (?)      |     77 (?)      |       77        |      77 (?)      |        484 (?)         |        484 (?)        |       484 (746)       |
|      `(2, 4, 13)`      |      84 (?)      |     84 (?)      |       83        |      84 (?)      |           -            |           -           |           -           |
|      `(2, 4, 14)`      |        90        |       90        |       90        |        90        |          616           |          616          |          616          |
|      `(2, 4, 15)`      |      96 (?)      |     96 (?)      |       96        |      96 (?)      |        662 (?)         |        662 (?)        |      662 (1314)       |
|      `(2, 4, 16)`      |       102        |       102       |       102       |       102        |          708           |          708          |          708          |
|      `(2, 5, 5)`       |        40        |       40        |       40        |        40        |          208           |          208          |          208          |
|      `(2, 5, 6)`       |        47        |       47        |       47        |        47        |          332           |          332          |          332          |
|      `(2, 5, 7)`       |      57 (?)      |     55 (?)      |       55        |        55        |           -            |           -           |           -           |
|      `(2, 5, 8)`       |      65 (?)      |     63 (?)      |       63        |        63        |           -            |           -           |           -           |
|      `(2, 5, 9)`       |      72 (?)      |     72 (?)      |       72        |      72 (?)      |        465 (?)         |        465 (?)        |       465 (565)       |
|      `(2, 5, 10)`      |      80 (?)      |     80 (?)      |       79        |      80 (?)      |           -            |           -           |           -           |
|      `(2, 5, 11)`      |        87        |       87        |       87        |        87        |          540           |          540          |          540          |
|      `(2, 5, 12)`      |        94        |       94        |       94        |        94        |          664           |          664          |          664          |
|      `(2, 5, 13)`      |     104 (?)      |     102 (?)     |       102       |       102        |           -            |           -           |           -           |
|      `(2, 5, 14)`      |     112 (?)      |     110 (?)     |       110       |       110        |           -            |           -           |           -           |
|      `(2, 5, 15)`      |     119 (?)      |     118 (?)     |       118       |       118        |           -            |           -           |           -           |
|      `(2, 5, 16)`      |     127 (?)      |     126 (?)     |       126       |     126 (?)      |           -            |           -           |           -           |
|      `(2, 6, 6)`       |      57 (?)      |       56        |       56        |        56        |           -            |           -           |           -           |
|      `(2, 6, 7)`       |      67 (?)      |       66        |       66        |        66        |           -            |           -           |           -           |
|      `(2, 6, 8)`       |      77 (?)      |     75 (?)      |       75        |        75        |           -            |           -           |           -           |
|      `(2, 6, 9)`       |      86 (?)      |       86        |       86        |        86        |        548 (?)         |       548 (691)       |       548 (691)       |
|      `(2, 6, 10)`      |        94        |       94        |       94        |        94        |          668           |          668          |          668          |
|      `(2, 6, 11)`      |     104 (?)      |       103       |       103       |       103        |           -            |           -           |           -           |
|      `(2, 6, 12)`      |     114 (?)      |       112       |       112       |       112        |           -            |           -           |           -           |
|      `(2, 6, 13)`      |     124 (?)      |     122 (?)     |       122       |       122        |           -            |           -           |           -           |
|      `(2, 6, 14)`      |     133 (?)      |     131 (?)     |       131       |       131        |           -            |           -           |           -           |
|      `(2, 6, 15)`      |       141        |       141       |       141       |       141        |          1002          |         1002          |         1002          |
|      `(2, 6, 16)`      |     151 (?)      |       150       |       150       |       150        |           -            |           -           |           -           |
|      `(2, 7, 7)`       |      77 (?)      |     76 (?)      |       76        |        76        |           -            |           -           |           -           |
|      `(2, 7, 8)`       |      88 (?)      |       88        |       88        |        88        |        745 (?)         |       745 (783)       |       745 (783)       |
|      `(2, 7, 9)`       |     102 (?)      |     100 (?)     |       99        |     100 (?)      |           -            |           -           |           -           |
|      `(2, 7, 10)`      |     112 (?)      |       110       |       110       |       110        |           -            |           -           |           -           |
|      `(2, 7, 11)`      |     122 (?)      |       121       |       121       |       121        |           -            |           -           |           -           |
|      `(2, 7, 12)`      |     133 (?)      |     131 (?)     |       131       |       131        |           -            |           -           |           -           |
|      `(2, 7, 13)`      |     144 (?)      |     142 (?)     |       142       |       142        |           -            |           -           |           -           |
|      `(2, 7, 14)`      |     154 (?)      |     152 (?)     |       152       |       152        |           -            |           -           |           -           |
|      `(2, 7, 15)`      |     165 (?)      |     164 (?)     |       164       |       164        |           -            |           -           |           -           |
|      `(2, 7, 16)`      |     176 (?)      |     176 (?)     |       175       |       175        |           -            |           -           |           -           |
|      `(2, 8, 8)`       |       100        |       100       |       100       |       100        |          608           |          608          |          608          |
|      `(2, 8, 9)`       |     116 (?)      |     114 (?)     |       113       |     114 (?)      |           -            |           -           |           -           |
|      `(2, 8, 10)`      |     128 (?)      |       125       |       125       |       125        |           -            |           -           |           -           |
|      `(2, 8, 11)`      |     139 (?)      |       138       |       138       |       138        |           -            |           -           |           -           |
|      `(2, 8, 12)`      |     151 (?)      |       150       |       150       |       150        |           -            |           -           |           -           |
|      `(2, 8, 13)`      |     165 (?)      |     163 (?)     |    163 (164)    |     163 (?)      |           -            |           -           |           -           |
|      `(2, 8, 14)`      |     176 (?)      |     175 (?)     |       175       |     175 (?)      |           -            |           -           |           -           |
|      `(2, 8, 15)`      |     188 (?)      |       188       |       188       |       188        |        1355 (?)        |      1355 (1393)      |      1355 (1393)      |
|      `(2, 8, 16)`      |       200        |       200       |       200       |       200        |          1216          |         1216          |         1216          |
|      `(2, 9, 9)`       |       126        |       126       |       126       |       126        |          804           |          804          |          804          |
|      `(2, 9, 10)`      |     144 (?)      |       140       |       140       |       140        |           -            |           -           |           -           |
|      `(2, 9, 11)`      |     158 (?)      |       154       |       154       |       154        |           -            |           -           |           -           |
|      `(2, 9, 12)`      |     171 (?)      |       168       |       168       |       168        |           -            |           -           |           -           |
|      `(2, 9, 13)`      |     185 (?)      |     185 (?)     |       182       |     185 (?)      |           -            |           -           |           -           |
|      `(2, 9, 14)`      |     198 (?)      |     198 (?)     |       196       |     198 (?)      |           -            |           -           |           -           |
|     `(2, 10, 10)`      |       155        |       155       |       155       |       155        |          1016          |         1016          |         1016          |
|     `(2, 10, 11)`      |     174 (?)      |       171       |       171       |       171        |           -            |           -           |           -           |
|     `(2, 10, 12)`      |     188 (?)      |       186       |       186       |       186        |           -            |           -           |           -           |
|     `(2, 11, 11)`      |       187        |       187       |       187       |       187        |          1218          |         1218          |         1218          |
|      `(3, 3, 3)`       |        23        |       23        |       23        |        23        |           84           |          84           |          84           |
|      `(3, 3, 4)`       |        29        |       29        |       29        |        29        |          134           |          134          |          134          |
|      `(3, 3, 5)`       |        36        |       36        |       36        |        36        |       178 (193)        |       178 (185)       |       178 (185)       |
|      `(3, 3, 6)`       |      42 (?)      |       42        |       40        |        42        |           -            |           -           |           -           |
|      `(3, 3, 7)`       |      49 (?)      |     49 (?)      |       49        |      49 (?)      |        404 (?)         |        404 (?)        |       404 (868)       |
|      `(3, 3, 8)`       |      56 (?)      |     56 (?)      |       55        |      55 (?)      |           -            |           -           |           -           |
|      `(3, 3, 9)`       |      63 (?)      |     63 (?)      |       63        |      63 (?)      |        411 (?)         |        411 (?)        |       411 (960)       |
|      `(3, 3, 10)`      |      71 (?)      |     71 (?)      |       69        |      71 (?)      |           -            |           -           |           -           |
|      `(3, 3, 11)`      |      78 (?)      |     78 (?)      |       76        |      78 (?)      |           -            |           -           |           -           |
|      `(3, 3, 12)`      |      84 (?)      |     84 (?)      |       80        |      84 (?)      |           -            |           -           |           -           |
|      `(3, 3, 13)`      |      91 (?)      |     91 (?)      |       89        |      91 (?)      |           -            |           -           |           -           |
|      `(3, 3, 14)`      |      98 (?)      |     98 (?)      |       95        |      98 (?)      |           -            |           -           |           -           |
|      `(3, 3, 15)`      |     105 (?)      |     105 (?)     |       103       |     105 (?)      |           -            |           -           |           -           |
|      `(3, 3, 16)`      |     112 (?)      |     112 (?)     |       109       |     112 (?)      |           -            |           -           |           -           |
|      `(3, 4, 4)`       |        38        |       38        |       38        |        38        |          192           |          192          |          192          |
|      `(3, 4, 5)`       |      47 (?)      |       47        |       47        |        47        |        277 (?)         |       277 (293)       |       277 (293)       |
|      `(3, 4, 6)`       |      54 (?)      |       54        |       54        |        54        |        700 (?)         |       700 (820)       |          538          |
|      `(3, 4, 7)`       |      64 (?)      |       64        |       63        |        64        |           -            |           -           |           -           |
|      `(3, 4, 8)`       |        74        |     73 (74)     |       73        |        73        |           -            |           -           |           -           |
|      `(3, 4, 9)`       |      83 (?)      |     83 (?)      |       83        |      83 (?)      |        837 (?)         |        837 (?)        |          675          |
|      `(3, 4, 10)`      |      92 (?)      |     92 (?)      |       92        |      92 (?)      |        892 (?)         |        892 (?)        |          725          |
|      `(3, 4, 11)`      |     101 (?)      |     101 (?)     |       101       |     101 (?)      |        977 (?)         |        977 (?)        |          831          |
|      `(3, 4, 12)`      |     108 (?)      |     108 (?)     |       108       |     108 (?)      |        1400 (?)        |       1400 (?)        |         1076          |
|      `(3, 4, 13)`      |     118 (?)      |     118 (?)     |       117       |     118 (?)      |           -            |           -           |           -           |
|      `(3, 4, 14)`      |     128 (?)      |     127 (?)     |       126       |     127 (?)      |           -            |           -           |           -           |
|      `(3, 4, 15)`      |     137 (?)      |     137 (?)     |       136       |     137 (?)      |           -            |           -           |           -           |
|      `(3, 4, 16)`      |     146 (?)      |     146 (?)     |       146       |     146 (?)      |        1592 (?)        |       1592 (?)        |         1260          |
|      `(3, 5, 5)`       |        58        |       58        |       58        |        58        |       351 (357)        |       351 (357)       |       351 (357)       |
|      `(3, 5, 6)`       |      70 (?)      |       68        |       68        |        68        |           -            |           -           |           -           |
|      `(3, 5, 7)`       |      81 (?)      |     79 (80)     |       79        |        79        |           -            |           -           |           -           |
|      `(3, 5, 8)`       |      92 (?)      |       90        |       90        |        90        |           -            |           -           |           -           |
|      `(3, 5, 9)`       |     105 (?)      |       104       |       104       |       104        |           -            |           -           |           -           |
|      `(3, 5, 10)`      |     115 (?)      |       115       |       115       |       115        |        730 (?)         |       730 (778)       |       730 (778)       |
|      `(3, 5, 11)`      |     128 (?)      |       126       |       126       |       126        |           -            |           -           |           -           |
|      `(3, 5, 12)`      |     139 (?)      |       136       |       136       |       136        |           -            |           -           |           -           |
|      `(3, 5, 13)`      |     150 (?)      |     147 (?)     |       147       |       147        |           -            |           -           |           -           |
|      `(3, 5, 14)`      |     162 (?)      |     158 (?)     |       158       |       158        |           -            |           -           |           -           |
|      `(3, 5, 15)`      |     173 (?)      |     169 (?)     |       169       |       169        |           -            |           -           |           -           |
|      `(3, 5, 16)`      |     184 (?)      |       180       |       180       |       180        |           -            |           -           |           -           |
|      `(3, 6, 6)`       |      83 (?)      |     83 (?)      |       80        |     83 (86)      |           -            |           -           |           -           |
|      `(3, 6, 7)`       |      96 (?)      |     96 (?)      |       94        |      96 (?)      |           -            |           -           |           -           |
|      `(3, 6, 8)`       |     108 (?)      |       108       |       108       |       108        |        1412 (?)        |      1412 (2123)      |         1088          |
|      `(3, 6, 9)`       |     124 (?)      |     122 (?)     |       120       |     122 (?)      |           -            |           -           |           -           |
|      `(3, 6, 10)`      |     137 (?)      |     136 (?)     |       134       |     136 (?)      |           -            |           -           |           -           |
|      `(3, 6, 11)`      |     150 (?)      |     150 (?)     |       148       |     150 (?)      |           -            |           -           |           -           |
|      `(3, 6, 12)`      |     162 (?)      |     162 (?)     |       160       |     162 (?)      |           -            |           -           |           -           |
|      `(3, 6, 13)`      |     178 (?)      |     176 (?)     |       174       |     176 (?)      |           -            |           -           |           -           |
|      `(3, 6, 14)`      |     191 (?)      |     190 (?)     |       188       |     190 (?)      |           -            |           -           |           -           |
|      `(3, 6, 15)`      |     204 (?)      |     204 (?)     |       200       |     204 (?)      |           -            |           -           |           -           |
|      `(3, 6, 16)`      |     216 (?)      |     216 (?)     |       214       |     216 (?)      |           -            |           -           |           -           |
|      `(3, 7, 7)`       |     113 (?)      |     111 (?)     |       111       |       111        |           -            |           -           |           -           |
|      `(3, 7, 8)`       |     128 (?)      |     128 (?)     |       126       |     128 (?)      |           -            |           -           |           -           |
|      `(3, 7, 9)`       |     145 (?)      |     143 (?)     |       142       |     143 (?)      |           -            |           -           |           -           |
|      `(3, 7, 10)`      |     160 (?)      |     158 (?)     |       157       |     158 (?)      |           -            |           -           |           -           |
|      `(3, 7, 11)`      |     177 (?)      |     175 (?)     |       173       |     175 (?)      |           -            |           -           |           -           |
|      `(3, 7, 12)`      |     192 (?)      |     190 (?)     |       188       |     190 (?)      |           -            |           -           |           -           |
|      `(3, 7, 13)`      |     209 (?)      |     207 (?)     |       205       |     207 (?)      |           -            |           -           |           -           |
|      `(3, 7, 14)`      |     224 (?)      |     222 (?)     |       220       |     222 (?)      |           -            |           -           |           -           |
|      `(3, 7, 15)`      |     241 (?)      |     237 (?)     |       236       |     237 (?)      |           -            |           -           |           -           |
|      `(3, 7, 16)`      |     256 (?)      |     254 (?)     |       251       |     254 (?)      |           -            |           -           |           -           |
|      `(3, 8, 8)`       |     148 (?)      |     146 (?)     |       145       |     145 (?)      |           -            |           -           |           -           |
|      `(3, 8, 9)`       |     164 (?)      |     163 (?)     |       163       |     163 (?)      |           -            |           -           |           -           |
|      `(3, 8, 10)`      |     182 (?)      |       180       |       180       |       180        |           -            |           -           |           -           |
|      `(3, 8, 11)`      |     200 (?)      |     198 (?)     |       198       |     198 (?)      |           -            |           -           |           -           |
|      `(3, 8, 12)`      |     216 (?)      |     216 (?)     |       216       |     216 (?)      |        2836 (?)        |       2836 (?)        |         2188          |
|      `(3, 8, 13)`      |     236 (?)      |     236 (?)     |       234       |     236 (?)      |           -            |           -           |           -           |
|      `(3, 8, 14)`      |     256 (?)      |     253 (?)     |       252       |     253 (?)      |           -            |           -           |           -           |
|      `(3, 8, 15)`      |     272 (?)      |       270       |       270       |       270        |           -            |           -           |           -           |
|      `(3, 8, 16)`      |     290 (?)      |     288 (?)     |       288       |     288 (?)      |           -            |           -           |           -           |
|      `(3, 9, 9)`       |     187 (?)      |     185 (?)     |       183       |     185 (?)      |           -            |           -           |           -           |
|      `(3, 9, 10)`      |     207 (?)      |     205 (?)     |       203       |     205 (?)      |           -            |           -           |           -           |
|      `(3, 9, 11)`      |     227 (?)      |     226 (?)     |       224       |     226 (?)      |           -            |           -           |           -           |
|      `(3, 9, 12)`      |     246 (?)      |     244 (?)     |       240       |     244 (?)      |           -            |           -           |           -           |
|      `(3, 9, 13)`      |     268 (?)      |     265 (?)     |       262       |     265 (?)      |           -            |           -           |           -           |
|      `(3, 9, 14)`      |     288 (?)      |     285 (?)     |       283       |     285 (?)      |           -            |           -           |           -           |
|     `(3, 10, 10)`      |     229 (?)      |     228 (?)     |       226       |     228 (?)      |           -            |           -           |           -           |
|     `(3, 10, 11)`      |     251 (?)      |     250 (?)     |       249       |     250 (?)      |           -            |           -           |           -           |
|     `(3, 10, 12)`      |     270 (?)      |     270 (?)     |       268       |     270 (?)      |           -            |           -           |           -           |
|     `(3, 11, 11)`      |     278 (?)      |     276 (?)     |       274       |     276 (?)      |           -            |           -           |           -           |
|      `(4, 4, 4)`       |        49        |       49        |       48        |        47        |           -            |           -           |           -           |
|      `(4, 4, 5)`       |        61        |       61        |       61        |        60        |       452 (455)        |       452 (455)       |       452 (455)       |
|      `(4, 4, 6)`       |      73 (?)      |       73        |       73        |        73        |        534 (?)         |       534 (740)       |       534 (740)       |
|      `(4, 4, 7)`       |        85        |       85        |       85        |        85        |          631           |          631          |          631          |
|      `(4, 4, 8)`       |      96 (?)      |     96 (?)      |       96        |      94 (?)      |        962 (?)         |        962 (?)        |      962 (1920)       |
|      `(4, 4, 9)`       |     107 (?)      |     107 (?)     |       104       |     107 (?)      |           -            |           -           |           -           |
|      `(4, 4, 10)`      |     115 (?)      |     115 (?)     |    115 (120)    |     115 (?)      |        1358 (?)        |       1358 (?)        |      1358 (1437)      |
|      `(4, 4, 11)`      |     130 (?)      |     130 (?)     |       130       |     130 (?)      |        1540 (?)        |       1540 (?)        |      1540 (1555)      |
|      `(4, 4, 12)`      |     141 (?)      |     141 (?)     |    141 (142)    |     141 (?)      |        1480 (?)        |       1480 (?)        |      1480 (1617)      |
|      `(4, 4, 13)`      |     153 (?)      |     153 (?)     |       152       |     153 (?)      |           -            |           -           |           -           |
|      `(4, 4, 14)`      |     164 (?)      |     164 (?)     |    163 (165)    |     164 (?)      |           -            |           -           |           -           |
|      `(4, 4, 15)`      |     176 (?)      |     176 (?)     |    176 (177)    |     176 (?)      |        1813 (?)        |       1813 (?)        |      1813 (2562)      |
|      `(4, 4, 16)`      |     188 (?)      |     188 (?)     |    188 (189)    |     188 (?)      |        1898 (?)        |       1898 (?)        |      1898 (2056)      |
|      `(4, 5, 5)`       |        76        |       76        |       76        |        73        |       528 (549)        |       528 (549)       |       528 (549)       |
|      `(4, 5, 6)`       |      90 (?)      |       90        |       90        |     89 (90)      |        998 (?)         |          775          |          775          |
|      `(4, 5, 7)`       |     104 (?)      |       104       |       104       |       104        |        924 (?)         |      924 (1386)       |      924 (1354)       |
|      `(4, 5, 8)`       |    118 (122)     |       118       |       118       |       118        |       1463 (918)       |      1463 (918)       |      1463 (918)       |
|      `(4, 5, 9)`       |     132 (?)      |    132 (139)    |    132 (136)    |    132 (139)     |        1761 (?)        |         1026          |         1026          |
|      `(4, 5, 10)`      |    146 (152)     |    146 (151)    |    146 (151)    |    146 (151)     |      2012 (1568)       |      1706 (1568)      |      1706 (1568)      |
|      `(4, 5, 11)`      |     160 (?)      |    160 (165)    |    160 (165)    |    160 (165)     |        2192 (?)        |         1869          |         1869          |
|      `(4, 5, 12)`      |     175 (?)      |    175 (180)    |    175 (180)    |    175 (180)     |        2465 (?)        |         2196          |         2196          |
|      `(4, 5, 13)`      |     192 (?)      |    192 (194)    |    192 (194)    |    192 (194)     |        2764 (?)        |         2508          |         2508          |
|      `(4, 5, 14)`      |     207 (?)      |    207 (208)    |    207 (208)    |    207 (208)     |        2472 (?)        |      2472 (2820)      |      2472 (2820)      |
|      `(4, 5, 15)`      |     221 (?)      |    221 (226)    |    221 (226)    |    221 (226)     |        2648 (?)        |         2328          |         2328          |
|      `(4, 5, 16)`      |     236 (?)      |     236 (?)     |    236 (240)    |     236 (?)      |        2921 (?)        |       2921 (?)        |      2921 (3260)      |
|      `(4, 6, 6)`       |       105        |       105       |       105       |       105        |          894           |          894          |          894          |
|      `(4, 6, 7)`       |     123 (?)      |       123       |       123       |       123        |        1562 (?)        |      1562 (1798)      |      1562 (1785)      |
|      `(4, 6, 8)`       |       140        |       140       |       140       |       140        |          1248          |         1248          |         1248          |
|      `(4, 6, 9)`       |     159 (?)      |     159 (?)     |       159       |     159 (?)      |        1600 (?)        |       1600 (?)        |         1438          |
|      `(4, 6, 10)`      |     175 (?)      |       175       |       175       |       175        |        1878 (?)        |         1854          |         1854          |
|      `(4, 6, 11)`      |     194 (?)      |     194 (?)     |       194       |     194 (?)      |        1954 (?)        |       1954 (?)        |         1792          |
|      `(4, 6, 12)`      |       210        |       210       |       210       |       210        |          1788          |         1788          |         1788          |
|      `(4, 6, 13)`      |     228 (?)      |       228       |       228       |       228        |        2456 (?)        |      2456 (2692)      |      2456 (2692)      |
|      `(4, 6, 14)`      |       245        |       245       |       245       |       245        |          2142          |         2142          |         2142          |
|      `(4, 6, 15)`      |     263 (?)      |       263       |       263       |       263        |        2810 (?)        |      2810 (3046)      |      2810 (3046)      |
|      `(4, 6, 16)`      |       280        |       280       |       280       |       280        |          2496          |         2496          |         2496          |
|      `(4, 7, 7)`       |     144 (?)      |       144       |       144       |       144        |        1983 (?)        |      1983 (2290)      |      1983 (2290)      |
|      `(4, 7, 8)`       |       164        |       164       |       164       |       164        |      1505 (1554)       |      1505 (1554)      |      1505 (1554)      |
|      `(4, 7, 9)`       |     187 (?)      |     187 (?)     |       186       |     187 (?)      |           -            |           -           |           -           |
|      `(4, 7, 10)`      |     206 (?)      |     206 (?)     |       203       |     206 (?)      |           -            |           -           |           -           |
|      `(4, 7, 11)`      |     226 (?)      |    226 (227)    |    226 (227)    |    226 (227)     |        3780 (?)        |         3220          |         3220          |
|      `(4, 7, 12)`      |     246 (?)      |       246       |       246       |       246        |        3132 (?)        |      3132 (3604)      |      3132 (3604)      |
|      `(4, 7, 13)`      |     267 (?)      |     267 (?)     |       266       |     267 (?)      |           -            |           -           |           -           |
|      `(4, 7, 14)`      |       285        |       285       |       285       |       285        |          3188          |         3188          |         3188          |
|      `(4, 7, 15)`      |     307 (?)      |     307 (?)     |       307       |     307 (?)      |        3436 (?)        |       3436 (?)        |      3436 (5216)      |
|      `(4, 7, 16)`      |       324        |       324       |       324       |       324        |          3760          |         3760          |         3760          |
|      `(4, 8, 8)`       |       182        |       182       |       182       |       182        |          1884          |         1884          |         1884          |
|      `(4, 8, 9)`       |     209 (?)      |     209 (?)     |       206       |     209 (?)      |           -            |           -           |           -           |
|      `(4, 8, 10)`      |     230 (?)      |     230 (?)     |       224       |     230 (?)      |           -            |           -           |           -           |
|      `(4, 8, 11)`      |     255 (?)      |     255 (?)     |       252       |     255 (?)      |           -            |           -           |           -           |
|      `(4, 8, 12)`      |       272        |       272       |       272       |       272        |          2834          |         2834          |         2834          |
|      `(4, 8, 13)`      |     297 (?)      |       297       |       297       |       297        |        3620 (?)        |      3620 (4190)      |      3620 (4190)      |
|      `(4, 8, 14)`      |       315        |       315       |       315       |       315        |          4258          |         4258          |         4258          |
|      `(4, 8, 15)`      |       339        |       339       |       339       |       339        |          4544          |         4544          |         4544          |
|      `(4, 8, 16)`      |       357        |       357       |       357       |       357        |          4886          |         4886          |         4886          |
|      `(4, 9, 9)`       |       225        |       225       |       225       |       225        |          2462          |         2462          |         2462          |
|      `(4, 9, 10)`      |       255        |       255       |       255       |       255        |          3136          |         3136          |         3136          |
|      `(4, 9, 11)`      |    279 (280)     |    279 (280)    |    279 (280)    |    279 (280)     |      3418 (3064)       |      3418 (3064)      |      3418 (3064)      |
|      `(4, 9, 12)`      |       300        |       300       |       300       |       300        |          3408          |         3408          |         3408          |
|      `(4, 9, 13)`      |     330 (?)      |     330 (?)     |       329       |     330 (?)      |           -            |           -           |           -           |
|      `(4, 9, 14)`      |     355 (?)      |       355       |       355       |       355        |        4150 (?)        |      4150 (4485)      |      4150 (4485)      |
|     `(4, 10, 10)`      |       280        |       280       |       280       |       280        |          2976          |         2976          |         2976          |
|     `(4, 10, 11)`      |       308        |       308       |       308       |       308        |          3778          |         3778          |         3778          |
|     `(4, 10, 12)`      |       329        |       329       |       329       |       329        |          4550          |         4550          |         4550          |
|     `(4, 11, 11)`      |     342 (?)      |       340       |       340       |       340        |           -            |           -           |           -           |
|      `(5, 5, 5)`       |        93        |       93        |       93        |        93        |       843 (846)        |       843 (846)       |       843 (846)       |
|      `(5, 5, 6)`       |     110 (?)      |       110       |       110       |       110        |        1192 (?)        |      1192 (1300)      |      1192 (1300)      |
|      `(5, 5, 7)`       |    127 (134)     |       127       |       127       |       127        |       1606 (918)       |      1606 (918)       |      1606 (918)       |
|      `(5, 5, 8)`       |     144 (?)      |       144       |       144       |       144        |        1872 (?)        |      1872 (2257)      |      1872 (1924)      |
|      `(5, 5, 9)`       |     163 (?)      |    163 (167)    |    163 (167)    |    163 (167)     |        2250 (?)        |         2220          |         2220          |
|      `(5, 5, 10)`      |     184 (?)      |     184 (?)     |       184       |    183 (184)     |        2083 (?)        |       2083 (?)        |      2083 (2582)      |
|      `(5, 5, 11)`      |     202 (?)      |     202 (?)     |       202       |    200 (202)     |        2271 (?)        |       2271 (?)        |      2271 (2731)      |
|      `(5, 5, 12)`      |     220 (?)      |       220       |       220       |    217 (220)     |        2444 (?)        |      2444 (3458)      |      2444 (3458)      |
|      `(5, 5, 13)`      |     237 (?)      |       237       |       237       |       237        |        2715 (?)        |      2715 (3741)      |      2715 (3741)      |
|      `(5, 5, 14)`      |     254 (?)      |       254       |       254       |       254        |        3064 (?)        |      3064 (4024)      |      3064 (4024)      |
|      `(5, 5, 15)`      |     271 (?)      |     271 (?)     |       271       |       271        |        3478 (?)        |       3478 (?)        |      3478 (4386)      |
|      `(5, 5, 16)`      |     288 (?)      |     288 (?)     |       288       |       288        |        3744 (?)        |       3744 (?)        |      3744 (4748)      |
|      `(5, 6, 6)`       |     130 (?)      |       130       |       130       |       130        |        1697 (?)        |      1697 (1766)      |      1697 (1758)      |
|      `(5, 6, 7)`       |     150 (?)      |       150       |       150       |       150        |        1994 (?)        |      1994 (2431)      |      1994 (2431)      |
|      `(5, 6, 8)`       |    170 (176)     |       170       |       170       |       170        |      2312 (1965)       |      2312 (1965)      |      2312 (1965)      |
|      `(5, 6, 9)`       |     197 (?)      |       197       |       197       |       197        |        2328 (?)        |      2328 (3049)      |      2328 (3049)      |
|      `(5, 6, 10)`      |     217 (?)      |    217 (218)    |    217 (218)    |    217 (218)     |        2772 (?)        |      2772 (3200)      |      2772 (3200)      |
|      `(5, 6, 11)`      |     240 (?)      |     238 (?)     |       236       |     238 (?)      |           -            |           -           |           -           |
|      `(5, 6, 12)`      |     258 (?)      |     258 (?)     |       250       |     258 (?)      |           -            |           -           |           -           |
|      `(5, 6, 13)`      |     280 (?)      |     280 (?)     |       278       |     280 (?)      |           -            |           -           |           -           |
|      `(5, 6, 14)`      |     300 (?)      |     300 (?)     |       297       |     300 (?)      |           -            |           -           |           -           |
|      `(5, 6, 15)`      |     320 (?)      |     320 (?)     |       318       |     320 (?)      |           -            |           -           |           -           |
|      `(5, 6, 16)`      |     340 (?)      |     340 (?)     |       340       |     340 (?)      |        4624 (?)        |       4624 (?)        |      4624 (7818)      |
|      `(5, 7, 7)`       |     176 (?)      |       176       |       176       |       176        |        2535 (?)        |      2535 (2846)      |      2535 (2846)      |
|      `(5, 7, 8)`       |     204 (?)      |     204 (?)     |    204 (205)    |    204 (205)     |        2606 (?)        |       2606 (?)        |      2606 (4049)      |
|      `(5, 7, 9)`       |     231 (?)      |    229 (234)    |       229       |       229        |           -            |           -           |           -           |
|      `(5, 7, 10)`      |     254 (?)      |       254       |       254       |       254        |        2931 (?)        |      2931 (4044)      |      2931 (4044)      |
|      `(5, 7, 11)`      |     277 (?)      |       277       |       277       |       277        |        3615 (?)        |      3615 (4742)      |      3615 (4742)      |
|      `(5, 7, 12)`      |     300 (?)      |     300 (?)     |       296       |     300 (?)      |           -            |           -           |           -           |
|      `(5, 7, 13)`      |     326 (?)      |     326 (?)     |       325       |     326 (?)      |           -            |           -           |           -           |
|      `(5, 7, 14)`      |     351 (?)      |     351 (?)     |       349       |     351 (?)      |           -            |           -           |           -           |
|      `(5, 7, 15)`      |     379 (?)      |     378 (?)     |       375       |     378 (?)      |           -            |           -           |           -           |
|      `(5, 7, 16)`      |     402 (?)      |     400 (?)     |       398       |     400 (?)      |           -            |           -           |           -           |
|      `(5, 8, 8)`       |       230        |       230       |       230       |       230        |      2638 (2842)       |      2638 (2842)      |      2638 (2842)      |
|      `(5, 8, 9)`       |     262 (?)      |     260 (?)     |       260       |     260 (?)      |           -            |           -           |           -           |
|      `(5, 8, 10)`      |     287 (?)      |     287 (?)     |       284       |     287 (?)      |           -            |           -           |           -           |
|      `(5, 8, 11)`      |     313 (?)      |     313 (?)     |       312       |     313 (?)      |           -            |           -           |           -           |
|      `(5, 8, 12)`      |     333 (?)      |     333 (?)     |       333       |     333 (?)      |        6192 (?)        |       6192 (?)        |         5586          |
|      `(5, 8, 13)`      |     365 (?)      |     365 (?)     |       363       |     365 (?)      |           -            |           -           |           -           |
|      `(5, 8, 14)`      |     391 (?)      |     391 (?)     |       387       |     391 (?)      |           -            |           -           |           -           |
|      `(5, 8, 15)`      |     423 (?)      |     421 (?)     |       419       |     421 (?)      |           -            |           -           |           -           |
|      `(5, 8, 16)`      |     449 (?)      |     445 (?)     |       445       |       445        |           -            |           -           |           -           |
|      `(5, 9, 9)`       |     295 (?)      |     295 (?)     |       294       |     295 (?)      |           -            |           -           |           -           |
|      `(5, 9, 10)`      |     323 (?)      |     323 (?)     |       322       |     323 (?)      |           -            |           -           |           -           |
|      `(5, 9, 11)`      |     355 (?)      |     353 (?)     |       353       |     353 (?)      |           -            |           -           |           -           |
|      `(5, 9, 12)`      |     381 (?)      |     377 (?)     |       377       |     377 (?)      |           -            |           -           |           -           |
|      `(5, 9, 13)`      |     417 (?)      |     412 (?)     |       411       |     412 (?)      |           -            |           -           |           -           |
|      `(5, 9, 14)`      |     448 (?)      |     441 (?)     |       439       |     441 (?)      |           -            |           -           |           -           |
|     `(5, 10, 10)`      |       352        |       352       |       352       |       352        |          3928          |         3928          |         3928          |
|     `(5, 10, 11)`      |     390 (?)      |       386       |       386       |       386        |           -            |           -           |           -           |
|     `(5, 10, 12)`      |     421 (?)      |       413       |       413       |       413        |           -            |           -           |           -           |
|     `(5, 11, 11)`      |     432 (?)      |     427 (?)     |       424       |     427 (?)      |           -            |           -           |           -           |
|      `(6, 6, 6)`       |       153        |       153       |       153       |       153        |      2171 (2232)       |      2171 (2232)      |      2171 (2232)      |
|      `(6, 6, 7)`       |     183 (?)      |       183       |       183       |       183        |        2493 (?)        |      2493 (3011)      |      2493 (3011)      |
|      `(6, 6, 8)`       |       203        |       203       |       203       |       203        |          1994          |         1994          |         1994          |
|      `(6, 6, 9)`       |       225        |       225       |       225       |       225        |          2440          |         2440          |         2440          |
|      `(6, 6, 10)`      |     252 (?)      |     252 (?)     |       247       |     252 (?)      |           -            |           -           |           -           |
|      `(6, 6, 11)`      |     276 (?)      |     276 (?)     |       268       |     276 (?)      |           -            |           -           |           -           |
|      `(6, 6, 12)`      |     294 (?)      |     294 (?)     |       280       |     294 (?)      |           -            |           -           |           -           |
|      `(6, 6, 13)`      |     322 (?)      |     322 (?)     |       316       |     322 (?)      |           -            |           -           |           -           |
|      `(6, 6, 14)`      |     343 (?)      |     343 (?)     |       336       |     343 (?)      |           -            |           -           |           -           |
|      `(6, 6, 15)`      |     371 (?)      |     371 (?)     |       360       |     371 (?)      |           -            |           -           |           -           |
|      `(6, 6, 16)`      |     392 (?)      |     392 (?)     |       385       |     392 (?)      |           -            |           -           |           -           |
|      `(6, 7, 7)`       |    212 (215)     |    212 (215)    |    212 (215)    |    212 (215)     |      2320 (2004)       |      2320 (2004)      |      2320 (2004)      |
|      `(6, 7, 8)`       |    238 (239)     |    238 (239)    |    238 (239)    |    238 (239)     |      2644 (2352)       |      2644 (2352)      |      2644 (2352)      |
|      `(6, 7, 9)`       |    268 (270)     |    268 (270)    |    268 (270)    |    268 (270)     |      3059 (2917)       |      3059 (2917)      |      3059 (2917)      |
|      `(6, 7, 10)`      |     296 (?)      |       296       |    293 (296)    |       296        |           -            |           -           |           -           |
|      `(6, 7, 11)`      |     322 (?)      |     322 (?)     |       318       |     322 (?)      |           -            |           -           |           -           |
|      `(6, 7, 12)`      |     342 (?)      |     342 (?)     |       336       |     342 (?)      |           -            |           -           |           -           |
|      `(6, 7, 13)`      |     376 (?)      |     376 (?)     |       372       |     376 (?)      |           -            |           -           |           -           |
|      `(6, 7, 14)`      |     403 (?)      |     403 (?)     |       399       |     403 (?)      |           -            |           -           |           -           |
|      `(6, 7, 15)`      |     437 (?)      |     435 (?)     |       430       |     435 (?)      |           -            |           -           |           -           |
|      `(6, 7, 16)`      |     464 (?)      |     460 (?)     |       457       |     460 (?)      |           -            |           -           |           -           |
|      `(6, 8, 8)`       |       266        |       266       |       266       |       266        |          2780          |         2780          |         2780          |
|      `(6, 8, 9)`       |       296        |       296       |       296       |       296        |          3536          |         3536          |         3536          |
|      `(6, 8, 10)`      |     329 (?)      |       329       |       329       |       329        |        3914 (?)        |      3914 (4106)      |      3914 (4106)      |
|      `(6, 8, 11)`      |     357 (?)      |     357 (?)     |       357       |     357 (?)      |        6778 (?)        |       6778 (?)        |         5730          |
|      `(6, 8, 12)`      |     378 (?)      |     378 (?)     |       378       |     378 (?)      |        9084 (?)        |       9084 (?)        |         7140          |
|      `(6, 8, 13)`      |     418 (?)      |     418 (?)     |       414       |     418 (?)      |           -            |           -           |           -           |
|      `(6, 8, 14)`      |     448 (?)      |     448 (?)     |       441       |     448 (?)      |           -            |           -           |           -           |
|      `(6, 8, 15)`      |     486 (?)      |     484 (?)     |       480       |     484 (?)      |           -            |           -           |           -           |
|      `(6, 8, 16)`      |     518 (?)      |     511 (?)     |       511       |       511        |           -            |           -           |           -           |
|      `(6, 9, 9)`       |     342 (?)      |       342       |       342       |       342        |        3837 (?)        |      3837 (3969)      |      3837 (3969)      |
|      `(6, 9, 10)`      |     373 (?)      |       373       |       373       |       373        |        4374 (?)        |      4374 (4504)      |      4374 (4504)      |
|      `(6, 9, 11)`      |     410 (?)      |     407 (?)     |       407       |     407 (?)      |           -            |           -           |           -           |
|      `(6, 9, 12)`      |     435 (?)      |     434 (?)     |       434       |     434 (?)      |           -            |           -           |           -           |
|      `(6, 9, 13)`      |     477 (?)      |     476 (?)     |       474       |     476 (?)      |           -            |           -           |           -           |
|      `(6, 9, 14)`      |     512 (?)      |     508 (?)     |       500       |     508 (?)      |           -            |           -           |           -           |
|     `(6, 10, 10)`      |       406        |       406       |       406       |       406        |          4984          |         4984          |         4984          |
|     `(6, 10, 11)`      |     454 (?)      |       446       |       446       |       446        |           -            |           -           |           -           |
|     `(6, 10, 12)`      |     489 (?)      |       476       |       476       |       476        |           -            |           -           |           -           |
|     `(6, 11, 11)`      |     501 (?)      |     496 (?)     |       490       |     496 (?)      |           -            |           -           |           -           |
|      `(7, 7, 7)`       |     250 (?)      |     250 (?)     |       249       |     248 (?)      |           -            |           -           |           -           |
|      `(7, 7, 8)`       |     278 (?)      |     278 (?)     |       277       |     273 (?)      |           -            |           -           |           -           |
|      `(7, 7, 9)`       |     316 (?)      |    316 (318)    |       315       |    313 (318)     |           -            |           -           |           -           |
|      `(7, 7, 10)`      |     346 (?)      |       346       |    345 (346)    |       346        |           -            |           -           |           -           |
|      `(7, 7, 11)`      |     378 (?)      |     378 (?)     |       376       |     378 (?)      |           -            |           -           |           -           |
|      `(7, 7, 12)`      |     404 (?)      |     404 (?)     |       402       |     404 (?)      |           -            |           -           |           -           |
|      `(7, 7, 13)`      |     443 (?)      |     443 (?)     |       441       |     443 (?)      |           -            |           -           |           -           |
|      `(7, 7, 14)`      |     475 (?)      |     475 (?)     |       471       |     475 (?)      |           -            |           -           |           -           |
|      `(7, 7, 15)`      |     513 (?)      |     511 (?)     |       508       |     511 (?)      |           -            |           -           |           -           |
|      `(7, 7, 16)`      |     544 (?)      |     540 (?)     |       539       |     540 (?)      |           -            |           -           |           -           |
|      `(7, 8, 8)`       |     310 (?)      |     310 (?)     |       306       |     302 (?)      |           -            |           -           |           -           |
|      `(7, 8, 9)`       |     352 (?)      |     352 (?)     |       350       |     352 (?)      |           -            |           -           |           -           |
|      `(7, 8, 10)`      |     385 (?)      |       385       |       385       |       385        |        5040 (?)        |      5040 (5149)      |      5040 (5149)      |
|      `(7, 8, 11)`      |     423 (?)      |     423 (?)     |       423       |     423 (?)      |        6666 (?)        |       6666 (?)        |      6666 (9912)      |
|      `(7, 8, 12)`      |     454 (?)      |     454 (?)     |       454       |     454 (?)      |        7872 (?)        |       7872 (?)        |     7872 (12740)      |
|      `(7, 8, 13)`      |     498 (?)      |     498 (?)     |       496       |     498 (?)      |           -            |           -           |           -           |
|      `(7, 8, 14)`      |     532 (?)      |     532 (?)     |       529       |     532 (?)      |           -            |           -           |           -           |
|      `(7, 8, 15)`      |     574 (?)      |     572 (?)     |    570 (571)    |     572 (?)      |           -            |           -           |           -           |
|      `(7, 8, 16)`      |     606 (?)      |     603 (?)     |       603       |     603 (?)      |           -            |           -           |           -           |
|      `(7, 9, 9)`       |     399 (?)      |     399 (?)     |       398       |     399 (?)      |           -            |           -           |           -           |
|      `(7, 9, 10)`      |     437 (?)      |       437       |       437       |       437        |        5508 (?)        |      5508 (5563)      |      5508 (5563)      |
|      `(7, 9, 11)`      |     482 (?)      |     480 (?)     |       480       |     480 (?)      |           -            |           -           |           -           |
|      `(7, 9, 12)`      |     516 (?)      |     516 (?)     |       510       |     516 (?)      |           -            |           -           |           -           |
|      `(7, 9, 13)`      |     564 (?)      |     563 (?)     |       562       |     563 (?)      |           -            |           -           |           -           |
|      `(7, 9, 14)`      |     603 (?)      |     600 (?)     |       597       |     600 (?)      |           -            |           -           |           -           |
|     `(7, 10, 10)`      |       478        |       478       |       478       |       478        |          6237          |         6237          |         6237          |
|     `(7, 10, 11)`      |     530 (?)      |       526       |       526       |       526        |           -            |           -           |           -           |
|     `(7, 10, 12)`      |     570 (?)      |       564       |       564       |       564        |           -            |           -           |           -           |
|     `(7, 11, 11)`      |     584 (?)      |     580 (?)     |       577       |     580 (?)      |           -            |           -           |           -           |
|      `(8, 8, 8)`       |     343 (?)      |     343 (?)     |       336       |     329 (?)      |           -            |           -           |           -           |
|      `(8, 8, 9)`       |     391 (?)      |     391 (?)     |       388       |     391 (?)      |           -            |           -           |           -           |
|      `(8, 8, 10)`      |       427        |       427       |       427       |       427        |          6230          |         6230          |         6230          |
|      `(8, 8, 11)`      |     475 (?)      |     475 (?)     |       475       |     475 (?)      |        6694 (?)        |       6694 (?)        |     6694 (10748)      |
|      `(8, 8, 12)`      |     511 (?)      |     511 (?)     |       504       |     511 (?)      |           -            |           -           |           -           |
|      `(8, 8, 13)`      |     559 (?)      |     559 (?)     |       559       |     559 (?)      |        7915 (?)        |       7915 (?)        |     7915 (10930)      |
|      `(8, 8, 14)`      |       595        |       595       |       595       |       595        |          8646          |         8646          |         8646          |
|      `(8, 8, 15)`      |     639 (?)      |     639 (?)     |       635       |     639 (?)      |           -            |           -           |           -           |
|      `(8, 8, 16)`      |     672 (?)      |     672 (?)     |    671 (672)    |     672 (?)      |           -            |           -           |           -           |
|      `(8, 9, 9)`       |     435 (?)      |     435 (?)     |       430       |     435 (?)      |           -            |           -           |           -           |
|      `(8, 9, 10)`      |       487        |       487       |       487       |       487        |          6760          |         6760          |         6760          |
|      `(8, 9, 11)`      |     533 (?)      |     533 (?)     |       533       |     533 (?)      |        7211 (?)        |       7211 (?)        |     7211 (17331)      |
|      `(8, 9, 12)`      |     570 (?)      |     570 (?)     |       560       |     570 (?)      |           -            |           -           |           -           |
|      `(8, 9, 13)`      |     624 (?)      |       624       |       624       |       624        |        8534 (?)        |      8534 (8738)      |      8534 (8738)      |
|      `(8, 9, 14)`      |     666 (?)      |    666 (669)    |    666 (669)    |    666 (669)     |       13890 (?)        |         9919          |         9919          |
|     `(8, 10, 10)`      |       532        |       532       |       532       |       532        |          7508          |         7508          |         7508          |
|     `(8, 10, 11)`      |     588 (?)      |       588       |       588       |       588        |       10338 (?)        |     10338 (11133)     |     10338 (11133)     |
|     `(8, 10, 12)`      |     630 (?)      |       630       |       630       |       630        |       13068 (?)        |     13068 (14268)     |     13068 (14268)     |
|     `(8, 11, 11)`      |     646 (?)      |     646 (?)     |       641       |     646 (?)      |           -            |           -           |           -           |
|      `(9, 9, 9)`       |       498        |       498       |       498       |       498        |          6553          |         6553          |         6553          |
|      `(9, 9, 10)`      |     540 (?)      |     540 (?)     |       534       |     540 (?)      |           -            |           -           |           -           |
|      `(9, 9, 11)`      |     594 (?)      |     594 (?)     |       576       |     594 (?)      |           -            |           -           |           -           |
|      `(9, 9, 12)`      |     630 (?)      |     630 (?)     |       600       |     630 (?)      |           -            |           -           |           -           |
|      `(9, 9, 13)`      |     693 (?)      |     693 (?)     |       681       |     693 (?)      |           -            |           -           |           -           |
|      `(9, 9, 14)`      |     735 (?)      |     735 (?)     |       726       |     735 (?)      |           -            |           -           |           -           |
|     `(9, 10, 10)`      |     599 (?)      |    599 (600)    |    599 (600)    |    599 (600)     |       11007 (?)        |         10707         |         10707         |
|     `(9, 10, 11)`      |     661 (?)      |     661 (?)     |       651       |     661 (?)      |           -            |           -           |           -           |
|     `(9, 10, 12)`      |     702 (?)      |     702 (?)     |       684       |     702 (?)      |           -            |           -           |           -           |
|     `(9, 11, 11)`      |     721 (?)      |     721 (?)     |    715 (725)    |     721 (?)      |           -            |           -           |           -           |
|     `(10, 10, 10)`     |     651 (?)      |       651       |       651       |       651        |       11246 (?)        |     11246 (13502)     |     11246 (13502)     |
|     `(10, 10, 11)`     |     719 (?)      |       719       |       719       |       719        |       13524 (?)        |     13524 (18015)     |     13524 (18015)     |
|     `(10, 10, 12)`     |     770 (?)      |       770       |       770       |       770        |       15644 (?)        |     15644 (22088)     |     15644 (22088)     |
|     `(10, 11, 11)`     |     793 (?)      |       793       |       793       |       793        |       16182 (?)        |     16182 (20801)     |     16182 (20801)     |
|     `(11, 11, 11)`     |     873 (?)      |       873       |       873       |       873        |       18863 (?)        |     18863 (22946)     |     18863 (22946)     |

## License and Citation
This project is for research purposes. Please use the following citation when referencing this code or dataset in your academic work:

```bibtex
@article{perminov2025fast,
    title={Fast Matrix Multiplication via Ternary Meta Flip Graphs},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2511.20317},
    url={https://arxiv.org/abs/2511.20317},
    year={2025}
}
```

```bibtex
@article{perminov2025parallel,
    title={Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2512.13365},
    url={https://arxiv.org/abs/2512.13365},
    year={2025}
}
```

```bibtex
@article{perminov202558,
    title={A 58-Addition, Rank-23 Scheme for General 3x3 Matrix Multiplication},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2512.21980},
    url={https://arxiv.org/abs/2512.21980},
    year={2025}
}
```
