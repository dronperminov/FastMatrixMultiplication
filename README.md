# FastMatrixMultiplication

[![arXiv:2511.20317](https://img.shields.io/badge/arXiv-2511.20317-b31b1b.svg)](https://arxiv.org/abs/2511.20317)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.13365-b31b1b.svg)](https://arxiv.org/abs/2512.13365)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.21980-b31b1b.svg)](https://arxiv.org/abs/2512.21980)

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `(2, 2, 2)` to `(8, 8, 8)`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`, focusing on all tensor shapes satisfying `max(n₁n₂, n₂n₃, n₃n₁) ≤ 64` and `max(n₁, n₂, n₃) ≤ 16`.

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

|    Format    |  Prev rank  |  New rank  |
|:------------:|:-----------:|:----------:|
| `(2, 4, 9)`  |  59 (`Q`)   |  58 (`Q`)  |
| `(4, 4, 10)` |  120 (`Q`)  | 115 (`ZT`) |
| `(4, 4, 12)` |  142 (`Q`)  | 141 (`ZT`) |
| `(4, 4, 14)` |  165 (`Q`)  | 163 (`Q`)  |
| `(4, 4, 15)` |  177 (`Q`)  | 176 (`ZT`) |
| `(4, 4, 16)` |  189 (`Q`)  | 188 (`ZT`) |
| `(4, 5, 10)` |  151 (`Z`)  | 150 (`Q`)  |
| `(4, 5, 12)` |  180 (`Z`)  | 179 (`ZT`) |
| `(5, 6, 10)` |  218 (`Z`)  | 217 (`ZT`) |
| `(6, 7, 9)`  | 270 (`ZT`)  | 268 (`ZT`) |


### Rediscovery in the ternary coefficient set (`ZT`)
The following schemes have been rediscovered in the `ZT` format. Originally known over the rational (`Q`) or integer (`Z`) fields, implementations
with coefficients restricted to the ternary set were previously unknown.

|    Format    | Rank | Known ring |
|:------------:|:----:|:----------:|
| `(2, 3, 10)` |  50  |    `Z`     |
| `(2, 3, 13)` |  65  |    `Z`     |
| `(2, 3, 15)` |  75  |    `Z`     |
| `(2, 4, 6)`  |  39  |    `Z`     |
| `(2, 4, 11)` |  71  |    `Q`     |
| `(2, 4, 12)` |  77  |    `Q`     |
| `(2, 4, 15)` |  96  |    `Q`     |
| `(2, 5, 9)`  |  72  |    `Q`     |
| `(2, 6, 9)`  |  86  |    `Z`     |
| `(2, 7, 8)`  |  88  |    `Z`     |
| `(3, 3, 7)`  |  49  |    `Q`     |
| `(3, 3, 9)`  |  63  |    `Q`     |
| `(3, 4, 5)`  |  47  |    `Z`     |
| `(3, 4, 6)`  |  54  |   `Z/Q`    |
| `(3, 4, 9)`  |  83  |    `Q`     |
| `(3, 4, 10)` |  92  |    `Q`     |
| `(3, 4, 11)` | 101  |    `Q`     |
| `(3, 4, 12)` | 108  |    `Q`     |
| `(3, 4, 16)` | 146  |    `Q`     |
| `(3, 5, 10)` | 115  |    `Z`     |
| `(3, 6, 8)`  | 108  |   `Z/Q`    |
| `(4, 4, 6)`  |  73  |   `Z/Q`    |
| `(4, 4, 8)`  |  96  |    `Q`     |
| `(4, 4, 11)` | 130  |    `Q`     |
| `(4, 5, 6)`  |  90  |    `Z`     |
| `(4, 5, 7)`  | 104  |   `Z/Q`    |
| `(4, 5, 8)`  | 118  |   `Z/Q`    |
| `(4, 5, 11)` | 165  |    `Z`     |
| `(4, 6, 7)`  | 123  |   `Z/Q`    |
| `(4, 6, 9)`  | 159  |    `Q`     |
| `(4, 6, 10)` | 175  |    `Z`     |
| `(5, 5, 6)`  | 110  |   `Z/Q`    |
| `(5, 5, 7)`  | 127  |   `Z/Q`    |
| `(5, 5, 8)`  | 144  |   `Z/Q`    |
| `(5, 5, 9)`  | 167  |    `Z`     |
| `(5, 5, 10)` | 184  |    `Q`     |
| `(5, 5, 11)` | 202  |    `Q`     |
| `(5, 5, 12)` | 220  |    `Z`     |
| `(5, 6, 6)`  | 130  |   `Z/Q`    |
| `(5, 6, 7)`  | 150  |   `Z/Q`    |
| `(5, 6, 8)`  | 170  |   `Z/Q`    |
| `(5, 6, 9)`  | 197  |    `Z`     |
| `(5, 7, 7)`  | 176  |   `Z/Q`    |
| `(6, 6, 7)`  | 183  |   `Z/Q`    |


### Rediscovery in the integer ring (`Z`)
The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).
Implementations restricted to integer coefficients were previously unknown.

|    Format    | Rank |
|:------------:|:----:|
| `(2, 5, 7)`  |  55  |
| `(2, 5, 8)`  |  63  |
| `(2, 6, 8)`  |  75  |
| `(2, 7, 7)`  |  76  |
| `(3, 4, 8)`  |  73  |
| `(3, 5, 7)`  |  79  |
| `(3, 7, 7)`  | 111  |
| `(5, 7, 8)`  | 205  |
| `(5, 7, 9)`  | 229  |


### Reduce addition complexity
The following schemes have been optimized for addition count, achieving fewer operations than previously known through common subexpression elimination:

The results compare different approaches using the [fmm_add_reduction](https://github.com/werekorren/fmm_add_reduction) tool:
* `fmm gv` - greedy vanilla,
* `fmm gp (5 steps)` - greedy potential with default parameters `0 0.5 5`),
* `fmm gp (40 steps)` - greedy potential with parameters `0 0.5 40`).

|    Format    |        Rank        | Best known | Naive | fmm<br>gv | fmm gp<br>5 steps | fmm gp<br>40 steps |  Proposed  | Saved | Improved (%) |
|:------------:|:------------------:|:----------:|:-----:|:---------:|:-----------------:|:------------------:|:----------:|:-----:|:------------:|
| `(2, 2, 2)`  |         7          |     15     |  24   |    15     |        15         |         15         |     15     |   9   |     37.5     |
| `(2, 2, 3)`  |         11         |     31     |  20   |    20     |        20         |         20         |     20     |   0   |     0.0      |
| `(2, 2, 4)`  |         14         |     65     |  36   |    31     |        31         |         31         |     31     |   5   |     13.9     |
| `(2, 2, 5)`  |         18         |     77     |  38   |    33     |        33         |         33         |     33     |   5   |     13.2     |
| `(2, 2, 6)`  |         21         |     ?      |  54   |    44     |        44         |         44         |     44     |  10   |     18.5     |
| `(2, 2, 7)`  |         25         |     ?      |  56   |    46     |        46         |         46         |     46     |  10   |     17.9     |
| `(2, 2, 8)`  |         28         |     ?      |  72   |    57     |        57         |         57         |     57     |  15   |     20.8     |
| `(2, 2, 9)`  |         32         |     ?      |  74   |    59     |        59         |         59         |     59     |  15   |     20.3     |
| `(2, 2, 10)` |         35         |     ?      |  90   |    70     |        70         |         70         |     70     |  20   |     22.2     |
| `(2, 2, 11)` |         39         |     ?      |  92   |    72     |        72         |         72         |     72     |  20   |     21.7     |
| `(2, 2, 12)` |         42         |     ?      |  108  |    83     |        83         |         83         |     83     |  25   |     23.1     |
| `(2, 2, 13)` |         46         |     ?      |  110  |    85     |        85         |         85         |     85     |  25   |     22.7     |
| `(2, 2, 14)` |         49         |     ?      |  126  |    96     |        96         |         96         |     96     |  30   |     23.8     |
| `(2, 2, 15)` |         53         |     ?      |  128  |    98     |        98         |         98         |     98     |  30   |     23.4     |
| `(2, 2, 16)` |         56         |     ?      |  144  |    109    |        109        |        109         |    109     |  35   |     24.3     |
| `(2, 3, 3)`  |         15         |     48     |  58   |    46     |        46         |         46         |     46     |  12   |     20.7     |
| `(2, 3, 4)`  |         20         |     99     |  82   |    58     |        58         |         58         |     58     |  24   |     29.3     |
| `(2, 3, 5)`  |         25         |    103     |  110  |    72     |      **71**       |       **71**       |   **71**   |  39   |     35.5     |
| `(2, 3, 6)`  |         30         |     ?      |  116  |    81     |        81         |         81         |     81     |  35   |     30.2     |
| `(2, 3, 7)`  |         35         |     ?      |  140  |    100    |      **99**       |       **99**       |   **99**   |  41   |     29.3     |
| `(2, 3, 8)`  |         40         |     ?      |  164  |    104    |        104        |        104         |    104     |  60   |     36.6     |
| `(2, 3, 9)`  |         45         |     ?      |  174  |    116    |        116        |        116         |    116     |  58   |     33.3     |
| `(2, 3, 10)` |         50         |     ?      |  198  |    135    |        135        |        135         |  **134**   |  64   |     32.3     |
| `(2, 3, 11)` |         55         |     ?      |  222  |    146    |      **145**      |      **145**       |  **145**   |  77   |     34.7     |
| `(2, 3, 12)` |         60         |     ?      |  232  |    151    |        151        |        151         |    151     |  81   |     34.9     |
| `(2, 3, 13)` |         65         |     ?      |  256  |    170    |        170        |        170         |  **169**   |  87   |     34.0     |
| `(2, 3, 14)` |         70         |     ?      |  280  |    181    |      **180**      |      **180**       |  **180**   |  100  |     35.7     |
| `(2, 3, 15)` |         75         |     ?      |  307  |    192    |        192        |        192         |    192     |  115  |     37.5     |
| `(2, 3, 16)` |         80         |     ?      |  328  |    196    |        196        |        196         |    196     |  132  |     40.2     |
| `(2, 4, 4)`  |         26         |    173     |  130  |    93     |      **92**       |       **92**       |   **92**   |  38   |     29.2     |
| `(2, 4, 5)`  | 33 (near optimal)  |    172     |  184  |    114    |      **112**      |      **112**       |  **112**   |  72   |     39.1     |
| `(2, 4, 6)`  |         39         |     ?      |  202  |    138    |      **136**      |      **136**       |  **136**   |  66   |     32.7     |
| `(2, 4, 7)`  |         45         |     ?      |  308  |    181    |        178        |        177         |  **174**   |  134  |     43.5     |
| `(2, 4, 8)`  |         51         |     ?      |  354  |    197    |        191        |        190         |  **188**   |  166  |     46.9     |
| `(2, 4, 9)`  |         59         |     ?      |  309  |    210    |        208        |        208         |  **207**   |  102  |     33.0     |
| `(2, 4, 10)` | 65 (near optimal)  |     ?      |  340  |    223    |      **222**      |      **222**       |  **222**   |  118  |     34.7     |
| `(2, 4, 11)` |         71         |     ?      |  430  |    275    |        271        |        268         |  **265**   |  165  |     38.4     |
| `(2, 4, 12)` |         77         |     ?      |  484  |    282    |        277        |        276         |  **274**   |  210  |     43.4     |
| `(2, 4, 13)` | 84 (near optimal)  |     ?      |  595  |    323    |        316        |        316         |  **313**   |  282  |     47.4     |
| `(2, 4, 14)` |         90         |     ?      |  616  |    326    |        320        |        318         |  **313**   |  303  |     49.2     |
| `(2, 4, 15)` |         96         |     ?      |  662  |    366    |        358        |        357         |  **351**   |  311  |     47.0     |
| `(2, 4, 16)` |        102         |     ?      |  708  |    352    |        344        |        342         |  **338**   |  370  |     52.3     |
| `(2, 5, 5)`  |         40         |    313     |  283  |    156    |        154        |        154         |  **153**   |  130  |     45.9     |
| `(2, 5, 6)`  |         47         |     ?      |  332  |    189    |        186        |        184         |  **181**   |  151  |     45.5     |
| `(2, 5, 7)`  | 57 (near optimal)  |     ?      |  340  |    197    |        194        |        192         |  **189**   |  151  |     44.4     |
| `(2, 5, 8)`  | 65 (near optimal)  |     ?      |  376  |    222    |        218        |        218         |  **214**   |  162  |     43.1     |
| `(2, 5, 9)`  |         72         |     ?      |  465  |    275    |        270        |        270         |  **266**   |  199  |     42.8     |
| `(2, 5, 10)` | 80 (near optimal)  |     ?      |  416  |    275    |      **273**      |      **273**       |  **273**   |  143  |     34.4     |
| `(2, 5, 11)` |         87         |     ?      |  540  |    331    |        326        |        326         |  **323**   |  217  |     40.2     |
| `(2, 5, 12)` |         94         |     ?      |  664  |    336    |        330        |        328         |  **322**   |  342  |     51.5     |
| `(2, 6, 6)`  | 57 (near optimal)  |     ?      |  326  |    231    |      **228**      |      **228**       |  **228**   |  98   |     30.1     |
| `(2, 6, 7)`  | 68 (near optimal)  |     ?      |  396  |    233    |        230        |        230         |  **226**   |  170  |     42.9     |
| `(2, 6, 8)`  | 77 (near optimal)  |     ?      |  456  |    272    |        269        |        269         |  **266**   |  190  |     41.7     |
| `(2, 6, 9)`  |         86         |     ?      |  548  |    302    |        296        |        295         |  **293**   |  255  |     46.5     |
| `(2, 6, 10)` |         94         |     ?      |  668  |    334    |        327        |        327         |  **325**   |  343  |     51.3     |
| `(2, 7, 7)`  | 77 (near optimal)  |     ?      |  452  |    323    |      **320**      |      **320**       |  **320**   |  132  |     29.2     |
| `(2, 7, 8)`  | 90 (near optimal)  |     ?      |  648  |    350    |        333        |        331         |  **329**   |  319  |     49.2     |
| `(2, 7, 9)`  | 102 (near optimal) |     ?      |  678  |    398    |        384        |        382         |  **379**   |  299  |     44.1     |
| `(2, 8, 8)`  |        100         |     ?      |  608  |    427    |      **424**      |      **424**       |  **424**   |  184  |     30.3     |
| `(3, 3, 3)`  |         23         |     60     |  119  |    58     |        58         |         58         |   **58**   |  61   |     51.3     |
| `(3, 3, 4)`  |         29         |    105     |  134  |    93     |      **92**       |       **92**       |   **92**   |  42   |     31.3     |
| `(3, 3, 5)`  |         36         |    176     |  193  |    125    |      **123**      |      **123**       |  **123**   |  70   |     36.3     |
| `(3, 3, 6)`  | 43 (near optimal)  |     ?      |  284  |    168    |        164        |        164         |  **160**   |  124  |     43.7     |
| `(3, 3, 7)`  | 51 (near optimal)  |     ?      |  279  |    155    |      **154**      |      **154**       |  **154**   |  125  |     44.8     |
| `(3, 3, 8)`  | 58 (near optimal)  |     ?      |  275  |    170    |      **169**      |      **169**       |  **169**   |  106  |     38.5     |
| `(3, 3, 9)`  | 65 (near optimal)  |     ?      |  347  |    218    |        216        |        216         |  **215**   |  132  |     38.0     |
| `(3, 3, 10)` | 72 (near optimal)  |     ?      |  386  |    217    |      **214**      |      **214**       |  **214**   |  172  |     44.6     |
| `(3, 3, 11)` | 79 (near optimal)  |     ?      |  493  |    296    |        287        |      **286**       |  **286**   |  207  |     42.0     |
| `(3, 3, 12)` | 86 (near optimal)  |     ?      |  582  |    303    |        297        |        297         |  **289**   |  293  |     50.3     |
| `(3, 3, 13)` | 94 (near optimal)  |     ?      |  593  |    341    |        335        |      **334**       |  **334**   |  259  |     43.7     |
| `(3, 3, 14)` | 101 (near optimal) |     ?      |  664  |    373    |        365        |        363         |  **361**   |  303  |     45.6     |
| `(3, 3, 15)` | 108 (near optimal) |     ?      |  579  |    309    |      **305**      |      **305**       |  **305**   |  274  |     47.3     |
| `(3, 3, 16)` | 115 (near optimal) |     ?      |  862  |    424    |        410        |      **407**       |  **407**   |  455  |     52.8     |
| `(3, 4, 4)`  |         38         |    198     |  194  |    136    |      **133**      |      **133**       |  **133**   |  61   |     31.4     |
| `(3, 4, 5)`  |         47         |    276     |  277  |    170    |      **161**      |      **161**       |  **161**   |  116  |     41.9     |
| `(3, 4, 6)`  | 56 (near optimal)  |    319     |  359  |    211    |        210        |        210         |  **209**   |  150  |     41.8     |
| `(3, 4, 7)`  | 64 (near optimal)  |     ?      |  446  |    252    |        251        |      **249**       |  **249**   |  197  |     44.2     |
| `(3, 4, 8)`  | 74 (near optimal)  |     ?      |  461  |    272    |      **267**      |      **267**       |  **267**   |  194  |     42.1     |
| `(3, 4, 9)`  | 84 (near optimal)  |     ?      |  535  |    324    |        317        |      **316**       |  **316**   |  219  |     40.9     |
| `(3, 4, 10)` | 93 (near optimal)  |     ?      |  582  |    351    |        346        |        346         |  **345**   |  237  |     40.7     |
| `(3, 4, 11)` | 102 (near optimal) |     ?      |  641  |    387    |        384        |      **381**       |  **381**   |  260  |     40.6     |
| `(3, 4, 12)` | 111 (near optimal) |     ?      |  721  |    424    |        412        |      **411**       |  **411**   |  310  |     43.0     |
| `(3, 4, 13)` | 121 (near optimal) |     ?      |  804  |    471    |        456        |      **455**       |  **455**   |  349  |     43.4     |
| `(3, 4, 14)` | 128 (near optimal) |     ?      |  896  |    466    |        460        |      **458**       |  **458**   |  438  |     48.9     |
| `(3, 4, 15)` | 138 (near optimal) |     ?      |  958  |    544    |        537        |        535         |  **533**   |  425  |     44.4     |
| `(3, 4, 16)` | 148 (near optimal) |     ?      | 1043  |    532    |      **518**      |      **518**       |  **518**   |  525  |     50.3     |
| `(3, 5, 5)`  |         58         |    326     |  357  |    230    |        224        |        223         |  **221**   |  136  |     38.1     |
| `(3, 5, 6)`  | 70 (near optimal)  |     ?      |  561  |    270    |        267        |        267         |  **265**   |  296  |     52.8     |
| `(3, 5, 7)`  | 83 (near optimal)  |     ?      |  494  |    315    |        308        |        305         |  **303**   |  191  |     38.7     |
| `(3, 5, 8)`  | 94 (near optimal)  |     ?      |  584  |    295    |        295        |        295         |    295     |  289  |     49.5     |
| `(3, 5, 9)`  | 105 (near optimal) |     ?      |  646  |    390    |        384        |        384         |  **383**   |  263  |     40.7     |
| `(3, 5, 10)` |        115         |     ?      |  730  |    391    |      **380**      |      **380**       |  **380**   |  350  |     47.9     |
| `(3, 5, 11)` | 128 (near optimal) |     ?      |  967  |    497    |        489        |        488         |  **484**   |  483  |     49.9     |
| `(3, 5, 12)` | 140 (near optimal) |     ?      | 1152  |    491    |        483        |        483         |  **482**   |  670  |     58.2     |
| `(3, 6, 6)`  | 85 (near optimal)  |     ?      |  998  |    367    |        364        |        359         |  **352**   |  646  |     64.7     |
| `(3, 6, 7)`  | 100 (near optimal) |     ?      |  704  |    364    |        352        |        351         |  **350**   |  354  |     50.3     |
| `(3, 6, 8)`  | 113 (near optimal) |     ?      | 1240  |    467    |        459        |        446         |  **445**   |  795  |     64.1     |
| `(3, 6, 9)`  | 127 (near optimal) |     ?      | 1095  |    519    |        502        |        493         |  **489**   |  606  |     55.3     |
| `(3, 6, 10)` | 140 (near optimal) |     ?      | 1152  |    494    |        484        |        477         |  **476**   |  676  |     58.7     |
| `(3, 7, 7)`  | 115 (near optimal) |     ?      |  789  |    441    |        434        |        434         |  **432**   |  357  |     45.2     |
| `(3, 7, 8)`  | 128 (near optimal) |     ?      |  930  |    462    |      **450**      |      **450**       |  **450**   |  480  |     51.6     |
| `(3, 7, 9)`  | 147 (near optimal) |     ?      | 1002  |    592    |        583        |        580         |  **579**   |  423  |     42.2     |
| `(3, 8, 8)`  | 148 (near optimal) |     ?      | 1020  |    519    |      **511**      |      **511**       |  **511**   |  509  |     49.9     |
| `(4, 4, 4)`  | 49 (near optimal)  |    325     |  474  |    167    |        164        |        163         |  **159**   |  315  |     66.5     |
| `(4, 4, 5)`  |         61         |     ?      |  452  |    247    |        237        |        237         |  **233**   |  219  |     48.5     |
| `(4, 4, 6)`  |         73         |     ?      |  540  |    288    |        282        |        281         |  **280**   |  260  |     48.1     |
| `(4, 4, 7)`  |         85         |     ?      |  631  |    326    |        323        |        320         |  **319**   |  312  |     49.4     |
| `(4, 4, 8)`  |         96         |     ?      |  973  |    396    |        391        |        387         |  **377**   |  596  |     61.3     |
| `(4, 4, 9)`  | 110 (near optimal) |     ?      |  925  |    445    |        424        |        422         |  **419**   |  506  |     54.7     |
| `(4, 4, 10)` | 122 (near optimal) |     ?      |  879  |    493    |        482        |        482         |  **480**   |  399  |     45.4     |
| `(4, 4, 11)` | 134 (near optimal) |     ?      | 1150  |    534    |        528        |        524         |  **519**   |  631  |     54.9     |
| `(4, 4, 12)` | 145 (near optimal) |     ?      | 1495  |    619    |        606        |        596         |  **590**   |  905  |     60.5     |
| `(4, 4, 13)` | 157 (near optimal) |     ?      | 1474  |    650    |        638        |        635         |  **628**   |  846  |     57.4     |
| `(4, 4, 14)` | 169 (near optimal) |     ?      | 1596  |    711    |        702        |        694         |  **691**   |  905  |     56.7     |
| `(4, 4, 15)` | 181 (near optimal) |     ?      | 1679  |    741    |        738        |        735         |  **729**   |  950  |     56.6     |
| `(4, 4, 16)` | 192 (near optimal) |     ?      | 2059  |    730    |        728        |        724         |  **718**   | 1341  |     65.1     |
| `(4, 5, 5)`  |         76         |    451     |  530  |    315    |        300        |      **299**       |  **299**   |  231  |     43.6     |
| `(4, 5, 6)`  |         90         |     ?      | 1023  |    401    |        393        |        386         |  **380**   |  643  |     62.9     |
| `(4, 5, 7)`  |        104         |     ?      |  931  |    423    |        413        |        405         |  **400**   |  531  |     57.0     |
| `(4, 5, 8)`  |        118         |     ?      | 1521  |    543    |        538        |        522         |  **513**   | 1008  |     66.3     |
| `(4, 5, 9)`  | 137 (near optimal) |     ?      | 1217  |    564    |        555        |        547         |  **542**   |  675  |     55.5     |
| `(4, 5, 10)` |        151         |     ?      | 1207  |    590    |        580        |        571         |  **566**   |  641  |     53.1     |
| `(4, 5, 11)` |        165         |     ?      | 1801  |    718    |        702        |        689         |  **681**   | 1120  |     62.2     |
| `(4, 5, 12)` |        179         |     ?      | 1977  |    778    |        772        |        761         |  **750**   | 1227  |     62.1     |
| `(4, 6, 6)`  |        105         |     ?      |  894  |    467    |        435        |        435         |  **430**   |  464  |     51.9     |
| `(4, 6, 7)`  |        123         |     ?      | 1586  |    535    |        533        |        518         |  **517**   | 1069  |     67.4     |
| `(4, 6, 8)`  |        140         |     ?      | 1248  |    576    |        558        |        558         |  **551**   |  697  |     55.8     |
| `(4, 6, 9)`  | 160 (near optimal) |     ?      | 1472  |    720    |        651        |        647         |  **646**   |  826  |     56.1     |
| `(4, 6, 10)` |        175         |     ?      | 1878  |    759    |        738        |        723         |  **715**   | 1163  |     61.9     |
| `(4, 7, 7)`  | 145 (near optimal) |     ?      | 1381  |    680    |        646        |        632         |  **629**   |  752  |     54.5     |
| `(4, 7, 8)`  |        164         |     ?      | 1505  |    752    |        729        |        698         |  **690**   |  815  |     54.2     |
| `(4, 7, 9)`  | 187 (near optimal) |     ?      | 2059  |    806    |        800        |        788         |  **785**   | 1274  |     61.9     |
| `(4, 8, 8)`  |        182         |     ?      | 1884  |    861    |        812        |        800         |  **795**   | 1089  |     57.8     |
| `(5, 5, 5)`  |         93         |     ?      |  843  |    392    |        391        |        387         |  **383**   |  460  |     54.6     |
| `(5, 5, 6)`  |        110         |     ?      | 1215  |    491    |        479        |        466         |  **460**   |  755  |     62.1     |
| `(5, 5, 7)`  |        127         |     ?      | 1607  |    561    |        553        |        539         |  **531**   | 1076  |     67.0     |
| `(5, 5, 8)`  |        144         |     ?      | 1924  |    645    |        638        |        631         |  **620**   | 1304  |     67.8     |
| `(5, 5, 9)`  |        167         |     ?      | 1814  |    706    |        699        |        690         |  **682**   | 1132  |     62.4     |
| `(5, 5, 10)` |        184         |     ?      | 2116  |    796    |        787        |        781         |  **774**   | 1342  |     63.4     |
| `(5, 5, 11)` |        202         |     ?      | 2272  |    879    |        872        |        859         |  **850**   | 1422  |     62.6     |
| `(5, 5, 12)` |        220         |     ?      | 2444  |    848    |        835        |        811         |  **799**   | 1645  |     67.3     |
| `(5, 6, 6)`  |        130         |     ?      | 1716  |    589    |        587        |        573         |  **562**   | 1154  |     67.2     |
| `(5, 6, 7)`  |        150         |     ?      | 2039  |    696    |        691        |        671         |  **664**   | 1375  |     67.4     |
| `(5, 6, 8)`  |        170         |     ?      | 2312  |    747    |        740        |        728         |  **720**   | 1592  |     68.9     |
| `(5, 6, 9)`  |        197         |     ?      | 2376  |    884    |        875        |        850         |  **840**   | 1536  |     64.6     |
| `(5, 6, 10)` |        217         |     ?      | 2772  |    956    |        954        |        940         |  **925**   | 1847  |     66.6     |
| `(5, 7, 7)`  |        176         |     ?      | 2605  |    832    |        820        |        799         |  **788**   | 1817  |     69.8     |
| `(5, 7, 8)`  | 206 (near optimal) |     ?      | 1880  |    948    |        892        |        882         |  **879**   | 1001  |     53.2     |
| `(5, 7, 9)`  | 231 (near optimal) |     ?      | 2554  |    993    |        981        |        971         |  **963**   | 1591  |     62.3     |
| `(5, 8, 8)`  |        230         |     ?      | 2747  |   1019    |       1010        |        980         |  **974**   | 1773  |     64.5     |
| `(6, 6, 6)`  |        153         |     ?      | 2182  |    704    |        685        |        671         |  **655**   | 1527  |     70.0     |
| `(6, 6, 7)`  |        183         |     ?      | 2502  |    810    |        790        |        777         |  **769**   | 1733  |     69.3     |
| `(6, 6, 8)`  |        203         |     ?      | 1994  |    896    |        880        |        868         |  **836**   | 1158  |     58.1     |
| `(6, 6, 9)`  |        225         |     ?      | 2440  |   1029    |        951        |        936         |  **923**   | 1517  |     62.2     |
| `(6, 6, 10)` | 252 (near optimal) |     ?      | 3540  |   1291    |       1249        |      **1167**      |    1210    | 2330  |     65.8     |
| `(6, 7, 7)`  |        215         |     ?      | 2004  |    965    |        900        |        886         |  **880**   | 1124  |     56.1     |
| `(6, 7, 8)`  |        239         |     ?      | 2263  |   1112    |       1050        |        1042        |  **1027**  | 1236  |     54.6     |
| `(6, 7, 9)`  |        268         |     ?      | 3062  |   1184    |       1166        |        1152        |  **1146**  | 1916  |     62.6     |
| `(6, 8, 8)`  |        266         |     ?      | 2780  |   1244    |       1214        |        1181        |  **1161**  | 1619  |     58.2     |
| `(7, 7, 7)`  | 250 (near optimal) |     ?      | 2417  |   1119    |       1077        |        1070        |  **1067**  | 1350  |     55.9     |
| `(7, 7, 8)`  | 279 (near optimal) |     ?      | 2926  |   1369    |       1260        |        1248        |  **1237**  | 1689  |     57.7     |
| `(7, 7, 9)`  | 316 (near optimal) |     ?      | 3452  |   1460    |       1404        |        1385        |  **1383**  | 2069  |     59.9     |
| `(7, 8, 8)`  | 310 (near optimal) |     ?      | 3604  |   1670    |       1498        |      **1471**      |    1494    | 2110  |     58.5     |
| `(8, 8, 8)`  | 343 (near optimal) |     ?      | 4434  |   1748    |       1709        |        1668        |  **1661**  | 2773  |     62.5     |

### New discoveries in binary field (`Z2`)
New schemes have been discovered that improve the state-of-the-art for matrix multiplication in the binary field (`Z2`),
achieving lower ranks than previously known.

|    Format    | Prev rank | New rank |
|:------------:|:---------:|:--------:|
| `(4, 4, 8)`  |    96     |    94    |
| `(4, 4, 10)` |    120    |   118    |
| `(4, 4, 12)` |    142    |   141    |
| `(4, 4, 16)` |    189    |   188    |
| `(4, 5, 6)`  |    90     |    89    |
| `(4, 5, 9)`  |    136    |   133    |
| `(4, 5, 10)` |    151    |   146    |
| `(4, 5, 11)` |    165    |   162    |
| `(4, 5, 12)` |    180    |   177    |
| `(5, 5, 9)`  |    167    |   166    |
| `(5, 5, 10)` |    184    |   183    |
| `(5, 5, 11)` |    202    |   200    |
| `(5, 5, 12)` |    220    |   217    |
| `(5, 6, 10)` |    218    |   217    |
| `(6, 7, 9)`  |    270    |   268    |
| `(7, 7, 7)`  |    249    |   248    |
| `(7, 7, 8)`  |    277    |   273    |
| `(7, 7, 9)`  |    315    |   313    |
| `(7, 8, 8)`  |    306    |   302    |
| `(8, 8, 8)`  |    336    |   329    |


### Reduce naive addition complexity
The naive addition complexity - is the number of nonzero coefficients minus `2·rank + n·p`.

|    Format    | Rank | Previous<br/>complexity | Current<br/>complexity |
|:------------:|:----:|:-----------------------:|:----------------------:|
| `(2, 3, 5)`  |  25  |           108           |          106           |
| `(2, 3, 10)` |  50  |           254           |          198           |
| `(2, 3, 13)` |  65  |           312           |          256           |
| `(2, 3, 15)` |  75  |           381           |          307           |
| `(2, 4, 6)`  |  39  |           329           |          202           |
| `(2, 4, 9)`  |  59  |           379           |          309           |
| `(2, 4, 11)` |  71  |           749           |          430           |
| `(2, 4, 12)` |  77  |           746           |          484           |
| `(2, 4, 15)` |  96  |          1314           |          662           |
| `(2, 5, 9)`  |  72  |           565           |          465           |
| `(2, 6, 9)`  |  86  |           691           |          548           |
| `(2, 7, 8)`  |  88  |           783           |          745           |
| `(3, 3, 5)`  |  36  |           185           |          178           |
| `(3, 3, 7)`  |  49  |           868           |          404           |
| `(3, 3, 9)`  |  63  |           960           |          411           |
| `(3, 4, 5)`  |  47  |           293           |          277           |
| `(3, 5, 5)`  |  58  |           357           |          351           |
| `(3, 5, 10)` | 115  |           778           |          730           |
| `(4, 4, 5)`  |  61  |           455           |          452           |
| `(4, 4, 6)`  |  73  |           740           |          534           |
| `(4, 4, 8)`  |  96  |          1920           |          962           |
| `(4, 4, 10)` | 120  |          1437           |          1273          |
| `(4, 4, 11)` | 130  |          1555           |          1540          |
| `(4, 5, 5)`  |  76  |           549           |          528           |
| `(4, 5, 7)`  | 104  |          1354           |          924           |
| `(4, 5, 8)`  | 118  |          1566           |          1463          |
| `(4, 5, 10)` | 151  |          1706           |          1207          |
| `(4, 5, 11)` | 165  |          1869           |          1801          |
| `(4, 5, 12)` | 180  |          2196           |          2138          |
| `(4, 6, 7)`  | 123  |          1785           |          1562          |
| `(4, 7, 8)`  | 164  |          1554           |          1505          |
| `(5, 5, 5)`  |  93  |           846           |          843           |
| `(5, 5, 6)`  | 110  |          1300           |          1192          |
| `(5, 5, 7)`  | 127  |          1662           |          1606          |
| `(5, 5, 8)`  | 144  |          1924           |          1872          |
| `(5, 5, 9)`  | 167  |          2220           |          1814          |
| `(5, 5, 10)` | 184  |          2582           |          2083          |
| `(5, 5, 11)` | 202  |          2731           |          2271          |
| `(5, 5, 12)` | 220  |          3458           |          2444          |
| `(5, 6, 6)`  | 130  |          1758           |          1697          |
| `(5, 6, 7)`  | 150  |          2431           |          1994          |
| `(5, 6, 8)`  | 170  |          2872           |          2312          |
| `(5, 6, 9)`  | 197  |          3049           |          2328          |
| `(5, 7, 7)`  | 176  |          2846           |          2535          |
| `(5, 8, 8)`  | 230  |          2842           |          2638          |
| `(6, 6, 6)`  | 153  |          2232           |          2171          |
| `(6, 6, 7)`  | 183  |          3011           |          2493          |
| `(6, 7, 8)`  | 239  |          2352           |          2263          |
| `(6, 7, 9)`  | 270  |          2917           |          2804          |

## Methodology & instruments
The research employs a multi-stage approach using custom-built tools:

### [ternary_flip_graph](https://github.com/dronperminov/ternary_flip_graph): core flip graph exploration toolkit
A comprehensive CPU-based toolkit for discovering fast matrix multiplication algorithms using flip graph techniques. Supports multiple coefficient sets
(`{0, 1}`, `{0, 1, 2}`, `{-1, 0, 1}`) and provides tools for rank minimization, complexity optimization, alternative scheme discovery, and meta operations
for transforming schemes between dimensions.

### [FlipGraphGPU](https://github.com/dronperminov/FlipGraphGPU): GPU-accelerated exploration
A high-performance instrument for exploring the fast matrix multiplication schemes using meta flip graph techniques, optimized for execution on NVIDIA GPUs with
coefficients restricted to the ternary integer set.

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
|      `(2, 4, 9)`       |      59 (?)      |     59 (?)      |     58 (59)     |      59 (?)      |           -            |           -           |           -           |
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
|      `(2, 6, 6)`       |      57 (?)      |       56        |       56        |        56        |           -            |           -           |           -           |
|      `(2, 6, 7)`       |      68 (?)      |       66        |       66        |        66        |           -            |           -           |           -           |
|      `(2, 6, 8)`       |      77 (?)      |     75 (?)      |       75        |        75        |           -            |           -           |           -           |
|      `(2, 6, 9)`       |      86 (?)      |       86        |       86        |        86        |        548 (?)         |       548 (691)       |       548 (691)       |
|      `(2, 6, 10)`      |        94        |       94        |       94        |        94        |          668           |          668          |          668          |
|      `(2, 7, 7)`       |      77 (?)      |     76 (?)      |       76        |        76        |           -            |           -           |           -           |
|      `(2, 7, 8)`       |      88 (?)      |       88        |       88        |        88        |        745 (?)         |       745 (783)       |       745 (783)       |
|      `(2, 7, 9)`       |     102 (?)      |     100 (?)     |       99        |     100 (?)      |           -            |           -           |           -           |
|      `(2, 8, 8)`       |       100        |       100       |       100       |       100        |          608           |          608          |          608          |
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
|      `(3, 5, 7)`       |      83 (?)      |     79 (80)     |       79        |        79        |           -            |           -           |           -           |
|      `(3, 5, 8)`       |      94 (?)      |       90        |       90        |        90        |           -            |           -           |           -           |
|      `(3, 5, 9)`       |     105 (?)      |       104       |       104       |       104        |           -            |           -           |           -           |
|      `(3, 5, 10)`      |     115 (?)      |       115       |       115       |       115        |        730 (?)         |       730 (778)       |       730 (778)       |
|      `(3, 5, 11)`      |     128 (?)      |       126       |       126       |       126        |           -            |           -           |           -           |
|      `(3, 5, 12)`      |     140 (?)      |       136       |       136       |       136        |           -            |           -           |           -           |
|      `(3, 6, 6)`       |      83 (?)      |     83 (?)      |       80        |     83 (86)      |           -            |           -           |           -           |
|      `(3, 6, 7)`       |      96 (?)      |     96 (?)      |       94        |      96 (?)      |           -            |           -           |           -           |
|      `(3, 6, 8)`       |     108 (?)      |       108       |       108       |       108        |        1412 (?)        |      1412 (2123)      |         1088          |
|      `(3, 6, 9)`       |     124 (?)      |     122 (?)     |       120       |     122 (?)      |           -            |           -           |           -           |
|      `(3, 6, 10)`      |     137 (?)      |     136 (?)     |       134       |     136 (?)      |           -            |           -           |           -           |
|      `(3, 7, 7)`       |     113 (?)      |     111 (?)     |       111       |       111        |           -            |           -           |           -           |
|      `(3, 7, 8)`       |     128 (?)      |     128 (?)     |       126       |     128 (?)      |           -            |           -           |           -           |
|      `(3, 7, 9)`       |     145 (?)      |     143 (?)     |       142       |     143 (?)      |           -            |           -           |           -           |
|      `(3, 8, 8)`       |     148 (?)      |     146 (?)     |       145       |     145 (?)      |           -            |           -           |           -           |
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
|      `(4, 5, 9)`       |     137 (?)      |    137 (139)    |       136       |    133 (139)     |           -            |           -           |           -           |
|      `(4, 5, 10)`      |    151 (152)     |       151       |    150 (151)    |    146 (151)     |           -            |           -           |           -           |
|      `(4, 5, 11)`      |     165 (?)      |       165       |       165       |    162 (165)     |        1801 (?)        |      1801 (1869)      |      1801 (1869)      |
|      `(4, 5, 12)`      |     179 (?)      |    179 (180)    |    179 (180)    |    177 (180)     |        1959 (?)        |      1959 (2196)      |      1959 (2196)      |
|      `(4, 6, 6)`       |       105        |       105       |       105       |       105        |          894           |          894          |          894          |
|      `(4, 6, 7)`       |     123 (?)      |       123       |       123       |       123        |        1562 (?)        |      1562 (1798)      |      1562 (1785)      |
|      `(4, 6, 8)`       |       140        |       140       |       140       |       140        |          1248          |         1248          |         1248          |
|      `(4, 6, 9)`       |     159 (?)      |     159 (?)     |       159       |     159 (?)      |        1600 (?)        |       1600 (?)        |         1438          |
|      `(4, 6, 10)`      |     175 (?)      |       175       |       175       |       175        |        1878 (?)        |         1854          |         1854          |
|      `(4, 7, 7)`       |     145 (?)      |       144       |       144       |       144        |           -            |           -           |           -           |
|      `(4, 7, 8)`       |       164        |       164       |       164       |       164        |      1505 (1554)       |      1505 (1554)      |      1505 (1554)      |
|      `(4, 7, 9)`       |     187 (?)      |     187 (?)     |       186       |     187 (?)      |           -            |           -           |           -           |
|      `(4, 8, 8)`       |       182        |       182       |       182       |       182        |          1884          |         1884          |         1884          |
|      `(5, 5, 5)`       |        93        |       93        |       93        |        93        |       843 (846)        |       843 (846)       |       843 (846)       |
|      `(5, 5, 6)`       |     110 (?)      |       110       |       110       |       110        |        1192 (?)        |      1192 (1300)      |      1192 (1300)      |
|      `(5, 5, 7)`       |    127 (134)     |       127       |       127       |       127        |       1606 (918)       |      1606 (918)       |      1606 (918)       |
|      `(5, 5, 8)`       |     144 (?)      |       144       |       144       |       144        |        1872 (?)        |      1872 (2257)      |      1872 (1924)      |
|      `(5, 5, 9)`       |     167 (?)      |       167       |       167       |    166 (167)     |        1814 (?)        |      1814 (2220)      |      1814 (2220)      |
|      `(5, 5, 10)`      |     184 (?)      |     184 (?)     |       184       |    183 (184)     |        2083 (?)        |       2083 (?)        |      2083 (2582)      |
|      `(5, 5, 11)`      |     202 (?)      |     202 (?)     |       202       |    200 (202)     |        2271 (?)        |       2271 (?)        |      2271 (2731)      |
|      `(5, 5, 12)`      |     220 (?)      |       220       |       220       |    217 (220)     |        2444 (?)        |      2444 (3458)      |      2444 (3458)      |
|      `(5, 6, 6)`       |     130 (?)      |       130       |       130       |       130        |        1697 (?)        |      1697 (1766)      |      1697 (1758)      |
|      `(5, 6, 7)`       |     150 (?)      |       150       |       150       |       150        |        1994 (?)        |      1994 (2431)      |      1994 (2431)      |
|      `(5, 6, 8)`       |    170 (176)     |       170       |       170       |       170        |      2312 (1965)       |      2312 (1965)      |      2312 (1965)      |
|      `(5, 6, 9)`       |     197 (?)      |       197       |       197       |       197        |        2328 (?)        |      2328 (3049)      |      2328 (3049)      |
|      `(5, 6, 10)`      |     217 (?)      |    217 (218)    |    217 (218)    |    217 (218)     |        2772 (?)        |      2772 (3200)      |      2772 (3200)      |
|      `(5, 7, 7)`       |     176 (?)      |       176       |       176       |       176        |        2535 (?)        |      2535 (2846)      |      2535 (2846)      |
|      `(5, 7, 8)`       |     206 (?)      |     205 (?)     |       205       |       205        |           -            |           -           |           -           |
|      `(5, 7, 9)`       |     231 (?)      |    229 (234)    |       229       |       229        |           -            |           -           |           -           |
|      `(5, 8, 8)`       |       230        |       230       |       230       |       230        |      2638 (2842)       |      2638 (2842)      |      2638 (2842)      |
|      `(6, 6, 6)`       |       153        |       153       |       153       |       153        |      2171 (2232)       |      2171 (2232)      |      2171 (2232)      |
|      `(6, 6, 7)`       |     183 (?)      |       183       |       183       |       183        |        2493 (?)        |      2493 (3011)      |      2493 (3011)      |
|      `(6, 6, 8)`       |       203        |       203       |       203       |       203        |          1994          |         1994          |         1994          |
|      `(6, 6, 9)`       |       225        |       225       |       225       |       225        |          2440          |         2440          |         2440          |
|      `(6, 6, 10)`      |     252 (?)      |     252 (?)     |       247       |     252 (?)      |           -            |           -           |           -           |
|      `(6, 7, 7)`       |       215        |       215       |       215       |       215        |          2004          |         2004          |         2004          |
|      `(6, 7, 8)`       |       239        |       239       |       239       |       239        |      2263 (2352)       |      2263 (2352)      |      2263 (2352)      |
|      `(6, 7, 9)`       |    268 (270)     |    268 (270)    |    268 (270)    |    268 (270)     |      3059 (2917)       |      3059 (2917)      |      3059 (2917)      |
|      `(6, 8, 8)`       |       266        |       266       |       266       |       266        |          2780          |         2780          |         2780          |
|      `(7, 7, 7)`       |     250 (?)      |     250 (?)     |       249       |     248 (?)      |           -            |           -           |           -           |
|      `(7, 7, 8)`       |     279 (?)      |     279 (?)     |       277       |     273 (?)      |           -            |           -           |           -           |
|      `(7, 7, 9)`       |     316 (?)      |    316 (318)    |       315       |    313 (318)     |           -            |           -           |           -           |
|      `(7, 8, 8)`       |     310 (?)      |     310 (?)     |       306       |     302 (?)      |           -            |           -           |           -           |
|      `(8, 8, 8)`       |     343 (?)      |     343 (?)     |       336       |     329 (?)      |           -            |           -           |           -           |

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
