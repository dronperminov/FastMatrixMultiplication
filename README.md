# FastMatrixMultiplication

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `(2, 2, 2)` to `(10, 10, 10)`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`.

## Overview
This repository documents the search for fast matrix multiplication (FMM) schemes using a custom GPU-accelerated meta flip graph method. The search is conducted in the ternary
integer field (`ZT`), focusing on schemes that use only the coefficients `-1`, `0`, and `1`. This constraint is significant for practical implementations where computational
complexity and hardware efficiency are critical.

Key insight: I have successfully "rediscovered" several known optimal schemes originally found over the rationals (`Q`) or integers (`Z`), now providing them with minimal, ternary
coefficients. This can lead to more efficient and hardware-friendly implementations.

## Key results

### Conversions to ternary field (`ZT`)
I have discovered and converted the following schemes to the `ZT` field, which were previously known over rational (`Q`) or integer (`Z`) fields but lacked known ternary
implementations:

|    Format    | Rank | Note                      |
|:------------:|:----:|:--------------------------|
| `(2, 3, 5)`  |  25  | Previously known in `Z`   |
| `(2, 3, 10)` |  50  | Previously known in `Z`   |
| `(2, 4, 9)`  |  59  | Previously known in `Q`   |
| `(2, 5, 9)`  |  72  | Previously known in `Q`   |
| `(2, 6, 9)`  |  86  | Previously known in `Q/Z` |
| `(3, 4, 5)`  |  47  | Previously known in `Z`   |
| `(4, 4, 6)`  |  73  | Previously known in `Q/Z` |
| `(4, 4, 8)`  |  96  | Previously known in `Q`   |
| `(4, 5, 6)`  |  90  | Previously known in `Z`   |
| `(4, 5, 7)`  | 104  | Previously known in `Q/Z` |
| `(4, 5, 8)`  | 118  | Previously known in `Q/Z` |
| `(4, 5, 10)` | 151  | Previously known in `Z`   |
| `(4, 6, 7)`  | 123  | Previously known in `Q/Z` |
| `(5, 5, 6)`  | 110  | Previously known in `Q/Z` |
| `(5, 5, 7)`  | 127  | Previously known in `Q/Z` |
| `(5, 5, 8)`  | 144  | Previously known in `Q/Z` |
| `(5, 5, 9)`  | 167  | Previously known in `Z`   |
| `(5, 6, 6)`  | 130  | Previously known in `Q/Z` |
| `(5, 6, 7)`  | 150  | Previously known in `Q/Z` |
| `(5, 6, 9)`  | 197  | Previously known in `Z`   |

### New discoveries in binary field (`Z2`)

|    Format    | Prev<br/>rank | Curr<br/>rank | Best<br/>rank |
|:------------:|:-------------:|:-------------:|:-------------:|
| `(3, 3, 7)`  |      51       |      49       |  49 (in `Q`)  |
| `(3, 4, 10)` |      94       |      92       |  92 (in `Q`)  |
| `(3, 5, 7)`  |      80       |      79       |  79 (in `Q`)  |
| `(3, 8, 8)`  |      148      |      145      | 145 (in `Q`)  |
| `(4, 4, 5)`  |      61       |      60       | 61 (in `Q/Z`) |
| `(4, 4, 10)` |      122      |      120      | 120 (in `Q`)  |
| `(4, 5, 5)`  |      76       |      73       | 76 (in `Q/Z`) |
| `(4, 5, 6)`  |      90       |      89       | 90 (in `Q/Z`) |
| `(4, 5, 9)`  |       ?       |      133      | 136 (in `Q`)  |
| `(4, 5, 10)` |      151      |      146      | 151 (in `Q`)  |
| `(5, 5, 9)`  |      167      |      166      | 167 (in `Q`)  |
| `(5, 5, 10)` |      185      |      183      | 184 (in `Q`)  |


### Reduce naive addition complexity

The naive addition complexity - is the number of nonzero coefficients minus `2·rank + n·p`.

|   Format    | Rank | Previous<br/>complexity | Current<br/>complexity |
|:-----------:|:----:|:-----------------------:|:----------------------:|
| `(2, 4, 4)` |  26  |           130           |          122           |
| `(3, 3, 3)` |  23  |           98            |           88           |
| `(3, 4, 5)` |  47  |           293           |          277           |
| `(4, 4, 5)` |  61  |           455           |          452           |
| `(4, 4, 6)` |  73  |           740           |          540           |
| `(4, 4, 8)` |  96  |          1920           |          973           |
| `(4, 5, 5)` |  76  |           549           |          532           |
| `(4, 5, 7)` | 104  |          1354           |          927           |
| `(4, 6, 7)` | 123  |          1785           |          1586          |
| `(4, 7, 8)` | 164  |          1554           |          1522          |
| `(5, 5, 5)` |  93  |           846           |          843           |
| `(5, 5, 6)` | 110  |          1300           |          1215          |
| `(5, 5, 7)` | 127  |          1662           |          1606          |
| `(5, 5, 8)` | 144  |          1924           |          1908          |
| `(5, 6, 6)` | 130  |          1758           |          1716          |
| `(5, 6, 7)` | 150  |          2431           |          2039          |
| `(6, 6, 6)` | 153  |          2232           |          2171          |

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

| Source              | Description                                                                                                                                                                                      |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FMM catalogue       | The central repository for known fast matrix multiplication algorithms ([fmm.univ-lille.fr](https://fmm.univ-lille.fr)).                                                                         |
| Alpha Evolve        | Schemes from DeepMind's AlphaEvolve project ([mathematical_results.ipynb](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)). |
| Original Flip Graph | Foundational work by Jakob Moosbauer ([flips](https://github.com/jakobmoosbauer/flips/tree/main/solutions)).                                                                                     |
| Meta Flip Graph     | Advanced flip graph techniques by M. Kauers et al. ([matrix-multiplication](https://github.com/mkauers/matrix-multiplication)).                                                                  |
| FMM Add Reduction   | Work on additive reductions by @werekorren ([fmm_add_reduction](https://github.com/werekorren/fmm_add_reduction/tree/main/algorithms)).                                                          |


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
|      `(2, 3, 3)`       |        15        |       15        |       15        |        15        |           58           |          58           |          58           |
|      `(2, 3, 4)`       |        20        |       20        |       20        |        20        |           82           |          82           |          82           |
|      `(2, 3, 5)`       |      25 (?)      |       25        |       25        |        25        |        129 (?)         |        **108**        |        **108**        |
|      `(2, 3, 6)`       |        30        |       30        |       30        |        30        |          116           |          116          |          116          |
|      `(2, 3, 7)`       |        35        |       35        |       35        |        35        |          140           |          140          |          140          |
|      `(2, 3, 8)`       |        40        |       40        |       40        |        40        |          164           |          164          |          164          |
|      `(2, 3, 9)`       |        45        |       45        |       45        |        45        |          174           |          174          |          174          |
|      `(2, 3, 10)`      |      50 (?)      |       50        |       50        |        50        |        198 (?)         |       198 (254)       |       198 (254)       |
|      `(2, 4, 4)`       |        26        |       26        |       26        |        26        |       122 (130)        |       122 (130)       |       122 (130)       |
|      `(2, 4, 5)`       |      33 (?)      |       33        |     **32**      |        33        |           -            |           -           |           -           |
|      `(2, 4, 6)`       |      39 (?)      |     39 (?)      |     39 (?)      |        39        |        202 (?)         |        202 (?)        |        202 (?)        |
|      `(2, 4, 7)`       |        45        |       45        |       45        |        45        |          308           |          308          |          308          |
|      `(2, 4, 8)`       |        51        |       51        |       51        |        51        |          354           |          354          |          354          |
|      `(2, 4, 9)`       |      59 (?)      |     59 (?)      |       59        |      59 (?)      |        332 (?)         |        332 (?)        |       332 (379)       |
|      `(2, 4, 10)`      |      65 (?)      |     65 (?)      |     **64**      |      65 (?)      |           -            |           -           |           -           |
|      `(2, 5, 5)`       |        40        |       40        |       40        |        40        |          208           |          208          |          208          |
|      `(2, 5, 6)`       |        47        |       47        |       47        |        47        |          332           |          332          |          332          |
|      `(2, 5, 7)`       |      57 (?)      |     57 (?)      |     **55**      |      57 (?)      |           -            |           -           |           -           |
|      `(2, 5, 8)`       |      65 (?)      |     65 (?)      |     **63**      |      65 (?)      |           -            |           -           |           -           |
|      `(2, 5, 9)`       |      72 (?)      |     72 (?)      |       72        |      72 (?)      |        465 (?)         |        465 (?)        |       465 (565)       |
|      `(2, 5, 10)`      |      80 (?)      |     80 (?)      |     **79**      |      80 (?)      |           -            |           -           |           -           |
|      `(2, 6, 6)`       |      57 (?)      |     **56**      |     **56**      |      **56**      |           -            |           -           |           -           |
|      `(2, 6, 7)`       |      68 (?)      |     **66**      |     **66**      |      **66**      |           -            |           -           |           -           |
|      `(2, 6, 8)`       |      77 (?)      |     77 (?)      |     **75**      |      77 (?)      |           -            |           -           |           -           |
|      `(2, 6, 9)`       |      86 (?)      |       86        |       86        |        86        |        553 (?)         |       553 (691)       |       553 (691)       |
|      `(2, 6, 10)`      |        94        |       94        |       94        |        94        |          668           |          668          |          668          |
|      `(2, 7, 7)`       |      77 (?)      |     77 (?)      |     **76**      |      77 (?)      |           -            |           -           |           -           |
|      `(2, 7, 8)`       |      90 (?)      |     **88**      |     **88**      |      **88**      |           -            |           -           |           -           |
|      `(2, 7, 9)`       |     102 (?)      |     102 (?)     |     **99**      |     101 (?)      |           -            |           -           |           -           |
|      `(2, 8, 8)`       |       100        |       100       |       100       |       100        |          608           |          608          |          608          |
|      `(3, 3, 3)`       |        23        |       23        |       23        |        23        |        88 (98)         |        88 (98)        |        88 (98)        |
|      `(3, 3, 4)`       |        29        |       29        |       29        |        29        |          134           |          134          |          134          |
|      `(3, 3, 5)`       |        36        |       36        |       36        |        36        |          193           |          193          |          193          |
|      `(3, 3, 6)`       |      44 (?)      |       42        |     **40**      |        42        |           -            |           -           |           -           |
|      `(3, 3, 7)`       |      51 (?)      |     51 (?)      |     **49**      |    **49** (?)    |           -            |           -           |           -           |
|      `(3, 3, 8)`       |      58 (?)      |     58 (?)      |     **55**      |      57 (?)      |           -            |           -           |           -           |
|      `(3, 3, 9)`       |      65 (?)      |     65 (?)      |     **63**      |      64 (?)      |           -            |           -           |           -           |
|      `(3, 3, 10)`      |      72 (?)      |     72 (?)      |     **69**      |      71 (?)      |           -            |           -           |           -           |
|      `(3, 4, 4)`       |        38        |       38        |       38        |        38        |          192           |          192          |          192          |
|      `(3, 4, 5)`       |      47 (?)      |       47        |       47        |        47        |        277 (?)         |       277 (293)       |       277 (293)       |
|      `(3, 4, 6)`       |      57 (?)      |     **54**      |     **54**      |      **54**      |           -            |           -           |           -           |
|      `(3, 4, 7)`       |      66 (?)      |       64        |     **63**      |        64        |           -            |           -           |           -           |
|      `(3, 4, 8)`       |        74        |       74        |     **73**      |        74        |           -            |           -           |           -           |
|      `(3, 4, 9)`       |      85 (?)      |     85 (?)      |     **83**      |    **83** (?)    |           -            |           -           |           -           |
|      `(3, 4, 10)`      |      94 (?)      |     94 (?)      |     **92**      |    **92** (?)    |           -            |           -           |           -           |
|      `(3, 5, 5)`       |        58        |       58        |       58        |        58        |          357           |          357          |          357          |
|      `(3, 5, 6)`       |      70 (?)      |     **68**      |     **68**      |      **68**      |           -            |           -           |           -           |
|      `(3, 5, 7)`       |      83 (?)      |       80        |     **79**      |   **79** (80)    |           -            |           -           |           -           |
|      `(3, 5, 8)`       |      94 (?)      |     **90**      |     **90**      |      **90**      |           -            |           -           |           -           |
|      `(3, 5, 9)`       |     105 (?)      |     **104**     |     **104**     |     **104**      |           -            |           -           |           -           |
|      `(3, 5, 10)`      |     116 (?)      |     **115**     |     **115**     |     **115**      |           -            |           -           |           -           |
|      `(3, 6, 6)`       |      85 (?)      |     85 (?)      |     **80**      |     84 (86)      |           -            |           -           |           -           |
|      `(3, 6, 7)`       |     100 (?)      |     100 (?)     |     **94**      |      96 (?)      |           -            |           -           |           -           |
|      `(3, 6, 8)`       |     113 (?)      |     **108**     |     **108**     |     **108**      |           -            |           -           |           -           |
|      `(3, 6, 9)`       |     127 (?)      |     127 (?)     |     **120**     |     122 (?)      |           -            |           -           |           -           |
|      `(3, 6, 10)`      |     140 (?)      |     140 (?)     |     **134**     |     136 (?)      |           -            |           -           |           -           |
|      `(3, 7, 7)`       |     117 (?)      |     117 (?)     |     **111**     |     113 (?)      |           -            |           -           |           -           |
|      `(3, 7, 8)`       |     132 (?)      |     132 (?)     |     **126**     |     128 (?)      |           -            |           -           |           -           |
|      `(3, 7, 9)`       |     149 (?)      |     149 (?)     |     **142**     |     143 (?)      |           -            |           -           |           -           |
|      `(3, 8, 8)`       |     148 (?)      |     148 (?)     |     **145**     |   **145** (?)    |           -            |           -           |           -           |
|      `(4, 4, 4)`       |      49 (?)      |       49        |     **48**      |      **47**      |           -            |           -           |           -           |
|      `(4, 4, 5)`       |        61        |       61        |       61        |        60        |       452 (455)        |       452 (455)       |       452 (455)       |
|      `(4, 4, 6)`       |      73 (?)      |       73        |       73        |        73        |        540 (?)         |       540 (740)       |       540 (740)       |
|      `(4, 4, 7)`       |        85        |       85        |       85        |        85        |          631           |          631          |          631          |
|      `(4, 4, 8)`       |      96 (?)      |     96 (?)      |       96        |      94 (?)      |        973 (?)         |        973 (?)        |      973 (1920)       |
|      `(4, 4, 9)`       |     110 (?)      |     110 (?)     |     **104**     |     107 (?)      |           -            |           -           |           -           |
|      `(4, 4, 10)`      |     122 (?)      |     122 (?)     |     **120**     |   **120** (?)    |           -            |           -           |           -           |
|      `(4, 5, 5)`       |        76        |       76        |       76        |        73        |       532 (549)        |       532 (549)       |       532 (549)       |
|      `(4, 5, 6)`       |      90 (?)      |       90        |       90        |     89 (90)      |        1023 (?)        |        **775**        |        **775**        |
|      `(4, 5, 7)`       |     104 (?)      |       104       |       104       |       104        |        927 (?)         |      927 (1386)       |      927 (1354)       |
|      `(4, 5, 8)`       |    118 (122)     |       118       |       118       |       118        |       1521 (918)       |      1521 (918)       |      1521 (918)       |
|      `(4, 5, 9)`       |     137 (?)      |     137 (?)     |     **136**     |   **133** (?)    |           -            |           -           |           -           |
|      `(4, 5, 10)`      |     151 (?)      |       151       |       151       |    146 (151)     |        1218 (?)        |      1218 (1706)      |      1218 (1706)      |
|      `(4, 6, 6)`       |       105        |       105       |       105       |       105        |          894           |          894          |          894          |
|      `(4, 6, 7)`       |     123 (?)      |       123       |       123       |       123        |        1586 (?)        |      1586 (1798)      |      1586 (1785)      |
|      `(4, 6, 8)`       |       140        |       140       |       140       |       140        |          1248          |         1248          |         1248          |
|      `(4, 6, 9)`       |     162 (?)      |     162 (?)     |     **159**     |     160 (?)      |           -            |           -           |           -           |
|      `(4, 6, 10)`      |     178 (?)      |     **175**     |     **175**     |     **175**      |           -            |           -           |           -           |
|      `(4, 7, 7)`       |     148 (?)      |     **144**     |     **144**     |     **144**      |           -            |           -           |           -           |
|      `(4, 7, 8)`       |       164        |       164       |       164       |       164        |      1522 (1554)       |      1522 (1554)      |      1522 (1554)      |
|      `(4, 7, 9)`       |     189 (?)      |     189 (?)     |     **186**     |     187 (?)      |           -            |           -           |           -           |
|      `(4, 8, 8)`       |       182        |       182       |       182       |       182        |          1884          |         1884          |         1884          |
|      `(5, 5, 5)`       |        93        |       93        |       93        |        93        |       843 (846)        |       843 (846)       |       843 (846)       |
|      `(5, 5, 6)`       |     110 (?)      |       110       |       110       |       110        |        1215 (?)        |      1215 (1300)      |      1215 (1300)      |
|      `(5, 5, 7)`       |     127 (?)      |       127       |       127       |       127        |        1606 (?)        |      1606 (1662)      |      1606 (1662)      |
|      `(5, 5, 8)`       |     144 (?)      |       144       |       144       |       144        |        1908 (?)        |      1908 (2257)      |      1908 (1924)      |
|      `(5, 5, 9)`       |     167 (?)      |       167       |       167       |    166 (167)     |        1814 (?)        |      1814 (2220)      |      1814 (2220)      |
|      `(5, 5, 10)`      |     185 (?)      |     185 (?)     |     **184**     |   **183** (?)    |           -            |           -           |           -           |
|      `(5, 6, 6)`       |     130 (?)      |       130       |       130       |       130        |        1716 (?)        |      1716 (1766)      |      1716 (1758)      |
|      `(5, 6, 7)`       |     150 (?)      |       150       |       150       |       150        |        2039 (?)        |      2039 (2431)      |      2039 (2431)      |
|      `(5, 6, 8)`       |       176        |     **170**     |     **170**     |     **170**      |           -            |           -           |           -           |
|      `(5, 6, 9)`       |     197 (?)      |       197       |       197       |       197        |        2373 (?)        |      2373 (3049)      |      2373 (3049)      |
|      `(5, 6, 10)`      |     220 (?)      |     **218**     |     **218**     |     **218**      |           -            |           -           |           -           |
|      `(5, 7, 7)`       |     184 (?)      |     **176**     |     **176**     |     **176**      |           -            |           -           |           -           |
|      `(5, 7, 8)`       |     207 (?)      |     207 (?)     |     **205**     |     206 (?)      |           -            |           -           |           -           |
|      `(5, 7, 9)`       |     231 (?)      |     231 (?)     |     **229**     |     231 (?)      |           -            |           -           |           -           |
|      `(5, 8, 8)`       |       230        |       230       |       230       |       230        |          2842          |         2842          |         2842          |
|      `(6, 6, 6)`       |       153        |       153       |       153       |       153        |      2171 (2232)       |      2171 (2232)      |      2171 (2232)      |
|      `(6, 6, 7)`       |     185 (?)      |     **183**     |     **183**     |     **183**      |           -            |           -           |           -           |
|      `(6, 6, 8)`       |       203        |       203       |       203       |       203        |          1994          |         1994          |         1994          |
|      `(6, 6, 9)`       |       225        |       225       |       225       |       225        |          2440          |         2440          |         2440          |
|      `(6, 6, 10)`      |     258 (?)      |     258 (?)     |     **247**     |     258 (?)      |           -            |           -           |           -           |
|      `(6, 7, 7)`       |       215        |       215       |       215       |       215        |          2004          |         2004          |         2004          |
|      `(6, 7, 8)`       |       239        |       239       |       239       |       239        |          2352          |         2352          |         2352          |
|      `(6, 7, 9)`       |       270        |       270       |       270       |       270        |          2917          |         2917          |         2917          |
|      `(6, 8, 8)`       |       266        |       266       |       266       |       266        |          2780          |         2780          |         2780          |
|      `(7, 7, 7)`       |     261 (?)      |     261 (?)     |     **249**     |     261 (?)      |           -            |           -           |           -           |
|      `(7, 7, 8)`       |     292 (?)      |     292 (?)     |     **277**     |     288 (?)      |           -            |           -           |           -           |
|      `(7, 7, 9)`       |     332 (?)      |     332 (?)     |     **315**     |     332 (?)      |           -            |           -           |           -           |
|      `(7, 8, 8)`       |     328 (?)      |     328 (?)     |     **306**     |     328 (?)      |           -            |           -           |           -           |
|      `(8, 8, 8)`       |     364 (?)      |     364 (?)     |     **336**     |     364 (?)      |           -            |           -           |           -           |

## License and Citation
This project is for research purposes. Please cite the original sources for any algorithms used from the linked repositories.
