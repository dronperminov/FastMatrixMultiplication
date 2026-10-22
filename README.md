# FastMatrixMultiplication

[![arXiv:2606.02480](https://img.shields.io/badge/arXiv-2606.02480-b31b1b.svg)](https://arxiv.org/abs/2606.02480)
[![arXiv:2603.02398](https://img.shields.io/badge/arXiv-2603.02398-b31b1b.svg)](https://arxiv.org/abs/2603.02398)
[![arXiv:2512.21980](https://img.shields.io/badge/arXiv-2512.21980-b31b1b.svg)](https://arxiv.org/abs/2512.21980)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.13365-b31b1b.svg)](https://arxiv.org/abs/2512.13365)
[![arXiv:2511.20317](https://img.shields.io/badge/arXiv-2511.20317-b31b1b.svg)](https://arxiv.org/abs/2511.20317)

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `2x2x2` to `16x16x16`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`, focusing on all tensor shapes satisfying `max(n₁, n₂, n₃) ≤ 16`.

## Overview
This repository documents the search for fast matrix multiplication (FMM) schemes using a custom meta flip graph method. The search focuses on schemes that use only the
coefficients `-1`, `0`, and `1`, denoted as `ZT`. This constraint is significant for practical implementations where computational complexity and hardware efficiency are critical.

Key insight: several known optimal schemes originally found over the rationals (`Q`) or integers (`Z`) have been successfully rediscovered with minimal, ternary
coefficients. This can lead to more efficient and hardware-friendly implementations.

## Latest progress

For a detailed history of discoveries and improvements, see the [CHANGELOG.md](CHANGELOG.md).

## Publications

* [Meta Flip Graph meets Serendipitous Product: new Fast Matrix Multiplication results](https://arxiv.org/abs/2606.02480) (arxiv)
* [Fast Matrix Multiplication in Small Formats: Discovering New Schemes with an Open-Source Flip Graph Framework](https://arxiv.org/abs/2603.02398) (arxiv)
* [A 58-Addition, Rank-23 Scheme for General 3x3 Matrix Multiplication](https://arxiv.org/abs/2512.21980) (arxiv)
* [Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication](https://arxiv.org/abs/2512.13365) (arxiv)
* [Fast Matrix Multiplication via Ternary Meta Flip Graphs](https://arxiv.org/abs/2511.20317) (arxiv)

## Key results
- [New best ranks and rediscoveries](docs/results.md)
- [Rank comparison across rings](docs/ranks.md)
- [Additions reduction and leading coefficients](docs/additions.md)

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

| Source                              | Description                                                                                                                                                                                      |
|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FMM catalogue                       | The central repository for known fast matrix multiplication algorithms ([fmm.univ-lille.fr](https://fmm.univ-lille.fr)).                                                                         |
| MMC — Matrix Multiplication Catalog | Large catalog tracking history and fields, maintained by [@blacelle](https://github.com/blacelle) ([matmulcatalog](https://solven.eu/matmulcatalog)).                                            |
| Alpha Tensor                        | Schemes from DeepMind's AlphaTensor project ([https://github.com/google-deepmind/alphatensor/tree/main/algorithms](https://github.com/google-deepmind/alphatensor/tree/main/algorithms)).        |
| Alpha Evolve                        | Schemes from DeepMind's AlphaEvolve project ([mathematical_results.ipynb](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)). |
| Original Flip Graph                 | Foundational work by Jakob Moosbauer ([flips](https://github.com/jakobmoosbauer/flips/tree/main/solutions)).                                                                                     |
| Adaptive flip graph                 | Improved flip graph approach ([adap](https://github.com/Yamato-Arai/adap)).                                                                                                                      |
| Symmetric flip graph                | Flip graphs with symmetry ([symmetric-flips](https://github.com/jakobmoosbauer/symmetric-flips)).                                                                                                |
| Meta Flip Graph                     | Advanced flip graph techniques by M. Kauers et al. ([matrix-multiplication](https://github.com/mkauers/matrix-multiplication)).                                                                  |
| FMM Add Reduction                   | Work on additive reductions by [@werekorren](https://github.com/werekorren) ([fmm_add_reduction](https://github.com/werekorren/fmm_add_reduction/tree/main/algorithms)).                         |
| LITA                                | Local Improvements to Trilinear Aggregation by [@khoruzhii](https://github.com/khoruzhii) ([lita](https://github.com/khoruzhii/lita)).                                                           |
| fmm_schemes                         | New fast matrix multiplication schemes by [@MerlijnW70](https://github.com/MerlijnW70) ([fmm_schemes](https://github.com/MerlijnW70/fmm-schemes)).                                               |
| cloudroom-math                      | Cloudroom Math: new matrix multiplication algorithms found by AI agents by [@matyasstoch](https://github.com/matyasstoch) ([cloudroom-math](https://github.com/matyasstoch/cloudroom-math))      |
| mizopl                              | Near optimal ternary schemes from [@mizopl](https://github.com/mizopl)                                                                                                                           |

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
Reduced `(2, 2, 2: 7)` from 24 to 15 additions:
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
scheme.show_tensors()  # print the scheme in (a)*(b)*(c) format

# scheme saving
scheme.save("scheme.json")  # save in json format
scheme.save_maple("scheme.m")  # save in maple format
scheme.save_txt("scheme.txt")  # save in txt format
scheme.save_tensor_mpl("scheme.tensor.mpl")  # save in tensor.mpl format
```

## License and Citation
This project is for research purposes. Please use the following citation when referencing this code or dataset in your academic work:


```bibtex
@article{perminov2026meta,
    title={Meta Flip Graph meets Serendipitous Product: new Fast Matrix Multiplication results},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2606.02480},
    url={https://arxiv.org/abs/2606.02480},
    year={2026}
}
```

```bibtex
@article{perminov2026fast,
    title={Fast Matrix Multiplication in Small Formats: Discovering New Schemes with an Open-Source Flip Graph Framework},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2603.02398},
    url={https://arxiv.org/abs/2603.02398},
    year={2026}
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
@article{perminov2025fast,
    title={Fast Matrix Multiplication via Ternary Meta Flip Graphs},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2511.20317},
    url={https://arxiv.org/abs/2511.20317},
    year={2025}
}
```
