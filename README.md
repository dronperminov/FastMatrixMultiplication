# FastMatrixMultiplication

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `(2, 2, 2)` to `(8, 8, 8)`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`.

## Overview
This repository documents the search for fast matrix multiplication (FMM) schemes using a custom GPU-accelerated meta flip graph method. The search is conducted in the ternary
integer field (`ZT`), focusing on schemes that use only the coefficients `-1`, `0`, and `1`. This constraint is significant for practical implementations where computational
complexity and hardware efficiency are critical.

Key insight: I have successfully "rediscovered" several known optimal schemes originally found over the rationals (`Q`) or integers (`Z`), now providing them with minimal, ternary
coefficients. This can lead to more efficient and hardware-friendly implementations.

## Key results

### New discoveries in binary field (`Z2`)

| Format      | Previous<br/>rank | Current<br/>rank | Best <br/>rank |
|:------------|:-----------------:|:----------------:|:--------------:|
| `(3, 3, 7)` |        51         |        49        |  49 (in `Q`)   |
| `(3, 3, 8)` |         ?         |        58        |  55 (in `Q`)   |
| `(3, 5, 7)` |        80         |        79        |  79 (in `Q`)   |
| `(3, 6, 7)` |         ?         |        98        |  94 (in `Q`)   |
| `(3, 7, 7)` |         ?         |       116        |  111 (in `Q`)  |
| `(3, 7, 8)` |         ?         |       128        |  126 (in `Q`)  |
| `(3, 8, 8)` |        148        |       145        |  145 (in `Q`)  |
| `(4, 4, 8)` |        96         |        94        |  96 (in `Q`)   |
| `(4, 5, 6)` |        90         |        89        |  90 (in `Q`)   |
| `(5, 7, 8)` |         ?         |       207        |  205 (in `Q`)  |

### Conversions to ternary field (`ZT`)
I have discovered and converted the following schemes to the `ZT` field, which were previously known over rational (`Q`) or integer (`Z`) fields but lacked known ternary
implementations:

| Format      | Rank | Note                      |
|:------------|:----:|:--------------------------|
| `(2, 3, 5)` |  25  | Previously known in `Z`   |
| `(3, 4, 5)` |  47  | Previously known in `Z`   |
| `(4, 4, 6)` |  73  | Previously known in `Q/Z` |
| `(4, 4, 8)` |  96  | Previously known in `Q`   |
| `(4, 5, 6)` |  90  | Previously known in `Z`   |
| `(4, 5, 7)` | 104  | Previously known in `Q/Z` |
| `(4, 5, 8)` | 118  | Previously known in `Q/Z` |
| `(4, 6, 7)` | 123  | Previously known in `Q/Z` |
| `(5, 5, 6)` | 110  | Previously known in `Q/Z` |
| `(5, 5, 7)` | 127  | Previously known in `Q/Z` |
| `(5, 5, 8)` | 144  | Previously known in `Q/Z` |
| `(5, 6, 6)` | 130  | Previously known in `Q/Z` |
| `(5, 6, 7)` | 150  | Previously known in `Q/Z` |

## Methodology & instruments
The research employs a multi-stage approach using custom-built tools:

### [FlipGraphGPU](https://github.com/dronperminov/FlipGraphGPU): primary exploration tool
A high-performance instrument for exploring the fast matrix multiplication schemes using meta flip graph techniques, optimized for execution on NVIDIA GPUs in the ternary integer
field.

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

### Ternary Field Lifting
This script lifts binary (`Z2`) schemes to the ternary integer field (`ZT`, coefficients `{-1, 0, 1}`)
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

| Source                                     | Description                                                                                                                                                                                      |
|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FMM catalogue](https://fmm.univ-lille.fr) | The central repository for known fast matrix multiplication algorithms.                                                                                                                          |
| Alpha Evolve                               | Schemes from DeepMind's AlphaEvolve project ([mathematical_results.ipynb](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)). |
| Original Flip Graph                        | Foundational work by Jakob Moosbauer ([flips](https://github.com/jakobmoosbauer/flips/tree/main/solutions)).                                                                                     |
| Meta Flip Graph                            | Advanced flip graph techniques by M. Kauers et al. ([matrix-multiplication](https://github.com/mkauers/matrix-multiplication)).                                                                  |
| FMM Add Reduction                          | Work on additive reductions by @werekorren ([fmm_add_reduction](https://github.com/werekorren/fmm_add_reduction/tree/main/algorithms)).                                                          |


## Research Findings & Status

The table below summarizes the current state of researched matrix multiplication schemes. It highlights where ternary schemes (ZT) match or approximate the known minimal ranks
from other fields. The best ranks of previously known schemes are given in brackets.

|    size     | rank in `ZT`  | rank in `Z` | rank in `Q` |  rank in `Z2`   |
|:-----------:|:-------------:|:-----------:|:-----------:|:---------------:|
| `(2, 2, 2)` |     **7**     |    **7**    |    **7**    |      **7**      |
| `(2, 2, 3)` |    **11**     |   **11**    |   **11**    |     **11**      |
| `(2, 2, 4)` |    **14**     |   **14**    |   **14**    |     **14**      |
| `(2, 2, 5)` |    **18**     |   **18**    |   **18**    |     **18**      |
| `(2, 2, 6)` |    **21**     |   **21**    |   **21**    |     **21**      |
| `(2, 2, 7)` |    **25**     |   **25**    |   **25**    |     **25**      |
| `(2, 2, 8)` |    **28**     |   **28**    |   **28**    |     **28**      |
| `(2, 3, 3)` |    **15**     |   **15**    |   **15**    |     **15**      |
| `(2, 3, 4)` |    **20**     |   **20**    |   **20**    |     **20**      |
| `(2, 3, 5)` |  **25** (?)   |   **25**    |   **25**    |     **25**      |
| `(2, 3, 6)` |    **30**     |   **30**    |   **30**    |     **30**      |
| `(2, 3, 7)` |    **35**     |   **35**    |   **35**    |     **35**      |
| `(2, 3, 8)` |    **40**     |   **40**    |   **40**    |     **40**      |
| `(2, 4, 4)` |    **26**     |   **26**    |   **26**    |     **26**      |
| `(2, 4, 5)` |    33 (?)     |     33      |   **32**    |       33        |
| `(2, 4, 6)` |  **39** (?)   | **39** (?)  | **39** (?)  |     **39**      |
| `(2, 4, 7)` |    **45**     |   **45**    |   **45**    |     **45**      |
| `(2, 4, 8)` |    **51**     |   **51**    |   **51**    |     **51**      |
| `(2, 5, 5)` |    **40**     |   **40**    |   **40**    |     **40**      |
| `(2, 5, 6)` |    **47**     |   **47**    |   **47**    |     **47**      |
| `(2, 5, 7)` |    57 (?)     |   57 (?)    |   **55**    |     57 (?)      |
| `(2, 5, 8)` |    66 (?)     |   66 (?)    |   **63**    |     66 (?)      |
| `(2, 6, 6)` |    57 (?)     |   **56**    |   **56**    |     **56**      |
| `(2, 6, 7)` |    69 (?)     |   **66**    |   **66**    |     **66**      |
| `(2, 6, 8)` |    78 (?)     |   78 (?)    |   **75**    |     78 (?)      |
| `(2, 7, 7)` |    77 (?)     |   77 (?)    |   **76**    |     77 (?)      |
| `(2, 7, 8)` |    90 (?)     |   **88**    |   **88**    |     **88**      |
| `(2, 8, 8)` |    **100**    |   **100**   |   **100**   |     **100**     |
| `(3, 3, 3)` |    **23**     |   **23**    |   **23**    |     **23**      |
| `(3, 3, 4)` |    **29**     |   **29**    |   **29**    |     **29**      |
| `(3, 3, 5)` |    **36**     |   **36**    |   **36**    |     **36**      |
| `(3, 3, 6)` |    44 (?)     |     42      |   **40**    |       42        |
| `(3, 3, 7)` |    51 (?)     |   51 (?)    |   **49**    |   **49** (?)    |
| `(3, 3, 8)` |    58 (?)     |   58 (?)    |   **55**    |     58 (?)      |
| `(3, 4, 4)` |    **38**     |   **38**    |   **38**    |     **38**      |
| `(3, 4, 5)` |  **47** (?)   |   **47**    |   **47**    |     **47**      |
| `(3, 4, 6)` |    58 (?)     |   **54**    |   **54**    |     **54**      |
| `(3, 4, 7)` |    67 (?)     |     64      |   **63**    |       64        |
| `(3, 4, 8)` |      74       |     74      |   **73**    |       74        |
| `(3, 5, 5)` |    **58**     |   **58**    |   **58**    |     **58**      |
| `(3, 5, 6)` |    70 (?)     |   **68**    |   **68**    |     **68**      |
| `(3, 5, 7)` |    84 (?)     |     80      |   **79**    |   **79** (80)   |
| `(3, 5, 8)` |    94 (?)     |   **90**    |   **90**    |     **90**      |
| `(3, 6, 6)` |    85 (?)     |   85 (?)    |   **80**    |     84 (86)     |
| `(3, 6, 7)` |    101 (?)    |   101 (?)   |   **94**    |     98 (?)      |
| `(3, 6, 8)` |    116 (?)    |   **108**   |   **108**   |     **108**     |
| `(3, 7, 7)` |    119 (?)    |   119 (?)   |   **111**   |     116 (?)     |
| `(3, 7, 8)` |    133 (?)    |   133 (?)   |   **126**   |     128 (?)     |
| `(3, 8, 8)` |    148 (?)    |   148 (?)   |   **145**   |   **145** (?)   |
| `(4, 4, 4)` |    49 (?)     |     49      |   **48**    |     **47**      |
| `(4, 4, 5)` |    **61**     |   **61**    |   **61**    |     **60**      |
| `(4, 4, 6)` |  **73** (?)   |   **73**    |   **73**    |     **73**      |
| `(4, 4, 7)` |    **85**     |   **85**    |   **85**    |     **85**      |
| `(4, 4, 8)` |  **96** (?)   | **96** (?)  |   **96**    |   **94** (?)    |
| `(4, 5, 5)` |    **76**     |   **76**    |   **76**    |     **73**      |
| `(4, 5, 6)` |  **90** (?)   |   **90**    |   **90**    | **89** (**90**) |
| `(4, 5, 7)` |  **104** (?)  |   **104**   |   **104**   |     **104**     |
| `(4, 5, 8)` | **118** (122) |   **118**   |   **118**   |     **118**     |
| `(4, 6, 6)` |    **105**    |   **105**   |   **105**   |     **105**     |
| `(4, 6, 7)` |  **123** (?)  |   **123**   |   **123**   |     **123**     |
| `(4, 6, 8)` |    **140**    |   **140**   |   **140**   |     **140**     |
| `(4, 7, 7)` |    149 (?)    |   **144**   |   **144**   |     **144**     |
| `(4, 7, 8)` |    **164**    |   **164**   |   **164**   |     **164**     |
| `(4, 8, 8)` |    **182**    |   **182**   |   **182**   |     **182**     |
| `(5, 5, 5)` |    **93**     |   **93**    |   **93**    |     **93**      |
| `(5, 5, 6)` |  **110** (?)  |   **110**   |   **110**   |     **110**     |
| `(5, 5, 7)` |  **127** (?)  |   **127**   |   **127**   |     **127**     |
| `(5, 5, 8)` |  **144** (?)  |   **144**   |   **144**   |     **144**     |
| `(5, 6, 6)` |  **130** (?)  |   **130**   |   **130**   |     **130**     |
| `(5, 6, 7)` |  **150** (?)  |   **150**   |   **150**   |     **150**     |
| `(5, 6, 8)` |      176      |   **170**   |   **170**   |     **170**     |
| `(5, 7, 7)` |    185 (?)    |   **176**   |   **176**   |     **176**     |
| `(5, 7, 8)` |    208 (?)    |   208 (?)   |   **205**   |     207 (?)     |
| `(5, 8, 8)` |    **230**    |   **230**   |   **230**   |     **230**     |
| `(6, 6, 6)` |    **153**    |   **153**   |   **153**   |     **153**     |
| `(6, 6, 7)` |    185 (?)    |   **183**   |   **183**   |     **183**     |
| `(6, 6, 8)` |    **203**    |   **203**   |   **203**   |     **203**     |
| `(6, 7, 7)` |    **215**    |   **215**   |   **215**   |     **215**     |
| `(6, 7, 8)` |    **239**    |   **239**   |   **239**   |     **239**     |
| `(6, 8, 8)` |    **266**    |   **266**   |   **266**   |     **266**     |
| `(7, 7, 7)` |    281 (?)    |   281 (?)   |   **249**   |     281 (?)     |
| `(7, 7, 8)` |    302 (?)    |   302 (?)   |   **277**   |     302 (?)     |
| `(7, 8, 8)` |       ?       |      ?      |   **306**   |        ?        |
| `(8, 8, 8)` |       ?       |      ?      |   **336**   |        ?        |


## License and Citation
This project is for research purposes. Please cite the original sources for any algorithms used from the linked repositories.
