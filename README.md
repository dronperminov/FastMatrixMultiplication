# FastMatrixMultiplication

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `(2, 2, 2)` to `(8, 8, 8)`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`, focusing on all tensor shapes satisfying `max(n₁n₂, n₂n₃, n₃n₁) ≤ 64` and `max(n₁, n₂, n₃) ≤ 16`.

## Overview
This repository documents the search for fast matrix multiplication (FMM) schemes using a custom GPU-accelerated meta flip graph method. The search is conducted in the ternary
integer field (`ZT`), focusing on schemes that use only the coefficients `-1`, `0`, and `1`. This constraint is significant for practical implementations where computational
complexity and hardware efficiency are critical.

Key insight: I have successfully "rediscovered" several known optimal schemes originally found over the rationals (`Q`) or integers (`Z`), now providing them with minimal, ternary
coefficients. This can lead to more efficient and hardware-friendly implementations.

## Publications

* [Fast Matrix Multiplication via Ternary Meta Flip Graphs](https://arxiv.org/abs/2511.20317) (arxiv)

## Key results

### New best ranks in the ternary coefficient set (`ZT`)
New schemes have been discovered that improve the state-of-the-art for matrix multiplication with coefficients restricted to the ternary set `{-1, 0, 1}`,
achieving lower ranks than previously known.

|    Format    |  Prev rank  | New rank | Naive complexity |
|:------------:|:-----------:|:--------:|:----------------:|
| `(4, 5, 12)` |  180 (`Z`)  |   179    |       1977       |
| `(5, 6, 10)` |  218 (`Z`)  |   217    |       2772       |
| `(6, 7, 9)`  | 270 (`ZT`)  |   268    |       3062       |


### Conversions to the ternary coefficient set (`ZT`)
The following schemes have been converted to the `ZT` format, having been previously known over the rational (`Q`) or integer (`Z`) fields but lacking known
implementations with coefficients restricted to the ternary set:

|    Format    | Rank | Known ring |
|:------------:|:----:|:----------:|
| `(2, 3, 10)` |  50  |    `Z`     |
| `(2, 3, 13)` |  65  |    `Z`     |
| `(2, 3, 15)` |  75  |    `Z`     |
| `(2, 4, 6)`  |  39  |    `Z`     |
| `(2, 4, 9)`  |  59  |    `Q`     |
| `(2, 4, 11)` |  71  |    `Q`     |
| `(2, 4, 12)` |  77  |    `Q`     |
| `(2, 4, 15)` |  96  |    `Q`     |
| `(2, 5, 9)`  |  72  |    `Q`     |
| `(2, 6, 9)`  |  86  |    `Z`     |
| `(3, 4, 5)`  |  47  |    `Z`     |
| `(4, 4, 6)`  |  73  |   `Z/Q`    |
| `(4, 4, 8)`  |  96  |    `Q`     |
| `(4, 5, 6)`  |  90  |    `Z`     |
| `(4, 5, 7)`  | 104  |   `Z/Q`    |
| `(4, 5, 8)`  | 118  |   `Z/Q`    |
| `(4, 5, 10)` | 151  |    `Z`     |
| `(4, 5, 11)` | 165  |    `Z`     |
| `(4, 6, 7)`  | 123  |   `Z/Q`    |
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


### Reduce addition complexity
The following schemes have been optimized for addition count, achieving fewer operations than previously known through common subexpression elimination:

|    Format    |        Rank        | Best known | Naive | Greedy<br>Vanilla | Greedy<br>Potential | Current | Saved | Improved (%) |
|:------------:|:------------------:|:----------:|:-----:|:-----------------:|:-------------------:|:-------:|:-----:|:------------:|
| `(2, 2, 2)`  |         7          |     15     |  24   |        15         |         15          |   15    |   9   |     37.5     |
| `(2, 2, 3)`  |         11         |     21     |  20   |        20         |         20          |   20    |   0   |     0.0      |
| `(2, 2, 4)`  |         14         |     37     |  36   |        31         |         31          |   31    |   5   |     13.9     |
| `(2, 2, 5)`  |         18         |     40     |  38   |        33         |         33          |   33    |   5   |     13.2     |
| `(2, 2, 6)`  |         21         |     ?      |  54   |        44         |         44          |   44    |  10   |     18.5     |
| `(2, 2, 7)`  |         25         |     ?      |  56   |        46         |         46          |   46    |  10   |     17.9     |
| `(2, 2, 8)`  |         28         |     ?      |  72   |        57         |         57          |   57    |  15   |     20.8     |
| `(2, 2, 9)`  |         32         |     ?      |  74   |         ?         |         59          |   59    |  15   |     20.3     |
| `(2, 2, 10)` |         35         |     ?      |  90   |         ?         |          ?          |   70    |  20   |     22.2     |
| `(2, 2, 11)` |         39         |     ?      |  92   |         ?         |          ?          |   72    |  20   |     21.7     |
| `(2, 2, 12)` |         42         |     ?      |  108  |         ?         |          ?          |   83    |  25   |     23.1     |
| `(2, 2, 13)` |         46         |     ?      |  110  |         ?         |          ?          |   85    |  25   |     22.7     |
| `(2, 2, 14)` |         49         |     ?      |  126  |         ?         |          ?          |   96    |  30   |     23.8     |
| `(2, 2, 15)` |         53         |     ?      |  128  |         ?         |          ?          |   98    |  30   |     23.4     |
| `(2, 2, 16)` |         56         |     ?      |  144  |         ?         |          ?          |   109   |  35   |     24.3     |
| `(2, 3, 3)`  |         15         |     44     |  58   |        46         |         46          |   46    |  12   |     20.7     |
| `(2, 3, 4)`  |         20         |     58     |  82   |        58         |         58          |   58    |  24   |     29.3     |
| `(2, 3, 5)`  |         25         |    103     |  110  |        74         |         73          | **71**  |  39   |     35.5     |
| `(2, 3, 6)`  |         30         |     ?      |  116  |        81         |         81          |   81    |  35   |     30.2     |
| `(2, 3, 7)`  |         35         |     ?      |  140  |        100        |       **99**        | **99**  |  41   |     29.3     |
| `(2, 3, 8)`  |         40         |     ?      |  164  |        104        |         104         |   104   |  60   |     36.6     |
| `(2, 3, 9)`  |         45         |     ?      |  174  |         ?         |         116         |   116   |  58   |     33.3     |
| `(2, 3, 10)` |         50         |     ?      |  198  |         ?         |          ?          |   134   |  64   |     32.3     |
| `(2, 3, 11)` |         55         |     ?      |  222  |         ?         |          ?          |   145   |  77   |     34.7     |
| `(2, 3, 12)` |         60         |     ?      |  232  |         ?         |          ?          |   151   |  81   |     34.9     |
| `(2, 3, 13)` |         65         |     ?      |  256  |         ?         |          ?          |   169   |  87   |     34.0     |
| `(2, 3, 14)` |         70         |     ?      |  280  |         ?         |          ?          |   180   |  100  |     35.7     |
| `(2, 3, 15)` |         75         |     ?      |  307  |         ?         |          ?          |   192   |  115  |     37.5     |
| `(2, 3, 16)` |         80         |     ?      |  328  |         ?         |          ?          |   196   |  132  |     40.2     |
| `(2, 4, 4)`  |         26         |    173     |  130  |        93         |       **92**        | **92**  |  38   |     29.2     |
| `(2, 4, 5)`  | 33 (near optimal)  |    172     |  184  |        114        |       **112**       | **112** |  72   |     39.1     |
| `(2, 4, 6)`  |         39         |     ?      |  202  |        138        |       **136**       | **136** |  66   |     32.7     |
| `(2, 4, 7)`  |         45         |     ?      |  308  |        181        |         178         | **175** |  133  |     43.2     |
| `(2, 4, 8)`  |         51         |     ?      |  354  |        197        |         191         | **189** |  165  |     46.6     |
| `(2, 4, 9)`  |         59         |     ?      |  309  |        210        |         208         | **207** |  102  |     33.0     |
| `(2, 4, 10)` | 65 (near optimal)  |     ?      |  340  |         ?         |          ?          |   222   |  118  |     34.7     |
| `(2, 4, 11)` |         71         |     ?      |  430  |         ?         |          ?          |   268   |  162  |     37.7     |
| `(2, 4, 12)` |         77         |     ?      |  484  |         ?         |          ?          |   276   |  208  |     43.0     |
| `(2, 4, 13)` | 84 (near optimal)  |     ?      |  595  |         ?         |          ?          |   317   |  278  |     46.7     |
| `(2, 4, 14)` |         90         |     ?      |  616  |         ?         |          ?          |   320   |  296  |     48.1     |
| `(2, 4, 15)` |         96         |     ?      |  662  |         ?         |          ?          |   358   |  304  |     45.9     |
| `(2, 4, 16)` |        102         |     ?      |  708  |         ?         |          ?          |   342   |  366  |     51.7     |
| `(2, 5, 5)`  |         40         |    313     |  283  |        155        |         154         | **153** |  130  |     45.9     |
| `(2, 5, 6)`  |         47         |     ?      |  332  |        189        |         186         | **184** |  148  |     44.6     |
| `(2, 5, 7)`  | 57 (near optimal)  |     ?      |  340  |        197        |         194         | **192** |  148  |     43.5     |
| `(2, 5, 8)`  | 65 (near optimal)  |     ?      |  376  |        222        |         218         | **216** |  160  |     42.6     |
| `(2, 5, 9)`  |         72         |     ?      |  465  |        275        |         270         | **269** |  196  |     42.2     |
| `(2, 5, 10)` | 80 (near optimal)  |     ?      |  416  |         ?         |          ?          |   273   |  143  |     34.4     |
| `(2, 5, 11)` |         87         |     ?      |  540  |         ?         |          ?          |   326   |  214  |     39.6     |
| `(2, 5, 12)` |         94         |     ?      |  664  |         ?         |          ?          |   329   |  335  |     50.5     |
| `(2, 6, 6)`  | 57 (near optimal)  |     ?      |  326  |        231        |       **228**       | **228** |  98   |     30.1     |
| `(2, 6, 7)`  | 68 (near optimal)  |     ?      |  396  |        233        |         230         | **229** |  167  |     42.2     |
| `(2, 6, 8)`  | 77 (near optimal)  |     ?      |  456  |        272        |       **269**       | **269** |  187  |     41.0     |
| `(2, 6, 9)`  |         86         |     ?      |  548  |        302        |         296         | **295** |  253  |     46.2     |
| `(2, 6, 10)` |         94         |     ?      |  668  |         ?         |          ?          |   327   |  341  |     51.0     |
| `(2, 7, 7)`  | 77 (near optimal)  |     ?      |  452  |        323        |       **320**       |   321   |  131  |     29.0     |
| `(2, 7, 8)`  | 90 (near optimal)  |     ?      |  648  |        347        |       **333**       |   336   |  312  |     48.1     |
| `(2, 7, 9)`  | 102 (near optimal) |     ?      |  678  |        398        |       **384**       | **384** |  294  |     43.4     |
| `(2, 8, 8)`  |        100         |     ?      |  608  |        427        |       **424**       |   426   |  182  |     29.9     |
| `(3, 3, 3)`  |         23         |     60     |  97   |        60         |         60          |   60    |  37   |     38.1     |
| `(3, 3, 4)`  |         29         |     98     |  134  |        93         |       **92**        | **92**  |  42   |     31.3     |
| `(3, 3, 5)`  |         36         |    176     |  193  |        125        |       **123**       | **123** |  70   |     36.3     |
| `(3, 3, 6)`  | 43 (near optimal)  |     ?      |  284  |        169        |         165         | **163** |  121  |     42.6     |
| `(3, 3, 7)`  | 51 (near optimal)  |     ?      |  279  |        157        |         155         | **154** |  125  |     44.8     |
| `(3, 3, 8)`  | 58 (near optimal)  |     ?      |  275  |        172        |         171         | **169** |  106  |     38.5     |
| `(3, 3, 9)`  | 65 (near optimal)  |     ?      |  347  |        221        |         218         | **217** |  130  |     37.5     |
| `(3, 3, 10)` | 72 (near optimal)  |     ?      |  386  |         ?         |          ?          |   214   |  172  |     44.6     |
| `(3, 3, 11)` | 79 (near optimal)  |     ?      |  497  |         ?         |          ?          |   289   |  208  |     41.9     |
| `(3, 3, 12)` | 86 (near optimal)  |     ?      |  582  |         ?         |          ?          |   297   |  285  |     49.0     |
| `(3, 3, 13)` | 94 (near optimal)  |     ?      |  593  |         ?         |          ?          |   337   |  256  |     43.2     |
| `(3, 3, 14)` | 101 (near optimal) |     ?      |  664  |         ?         |          ?          |   364   |  300  |     45.2     |
| `(3, 3, 15)` | 108 (near optimal) |     ?      |  579  |         ?         |          ?          |   305   |  274  |     47.3     |
| `(3, 3, 16)` | 115 (near optimal) |     ?      |  862  |         ?         |          ?          |   414   |  448  |     52.0     |
| `(3, 4, 4)`  |         38         |    198     |  194  |        136        |         134         | **133** |  61   |     31.4     |
| `(3, 4, 5)`  |         47         |    276     |  277  |        170        |       **161**       | **161** |  116  |     41.9     |
| `(3, 4, 6)`  | 57 (near optimal)  |     ?      |  387  |        209        |         206         | **205** |  182  |     47.0     |
| `(3, 4, 7)`  | 64 (near optimal)  |     ?      |  446  |        259        |         257         | **249** |  197  |     44.2     |
| `(3, 4, 8)`  | 74 (near optimal)  |     ?      |  461  |        272        |       **267**       | **267** |  194  |     42.1     |
| `(3, 4, 9)`  | 84 (near optimal)  |     ?      |  537  |        328        |         321         | **317** |  220  |     41.0     |
| `(3, 4, 10)` | 93 (near optimal)  |     ?      |  582  |         ?         |          ?          |   346   |  236  |     40.5     |
| `(3, 4, 11)` | 102 (near optimal) |     ?      |  641  |         ?         |          ?          |   382   |  259  |     40.4     |
| `(3, 4, 12)` | 111 (near optimal) |     ?      |  721  |         ?         |          ?          |   416   |  305  |     42.3     |
| `(3, 4, 13)` | 121 (near optimal) |     ?      |  807  |         ?         |          ?          |   459   |  348  |     43.1     |
| `(3, 4, 14)` | 128 (near optimal) |     ?      |  898  |         ?         |          ?          |   460   |  438  |     48.8     |
| `(3, 4, 15)` | 138 (near optimal) |     ?      |  958  |         ?         |          ?          |   533   |  425  |     44.4     |
| `(3, 4, 16)` | 148 (near optimal) |     ?      | 1046  |         ?         |          ?          |   520   |  526  |     50.3     |
| `(3, 5, 5)`  |         58         |    326     |  357  |        230        |         224         | **222** |  135  |     37.8     |
| `(3, 5, 6)`  | 70 (near optimal)  |     ?      |  561  |        275        |         271         | **267** |  294  |     52.4     |
| `(3, 5, 7)`  | 83 (near optimal)  |     ?      |  494  |        318        |         310         | **306** |  188  |     38.1     |
| `(3, 5, 8)`  | 94 (near optimal)  |     ?      |  584  |        295        |         295         |   295   |  289  |     49.5     |
| `(3, 5, 9)`  | 105 (near optimal) |     ?      |  646  |        392        |         387         | **386** |  260  |     40.2     |
| `(3, 5, 10)` | 116 (near optimal) |     ?      |  714  |         ?         |          ?          |   394   |  320  |     44.8     |
| `(3, 5, 11)` | 128 (near optimal) |     ?      |  967  |         ?         |          ?          |   492   |  475  |     49.1     |
| `(3, 5, 12)` | 140 (near optimal) |     ?      | 1152  |         ?         |          ?          |   484   |  668  |     58.0     |
| `(3, 6, 6)`  | 85 (near optimal)  |     ?      |  998  |        375        |         368         | **362** |  636  |     63.7     |
| `(3, 6, 7)`  | 100 (near optimal) |     ?      |  702  |        368        |       **355**       |   357   |  345  |     49.1     |
| `(3, 6, 8)`  | 113 (near optimal) |     ?      | 1245  |        471        |         461         | **454** |  791  |     63.5     |
| `(3, 6, 9)`  | 127 (near optimal) |     ?      | 1096  |        520        |       **500**       |   501   |  595  |     54.3     |
| `(3, 6, 10)` | 140 (near optimal) |     ?      | 1152  |         ?         |          ?          |   483   |  669  |     58.1     |
| `(3, 7, 7)`  | 115 (near optimal) |     ?      |  781  |        445        |         438         | **436** |  345  |     44.2     |
| `(3, 7, 8)`  | 128 (near optimal) |     ?      |  930  |        462        |       **450**       |   452   |  478  |     51.4     |
| `(3, 7, 9)`  | 147 (near optimal) |     ?      | 1002  |        597        |       **585**       | **585** |  417  |     41.6     |
| `(3, 8, 8)`  | 148 (near optimal) |     ?      | 1020  |        519        |       **511**       |   513   |  507  |     49.7     |
| `(4, 4, 4)`  | 49 (near optimal)  |    325     |  468  |        180        |         171         | **169** |  299  |     63.9     |
| `(4, 4, 5)`  |         61         |     ?      |  452  |        247        |         238         | **236** |  216  |     47.8     |
| `(4, 4, 6)`  |         73         |     ?      |  540  |        288        |       **282**       | **282** |  258  |     47.8     |
| `(4, 4, 7)`  |         85         |     ?      |  631  |        326        |         323         | **322** |  309  |     49.0     |
| `(4, 4, 8)`  |         96         |     ?      |  973  |        396        |         391         | **388** |  585  |     60.1     |
| `(4, 4, 9)`  | 110 (near optimal) |     ?      |  925  |        445        |       **424**       | **424** |  501  |     54.2     |
| `(4, 4, 10)` | 122 (near optimal) |     ?      |  878  |         ?         |          ?          |   483   |  395  |     45.0     |
| `(4, 4, 11)` | 134 (near optimal) |     ?      | 1150  |         ?         |          ?          |   526   |  624  |     54.3     |
| `(4, 4, 12)` | 145 (near optimal) |     ?      | 1495  |         ?         |          ?          |   608   |  887  |     59.3     |
| `(4, 4, 13)` | 157 (near optimal) |     ?      | 1474  |         ?         |          ?          |   639   |  835  |     56.6     |
| `(4, 4, 14)` | 169 (near optimal) |     ?      | 1596  |         ?         |          ?          |   700   |  896  |     56.1     |
| `(4, 4, 15)` | 181 (near optimal) |     ?      | 1679  |         ?         |          ?          |   737   |  942  |     56.1     |
| `(4, 4, 16)` | 192 (near optimal) |     ?      | 2059  |         ?         |          ?          |   729   | 1330  |     64.6     |
| `(4, 5, 5)`  |         76         |    451     |  530  |        315        |       **301**       |   303   |  227  |     42.8     |
| `(4, 5, 6)`  |         90         |     ?      | 1023  |        401        |         393         | **387** |  636  |     62.2     |
| `(4, 5, 7)`  |        104         |     ?      |  931  |        424        |       **415**       | **415** |  516  |     55.4     |
| `(4, 5, 8)`  |        118         |     ?      | 1521  |        541        |         534         | **526** |  995  |     65.4     |
| `(4, 5, 9)`  | 137 (near optimal) |     ?      | 1217  |        568        |         560         | **555** |  662  |     54.4     |
| `(4, 5, 10)` |        151         |     ?      | 1207  |         ?         |          ?          |   580   |  627  |     51.9     |
| `(4, 5, 11)` |        165         |     ?      | 1801  |         ?         |          ?          |   695   | 1106  |     61.4     |
| `(4, 5, 12)` |        179         |     ?      | 1977  |         ?         |          ?          |   759   | 1218  |     61.6     |
| `(4, 6, 6)`  |        105         |     ?      |  894  |        467        |       **435**       |   441   |  453  |     50.7     |
| `(4, 6, 7)`  |        123         |     ?      | 1586  |        535        |         533         | **519** | 1067  |     67.3     |
| `(4, 6, 8)`  |        140         |     ?      | 1248  |        576        |       **558**       |   565   |  683  |     54.7     |
| `(4, 6, 9)`  | 160 (near optimal) |     ?      | 1472  |        720        |       **653**       |   676   |  796  |     54.1     |
| `(4, 6, 10)` |        175         |     ?      | 1878  |         ?         |          ?          |   729   | 1149  |     61.2     |
| `(4, 7, 7)`  | 145 (near optimal) |     ?      | 1381  |        682        |         648         | **644** |  737  |     53.4     |
| `(4, 7, 8)`  |        164         |     ?      | 1505  |        749        |       **719**       |   728   |  777  |     51.6     |
| `(4, 7, 9)`  | 187 (near optimal) |     ?      | 2059  |        808        |         806         | **791** | 1268  |     61.6     |
| `(4, 8, 8)`  |        182         |     ?      | 1884  |        861        |       **812**       |   818   | 1066  |     56.6     |
| `(5, 5, 5)`  |         93         |     ?      |  843  |        392        |       **388**       | **388** |  455  |     54.0     |
| `(5, 5, 6)`  |        110         |     ?      | 1215  |        491        |         479         | **475** |  740  |     60.9     |
| `(5, 5, 7)`  |        127         |     ?      | 1607  |        565        |         557         | **546** | 1061  |     66.0     |
| `(5, 5, 8)`  |        144         |     ?      | 1924  |        648        |         640         | **632** | 1292  |     67.2     |
| `(5, 5, 9)`  |        167         |     ?      | 1814  |        706        |         699         | **691** | 1123  |     61.9     |
| `(5, 5, 10)` |        184         |     ?      | 2116  |         ?         |          ?          |   781   | 1335  |     63.1     |
| `(5, 5, 11)` |        202         |     ?      | 2272  |         ?         |          ?          |   858   | 1414  |     62.2     |
| `(5, 5, 12)` |        220         |     ?      | 2444  |         ?         |          ?          |   831   | 1613  |     66.0     |
| `(5, 6, 6)`  |        130         |     ?      | 1716  |        588        |         586         | **576** | 1140  |     66.4     |
| `(5, 6, 7)`  |        150         |     ?      | 2039  |        696        |         691         | **681** | 1358  |     66.6     |
| `(5, 6, 8)`  |        170         |     ?      | 2312  |        750        |         743         | **732** | 1580  |     68.3     |
| `(5, 6, 9)`  |        197         |     ?      | 2376  |        886        |         877         | **866** | 1510  |     63.6     |
| `(5, 6, 10)` |        217         |     ?      | 2772  |         ?         |          ?          |   940   | 1832  |     66.1     |
| `(5, 7, 7)`  |        176         |     ?      | 2610  |        833        |         821         | **819** | 1791  |     68.6     |
| `(5, 7, 8)`  | 206 (near optimal) |     ?      | 1880  |        948        |       **892**       |   908   |  972  |     51.7     |
| `(5, 7, 9)`  | 231 (near optimal) |     ?      | 2554  |        993        |         982         | **979** | 1575  |     61.7     |
| `(5, 8, 8)`  |        230         |     ?      | 2741  |       1016        |        1007         | **993** | 1748  |     63.8     |
| `(6, 6, 6)`  |        153         |     ?      | 2182  |        704        |         686         | **681** | 1501  |     68.8     |
| `(6, 6, 7)`  | 185 (near optimal) |     ?      | 1922  |        858        |         827         | **820** | 1102  |     57.3     |
| `(6, 6, 8)`  |        203         |     ?      | 1994  |        896        |         880         | **875** | 1119  |     56.1     |
| `(6, 6, 9)`  |        225         |     ?      | 2440  |       1029        |       **951**       |   984   | 1456  |     59.7     |
| `(6, 6, 10)` | 252 (near optimal) |     ?      | 3540  |         ?         |          ?          |  1259   | 2281  |     64.4     |
| `(6, 7, 7)`  |        215         |     ?      | 2004  |        965        |       **900**       |   926   | 1078  |     53.8     |
| `(6, 7, 8)`  |        239         |     ?      | 2263  |       1112        |      **1050**       |  1089   | 1174  |     51.9     |
| `(6, 7, 9)`  |        268         |     ?      | 3056  |       1184        |      **1166**       |  1172   | 1884  |     61.6     |
| `(6, 8, 8)`  |        266         |     ?      | 2780  |       1244        |      **1214**       |  1226   | 1554  |     55.9     |
| `(7, 7, 7)`  | 250 (near optimal) |     ?      | 2417  |       1119        |      **1077**       |  1099   | 1318  |     54.5     |
| `(7, 7, 8)`  | 279 (near optimal) |     ?      | 2932  |       1369        |      **1260**       |  1324   | 1608  |     54.8     |
| `(7, 7, 9)`  | 316 (near optimal) |     ?      | 3452  |       1460        |      **1404**       |  1414   | 2038  |     59.0     |
| `(7, 8, 8)`  | 310 (near optimal) |     ?      | 3604  |       1670        |      **1498**       |  1566   | 2038  |     56.5     |
| `(8, 8, 8)`  | 343 (near optimal) |     ?      | 4434  |         ?         |      **1709**       |  1756   | 2678  |     60.4     |


### New discoveries in binary field (`Z2`)
New schemes have been discovered that improve the state-of-the-art for matrix multiplication in the binary field (`Z2`),
achieving lower ranks than previously known.

|    Format    | Prev rank | New rank | Note              |
|:------------:|:---------:|:--------:|:------------------|
| `(3, 3, 7)`  |     ?     |    49    | equal to `Q` ring |
| `(3, 4, 9)`  |     ?     |    83    | equal to `Q` ring |
| `(3, 4, 10)` |     ?     |    92    | equal to `Q` ring |
| `(3, 4, 11)` |     ?     |   101    | equal to `Q` ring |
| `(3, 4, 12)` |     ?     |   108    | equal to `Q` ring |
| `(3, 4, 16)` |     ?     |   146    | equal to `Q` ring |
| `(3, 5, 7)`  |    80     |    79    | equal to `Q` ring |
| `(3, 8, 8)`  |     ?     |   145    | equal to `Q` ring |
| `(4, 4, 8)`  |    96     |    94    |                   |
| `(4, 4, 10)` |     ?     |   120    | equal to `Q` ring |
| `(4, 4, 12)` |    142    |   141    |                   |
| `(4, 4, 16)` |    189    |   188    |                   |
| `(4, 5, 6)`  |    90     |    89    |                   |
| `(4, 5, 9)`  |    136    |   133    |                   |
| `(4, 5, 10)` |    151    |   146    |                   |
| `(4, 5, 11)` |    165    |   162    |                   |
| `(4, 5, 12)` |    180    |   177    |                   |
| `(4, 6, 9)`  |     ?     |   159    | equal to `Q` ring |
| `(5, 5, 9)`  |    167    |   166    |                   |
| `(5, 5, 10)` |    184    |   183    |                   |
| `(5, 5, 11)` |    202    |   200    |                   |
| `(5, 5, 12)` |    220    |   217    |                   |
| `(5, 6, 10)` |    218    |   217    |                   |
| `(5, 7, 9)`  |    234    |   229    | equal to `Q` ring |
| `(6, 7, 9)`  |    270    |   268    |                   |
| `(7, 7, 7)`  |    249    |   248    |                   |
| `(7, 7, 8)`  |    277    |   275    |                   |
| `(7, 7, 9)`  |    315    |   313    |                   |
| `(7, 8, 8)`  |    306    |   302    |                   |
| `(8, 8, 8)`  |    336    |   329    |                   |


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
| `(3, 4, 5)`  |  47  |           293           |          277           |
| `(4, 4, 5)`  |  61  |           455           |          452           |
| `(4, 4, 6)`  |  73  |           740           |          540           |
| `(4, 4, 8)`  |  96  |          1920           |          973           |
| `(4, 5, 5)`  |  76  |           549           |          532           |
| `(4, 5, 7)`  | 104  |          1354           |          927           |
| `(4, 5, 8)`  | 118  |          1566           |          1521          |
| `(4, 5, 10)` | 151  |          1706           |          1207          |
| `(4, 5, 11)` | 165  |          1869           |          1801          |
| `(4, 5, 12)` | 180  |          2196           |          2138          |
| `(4, 6, 7)`  | 123  |          1785           |          1586          |
| `(4, 7, 8)`  | 164  |          1554           |          1505          |
| `(5, 5, 5)`  |  93  |           846           |          843           |
| `(5, 5, 6)`  | 110  |          1300           |          1215          |
| `(5, 5, 7)`  | 127  |          1662           |          1606          |
| `(5, 5, 8)`  | 144  |          1924           |          1908          |
| `(5, 5, 9)`  | 167  |          2220           |          1814          |
| `(5, 5, 10)` | 184  |          2582           |          2116          |
| `(5, 5, 11)` | 202  |          2731           |          2272          |
| `(5, 5, 12)` | 220  |          3458           |          2444          |
| `(5, 6, 6)`  | 130  |          1758           |          1714          |
| `(5, 6, 7)`  | 150  |          2431           |          2039          |
| `(5, 6, 8)`  | 170  |          2872           |          2312          |
| `(5, 6, 9)`  | 197  |          3049           |          2373          |
| `(5, 7, 7)`  | 176  |          2846           |          2610          |
| `(5, 8, 8)`  | 230  |          2842           |          2741          |
| `(6, 6, 6)`  | 153  |          2232           |          2171          |
| `(6, 7, 8)`  | 239  |          2352           |          2263          |
| `(6, 7, 9)`  | 270  |          2917           |          2804          |

## Methodology & instruments
The research employs a multi-stage approach using custom-built tools:

### [FlipGraphGPU](https://github.com/dronperminov/FlipGraphGPU): primary exploration tool
A high-performance instrument for exploring the fast matrix multiplication schemes using meta flip graph techniques, optimized for execution on NVIDIA GPUs with
coefficients restricted to the ternary integer set.

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
```json
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
```json
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

```json
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

```json
[{ "index": i, "value": c }, ...]
```

#### Example
Reduces `(2, 2, 2: 7)` from 18 to 15 multiplications:
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
* Full scheme format;
* Addition-reduced scheme format;
* `.m` (Maple)
* `.exp` (explicit circuit description)
* `.tensor.mpl` (Maple tensor representation)

This allows seamless integration of circuits produced by different tools and sources.

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
|      `(2, 4, 9)`       |      59 (?)      |     59 (?)      |       59        |      59 (?)      |        309 (?)         |        309 (?)        |       309 (379)       |
|      `(2, 4, 10)`      |      65 (?)      |     65 (?)      |       64        |      65 (?)      |           -            |           -           |           -           |
|      `(2, 4, 11)`      |      71 (?)      |     71 (?)      |       71        |      71 (?)      |        430 (?)         |        430 (?)        |       430 (749)       |
|      `(2, 4, 12)`      |      77 (?)      |     77 (?)      |       77        |      77 (?)      |        484 (?)         |        484 (?)        |       484 (746)       |
|      `(2, 4, 13)`      |      84 (?)      |     84 (?)      |       83        |      84 (?)      |           -            |           -           |           -           |
|      `(2, 4, 14)`      |        90        |       90        |       90        |        90        |          616           |          616          |          616          |
|      `(2, 4, 15)`      |      96 (?)      |     96 (?)      |       96        |      96 (?)      |        662 (?)         |        662 (?)        |      662 (1314)       |
|      `(2, 4, 16)`      |       102        |       102       |       102       |       102        |          708           |          708          |          708          |
|      `(2, 5, 5)`       |        40        |       40        |       40        |        40        |          208           |          208          |          208          |
|      `(2, 5, 6)`       |        47        |       47        |       47        |        47        |          332           |          332          |          332          |
|      `(2, 5, 7)`       |      57 (?)      |     57 (?)      |       55        |      57 (?)      |           -            |           -           |           -           |
|      `(2, 5, 8)`       |      65 (?)      |     65 (?)      |       63        |      65 (?)      |           -            |           -           |           -           |
|      `(2, 5, 9)`       |      72 (?)      |     72 (?)      |       72        |      72 (?)      |        465 (?)         |        465 (?)        |       465 (565)       |
|      `(2, 5, 10)`      |      80 (?)      |     80 (?)      |       79        |      80 (?)      |           -            |           -           |           -           |
|      `(2, 5, 11)`      |        87        |       87        |       87        |        87        |          540           |          540          |          540          |
|      `(2, 5, 12)`      |        94        |       94        |       94        |        94        |          664           |          664          |          664          |
|      `(2, 6, 6)`       |      57 (?)      |       56        |       56        |        56        |           -            |           -           |           -           |
|      `(2, 6, 7)`       |      68 (?)      |       66        |       66        |        66        |           -            |           -           |           -           |
|      `(2, 6, 8)`       |      77 (?)      |     77 (?)      |       75        |      77 (?)      |           -            |           -           |           -           |
|      `(2, 6, 9)`       |      86 (?)      |       86        |       86        |        86        |        548 (?)         |       548 (691)       |       548 (691)       |
|      `(2, 6, 10)`      |        94        |       94        |       94        |        94        |          668           |          668          |          668          |
|      `(2, 7, 7)`       |      77 (?)      |     77 (?)      |       76        |      77 (?)      |           -            |           -           |           -           |
|      `(2, 7, 8)`       |      90 (?)      |       88        |       88        |        88        |           -            |           -           |           -           |
|      `(2, 7, 9)`       |     102 (?)      |     102 (?)     |       99        |     101 (?)      |           -            |           -           |           -           |
|      `(2, 8, 8)`       |       100        |       100       |       100       |       100        |          608           |          608          |          608          |
|      `(3, 3, 3)`       |        23        |       23        |       23        |        23        |           84           |          84           |          84           |
|      `(3, 3, 4)`       |        29        |       29        |       29        |        29        |          134           |          134          |          134          |
|      `(3, 3, 5)`       |        36        |       36        |       36        |        36        |          193           |          185          |          185          |
|      `(3, 3, 6)`       |      43 (?)      |       42        |       40        |        42        |           -            |           -           |           -           |
|      `(3, 3, 7)`       |      51 (?)      |     51 (?)      |       49        |      49 (?)      |           -            |           -           |           -           |
|      `(3, 3, 8)`       |      58 (?)      |     58 (?)      |       55        |      56 (?)      |           -            |           -           |           -           |
|      `(3, 3, 9)`       |      65 (?)      |     65 (?)      |       63        |      64 (?)      |           -            |           -           |           -           |
|      `(3, 3, 10)`      |      72 (?)      |     72 (?)      |       69        |      71 (?)      |           -            |           -           |           -           |
|      `(3, 3, 11)`      |      79 (?)      |     79 (?)      |       76        |      78 (?)      |           -            |           -           |           -           |
|      `(3, 3, 12)`      |      86 (?)      |     86 (?)      |       80        |      84 (?)      |           -            |           -           |           -           |
|      `(3, 3, 13)`      |      94 (?)      |     94 (?)      |       89        |      91 (?)      |           -            |           -           |           -           |
|      `(3, 3, 14)`      |     101 (?)      |     101 (?)     |       95        |      98 (?)      |           -            |           -           |           -           |
|      `(3, 3, 15)`      |     108 (?)      |     108 (?)     |       103       |     105 (?)      |           -            |           -           |           -           |
|      `(3, 3, 16)`      |     115 (?)      |     115 (?)     |       109       |     112 (?)      |           -            |           -           |           -           |
|      `(3, 4, 4)`       |        38        |       38        |       38        |        38        |          192           |          192          |          192          |
|      `(3, 4, 5)`       |      47 (?)      |       47        |       47        |        47        |        277 (?)         |       277 (293)       |       277 (293)       |
|      `(3, 4, 6)`       |      57 (?)      |       54        |       54        |        54        |           -            |           -           |           -           |
|      `(3, 4, 7)`       |      64 (?)      |       64        |       63        |        64        |           -            |           -           |           -           |
|      `(3, 4, 8)`       |        74        |       74        |       73        |        74        |           -            |           -           |           -           |
|      `(3, 4, 9)`       |      84 (?)      |     84 (?)      |       83        |      83 (?)      |           -            |           -           |           -           |
|      `(3, 4, 10)`      |      93 (?)      |     93 (?)      |       92        |      92 (?)      |           -            |           -           |           -           |
|      `(3, 4, 11)`      |     102 (?)      |     102 (?)     |       101       |     101 (?)      |           -            |           -           |           -           |
|      `(3, 4, 12)`      |     111 (?)      |     111 (?)     |       108       |     108 (?)      |           -            |           -           |           -           |
|      `(3, 4, 13)`      |     121 (?)      |     121 (?)     |       117       |     118 (?)      |           -            |           -           |           -           |
|      `(3, 4, 14)`      |     128 (?)      |     128 (?)     |       126       |     128 (?)      |           -            |           -           |           -           |
|      `(3, 4, 15)`      |     138 (?)      |     138 (?)     |       136       |     137 (?)      |           -            |           -           |           -           |
|      `(3, 4, 16)`      |     148 (?)      |     148 (?)     |       146       |     146 (?)      |           -            |           -           |           -           |
|      `(3, 5, 5)`       |        58        |       58        |       58        |        58        |          357           |          357          |          357          |
|      `(3, 5, 6)`       |      70 (?)      |       68        |       68        |        68        |           -            |           -           |           -           |
|      `(3, 5, 7)`       |      83 (?)      |       80        |       79        |     79 (80)      |           -            |           -           |           -           |
|      `(3, 5, 8)`       |      94 (?)      |       90        |       90        |        90        |           -            |           -           |           -           |
|      `(3, 5, 9)`       |     105 (?)      |       104       |       104       |       104        |           -            |           -           |           -           |
|      `(3, 5, 10)`      |     116 (?)      |       115       |       115       |       115        |           -            |           -           |           -           |
|      `(3, 5, 11)`      |     128 (?)      |       126       |       126       |       126        |           -            |           -           |           -           |
|      `(3, 5, 12)`      |     140 (?)      |       136       |       136       |       136        |           -            |           -           |           -           |
|      `(3, 6, 6)`       |      85 (?)      |     85 (?)      |       80        |     84 (86)      |           -            |           -           |           -           |
|      `(3, 6, 7)`       |     100 (?)      |     100 (?)     |       94        |      96 (?)      |           -            |           -           |           -           |
|      `(3, 6, 8)`       |     113 (?)      |       108       |       108       |       108        |           -            |           -           |           -           |
|      `(3, 6, 9)`       |     127 (?)      |     127 (?)     |       120       |     122 (?)      |           -            |           -           |           -           |
|      `(3, 6, 10)`      |     140 (?)      |     140 (?)     |       134       |     136 (?)      |           -            |           -           |           -           |
|      `(3, 7, 7)`       |     115 (?)      |     115 (?)     |       111       |     113 (?)      |           -            |           -           |           -           |
|      `(3, 7, 8)`       |     128 (?)      |     128 (?)     |       126       |     128 (?)      |           -            |           -           |           -           |
|      `(3, 7, 9)`       |     147 (?)      |     147 (?)     |       142       |     143 (?)      |           -            |           -           |           -           |
|      `(3, 8, 8)`       |     148 (?)      |     148 (?)     |       145       |     145 (?)      |           -            |           -           |           -           |
|      `(4, 4, 4)`       |        49        |       49        |       48        |        47        |           -            |           -           |           -           |
|      `(4, 4, 5)`       |        61        |       61        |       61        |        60        |       452 (455)        |       452 (455)       |       452 (455)       |
|      `(4, 4, 6)`       |      73 (?)      |       73        |       73        |        73        |        540 (?)         |       540 (740)       |       540 (740)       |
|      `(4, 4, 7)`       |        85        |       85        |       85        |        85        |          631           |          631          |          631          |
|      `(4, 4, 8)`       |      96 (?)      |     96 (?)      |       96        |      94 (?)      |        973 (?)         |        973 (?)        |      973 (1920)       |
|      `(4, 4, 9)`       |     110 (?)      |     110 (?)     |       104       |     107 (?)      |           -            |           -           |           -           |
|      `(4, 4, 10)`      |     122 (?)      |     122 (?)     |       120       |     120 (?)      |           -            |           -           |           -           |
|      `(4, 4, 11)`      |     134 (?)      |     134 (?)     |       130       |     132 (?)      |           -            |           -           |           -           |
|      `(4, 4, 12)`      |     145 (?)      |     145 (?)     |       142       |     141 (?)      |           -            |           -           |           -           |
|      `(4, 4, 13)`      |     157 (?)      |     157 (?)     |       152       |     154 (?)      |           -            |           -           |           -           |
|      `(4, 4, 14)`      |     169 (?)      |     169 (?)     |       165       |     167 (?)      |           -            |           -           |           -           |
|      `(4, 4, 15)`      |     181 (?)      |     181 (?)     |       177       |     179 (?)      |           -            |           -           |           -           |
|      `(4, 4, 16)`      |     192 (?)      |     192 (?)     |       189       |     188 (?)      |           -            |           -           |           -           |
|      `(4, 5, 5)`       |        76        |       76        |       76        |        73        |       532 (549)        |       532 (549)       |       532 (549)       |
|      `(4, 5, 6)`       |      90 (?)      |       90        |       90        |     89 (90)      |        1023 (?)        |          775          |          775          |
|      `(4, 5, 7)`       |     104 (?)      |       104       |       104       |       104        |        927 (?)         |      927 (1386)       |      927 (1354)       |
|      `(4, 5, 8)`       |    118 (122)     |       118       |       118       |       118        |       1521 (918)       |      1521 (918)       |      1521 (918)       |
|      `(4, 5, 9)`       |     137 (?)      |    137 (139)    |       136       |    133 (139)     |           -            |           -           |           -           |
|      `(4, 5, 10)`      |    151 (152)     |       151       |       151       |    146 (151)     |      1207 (1568)       |      1207 (1568)      |      1207 (1568)      |
|      `(4, 5, 11)`      |     165 (?)      |       165       |       165       |    162 (165)     |        1801 (?)        |      1801 (1869)      |      1801 (1869)      |
|      `(4, 5, 12)`      |     179 (?)      |    179 (180)    |    179 (180)    |    177 (180)     |        1977 (?)        |      1977 (2196)      |      1977 (2196)      |
|      `(4, 6, 6)`       |       105        |       105       |       105       |       105        |          894           |          894          |          894          |
|      `(4, 6, 7)`       |     123 (?)      |       123       |       123       |       123        |        1586 (?)        |      1586 (1798)      |      1586 (1785)      |
|      `(4, 6, 8)`       |       140        |       140       |       140       |       140        |          1248          |         1248          |         1248          |
|      `(4, 6, 9)`       |     160 (?)      |     160 (?)     |       159       |     159 (?)      |           -            |           -           |           -           |
|      `(4, 6, 10)`      |     175 (?)      |       175       |       175       |       175        |        1878 (?)        |         1854          |         1854          |
|      `(4, 7, 7)`       |     145 (?)      |       144       |       144       |       144        |           -            |           -           |           -           |
|      `(4, 7, 8)`       |       164        |       164       |       164       |       164        |      1505 (1554)       |      1505 (1554)      |      1505 (1554)      |
|      `(4, 7, 9)`       |     187 (?)      |     187 (?)     |       186       |     187 (?)      |           -            |           -           |           -           |
|      `(4, 8, 8)`       |       182        |       182       |       182       |       182        |          1884          |         1884          |         1884          |
|      `(5, 5, 5)`       |        93        |       93        |       93        |        93        |       843 (846)        |       843 (846)       |       843 (846)       |
|      `(5, 5, 6)`       |     110 (?)      |       110       |       110       |       110        |        1215 (?)        |      1215 (1300)      |      1215 (1300)      |
|      `(5, 5, 7)`       |    127 (134)     |       127       |       127       |       127        |       1606 (918)       |      1606 (918)       |      1606 (918)       |
|      `(5, 5, 8)`       |     144 (?)      |       144       |       144       |       144        |        1908 (?)        |      1908 (2257)      |      1908 (1924)      |
|      `(5, 5, 9)`       |     167 (?)      |       167       |       167       |    166 (167)     |        1814 (?)        |      1814 (2220)      |      1814 (2220)      |
|      `(5, 5, 10)`      |     184 (?)      |     184 (?)     |       184       |     183 (?)      |        2116 (?)        |       2116 (?)        |      2116 (2582)      |
|      `(5, 5, 11)`      |     202 (?)      |     202 (?)     |       202       |     200 (?)      |        2272 (?)        |       2272 (?)        |      2272 (2731)      |
|      `(5, 5, 12)`      |     220 (?)      |       220       |       220       |    217 (220)     |        2444 (?)        |      2444 (3458)      |      2444 (3458)      |
|      `(5, 6, 6)`       |     130 (?)      |       130       |       130       |       130        |        1714 (?)        |      1714 (1766)      |      1714 (1758)      |
|      `(5, 6, 7)`       |     150 (?)      |       150       |       150       |       150        |        2039 (?)        |      2039 (2431)      |      2039 (2431)      |
|      `(5, 6, 8)`       |    170 (176)     |       170       |       170       |       170        |      2312 (1965)       |      2312 (1965)      |      2312 (1965)      |
|      `(5, 6, 9)`       |     197 (?)      |       197       |       197       |       197        |        2373 (?)        |      2373 (3049)      |      2373 (3049)      |
|      `(5, 6, 10)`      |     217 (?)      |    217 (218)    |    217 (218)    |    217 (218)     |        2772 (?)        |      2772 (3200)      |      2772 (3200)      |
|      `(5, 7, 7)`       |     176 (?)      |       176       |       176       |       176        |        2610 (?)        |      2610 (2846)      |      2610 (2846)      |
|      `(5, 7, 8)`       |     206 (?)      |     206 (?)     |       205       |     206 (?)      |           -            |           -           |           -           |
|      `(5, 7, 9)`       |     231 (?)      |    231 (234)    |       229       |    229 (234)     |           -            |           -           |           -           |
|      `(5, 8, 8)`       |       230        |       230       |       230       |       230        |      2741 (2842)       |      2741 (2842)      |      2741 (2842)      |
|      `(6, 6, 6)`       |       153        |       153       |       153       |       153        |      2171 (2232)       |      2171 (2232)      |      2171 (2232)      |
|      `(6, 6, 7)`       |     185 (?)      |       183       |       183       |       183        |           -            |           -           |           -           |
|      `(6, 6, 8)`       |       203        |       203       |       203       |       203        |          1994          |         1994          |         1994          |
|      `(6, 6, 9)`       |       225        |       225       |       225       |       225        |          2440          |         2440          |         2440          |
|      `(6, 6, 10)`      |     252 (?)      |     252 (?)     |       247       |     252 (?)      |           -            |           -           |           -           |
|      `(6, 7, 7)`       |       215        |       215       |       215       |       215        |          2004          |         2004          |         2004          |
|      `(6, 7, 8)`       |       239        |       239       |       239       |       239        |      2263 (2352)       |      2263 (2352)      |      2263 (2352)      |
|      `(6, 7, 9)`       |    268 (270)     |    268 (270)    |    268 (270)    |    268 (270)     |      3062 (2917)       |      3062 (2917)      |      3062 (2917)      |
|      `(6, 8, 8)`       |       266        |       266       |       266       |       266        |          2780          |         2780          |         2780          |
|      `(7, 7, 7)`       |     250 (?)      |     250 (?)     |       249       |     248 (?)      |           -            |           -           |           -           |
|      `(7, 7, 8)`       |     279 (?)      |     279 (?)     |       277       |     275 (?)      |           -            |           -           |           -           |
|      `(7, 7, 9)`       |     316 (?)      |    316 (318)    |       315       |    313 (318)     |           -            |           -           |           -           |
|      `(7, 8, 8)`       |     310 (?)      |     310 (?)     |       306       |     302 (?)      |           -            |           -           |           -           |
|      `(8, 8, 8)`       |     343 (?)      |     343 (?)     |       336       |     329 (?)      |           -            |           -           |           -           |

## License and Citation
This project is for research purposes. Please use the following citation when referencing this code or dataset in your academic work:

```bibtex
@misc{perminov2025fastmatrixmultiplicationternary,
      title={Fast Matrix Multiplication via Ternary Meta Flip Graphs},
      author={A. I. Perminov},
      year={2025},
      eprint={2511.20317},
      archivePrefix={arXiv},
      primaryClass={cs.SC},
      url={https://arxiv.org/abs/2511.20317}
}
```