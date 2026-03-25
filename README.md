# FastMatrixMultiplication

[![arXiv:2511.20317](https://img.shields.io/badge/arXiv-2511.20317-b31b1b.svg)](https://arxiv.org/abs/2511.20317)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.13365-b31b1b.svg)](https://arxiv.org/abs/2512.13365)
[![arXiv:2512.21980](https://img.shields.io/badge/arXiv-2512.21980-b31b1b.svg)](https://arxiv.org/abs/2512.21980)
[![arXiv:2603.02398](https://img.shields.io/badge/arXiv-2603.02398-b31b1b.svg)](https://arxiv.org/abs/2603.02398)

A research project investigating fast matrix multiplication algorithms for small matrix formats, from `2×2×2` to `16×16×16`. The primary goal is to discover efficient schemes
with coefficients restricted to the ternary set `{-1, 0, 1}`, focusing on all tensor shapes satisfying `max(n₁, n₂, n₃) ≤ 16`.

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
* [Fast Matrix Multiplication in Small Formats: Discovering New Schemes with an Open-Source Flip Graph Framework](https://arxiv.org/abs/2603.02398) (arxiv)

## Key results

### New best ranks
New schemes have been discovered that improve the state-of-the-art for matrix multiplication achieving lower ranks than previously known.

|   Format   |  Prev rank  |                          New rank                          |        ω        |
|:----------:|:-----------:|:----------------------------------------------------------:|:---------------:|
|  `3×5×9`   |  104 (`Z`)  |    [102](schemes/results/ZT/3x5x9_m102_ZT.json) (`ZT`)     |   2.828571093   |
|  `3×5×10`  |  115 (`Z`)  |    [114](schemes/results/ZT/3x5x10_m114_ZT.json) (`ZT`)    |   2.835687395   |
|  `3×7×9`   |  142 (`Q`)  |    [141](schemes/results/ZT/3x7x9_m141_ZT.json) (`ZT`)     |   2.832315186   |
|  `3×7×13`  |  205 (`Q`)  |     [204](schemes/results/Q/3x7x13_m204_Q.json) (`Q`)      |   2.844182227   |
|  `3×7×15`  |  236 (`Q`)  |     [235](schemes/results/Q/3x7x15_m235_Q.json) (`Q`)      |   2.847205515   |
|  `3×9×11`  |  224 (`Q`)  |     [222](schemes/results/Q/3x9x11_m222_Q.json) (`Q`)      |   2.846644652   |
|  `3×9×13`  |  262 (`Q`)  |     [261](schemes/results/Q/3x9x13_m261_Q.json) (`Q`)      |   2.848348427   |
|  `3×9×14`  |  283 (`Q`)  |    [281](schemes/results/ZT/3x9x14_m281_ZT.json) (`ZT`)    |   2.850103717   |
| `3×10×11`  |  249 (`Q`)  |     [248](schemes/results/Q/3x10x11_m248_Q.json) (`Q`)     |   2.852219687   |
| `3×10×14`  |  314 (`Q`)  |   [312](schemes/results/ZT/3x10x14_m312_ZT.json) (`ZT`)    |   2.852364741   |
| `3×10×16`  |  360 (`Q`)  |     [357](schemes/results/Z/3x10x16_m357_Z.json) (`Z`)     |   2.856141604   |
| `3×13×13`  |  379 (`Q`)  |     [378](schemes/results/Q/3x13x13_m378_Q.json) (`Q`)     |   2.858577688   |
| `3×13×14`  |  408 (`Q`)  |     [407](schemes/results/Q/3x13x14_m407_Q.json) (`Q`)     |   2.860150618   |
| `3×13×15`  |  436 (`Q`)  |     [435](schemes/results/Q/3x13x15_m435_Q.json) (`Q`)     |   2.860506655   |
| `3×14×14`  |  440 (`Q`)  |     [438](schemes/results/Q/3x14x14_m438_Q.json) (`Q`)     |   2.861445516   |
| `3×14×15`  |  470 (`Q`)  |     [469](schemes/results/Q/3x14x15_m469_Q.json) (`Q`)     |   2.862645108   |
| `3×14×16`  |  502 (`Q`)  |     [500](schemes/results/Q/3x14x16_m500_Q.json) (`Q`)     |   2.863761055   |
| `3×16×16`  |  574 (`Q`)  |     [571](schemes/results/Q/3x16x16_m571_Q.json) (`Q`)     |   2.866160489   |
|  `4×4×10`  |  120 (`Q`)  |    [115](schemes/results/ZT/4x4x10_m115_ZT.json) (`ZT`)    | **2.804789925** |
|  `4×4×12`  |  142 (`Q`)  |    [141](schemes/results/ZT/4x4x12_m141_ZT.json) (`ZT`)    |   2.823831239   |
|  `4×4×14`  |  165 (`Q`)  |     [163](schemes/results/Q/4x4x14_m163_Q.json) (`Q`)      |   2.823771262   |
|  `4×4×15`  |  177 (`Q`)  |    [176](schemes/results/ZT/4x4x15_m176_ZT.json) (`ZT`)    |   2.830226950   |
|  `4×4×16`  |  189 (`Q`)  |    [188](schemes/results/ZT/4x4x16_m188_ZT.json) (`ZT`)    |   2.832970819   |
|  `4×5×9`   |  136 (`Q`)  |    [132](schemes/results/ZT/4x5x9_m132_ZT.json) (`ZT`)     |   2.820821776   |
|  `4×5×10`  |  151 (`Z`)  |    [146](schemes/results/ZT/4x5x10_m146_ZT.json) (`ZT`)    |   2.821805270   |
|  `4×5×11`  |  165 (`Z`)  |    [160](schemes/results/ZT/4x5x11_m160_ZT.json) (`ZT`)    |   2.822872235   |
|  `4×5×12`  |  180 (`Z`)  |    [174](schemes/results/ZT/4x5x12_m174_ZT.json) (`ZT`)    |   2.823971094   |
|  `4×5×13`  |  194 (`Z`)  |    [191](schemes/results/ZT/4x5x13_m191_ZT.json) (`ZT`)    |   2.833613095   |
|  `4×5×14`  |  208 (`Z`)  |     [206](schemes/results/Q/4x5x14_m206_Q.json) (`Q`)      |   2.836597217   |
|  `4×5×15`  |  226 (`Z`)  |    [221](schemes/results/ZT/4x5x15_m221_ZT.json) (`ZT`)    |   2.839254157   |
|  `4×5×16`  |  240 (`Q`)  |    [235](schemes/results/ZT/4x5x16_m235_ZT.json) (`ZT`)    |   2.839432229   |
|  `4×6×13`  |  228 (`Z`)  |    [227](schemes/results/ZT/4x6x13_m227_ZT.json) (`ZT`)    |   2.833857047   |
|  `4×7×8`   | 164 (`ZT`)  |   [163](schemes/results/ZT/4x7x8_m163_ZT.json) (`ZT/Z`)    |   2.823771262   |
|  `4×7×11`  |  227 (`Z`)  |    [226](schemes/results/ZT/4x7x11_m226_ZT.json) (`ZT`)    |   2.837927019   |
|  `4×9×11`  | 280 (`ZT`)  |    [279](schemes/results/ZT/4x9x11_m279_ZT.json) (`ZT`)    |   2.824354701   |
| `4×12×16`  | 520 (`ZT`)  |   [516](schemes/results/ZT/4x12x16_m516_ZT.json) (`ZT`)    |   2.820426451   |
| `4×15×15`  | 600 (`ZT`)  |     [599](schemes/results/Z/4x15x15_m599_Z.json) (`Z`)     |   2.820445661   |
| `4×15×16`  |  640 (`Q`)  |     [636](schemes/results/Q/4x15x16_m636_Q.json) (`Q`)     |   2.820122883   |
|  `5×5×9`   |  167 (`Z`)  |    [161](schemes/results/ZT/5x5x9_m161_ZT.json) (`ZT`)     |   2.814610506   |
|  `5×5×10`  |  184 (`Q`)  |    [178](schemes/results/ZT/5x5x10_m178_ZT.json) (`ZT`)    |   2.815441580   |
|  `5×5×11`  |  202 (`Q`)  |    [195](schemes/results/ZT/5x5x11_m195_ZT.json) (`ZT`)    |   2.816386568   |
|  `5×5×12`  |  220 (`Z`)  |    [207](schemes/results/ZT/5x5x12_m207_ZT.json) (`ZT`)    | **2.804832837** |
|  `5×5×13`  |  237 (`Z`)  |    [228](schemes/results/ZT/5x5x13_m228_ZT.json) (`ZT`)    |   2.816135753   |
|  `5×5×14`  |  254 (`Z`)  |    [247](schemes/results/ZT/5x5x14_m247_ZT.json) (`ZT`)    |   2.821501129   |
|  `5×5×15`  |  271 (`Q`)  |    [265](schemes/results/ZT/5x5x15_m265_ZT.json) (`ZT`)    |   2.824261583   |
|  `5×5×16`  |  288 (`Q`)  |    [283](schemes/results/ZT/5x5x16_m283_ZT.json) (`ZT`)    |   2.826744707   |
|  `5×6×9`   |  197 (`Z`)  |    [193](schemes/results/ZT/5x6x9_m193_ZT.json) (`ZT`)     |   2.820092998   |
|  `5×6×10`  |  218 (`Z`)  |    [217](schemes/results/ZT/5x6x10_m217_ZT.json) (`ZT`)    |   2.829647192   |
|  `5×7×8`   |  205 (`Q`)  |    [204](schemes/results/ZT/5x7x8_m204_ZT.json) (`ZT`)     |   2.831402964   |
|  `5×9×9`   |  294 (`Q`)  |    [293](schemes/results/ZT/5x9x9_m293_ZT.json) (`ZT`)     |   2.838247561   |
| `5×13×13`  |  588 (`Q`)  |     [587](schemes/results/Q/5x13x13_m587_Q.json) (`Q`)     |   2.837827448   |
| `5×13×14`  |  630 (`Q`)  |     [628](schemes/results/Q/5x13x14_m628_Q.json) (`Q`)     |   2.836688582   |
| `5×14×14`  |  676 (`Q`)  |  [672](schemes/results/ZT/5x14x14_m672_ZT.json) (`ZT/Z`)   |   2.835662569   |
|  `6×7×7`   | 215 (`ZT`)  |    [212](schemes/results/ZT/6x7x7_m212_ZT.json) (`ZT`)     |   2.827400948   |
|  `6×7×8`   | 239 (`ZT`)  |    [238](schemes/results/ZT/6x7x8_m238_ZT.json) (`ZT`)     |   2.822158898   |
|  `6×7×9`   | 270 (`ZT`)  |    [268](schemes/results/ZT/6x7x9_m268_ZT.json) (`ZT`)     |   2.826160061   |
|  `6×7×10`  |  296 (`Z`)  |     [293](schemes/results/Q/6x7x10_m293_Q.json) (`Q`)      |   2.821158816   |
|  `6×9×9`   |  342 (`Z`)  |      [341](schemes/results/Z/6x9x9_m341_Z.json) (`Z`)      |   2.828169642   |
|  `6×9×10`  |  373 (`Z`)  |    [371](schemes/results/ZT/6x9x10_m371_ZT.json) (`ZT`)    |   2.821014248   |
|  `6×9×12`  |  434 (`Q`)  |    [433](schemes/results/ZT/6x9x12_m433_ZT.json) (`ZT`)    |   2.813178974   |
| `6×12×15`  |  705 (`Z`)  |     [703](schemes/results/Z/6x12x15_m703_Z.json) (`Z`)     |   2.815586170   |
| `6×13×13`  |  680 (`Q`)  |     [678](schemes/results/Q/6x13x13_m678_Q.json) (`Q`)     |   2.825542860   |
| `6×13×14`  |  730 (`Q`)  |     [726](schemes/results/Q/6x13x14_m726_Q.json) (`Q`)     |   2.824944345   |
| `6×14×15`  |  825 (`Q`)  |     [818](schemes/results/Z/6x14x15_m818_Z.json) (`Z`)     |   2.818456628   |
| `6×15×15`  | 870 (`ZT`)  |   [868](schemes/results/ZT/6x15x15_m868_ZT.json) (`ZT`)    |   2.816172277   |
| `6×15×16`  |  928 (`Q`)  |     [922](schemes/results/Q/6x15x16_m922_Q.json) (`Q`)     |   2.816077251   |
| `6×16×16`  | 988 (`ZT`)  |     [985](schemes/results/Z/6x16x16_m985_Z.json) (`Z`)     |   2.818332114   |
|  `7×7×10`  |  346 (`Z`)  |     [345](schemes/results/Q/7x7x10_m345_Q.json) (`Q`)      |   2.830075228   |
|  `7×8×15`  |  571 (`Q`)  |     [570](schemes/results/Q/7x8x15_m570_Q.json) (`Q`)      |   2.827234938   |
|  `7×9×11`  |  480 (`Q`)  |    [478](schemes/results/ZT/7x9x11_m478_ZT.json) (`ZT`)    |   2.829651018   |
|  `7×9×15`  |  639 (`Z`)  |     [634](schemes/results/Q/7x9x15_m634_Q.json) (`Q`)      |   2.825226157   |
| `7×10×15`  |  711 (`Q`)  |  [703](schemes/results/ZT/7x10x15_m703_ZT.json) (`ZT/Z`)   |   2.826988027   |
| `7×10×16`  |  752 (`Q`)  |  [742](schemes/results/ZT/7x10x16_m742_ZT.json) (`ZT/Z`)   |   2.824072156   |
| `7×11×15`  |  778 (`Z`)  |     [777](schemes/results/Q/7x11x15_m777_Q.json) (`Q`)     |   2.831357038   |
| `7×11×16`  |  827 (`Q`)  |  [822](schemes/results/ZT/7x11x16_m822_ZT.json) (`ZT/Z`)   |   2.829413433   |
| `7×13×13`  |  795 (`Q`)  |     [794](schemes/results/Q/7x13x13_m794_Q.json) (`Q`)     |   2.830948485   |
| `7×13×14`  |  852 (`Q`)  |     [850](schemes/results/Q/7x13x14_m850_Q.json) (`Q`)     |   2.830202017   |
| `7×13×16`  |  968 (`Q`)  |     [966](schemes/results/Q/7x13x16_m966_Q.json) (`Q`)     |   2.831006805   |
| `7×14×14`  |  912 (`Q`)  |  [909](schemes/results/ZT/7x14x14_m909_ZT.json) (`ZT/Z`)   |   2.829037251   |
| `7×14×15`  |  976 (`Z`)  |  [969](schemes/results/ZT/7x14x15_m969_ZT.json) (`ZT/Z`)   |   2.828567644   |
| `7×14×16`  | 1034 (`Q`)  |    [1030](schemes/results/Q/7x14x16_m1030_Q.json) (`Q`)    |   2.828648763   |
|  `8×8×15`  |  635 (`Q`)  |     [628](schemes/results/Q/8x8x15_m628_Q.json) (`Q`)      |   2.814592730   |
|  `8×8×16`  |  672 (`Q`)  |     [671](schemes/results/Q/8x8x16_m671_Q.json) (`Q`)      |   2.817050687   |
|  `8×9×11`  |  533 (`Q`)  |    [531](schemes/results/ZT/8x9x11_m531_ZT.json) (`ZT`)    |   2.820303082   |
|  `8×9×14`  |  669 (`Z`)  |    [666](schemes/results/ZT/8x9x14_m666_ZT.json) (`ZT`)    |   2.820221074   |
|  `8×9×15`  |  705 (`Z`)  |     [703](schemes/results/Z/8x9x15_m703_Z.json) (`Z`)      |   2.815586170   |
| `8×10×12`  |  630 (`Z`)  |     [628](schemes/results/Q/8x10x12_m628_Q.json) (`Q`)     |   2.814592730   |
| `8×10×15`  |  789 (`Z`)  |   [784](schemes/results/ZT/8x10x15_m784_ZT.json) (`ZT`)    |   2.819888631   |
| `8×10×16`  |  832 (`Q`)  |   [826](schemes/results/ZT/8x10x16_m826_ZT.json) (`ZT`)    |   2.816333697   |
| `8×11×16`  |  920 (`Q`)  |   [914](schemes/results/ZT/8x11x16_m914_ZT.json) (`ZT`)    |   2.821200247   |
| `8×12×15`  | 915 (`ZT`)  |   [914](schemes/results/ZT/8x12x15_m914_ZT.json) (`ZT`)    |   2.812482294   |
| `8×15×15`  | 1140 (`ZT`) |    [1137](schemes/results/Z/8x15x15_m1137_Z.json) (`Z`)    |   2.816133328   |
|  `9×9×9`   | 498 (`ZT`)  |    [486](schemes/results/ZT/9x9x9_m486_ZT.json) (`ZT`)     |   2.815464877   |
|  `9×9×14`  |  726 (`Q`)  |     [725](schemes/results/Z/9x9x14_m725_Z.json) (`Z`)      |   2.809198372   |
| `9×10×10`  |  600 (`Z`)  |   [597](schemes/results/ZT/9x10x10_m597_ZT.json) (`ZT`)    |   2.818970672   |
| `9×10×13`  |  772 (`Z`)  |     [765](schemes/results/Q/9x10x13_m765_Q.json) (`Q`)     |   2.819576354   |
| `9×10×14`  |  820 (`Z`)  |     [819](schemes/results/Q/9x10x14_m819_Q.json) (`Q`)     |   2.818970048   |
| `9×10×15`  | 870 (`ZT`)  |     [866](schemes/results/Z/9x10x15_m866_Z.json) (`Z`)     |   2.815212156   |
| `9×10×16`  |  939 (`Q`)  |   [924](schemes/results/ZT/9x10x16_m924_ZT.json) (`ZT`)    |   2.816971116   |
| `9×11×11`  |  725 (`Q`)  |     [715](schemes/results/Q/9x11x11_m715_Q.json) (`Q`)     |   2.819505933   |
| `9×11×12`  |  760 (`Q`)  |     [754](schemes/results/Q/9x11x12_m754_Q.json) (`Q`)     |   2.807359140   |
| `9×11×13`  |  849 (`Z`)  |     [835](schemes/results/Q/9x11x13_m835_Q.json) (`Q`)     |   2.818729064   |
| `9×11×14`  |  904 (`Z`)  |     [889](schemes/results/Q/9x11x14_m889_Q.json) (`Q`)     |   2.815840862   |
| `9×11×15`  |  981 (`Q`)  |  [960](schemes/results/ZT/9x11x15_m960_ZT.json) (`ZT/Z`)   |   2.820802434   |
| `9×11×16`  | 1030 (`Z`)  |    [1023](schemes/results/Q/9x11x16_m1023_Q.json) (`Q`)    |   2.821974308   |
| `9×12×13`  |  900 (`Q`)  |     [884](schemes/results/Q/9x12x13_m884_Q.json) (`Q`)     |   2.808492461   |
| `9×12×16`  | 1080 (`Q`)  |    [1072](schemes/results/Q/9x12x16_m1072_Q.json) (`Q`)    |   2.807864570   |
| `9×13×13`  |  996 (`Z`)  |     [981](schemes/results/Q/9x13x13_m981_Q.json) (`Q`)     |   2.820440786   |
| `9×13×14`  | 1063 (`Z`)  |    [1041](schemes/results/Q/9x13x14_m1041_Q.json) (`Q`)    |   2.816262654   |
| `9×13×15`  | 1135 (`Q`)  | [1119](schemes/results/ZT/9x13x15_m1119_ZT.json) (`ZT/Z`)  |   2.819269106   |
| `9×13×16`  | 1210 (`Z`)  |    [1183](schemes/results/Q/9x13x16_m1183_Q.json) (`Q`)    |   2.817265461   |
| `9×14×14`  | 1136 (`Z`)  |    [1121](schemes/results/Q/9x14x14_m1121_Q.json) (`Q`)    |   2.818056626   |
| `9×14×15`  | 1185 (`Q`)  |    [1182](schemes/results/Q/9x14x15_m1182_Q.json) (`Q`)    |   2.813355681   |
| `9×15×15`  | 1290 (`Q`)  | [1284](schemes/results/ZT/9x15x15_m1284_ZT.json) (`ZT/Z`)  |   2.820476797   |
| `9×15×16`  | 1350 (`Z`)  |    [1341](schemes/results/Q/9x15x16_m1341_Q.json) (`Q`)    |   2.813740131   |
| `9×16×16`  | 1444 (`ZT`) |    [1431](schemes/results/Q/9x16x16_m1431_Q.json) (`Q`)    |   2.815455240   |
| `10×10×12` |  770 (`Z`)  |   [768](schemes/results/ZT/10x10x12_m768_ZT.json) (`ZT`)   |   2.811164062   |
| `10×11×15` | 1067 (`Q`)  |  [1055](schemes/results/ZT/10x11x15_m1055_ZT.json) (`ZT`)  |   2.818897479   |
| `10×11×16` | 1136 (`Q`)  |  [1112](schemes/results/ZT/10x11x16_m1112_ZT.json) (`ZT`)  |   2.815676689   |
| `10×12×15` | 1140 (`ZT`) |   [1122](schemes/results/Z/10x12x15_m1122_Z.json) (`Z`)    |   2.810818006   |
| `10×12×16` | 1216 (`Q`)  |  [1190](schemes/results/ZT/10x12x16_m1190_ZT.json) (`ZT`)  |   2.810171910   |
| `10×13×16` | 1332 (`Z`)  |  [1326](schemes/results/ZT/10x13x16_m1326_ZT.json) (`ZT`)  |   2.823222352   |
| `10×15×15` | 1395 (`Z`)  |   [1389](schemes/results/Z/10x15x15_m1389_Z.json) (`Z`)    |   2.812527864   |
| `10×15×16` | 1497 (`Z`)  |   [1484](schemes/results/Z/10x15x16_m1484_Z.json) (`Z`)    |   2.814706248   |
| `10×16×16` | 1586 (`ZT`) |  [1585](schemes/results/ZT/10x16x16_m1585_ZT.json) (`ZT`)  |   2.816728839   |
| `11×11×15` | 1181 (`Z`)  |  [1169](schemes/results/ZT/11x11x15_m1169_ZT.json) (`ZT`)  |   2.824115356   |
| `11×11×16` | 1236 (`Q`)  |  [1230](schemes/results/ZT/11x11x16_m1230_ZT.json) (`ZT`)  |   2.820195393   |
| `11×12×13` | 1102 (`Z`)  |   [1092](schemes/results/Q/11x12x13_m1092_Q.json) (`Q`)    |   2.817937614   |
| `11×12×15` | 1264 (`Q`)  |   [1240](schemes/results/Q/11x12x15_m1240_Q.json) (`Q`)    |   2.815046272   |
| `11×13×13` | 1210 (`Z`)  |  [1205](schemes/results/ZT/11x13x13_m1205_ZT.json) (`ZT`)  |   2.827216655   |
| `11×13×14` | 1298 (`Z`)  |  [1292](schemes/results/ZT/11x13x14_m1292_ZT.json) (`ZT`)  |   2.827166171   |
| `11×13×16` | 1472 (`Z`)  |   [1452](schemes/results/Q/11x13x16_m1452_Q.json) (`Q`)    |   2.823641623   |
| `11×14×14` | 1388 (`Z`)  |  [1376](schemes/results/ZT/11x14x14_m1376_ZT.json) (`ZT`)  |   2.824489318   |
| `11×14×15` | 1471 (`Z`)  | [1460](schemes/results/ZT/11x14x15_m1460_ZT.json) (`ZT/Z`) |   2.822281114   |
| `11×14×16` | 1571 (`Q`)  |   [1548](schemes/results/Q/11x14x16_m1548_Q.json) (`Q`)    |   2.821440626   |
| `12×12×14` | 1250 (`Q`)  |   [1234](schemes/results/Q/12x12x14_m1234_Q.json) (`Q`)    | **2.806467563** |
| `12×13×16` | 1556 (`Q`)  | [1548](schemes/results/ZT/12x13x16_m1548_ZT.json) (`ZT/Q`) |   2.816786558   |
| `12×14×15` | 1540 (`Q`)  |   [1538](schemes/results/Q/12x14x15_m1538_Q.json) (`Q`)    |   2.810862435   |
| `13×13×13` | 1426 (`Q`)  |   [1421](schemes/results/Q/13x13x13_m1421_Q.json) (`Q`)    |   2.830120644   |
| `13×13×14` | 1524 (`Z`)  |  [1511](schemes/results/ZT/13x13x14_m1511_ZT.json) (`ZT`)  |   2.826838093   |
| `13×13×16` | 1713 (`Q`)  |   [1704](schemes/results/Q/13x13x16_m1704_Q.json) (`Q`)    |   2.824705676   |
| `13×14×14` | 1625 (`Z`)  |  [1614](schemes/results/ZT/13x14x14_m1614_ZT.json) (`ZT`)  |   2.825351482   |
| `13×14×15` | 1714 (`Z`)  |  [1698](schemes/results/ZT/13x14x15_m1698_ZT.json) (`ZT`)  |   2.819951805   |
| `13×14×16` | 1825 (`Q`)  |   [1806](schemes/results/Q/13x14x16_m1806_Q.json) (`Q`)    |   2.820327226   |
| `13×15×16` | 1932 (`Z`)  |   [1908](schemes/results/Q/13x15x16_m1908_Q.json) (`Q`)    |   2.816628414   |
| `14×14×16` | 1939 (`Q`)  |   [1938](schemes/results/Q/14x14x16_m1938_Q.json) (`Q`)    |   2.820652346   |
| `14×15×15` | 1905 (`Z`)  |   [1895](schemes/results/Z/14x15x15_m1895_Z.json) (`Z`)    |   2.810736066   |
| `15×15×16` | 2173 (`Q`)  |   [2132](schemes/results/Z/15x15x16_m2132_Z.json) (`Z`)    |   2.808074285   |


### Rediscovery in the ternary coefficient set (`ZT`)
The following schemes have been rediscovered in the `ZT` format. Originally known over the rational (`Q`) or integer (`Z`) fields, implementations
with coefficients restricted to the ternary set were previously unknown.

|   Format   |                        Rank                        | Known ring |
|:----------:|:--------------------------------------------------:|:----------:|
|  `2×3×10`  |    [50](schemes/results/ZT/2x3x10_m50_ZT.json)     |    `Z`     |
|  `2×3×13`  |    [65](schemes/results/ZT/2x3x13_m65_ZT.json)     |    `Z`     |
|  `2×3×15`  |    [75](schemes/results/ZT/2x3x15_m75_ZT.json)     |    `Z`     |
|  `2×4×6`   |     [39](schemes/results/ZT/2x4x6_m39_ZT.json)     |    `Z`     |
|  `2×4×11`  |    [71](schemes/results/ZT/2x4x11_m71_ZT.json)     |    `Q`     |
|  `2×4×12`  |    [77](schemes/results/ZT/2x4x12_m77_ZT.json)     |    `Q`     |
|  `2×4×15`  |    [96](schemes/results/ZT/2x4x15_m96_ZT.json)     |    `Q`     |
|  `2×5×7`   |     [55](schemes/results/ZT/2x5x7_m55_ZT.json)     |    `Q`     |
|  `2×5×8`   |     [63](schemes/results/ZT/2x5x8_m63_ZT.json)     |    `Q`     |
|  `2×5×9`   |     [72](schemes/results/ZT/2x5x9_m72_ZT.json)     |    `Q`     |
|  `2×5×13`  |   [102](schemes/results/ZT/2x5x13_m102_ZT.json)    |    `Q`     |
|  `2×5×14`  |   [110](schemes/results/ZT/2x5x14_m110_ZT.json)    |    `Q`     |
|  `2×5×15`  |   [118](schemes/results/ZT/2x5x15_m118_ZT.json)    |    `Q`     |
|  `2×5×16`  |   [126](schemes/results/ZT/2x5x16_m126_ZT.json)    |    `Q`     |
|  `2×6×6`   |     [56](schemes/results/ZT/2x6x6_m56_ZT.json)     |    `Z`     |
|  `2×6×7`   |     [66](schemes/results/ZT/2x6x7_m66_ZT.json)     |   `Z/Q`    |
|  `2×6×8`   |     [75](schemes/results/ZT/2x6x8_m75_ZT.json)     |    `Q`     |
|  `2×6×9`   |     [86](schemes/results/ZT/2x6x9_m86_ZT.json)     |    `Z`     |
|  `2×6×11`  |   [103](schemes/results/ZT/2x6x11_m103_ZT.json)    |    `Z`     |
|  `2×6×12`  |   [112](schemes/results/ZT/2x6x12_m112_ZT.json)    |    `Z`     |
|  `2×6×13`  |   [122](schemes/results/ZT/2x6x13_m122_ZT.json)    |    `Q`     |
|  `2×6×14`  |   [131](schemes/results/ZT/2x6x14_m131_ZT.json)    |    `Q`     |
|  `2×6×16`  |   [150](schemes/results/ZT/2x6x16_m150_ZT.json)    |    `Z`     |
|  `2×7×7`   |     [76](schemes/results/ZT/2x7x7_m76_ZT.json)     |    `Q`     |
|  `2×7×8`   |     [88](schemes/results/ZT/2x7x8_m88_ZT.json)     |    `Z`     |
|  `2×7×10`  |   [110](schemes/results/ZT/2x7x10_m110_ZT.json)    |    `Z`     |
|  `2×7×11`  |   [121](schemes/results/ZT/2x7x11_m121_ZT.json)    |    `Z`     |
|  `2×7×12`  |   [131](schemes/results/ZT/2x7x12_m131_ZT.json)    |    `Q`     |
|  `2×7×13`  |   [142](schemes/results/ZT/2x7x13_m142_ZT.json)    |    `Q`     |
|  `2×7×14`  |   [152](schemes/results/ZT/2x7x14_m152_ZT.json)    |    `Q`     |
|  `2×7×15`  |   [164](schemes/results/ZT/2x7x15_m164_ZT.json)    |    `Q`     |
|  `2×8×9`   |    [113](schemes/results/ZT/2x8x9_m113_ZT.json)    |    `Q`     |
|  `2×8×11`  |   [138](schemes/results/ZT/2x8x11_m138_ZT.json)    |    `Z`     |
|  `2×8×12`  |   [150](schemes/results/ZT/2x8x12_m150_ZT.json)    |    `Z`     |
|  `2×8×14`  |   [175](schemes/results/ZT/2x8x14_m175_ZT.json)    |    `Q`     |
|  `2×8×15`  |   [188](schemes/results/ZT/2x8x15_m188_ZT.json)    |    `Z`     |
|  `3×3×7`   |     [49](schemes/results/ZT/3x3x7_m49_ZT.json)     |    `Q`     |
|  `3×3×9`   |     [63](schemes/results/ZT/3x3x9_m63_ZT.json)     |    `Q`     |
|  `3×4×5`   |     [47](schemes/results/ZT/3x4x5_m47_ZT.json)     |    `Z`     |
|  `3×4×6`   |     [54](schemes/results/ZT/3x4x6_m54_ZT.json)     |   `Z/Q`    |
|  `3×4×8`   |     [73](schemes/results/ZT/3x4x8_m73_ZT.json)     |    `Q`     |
|  `3×4×9`   |     [83](schemes/results/ZT/3x4x9_m83_ZT.json)     |    `Q`     |
|  `3×4×10`  |    [92](schemes/results/ZT/3x4x10_m92_ZT.json)     |    `Q`     |
|  `3×4×11`  |   [101](schemes/results/ZT/3x4x11_m101_ZT.json)    |    `Q`     |
|  `3×4×12`  |   [108](schemes/results/ZT/3x4x12_m108_ZT.json)    |    `Q`     |
|  `3×4×16`  |   [146](schemes/results/ZT/3x4x16_m146_ZT.json)    |    `Q`     |
|  `3×5×6`   |     [68](schemes/results/ZT/3x5x6_m68_ZT.json)     |    `Z`     |
|  `3×5×7`   |     [79](schemes/results/ZT/3x5x7_m79_ZT.json)     |    `Q`     |
|  `3×5×8`   |     [90](schemes/results/ZT/3x5x8_m90_ZT.json)     |   `Z/Q`    |
|  `3×5×11`  |   [126](schemes/results/ZT/3x5x11_m126_ZT.json)    |    `Z`     |
|  `3×5×12`  |   [136](schemes/results/ZT/3x5x12_m136_ZT.json)    |    `Z`     |
|  `3×5×13`  |   [147](schemes/results/ZT/3x5x13_m147_ZT.json)    |    `Q`     |
|  `3×5×14`  |   [158](schemes/results/ZT/3x5x14_m158_ZT.json)    |    `Q`     |
|  `3×5×15`  |   [169](schemes/results/ZT/3x5x15_m169_ZT.json)    |    `Q`     |
|  `3×5×16`  |   [180](schemes/results/ZT/3x5x16_m180_ZT.json)    |    `Z`     |
|  `3×6×8`   |    [108](schemes/results/ZT/3x6x8_m108_ZT.json)    |   `Z/Q`    |
|  `3×7×7`   |    [111](schemes/results/ZT/3x7x7_m111_ZT.json)    |    `Q`     |
|  `3×7×14`  |   [220](schemes/results/ZT/3x7x14_m220_ZT.json)    |    `Q`     |
|  `3×8×9`   |    [163](schemes/results/ZT/3x8x9_m163_ZT.json)    |    `Q`     |
|  `3×8×10`  |   [180](schemes/results/ZT/3x8x10_m180_ZT.json)    |    `Z`     |
|  `3×8×11`  |   [198](schemes/results/ZT/3x8x11_m198_ZT.json)    |    `Q`     |
|  `3×8×12`  |   [216](schemes/results/ZT/3x8x12_m216_ZT.json)    |    `Q`     |
|  `3×8×15`  |   [270](schemes/results/ZT/3x8x15_m270_ZT.json)    |    `Z`     |
|  `3×8×16`  |   [288](schemes/results/ZT/3x8x16_m288_ZT.json)    |    `Q`     |
|  `4×4×6`   |     [73](schemes/results/ZT/4x4x6_m73_ZT.json)     |   `Z/Q`    |
|  `4×4×8`   |     [96](schemes/results/ZT/4x4x8_m96_ZT.json)     |    `Q`     |
|  `4×4×11`  |   [130](schemes/results/ZT/4x4x11_m130_ZT.json)    |    `Q`     |
|  `4×5×6`   |     [90](schemes/results/ZT/4x5x6_m90_ZT.json)     |    `Z`     |
|  `4×5×7`   |    [104](schemes/results/ZT/4x5x7_m104_ZT.json)    |   `Z/Q`    |
|  `4×5×8`   |    [118](schemes/results/ZT/4x5x8_m118_ZT.json)    |   `Z/Q`    |
|  `4×6×7`   |    [123](schemes/results/ZT/4x6x7_m123_ZT.json)    |   `Z/Q`    |
|  `4×6×9`   |    [159](schemes/results/ZT/4x6x9_m159_ZT.json)    |    `Q`     |
|  `4×6×10`  |   [175](schemes/results/ZT/4x6x10_m175_ZT.json)    |    `Z`     |
|  `4×6×11`  |   [194](schemes/results/ZT/4x6x11_m194_ZT.json)    |    `Q`     |
|  `4×6×15`  |   [263](schemes/results/ZT/4x6x15_m263_ZT.json)    |    `Z`     |
|  `4×7×7`   |    [144](schemes/results/ZT/4x7x7_m144_ZT.json)    |   `Z/Q`    |
|  `4×7×12`  |   [246](schemes/results/ZT/4x7x12_m246_ZT.json)    |    `Z`     |
|  `4×7×15`  |   [307](schemes/results/ZT/4x7x15_m307_ZT.json)    |    `Q`     |
|  `4×8×13`  |   [297](schemes/results/ZT/4x8x13_m297_ZT.json)    |    `Z`     |
|  `4×9×14`  |   [355](schemes/results/ZT/4x9x14_m355_ZT.json)    |    `Z`     |
|  `4×9×15`  |   [375](schemes/results/ZT/4x9x15_m375_ZT.json)    |    `Z`     |
| `4×10×13`  |   [361](schemes/results/ZT/4x10x13_m361_ZT.json)   |    `Q`     |
| `4×10×14`  |   [385](schemes/results/ZT/4x10x14_m385_ZT.json)   |    `Q`     |
| `4×10×15`  |   [417](schemes/results/ZT/4x10x15_m417_ZT.json)   |    `Q`     |
| `4×10×16`  |   [441](schemes/results/ZT/4x10x16_m441_ZT.json)   |    `Q`     |
| `4×11×11`  |   [340](schemes/results/ZT/4x11x11_m340_ZT.json)   |    `Z`     |
| `4×11×12`  |   [365](schemes/results/ZT/4x11x12_m365_ZT.json)   |    `Z`     |
| `4×11×14`  |   [429](schemes/results/ZT/4x11x14_m429_ZT.json)   |    `Q`     |
| `4×11×16`  |   [489](schemes/results/ZT/4x11x16_m489_ZT.json)   |    `Q`     |
| `4×14×14`  |   [532](schemes/results/ZT/4x14x14_m532_ZT.json)   |    `Q`     |
|  `5×5×6`   |    [110](schemes/results/ZT/5x5x6_m110_ZT.json)    |   `Z/Q`    |
|  `5×5×7`   |    [127](schemes/results/ZT/5x5x7_m127_ZT.json)    |   `Z/Q`    |
|  `5×5×8`   |    [144](schemes/results/ZT/5x5x8_m144_ZT.json)    |   `Z/Q`    |
|  `5×6×6`   |    [130](schemes/results/ZT/5x6x6_m130_ZT.json)    |   `Z/Q`    |
|  `5×6×7`   |    [150](schemes/results/ZT/5x6x7_m150_ZT.json)    |   `Z/Q`    |
|  `5×6×8`   |    [170](schemes/results/ZT/5x6x8_m170_ZT.json)    |   `Z/Q`    |
|  `5×6×16`  |   [340](schemes/results/ZT/5x6x16_m340_ZT.json)    |    `Q`     |
|  `5×7×7`   |    [176](schemes/results/ZT/5x7x7_m176_ZT.json)    |   `Z/Q`    |
|  `5×7×9`   |    [229](schemes/results/ZT/5x7x9_m229_ZT.json)    |    `Q`     |
|  `5×7×10`  |   [254](schemes/results/ZT/5x7x10_m254_ZT.json)    |    `Z`     |
|  `5×7×11`  |   [277](schemes/results/ZT/5x7x11_m277_ZT.json)    |    `Z`     |
|  `5×7×13`  |   [325](schemes/results/ZT/5x7x13_m325_ZT.json)    |    `Q`     |
|  `5×8×9`   |    [260](schemes/results/ZT/5x8x9_m260_ZT.json)    |    `Q`     |
|  `5×8×12`  |   [333](schemes/results/ZT/5x8x12_m333_ZT.json)    |    `Q`     |
|  `5×8×16`  |   [445](schemes/results/ZT/5x8x16_m445_ZT.json)    |    `Q`     |
|  `5×9×10`  |   [322](schemes/results/ZT/5x9x10_m322_ZT.json)    |    `Q`     |
|  `5×9×11`  |   [353](schemes/results/ZT/5x9x11_m353_ZT.json)    |    `Q`     |
|  `5×9×12`  |   [377](schemes/results/ZT/5x9x12_m377_ZT.json)    |    `Q`     |
|  `5×9×15`  |   [474](schemes/results/ZT/5x9x15_m474_ZT.json)    |    `Z`     |
| `5×10×11`  |   [386](schemes/results/ZT/5x10x11_m386_ZT.json)   |    `Z`     |
| `5×10×12`  |   [413](schemes/results/ZT/5x10x12_m413_ZT.json)   |    `Z`     |
| `5×10×13`  |   [451](schemes/results/ZT/5x10x13_m451_ZT.json)   |    `Q`     |
| `5×10×14`  |   [481](schemes/results/ZT/5x10x14_m481_ZT.json)   |    `Q`     |
| `5×10×15`  |   [519](schemes/results/ZT/5x10x15_m519_ZT.json)   |    `Q`     |
| `5×10×16`  |   [549](schemes/results/ZT/5x10x16_m549_ZT.json)   |    `Q`     |
| `5×11×16`  |   [609](schemes/results/ZT/5x11x16_m609_ZT.json)   |    `Q`     |
| `5×15×16`  |   [813](schemes/results/ZT/5x15x16_m813_ZT.json)   |    `Z`     |
|  `6×6×7`   |    [183](schemes/results/ZT/6x6x7_m183_ZT.json)    |   `Z/Q`    |
|  `6×8×10`  |   [329](schemes/results/ZT/6x8x10_m329_ZT.json)    |    `Z`     |
|  `6×8×11`  |   [357](schemes/results/ZT/6x8x11_m357_ZT.json)    |    `Q`     |
|  `6×8×12`  |   [378](schemes/results/ZT/6x8x12_m378_ZT.json)    |    `Q`     |
|  `6×8×16`  |   [511](schemes/results/ZT/6x8x16_m511_ZT.json)    |    `Q`     |
|  `6×9×11`  |   [407](schemes/results/ZT/6x9x11_m407_ZT.json)    |    `Q`     |
| `6×10×11`  |   [446](schemes/results/ZT/6x10x11_m446_ZT.json)   |    `Z`     |
| `6×10×12`  |   [476](schemes/results/ZT/6x10x12_m476_ZT.json)   |    `Z`     |
| `6×10×13`  |   [520](schemes/results/ZT/6x10x13_m520_ZT.json)   |    `Q`     |
| `6×10×14`  |   [553](schemes/results/ZT/6x10x14_m553_ZT.json)   |    `Q`     |
| `6×10×15`  |   [597](schemes/results/ZT/6x10x15_m597_ZT.json)   |    `Q`     |
| `6×10×16`  |   [630](schemes/results/ZT/6x10x16_m630_ZT.json)   |    `Q`     |
| `6×11×15`  |   [661](schemes/results/ZT/6x11x15_m661_ZT.json)   |    `Z`     |
| `6×12×16`  |   [746](schemes/results/ZT/6x12x16_m746_ZT.json)   |    `Q`     |
| `6×13×15`  |   [771](schemes/results/ZT/6x13x15_m771_ZT.json)   |    `Z`     |
| `6×13×16`  |   [819](schemes/results/ZT/6x13x16_m819_ZT.json)   |    `Q`     |
| `6×14×14`  |   [777](schemes/results/ZT/6x14x14_m777_ZT.json)   |    `Q`     |
| `6×14×16`  |   [880](schemes/results/ZT/6x14x16_m880_ZT.json)   |    `Q`     |
|  `7×8×10`  |   [385](schemes/results/ZT/7x8x10_m385_ZT.json)    |    `Z`     |
|  `7×8×11`  |   [423](schemes/results/ZT/7x8x11_m423_ZT.json)    |    `Q`     |
|  `7×8×12`  |   [454](schemes/results/ZT/7x8x12_m454_ZT.json)    |    `Q`     |
|  `7×8×16`  |   [603](schemes/results/ZT/7x8x16_m603_ZT.json)    |    `Q`     |
|  `7×9×10`  |   [437](schemes/results/ZT/7x9x10_m437_ZT.json)    |    `Z`     |
| `7×10×11`  |   [526](schemes/results/ZT/7x10x11_m526_ZT.json)   |    `Z`     |
| `7×10×12`  |   [564](schemes/results/ZT/7x10x12_m564_ZT.json)   |    `Z`     |
| `7×10×13`  |   [614](schemes/results/ZT/7x10x13_m614_ZT.json)   |    `Q`     |
| `7×10×14`  |   [653](schemes/results/ZT/7x10x14_m653_ZT.json)   |    `Q`     |
| `7×12×15`  |   [831](schemes/results/ZT/7x12x15_m831_ZT.json)   |    `Z`     |
| `7×13×15`  |   [909](schemes/results/ZT/7x13x15_m909_ZT.json)   |    `Z`     |
|  `8×8×11`  |   [475](schemes/results/ZT/8x8x11_m475_ZT.json)    |    `Q`     |
|  `8×8×13`  |   [559](schemes/results/ZT/8x8x13_m559_ZT.json)    |    `Q`     |
|  `8×9×13`  |   [624](schemes/results/ZT/8x9x13_m624_ZT.json)    |    `Z`     |
|  `8×9×16`  |   [746](schemes/results/ZT/8x9x16_m746_ZT.json)    |    `Q`     |
| `8×10×11`  |   [588](schemes/results/ZT/8x10x11_m588_ZT.json)   |    `Z`     |
| `8×10×13`  |   [686](schemes/results/ZT/8x10x13_m686_ZT.json)   |    `Z`     |
| `8×10×14`  |   [728](schemes/results/ZT/8x10x14_m728_ZT.json)   |    `Z`     |
| `8×11×14`  |   [804](schemes/results/ZT/8x11x14_m804_ZT.json)   |    `Z`     |
| `8×11×15`  |   [859](schemes/results/ZT/8x11x15_m859_ZT.json)   |    `Z`     |
| `8×12×14`  |   [861](schemes/results/ZT/8x12x14_m861_ZT.json)   |    `Z`     |
| `8×13×14`  |   [945](schemes/results/ZT/8x13x14_m945_ZT.json)   |    `Z`     |
| `8×14×14`  |  [1008](schemes/results/ZT/8x14x14_m1008_ZT.json)  |    `Z`     |
| `10×10×10` |  [651](schemes/results/ZT/10x10x10_m651_ZT.json)   |    `Z`     |
| `10×10×11` |  [719](schemes/results/ZT/10x10x11_m719_ZT.json)   |    `Z`     |
| `10×10×13` |  [838](schemes/results/ZT/10x10x13_m838_ZT.json)   |    `Z`     |
| `10×10×14` |  [889](schemes/results/ZT/10x10x14_m889_ZT.json)   |    `Z`     |
| `10×10×15` |  [957](schemes/results/ZT/10x10x15_m957_ZT.json)   |    `Q`     |
| `10×10×16` | [1008](schemes/results/ZT/10x10x16_m1008_ZT.json)  |    `Q`     |
| `10×11×11` |  [793](schemes/results/ZT/10x11x11_m793_ZT.json)   |    `Z`     |
| `10×11×12` |  [850](schemes/results/ZT/10x11x12_m850_ZT.json)   |    `Z`     |
| `10×11×13` |  [924](schemes/results/ZT/10x11x13_m924_ZT.json)   |    `Z`     |
| `10×11×14` |  [981](schemes/results/ZT/10x11x14_m981_ZT.json)   |    `Z`     |
| `10×12×12` |  [910](schemes/results/ZT/10x12x12_m910_ZT.json)   |    `Z`     |
| `10×12×13` |  [990](schemes/results/ZT/10x12x13_m990_ZT.json)   |    `Z`     |
| `10×12×14` | [1050](schemes/results/ZT/10x12x14_m1050_ZT.json)  |    `Z`     |
| `10×13×13` | [1082](schemes/results/ZT/10x13x13_m1082_ZT.json)  |    `Z`     |
| `10×13×14` | [1154](schemes/results/ZT/10x13x14_m1154_ZT.json)  |    `Z`     |
| `10×13×15` | [1242](schemes/results/ZT/10x13x15_m1242_ZT.json)  |    `Z`     |
| `10×14×14` | [1232](schemes/results/ZT/10x14x14_m1232_ZT.json)  |    `Z`     |
| `10×14×15` | [1327](schemes/results/ZT/10x14x15_m1327_ZT.json)  |    `Z`     |
| `10×14×16` | [1423](schemes/results/ZT/10x14x16_m1423_ZT.json)  |    `Z`     |
| `11×11×11` |  [873](schemes/results/ZT/11x11x11_m873_ZT.json)   |    `Z`     |
| `11×11×12` |  [936](schemes/results/ZT/11x11x12_m936_ZT.json)   |    `Z`     |
| `11×11×13` | [1023](schemes/results/ZT/11x11x13_m1023_ZT.json)  |    `Z`     |
| `11×11×14` | [1093](schemes/results/ZT/11x11x14_m1093_ZT.json)  |    `Z`     |
| `11×12×14` | [1182](schemes/results/ZT/11x12x14_m1182_ZT.json)  |    `Z`     |
| `11×13×15` | [1377](schemes/results/ZT/11x13x15_m1377_ZT.json)  |    `Z`     |
| `13×13×15` | [1605](schemes/results/ZT/13x13x15_m1605_ZT.json)  |    `Z`     |
| `13×15×15` | [1803](schemes/results/ZT/13x15x15_m1803_ZT.json)  |    `Z`     |
| `14×14×15` | [1813](schemes/results/ZT/14x14x15_m1813_ZT.json)  |    `Z`     |
| `15×15×15` | [2058](schemes/results/ZT/15x15x15_m2058_ZT.json)  |    `Q`     |


### Rediscovery in the integer ring (`Z`)
The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).
Implementations restricted to integer coefficients were previously unknown.

|   Format   |                       Rank                       |
|:----------:|:------------------------------------------------:|
|  `2×7×9`   |     [99](schemes/results/Z/2x7x9_m99_Z.json)     |
|  `2×7×16`  |   [175](schemes/results/Z/2x7x16_m175_Z.json)    |
| `2×11×12`  |   [204](schemes/results/Z/2x11x12_m204_Z.json)   |
| `2×11×13`  |   [221](schemes/results/Z/2x11x13_m221_Z.json)   |
| `2×11×14`  |   [238](schemes/results/Z/2x11x14_m238_Z.json)   |
| `2×13×15`  |   [300](schemes/results/Z/2x13x15_m300_Z.json)   |
| `2×13×16`  |   [320](schemes/results/Z/2x13x16_m320_Z.json)   |
| `2×15×16`  |   [368](schemes/results/Z/2x15x16_m368_Z.json)   |

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
Scheme `2×2×2:7`:

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
Reduces `2×2×2:7` from 24 to 15 additions:
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
scheme.save_tensor_mpl("scheme.tensor.mpl")  # save in tensor.mpl format
```


## Research Findings & Status

The table below summarizes the current state of researched matrix multiplication schemes. It highlights where ternary schemes (ZT) match or approximate the known minimal ranks
from other fields. The best ranks of previously known schemes are given in brackets.

|   Format   |  `ZT` rank  |   `Z` rank   |   `Q` rank   |        ω        |
|:----------:|:-----------:|:------------:|:------------:|:---------------:|
|  `2×2×2`   |      7      |      7       |      7       |   2.807354922   |
|  `2×2×3`   |     11      |      11      |      11      |   2.894952138   |
|  `2×2×4`   |     14      |      14      |      14      |   2.855516192   |
|  `2×2×5`   |     18      |      18      |      18      |   2.894489388   |
|  `2×2×6`   |     21      |      21      |      21      |   2.873949845   |
|  `2×2×7`   |     25      |      25      |      25      |   2.897969631   |
|  `2×2×8`   |     28      |      28      |      28      |   2.884412953   |
|  `2×2×9`   |     32      |      32      |      32      |   2.901396054   |
|  `2×2×10`  |     35      |      35      |      35      |   2.891404915   |
|  `2×2×11`  |     39      |      39      |      39      |   2.904369496   |
|  `2×2×12`  |     42      |      42      |      42      |   2.896519407   |
|  `2×2×13`  |     46      |      46      |      46      |   2.906913622   |
|  `2×2×14`  |     49      |      49      |      49      |   2.900482192   |
|  `2×2×15`  |     53      |      53      |      53      |   2.909104390   |
|  `2×2×16`  |     56      |      56      |      56      |   2.903677461   |
|  `2×3×3`   |     15      |      15      |      15      |   2.810763211   |
|  `2×3×4`   |     20      |      20      |      20      |   2.827893201   |
|  `2×3×5`   |     25      |      25      |      25      |   2.839184673   |
|  `2×3×6`   |     30      |      30      |      30      |   2.847366603   |
|  `2×3×7`   |     35      |      35      |      35      |   2.853661579   |
|  `2×3×8`   |     40      |      40      |      40      |   2.858709308   |
|  `2×3×9`   |     45      |      45      |      45      |   2.862881209   |
|  `2×3×10`  |   50 (?)    |      50      |      50      |   2.866409712   |
|  `2×3×11`  |     55      |      55      |      55      |   2.869448748   |
|  `2×3×12`  |     60      |      60      |      60      |   2.872104893   |
|  `2×3×13`  |   65 (?)    |      65      |      65      |   2.874454619   |
|  `2×3×14`  |     70      |      70      |      70      |   2.876554438   |
|  `2×3×15`  |   75 (?)    |      75      |      75      |   2.878447154   |
|  `2×3×16`  |     80      |      80      |      80      |   2.880165875   |
|  `2×4×4`   |     26      |      26      |      26      |   2.820263831   |
|  `2×4×5`   |   33 (?)    |      33      |      32      |   2.818527371   |
|  `2×4×6`   |   39 (?)    |      39      |      39      |   2.839089189   |
|  `2×4×7`   |     45      |      45      |      45      |   2.837016079   |
|  `2×4×8`   |     51      |      51      |      51      |   2.836212671   |
|  `2×4×9`   |   59 (?)    |    59 (?)    |      58      |   2.848323599   |
|  `2×4×10`  |   65 (?)    |    65 (?)    |      64      |   2.847232637   |
|  `2×4×11`  |   71 (?)    |    71 (?)    |      71      |   2.856171014   |
|  `2×4×12`  |   77 (?)    |    77 (?)    |      77      |   2.855044295   |
|  `2×4×13`  |   84 (?)    |    84 (?)    |      83      |   2.854307941   |
|  `2×4×14`  |     90      |      90      |      90      |   2.860958406   |
|  `2×4×15`  |   96 (?)    |    96 (?)    |      96      |   2.860170902   |
|  `2×4×16`  |     102     |     102      |     102      |   2.859610861   |
|  `2×5×5`   |     40      |      40      |      40      |   2.828878651   |
|  `2×5×6`   |     47      |      47      |      47      |   2.821072489   |
|  `2×5×7`   |   55 (?)    |    55 (?)    |      55      |   2.829707666   |
|  `2×5×8`   |   63 (?)    |    63 (?)    |      63      |   2.836451080   |
|  `2×5×9`   |   72 (?)    |    72 (?)    |      72      |   2.851231340   |
|  `2×5×10`  |   80 (?)    |    80 (?)    |      79      |   2.846440637   |
|  `2×5×11`  |     87      |      87      |      87      |   2.850288335   |
|  `2×5×12`  |     94      |      94      |      94      |   2.846978142   |
|  `2×5×13`  |   102 (?)   |   102 (?)    |     102      |   2.850502360   |
|  `2×5×14`  |   110 (?)   |   110 (?)    |     110      |   2.853593986   |
|  `2×5×15`  |   118 (?)   |   118 (?)    |     118      |   2.856335182   |
|  `2×5×16`  |   126 (?)   |   126 (?)    |     126      |   2.858787945   |
|  `2×6×6`   |   56 (?)    |      56      |      56      |   2.823707705   |
|  `2×6×7`   |   66 (?)    |      66      |      66      |   2.836714944   |
|  `2×6×8`   |   75 (?)    |    75 (?)    |      75      |   2.837746771   |
|  `2×6×9`   |   86 (?)    |      86      |      86      |   2.854051123   |
|  `2×6×10`  |     94      |      94      |      94      |   2.846978142   |
|  `2×6×11`  |   103 (?)   |     103      |     103      |   2.847583659   |
|  `2×6×12`  |   112 (?)   |     112      |     112      |   2.848295451   |
|  `2×6×13`  |   122 (?)   |   122 (?)    |     122      |   2.853955264   |
|  `2×6×14`  |   131 (?)   |   131 (?)    |     131      |   2.854351051   |
|  `2×6×15`  |     141     |     141      |     141      |   2.858926060   |
|  `2×6×16`  |   150 (?)   |     150      |     150      |   2.859138205   |
|  `2×7×7`   |   76 (?)    |    76 (?)    |      76      |   2.833651510   |
|  `2×7×8`   |   88 (?)    |      88      |      88      |   2.846670267   |
|  `2×7×9`   |   100 (?)   |    99 (?)    |      99      |   2.850404467   |
|  `2×7×10`  |   110 (?)   |     110      |     110      |   2.853593986   |
|  `2×7×11`  |   121 (?)   |     121      |     121      |   2.856364308   |
|  `2×7×12`  |   131 (?)   |   131 (?)    |     131      |   2.854351051   |
|  `2×7×13`  |   142 (?)   |   142 (?)    |     142      |   2.856929683   |
|  `2×7×14`  |   152 (?)   |   152 (?)    |     152      |   2.855497187   |
|  `2×7×15`  |   164 (?)   |   164 (?)    |     164      |   2.861285133   |
|  `2×7×16`  |   176 (?)   |   175 (?)    |     175      |   2.863150652   |
|  `2×8×8`   |     100     |     100      |     100      |   2.847366938   |
|  `2×8×9`   |   113 (?)   |   113 (?)    |     113      |   2.853661214   |
|  `2×8×10`  |   126 (?)   |     125      |     125      |   2.854077858   |
|  `2×8×11`  |   138 (?)   |     138      |     138      |   2.858873767   |
|  `2×8×12`  |   150 (?)   |     150      |     150      |   2.859138205   |
|  `2×8×13`  |   163 (?)   |   163 (?)    |  163 (164)   |   2.862977345   |
|  `2×8×14`  |   175 (?)   |   175 (?)    |     175      |   2.863150652   |
|  `2×8×15`  |   188 (?)   |     188      |     188      |   2.866331117   |
|  `2×8×16`  |     200     |     200      |     200      |   2.866446071   |
|  `2×9×9`   |     126     |     126      |     126      |   2.851807566   |
|  `2×9×10`  |   144 (?)   |     140      |     140      |   2.854814260   |
|  `2×9×11`  |   158 (?)   |     154      |     154      |   2.857430935   |
|  `2×9×12`  |   171 (?)   |     168      |     168      |   2.859738747   |
|  `2×9×13`  |   185 (?)   |   185 (?)    |     182      |   2.861796718   |
|  `2×9×14`  |   198 (?)   |   198 (?)    |     196      |   2.863648982   |
|  `2×9×15`  |   212 (?)   |   212 (?)    |     210      |   2.865329321   |
|  `2×9×16`  |   226 (?)   |   225 (?)    |     224      |   2.866864110   |
| `2×10×10`  |     155     |     155      |     155      |   2.855675548   |
| `2×10×11`  |   174 (?)   |     171      |     171      |   2.859854622   |
| `2×10×12`  |   188 (?)   |     186      |     186      |   2.860476715   |
| `2×10×13`  |   204 (?)   |     202      |     202      |   2.863822126   |
| `2×10×14`  |   220 (?)   |   219 (?)    |     217      |   2.864293647   |
| `2×10×15`  |     235     |  234 (235)   |  234 (235)   |   2.869317583   |
| `2×10×16`  |     249     |     249      |     249      |   2.869528014   |
| `2×11×11`  |     187     |     187      |     187      |   2.859082510   |
| `2×11×12`  |   206 (?)   |   204 (?)    |     204      |   2.861281494   |
| `2×11×13`  |   224 (?)   |   221 (?)    |     221      |   2.863244617   |
| `2×11×14`  |   241 (?)   |   238 (?)    |     238      |   2.865013288   |
| `2×11×15`  |   258 (?)   |   257 (?)    |     255      |   2.866619250   |
| `2×11×16`  |   274 (?)   |   274 (?)    |     272      |   2.868087316   |
| `2×12×12`  |     222     |     222      |     222      |   2.862112883   |
| `2×12×13`  |   243 (?)   |     241      |     241      |   2.865119566   |
| `2×12×14`  |   262 (?)   |     259      |     259      |   2.865766826   |
| `2×12×15`  |   281 (?)   |     278      |     278      |   2.868257722   |
| `2×12×16`  |   299 (?)   |   298 (?)    |  298 (300)   |   2.872173939   |
| `2×13×13`  |     260     |     260      |     260      |   2.864831429   |
| `2×13×14`  |   283 (?)   |   283 (?)    |     280      |   2.866530057   |
| `2×13×15`  |   305 (?)   |   300 (?)    |     300      |   2.868073511   |
| `2×13×16`  |   325 (?)   |   320 (?)    |     320      |   2.869485347   |
| `2×14×14`  |     301     |     301      |     301      |   2.867288565   |
| `2×14×15`  |   327 (?)   |     323      |     323      |   2.869573850   |
| `2×14×16`  |   350 (?)   |     344      |     344      |   2.870191390   |
| `2×15×15`  |     345     |     345      |     345      |   2.869524113   |
| `2×15×16`  |   375 (?)   |   368 (?)    |     368      |   2.870888061   |
| `2×16×16`  |     392     |     392      |     392      |   2.871569948   |
|  `3×3×3`   |     23      |      23      |      23      |   2.854049830   |
|  `3×3×4`   |     29      |      29      |      29      |   2.818985378   |
|  `3×3×5`   |     36      |      36      |      36      |   2.824142367   |
|  `3×3×6`   |   42 (?)    |      42      |      40      | **2.774299980** |
|  `3×3×7`   |   49 (?)    |    49 (?)    |      49      |   2.818025883   |
|  `3×3×8`   |   56 (?)    |    56 (?)    |      55      |   2.811068066   |
|  `3×3×9`   |   63 (?)    |    63 (?)    |      63      |   2.828432812   |
|  `3×3×10`  |   71 (?)    |    71 (?)    |      69      |   2.822857064   |
|  `3×3×11`  |   78 (?)    |    78 (?)    |      76      |   2.827390894   |
|  `3×3×12`  |   84 (?)    |    84 (?)    |      80      |   2.807712827   |
|  `3×3×13`  |   91 (?)    |    91 (?)    |      89      |   2.827681075   |
|  `3×3×14`  |   98 (?)    |    98 (?)    |      95      |   2.824820996   |
|  `3×3×15`  |   105 (?)   |   105 (?)    |     103      |   2.834537838   |
|  `3×3×16`  |   112 (?)   |   112 (?)    |     109      |   2.831905908   |
|  `3×4×4`   |     38      |      38      |      38      |   2.818959400   |
|  `3×4×5`   |   47 (?)    |      47      |      47      |   2.821072489   |
|  `3×4×6`   |   54 (?)    |      54      |      54      | **2.798196494** |
|  `3×4×7`   |   64 (?)    |      64      |      63      | **2.805217355** |
|  `3×4×8`   |   73 (74)   |   73 (74)    |      73      |   2.819981689   |
|  `3×4×9`   |   83 (?)    |    83 (?)    |      83      |   2.831300786   |
|  `3×4×10`  |   92 (?)    |    92 (?)    |      92      |   2.833501646   |
|  `3×4×11`  |   101 (?)   |   101 (?)    |     101      |   2.835536188   |
|  `3×4×12`  |   108 (?)   |   108 (?)    |     108      |   2.826342326   |
|  `3×4×13`  |   118 (?)   |   118 (?)    |     117      |   2.829094886   |
|  `3×4×14`  |   127 (?)   |   127 (?)    |     126      |   2.831566689   |
|  `3×4×15`  |   137 (?)   |   137 (?)    |     136      |   2.838067999   |
|  `3×4×16`  |   146 (?)   |   146 (?)    |     146      |   2.843715269   |
|  `3×5×5`   |     58      |      58      |      58      |   2.821392604   |
|  `3×5×6`   |   68 (?)    |      68      |      68      |   2.813124119   |
|  `3×5×7`   |   79 (?)    |   79 (80)    |      79      |   2.816599750   |
|  `3×5×8`   |   90 (?)    |      90      |      90      |   2.819728939   |
|  `3×5×9`   |   102 (?)   |  102 (104)   |  102 (104)   |   2.828571093   |
|  `3×5×10`  |   114 (?)   |  114 (115)   |  114 (115)   |   2.835687395   |
|  `3×5×11`  |   126 (?)   |     126      |     126      |   2.841559080   |
|  `3×5×12`  |   136 (?)   |     136      |     136      |   2.838067999   |
|  `3×5×13`  |   147 (?)   |   147 (?)    |     147      |   2.839237439   |
|  `3×5×14`  |   158 (?)   |   158 (?)    |     158      |   2.840373980   |
|  `3×5×15`  |   169 (?)   |   169 (?)    |     169      |   2.841471724   |
|  `3×5×16`  |   180 (?)   |     180      |     180      |   2.842528174   |
|  `3×6×6`   |   83 (?)    |    83 (?)    |      80      |   2.807712827   |
|  `3×6×7`   |   96 (?)    |    96 (?)    |      94      |   2.818256795   |
|  `3×6×8`   |   108 (?)   |     108      |     108      |   2.826342326   |
|  `3×6×9`   |   122 (?)   |   122 (?)    |     120      |   2.823037498   |
|  `3×6×10`  |   136 (?)   |   136 (?)    |     134      |   2.829509241   |
|  `3×6×11`  |   150 (?)   |   150 (?)    |     148      |   2.834886501   |
|  `3×6×12`  |   162 (?)   |   162 (?)    |     160      |   2.832508438   |
|  `3×6×13`  |   176 (?)   |   176 (?)    |     174      |   2.837076970   |
|  `3×6×14`  |   190 (?)   |   190 (?)    |     188      |   2.841039398   |
|  `3×6×15`  |   204 (?)   |   204 (?)    |     200      |   2.839184366   |
|  `3×6×16`  |   216 (?)   |   216 (?)    |     214      |   2.842670031   |
|  `3×7×7`   |   111 (?)   |   111 (?)    |     111      |   2.831135449   |
|  `3×7×8`   |   128 (?)   |   128 (?)    |     126      |   2.831566689   |
|  `3×7×9`   |   141 (?)   |   141 (?)    |  141 (142)   |   2.832315186   |
|  `3×7×10`  |   158 (?)   |   158 (?)    |     157      |   2.836811740   |
|  `3×7×11`  |   175 (?)   |   175 (?)    |     173      |   2.840626282   |
|  `3×7×12`  |   190 (?)   |   190 (?)    |     188      |   2.841039398   |
|  `3×7×13`  |   205 (?)   |   205 (?)    |  204 (205)   |   2.844182227   |
|  `3×7×14`  |   220 (?)   |   220 (?)    |     220      |   2.846952678   |
|  `3×7×15`  |   236 (?)   |   236 (?)    |  235 (236)   |   2.847205515   |
|  `3×7×16`  |   252 (?)   |   252 (?)    |     251      |   2.849586051   |
|  `3×8×8`   |   146 (?)   |   146 (?)    |     145      |   2.839793508   |
|  `3×8×9`   |   163 (?)   |   163 (?)    |     163      |   2.842876116   |
|  `3×8×10`  |   180 (?)   |     180      |     180      |   2.842528174   |
|  `3×8×11`  |   198 (?)   |   198 (?)    |     198      |   2.845219854   |
|  `3×8×12`  |   216 (?)   |   216 (?)    |     216      |   2.847598050   |
|  `3×8×13`  |   236 (?)   |   236 (?)    |     234      |   2.849722142   |
|  `3×8×14`  |   253 (?)   |   253 (?)    |     252      |   2.851636630   |
|  `3×8×15`  |   270 (?)   |     270      |     270      |   2.853375643   |
|  `3×8×16`  |   288 (?)   |   288 (?)    |     288      |   2.854965878   |
|  `3×9×9`   |   185 (?)   |   185 (?)    |     183      |   2.845127188   |
|  `3×9×10`  |   204 (?)   |   204 (?)    |     203      |   2.847162657   |
|  `3×9×11`  |   224 (?)   |   224 (?)    |  222 (224)   |   2.846644652   |
|  `3×9×12`  |   243 (?)   |   243 (?)    |     240      |   2.844256405   |
|  `3×9×13`  |   263 (?)   |   263 (?)    |  261 (262)   |   2.848348427   |
|  `3×9×14`  |   281 (?)   |   281 (?)    |  281 (283)   |   2.850103717   |
|  `3×9×15`  |   304 (?)   |   304 (?)    |     303      |   2.855016796   |
|  `3×9×16`  |   326 (?)   |   326 (?)    |     323      |   2.856252700   |
| `3×10×10`  |   228 (?)   |   228 (?)    |     226      |   2.851021242   |
| `3×10×11`  |   250 (?)   |   250 (?)    |  248 (249)   |   2.852219687   |
| `3×10×12`  |   270 (?)   |   270 (?)    |     268      |   2.849586221   |
| `3×10×13`  |   294 (?)   |   294 (?)    |     291      |   2.852757491   |
| `3×10×14`  |   312 (?)   |   312 (?)    |  312 (314)   |   2.852364741   |
| `3×10×15`  |   338 (?)   |   338 (?)    |     336      |   2.856543829   |
| `3×10×16`  |   360 (?)   |   357 (?)    |  357 (360)   |   2.856141604   |
| `3×11×11`  |   276 (?)   |   276 (?)    |     274      |   2.856843143   |
| `3×11×12`  |   298 (?)   |   298 (?)    |     296      |   2.854020431   |
| `3×11×13`  |   323 (?)   |   323 (?)    |     321      |   2.856462333   |
| `3×11×14`  |   347 (?)   |   347 (?)    |     346      |   2.858631053   |
| `3×11×15`  |   373 (?)   |   373 (?)    |     369      |   2.857961939   |
| `3×11×16`  |   396 (?)   |   396 (?)    |     394      |   2.859910251   |
| `3×12×12`  |   324 (?)   |   324 (?)    |     320      |   2.851639645   |
| `3×12×13`  |   351 (?)   |   351 (?)    |     348      |   2.855444087   |
| `3×12×14`  |   378 (?)   |   378 (?)    |     376      |   2.858746388   |
| `3×12×15`  |   405 (?)   |   405 (?)    |     400      |   2.856901552   |
| `3×12×16`  |   432 (?)   |   432 (?)    |     428      |   2.859827202   |
| `3×13×13`  |   381 (?)   |   381 (?)    |  378 (379)   |   2.858577688   |
| `3×13×14`  |   408 (?)   |   408 (?)    |  407 (408)   |   2.860150618   |
| `3×13×15`  |   439 (?)   |   439 (?)    |  435 (436)   |   2.860506655   |
| `3×13×16`  |   468 (?)   |   468 (?)    |     465      |   2.862908907   |
| `3×14×14`  |   439 (?)   |   439 (?)    |  438 (440)   |   2.861445516   |
| `3×14×15`  |   470 (?)   |   470 (?)    |  469 (470)   |   2.862645108   |
| `3×14×16`  |   501 (?)   |   501 (?)    |  500 (502)   |   2.863761055   |
| `3×15×15`  |   506 (?)   |   506 (?)    |     503      |   2.864557717   |
| `3×15×16`  |   540 (?)   |   537 (?)    |     536      |   2.865432840   |
| `3×16×16`  |   576 (?)   |   573 (?)    |  571 (574)   |   2.866160489   |
|  `4×4×4`   |     49      |      49      |      48      | **2.792481250** |
|  `4×4×5`   |     61      |      61      |      61      |   2.814364818   |
|  `4×4×6`   |   73 (?)    |      73      |      73      |   2.819981689   |
|  `4×4×7`   |     85      |      85      |      85      |   2.824617348   |
|  `4×4×8`   |   96 (?)    |    96 (?)    |      96      |   2.822126786   |
|  `4×4×9`   |   107 (?)   |   107 (?)    |     104      | **2.803560588** |
|  `4×4×10`  |   115 (?)   |   115 (?)    |  115 (120)   | **2.804789925** |
|  `4×4×11`  |   130 (?)   |   130 (?)    |     130      |   2.824223683   |
|  `4×4×12`  |   141 (?)   |   141 (?)    |  141 (142)   |   2.823831239   |
|  `4×4×13`  |   153 (?)   |   153 (?)    |     152      |   2.823706611   |
|  `4×4×14`  |   164 (?)   |   164 (?)    |  163 (165)   |   2.823771262   |
|  `4×4×15`  |   176 (?)   |   176 (?)    |  176 (177)   |   2.830226950   |
|  `4×4×16`  |   188 (?)   |   188 (?)    |  188 (189)   |   2.832970819   |
|  `4×5×5`   |     76      |      76      |      76      |   2.821220388   |
|  `4×5×6`   |   90 (?)    |      90      |      90      |   2.819728939   |
|  `4×5×7`   |   104 (?)   |     104      |     104      |   2.819542878   |
|  `4×5×8`   |  118 (122)  |     118      |     118      |   2.820012554   |
|  `4×5×9`   |   132 (?)   |  132 (139)   |  132 (136)   |   2.820821776   |
|  `4×5×10`  |  146 (152)  |  146 (151)   |  146 (151)   |   2.821805270   |
|  `4×5×11`  |   160 (?)   |  160 (165)   |  160 (165)   |   2.822872235   |
|  `4×5×12`  |   174 (?)   |  174 (180)   |  174 (180)   |   2.823971094   |
|  `4×5×13`  |   191 (?)   |  191 (194)   |  191 (194)   |   2.833613095   |
|  `4×5×14`  |   207 (?)   |  207 (208)   |  206 (208)   |   2.836597217   |
|  `4×5×15`  |   221 (?)   |  221 (226)   |  221 (226)   |   2.839254157   |
|  `4×5×16`  |   235 (?)   |   235 (?)    |  235 (240)   |   2.839432229   |
|  `4×6×6`   |     105     |     105      |     105      |   2.809337134   |
|  `4×6×7`   |   123 (?)   |     123      |     123      |   2.817457953   |
|  `4×6×8`   |     140     |     140      |     140      |   2.819769913   |
|  `4×6×9`   |   159 (?)   |   159 (?)    |     159      |   2.829009300   |
|  `4×6×10`  |   175 (?)   |     175      |     175      |   2.827107959   |
|  `4×6×11`  |   194 (?)   |   194 (?)    |     194      |   2.834239371   |
|  `4×6×12`  |     210     |     210      |     210      |   2.832674296   |
|  `4×6×13`  |   227 (?)   |  227 (228)   |  227 (228)   |   2.833857047   |
|  `4×6×14`  |     245     |     245      |     245      |   2.837108348   |
|  `4×6×15`  |   263 (?)   |     263      |     263      |   2.839987538   |
|  `4×6×16`  |     280     |     280      |     280      |   2.840763608   |
|  `4×7×7`   |   144 (?)   |     144      |     144      |   2.824766202   |
|  `4×7×8`   |  163 (164)  |  163 (164)   |  163 (164)   |   2.823771262   |
|  `4×7×9`   |   187 (?)   |   187 (?)    |     186      |   2.835236653   |
|  `4×7×10`  |   206 (?)   |   206 (?)    |     203      |   2.828786709   |
|  `4×7×11`  |   226 (?)   |  226 (227)   |  226 (227)   |   2.837927019   |
|  `4×7×12`  |   246 (?)   |     246      |     246      |   2.839209043   |
|  `4×7×13`  |   267 (?)   |   267 (?)    |     266      |   2.840436133   |
|  `4×7×14`  |     285     |     285      |     285      |   2.839846584   |
|  `4×7×15`  |   307 (?)   |   307 (?)    |     307      |   2.844340854   |
|  `4×7×16`  |     324     |     324      |     324      |   2.840756417   |
|  `4×8×8`   |     182     |     182      |     182      |   2.815422990   |
|  `4×8×9`   |   209 (?)   |   209 (?)    |     206      |   2.822486324   |
|  `4×8×10`  |   230 (?)   |   230 (?)    |     224      |   2.814499777   |
|  `4×8×11`  |   255 (?)   |   255 (?)    |     252      |   2.829012734   |
|  `4×8×12`  |     272     |     272      |     272      |   2.826149622   |
|  `4×8×13`  |   297 (?)   |     297      |     297      |   2.832380680   |
|  `4×8×14`  |     315     |     315      |     315      |   2.826912765   |
|  `4×8×15`  |     339     |     339      |     339      |   2.831001921   |
|  `4×8×16`  |     357     |     357      |     357      |   2.826593421   |
|  `4×9×9`   |     225     |     225      |     225      |   2.810763211   |
|  `4×9×10`  |     255     |     255      |     255      |   2.824243429   |
|  `4×9×11`  |  279 (280)  |  279 (280)   |  279 (280)   |   2.824354701   |
|  `4×9×12`  |     300     |     300      |     300      |   2.819734242   |
|  `4×9×13`  |   330 (?)   |   330 (?)    |     329      |   2.828049591   |
|  `4×9×14`  |   355 (?)   |     355      |     355      |   2.831038562   |
|  `4×9×15`  |   375 (?)   |     375      |     375      |   2.826127741   |
|  `4×9×16`  |     400     |     400      |     400      |   2.827893201   |
| `4×10×10`  |     280     |     280      |     280      |   2.821408468   |
| `4×10×11`  |     308     |     308      |     308      |   2.824204956   |
| `4×10×12`  |     329     |     329      |     329      |   2.816452167   |
| `4×10×13`  |   361 (?)   |   361 (?)    |     361      |   2.824930840   |
| `4×10×14`  |   385 (?)   |   385 (?)    |     385      |   2.822362266   |
| `4×10×15`  |   417 (?)   |   417 (?)    |     417      |   2.829366531   |
| `4×10×16`  |   441 (?)   |   441 (?)    |     441      |   2.827087301   |
| `4×11×11`  |   340 (?)   |     340      |     340      |   2.828630974   |
| `4×11×12`  |   365 (?)   |     365      |     365      |   2.823324329   |
| `4×11×13`  |   401 (?)   |   401 (?)    |     400      |   2.830997032   |
| `4×11×14`  |   429 (?)   |   429 (?)    |     429      |   2.831024692   |
| `4×11×15`  |   463 (?)   |   463 (?)    |     452      |   2.825072241   |
| `4×11×16`  |   489 (?)   |   489 (?)    |     489      |   2.833264518   |
| `4×12×12`  |     390     |     390      |     390      |   2.815943526   |
| `4×12×13`  |   430 (?)   |   430 (?)    |     426      |   2.822077950   |
| `4×12×14`  |   462 (?)   |   462 (?)    |     456      |   2.821313298   |
| `4×12×15`  |   495 (?)   |   495 (?)    |     480      |   2.815116449   |
| `4×12×16`  |  516 (520)  |  516 (520)   |  516 (520)   |   2.820426451   |
| `4×13×13`  |   472 (?)   |   472 (?)    |     466      |   2.828730930   |
| `4×13×14`  |   502 (?)   |   502 (?)    |     500      |   2.828979156   |
| `4×13×15`  |   537 (?)   |   537 (?)    |     528      |   2.824216663   |
| `4×13×16`  |     568     |     568      |     568      |   2.829690422   |
| `4×14×14`  |   532 (?)   |   532 (?)    |     532      |   2.825446399   |
| `4×14×15`  |   572 (?)   |   572 (?)    |     568      |   2.825668891   |
| `4×14×16`  |     610     |     610      |     610      |   2.830324437   |
| `4×15×15`  |     600     |  599 (600)   |  599 (600)   |   2.820445661   |
| `4×15×16`  |   642 (?)   |   642 (?)    |  636 (640)   |   2.820122883   |
| `4×16×16`  |     676     |     676      |     676      |   2.820263831   |
|  `5×5×5`   |     93      |      93      |      93      |   2.816262409   |
|  `5×5×6`   |   110 (?)   |     110      |     110      |   2.814302034   |
|  `5×5×7`   |  127 (134)  |     127      |     127      |   2.813778022   |
|  `5×5×8`   |   144 (?)   |     144      |     144      |   2.813995249   |
|  `5×5×9`   |   161 (?)   |  161 (167)   |  161 (167)   |   2.814610506   |
|  `5×5×10`  |   178 (?)   |   178 (?)    |  178 (184)   |   2.815441580   |
|  `5×5×11`  |   195 (?)   |   195 (?)    |  195 (202)   |   2.816386568   |
|  `5×5×12`  |   207 (?)   |  207 (220)   |  207 (220)   | **2.804832837** |
|  `5×5×13`  |   228 (?)   |  228 (237)   |  228 (237)   |   2.816135753   |
|  `5×5×14`  |   247 (?)   |  247 (254)   |  247 (254)   |   2.821501129   |
|  `5×5×15`  |   265 (?)   |   265 (?)    |  265 (271)   |   2.824261583   |
|  `5×5×16`  |   283 (?)   |   283 (?)    |  283 (288)   |   2.826744707   |
|  `5×6×6`   |   130 (?)   |     130      |     130      |   2.812001673   |
|  `5×6×7`   |   150 (?)   |     150      |     150      |   2.811221917   |
|  `5×6×8`   |  170 (176)  |     170      |     170      |   2.811240720   |
|  `5×6×9`   |   193 (?)   |  193 (197)   |  193 (197)   |   2.820092998   |
|  `5×6×10`  |   217 (?)   |  217 (218)   |  217 (218)   |   2.829647192   |
|  `5×6×11`  |   238 (?)   |   238 (?)    |     236      |   2.826562083   |
|  `5×6×12`  |   258 (?)   |   258 (?)    |     250      |   2.814150526   |
|  `5×6×13`  |   280 (?)   |   280 (?)    |     278      |   2.829776752   |
|  `5×6×14`  |   300 (?)   |   300 (?)    |     297      |   2.827893397   |
|  `5×6×15`  |   320 (?)   |   320 (?)    |     318      |   2.829506239   |
|  `5×6×16`  |   340 (?)   |   340 (?)    |     340      |   2.832433220   |
|  `5×7×7`   |   176 (?)   |     176      |     176      |   2.819618966   |
|  `5×7×8`   |   204 (?)   |   204 (?)    |  204 (205)   |   2.831402964   |
|  `5×7×9`   |   229 (?)   |  229 (234)   |     229      |   2.833717544   |
|  `5×7×10`  |   254 (?)   |     254      |     254      |   2.835812967   |
|  `5×7×11`  |   277 (?)   |     277      |     277      |   2.834094219   |
|  `5×7×12`  |   300 (?)   |   300 (?)    |     296      |   2.826218294   |
|  `5×7×13`  |   325 (?)   |   325 (?)    |     325      |   2.835070644   |
|  `5×7×14`  |   351 (?)   |   351 (?)    |     349      |   2.835658091   |
|  `5×7×15`  |   378 (?)   |   378 (?)    |     375      |   2.838838811   |
|  `5×7×16`  |   400 (?)   |   400 (?)    |     398      |   2.838106105   |
|  `5×8×8`   |     230     |     230      |     230      |   2.828247238   |
|  `5×8×9`   |   260 (?)   |   260 (?)    |     260      |   2.834140342   |
|  `5×8×10`  |   287 (?)   |   287 (?)    |     284      |   2.828510889   |
|  `5×8×11`  |   313 (?)   |   313 (?)    |     312      |   2.830564681   |
|  `5×8×12`  |   333 (?)   |   333 (?)    |     333      |   2.822324450   |
|  `5×8×13`  |   365 (?)   |   365 (?)    |     363      |   2.827581156   |
|  `5×8×14`  |   391 (?)   |   391 (?)    |     387      |   2.824818687   |
|  `5×8×15`  |   421 (?)   |   421 (?)    |     419      |   2.831610434   |
|  `5×8×16`  |   445 (?)   |   445 (?)    |     445      |   2.831279571   |
|  `5×9×9`   |   293 (?)   |   293 (?)    |  293 (294)   |   2.838247561   |
|  `5×9×10`  |   322 (?)   |   322 (?)    |     322      |   2.835644554   |
|  `5×9×11`  |   353 (?)   |   353 (?)    |     353      |   2.836528379   |
|  `5×9×12`  |   377 (?)   |   377 (?)    |     377      |   2.828664069   |
|  `5×9×13`  |   412 (?)   |   412 (?)    |     411      |   2.833785246   |
|  `5×9×14`  |   441 (?)   |   441 (?)    |     439      |   2.831878945   |
|  `5×9×15`  |   474 (?)   |     474      |     474      |   2.837212145   |
|  `5×9×16`  |   503 (?)   |   503 (?)    |     497      |   2.830986305   |
| `5×10×10`  |     352     |     352      |     352      |   2.830571654   |
| `5×10×11`  |   386 (?)   |     386      |     386      |   2.831655074   |
| `5×10×12`  |   413 (?)   |     413      |     413      |   2.824846255   |
| `5×10×13`  |   451 (?)   |   451 (?)    |     451      |   2.830705612   |
| `5×10×14`  |   481 (?)   |   481 (?)    |     481      |   2.828175028   |
| `5×10×15`  |   519 (?)   |   519 (?)    |     519      |   2.833157741   |
| `5×10×16`  |   549 (?)   |   549 (?)    |     549      |   2.831023864   |
| `5×11×11`  |   427 (?)   |   427 (?)    |     424      |   2.833497741   |
| `5×11×12`  |   461 (?)   |   461 (?)    |     455      |   2.828129078   |
| `5×11×13`  |   503 (?)   |   503 (?)    |     498      |   2.834905546   |
| `5×11×14`  |   537 (?)   |   537 (?)    |     533      |   2.833953893   |
| `5×11×15`  |   577 (?)   |   577 (?)    |     575      |   2.838722531   |
| `5×11×16`  |   609 (?)   |   609 (?)    |     609      |   2.837120407   |
| `5×12×12`  |   498 (?)   |   498 (?)    |     488      |   2.822653463   |
| `5×12×13`  |   540 (?)   |   540 (?)    |     536      |   2.830991200   |
| `5×12×14`  |   582 (?)   |   582 (?)    |     574      |   2.830350615   |
| `5×12×15`  |   620 (?)   |   620 (?)    |     615      |   2.832071274   |
| `5×12×16`  |   657 (?)   |   657 (?)    |     656      |   2.833649544   |
| `5×13×13`  |   593 (?)   |   593 (?)    |  587 (588)   |   2.837827448   |
| `5×13×14`  |   632 (?)   |   632 (?)    |  628 (630)   |   2.836688582   |
| `5×13×15`  |   675 (?)   |   675 (?)    |     672      |   2.837770064   |
| `5×13×16`  |   718 (?)   |   718 (?)    |     717      |   2.839397681   |
| `5×14×14`  |   672 (?)   |   672 (?)    |  672 (676)   |   2.835662569   |
| `5×14×15`  |   722 (?)   |   722 (?)    |     721      |   2.837890958   |
| `5×14×16`  |   769 (?)   |   769 (?)    |     768      |   2.838788042   |
| `5×15×15`  |     762     |     762      |     762      |   2.833639043   |
| `5×15×16`  |   813 (?)   |     813      |     813      |   2.835257472   |
| `5×16×16`  |     868     |     868      |     868      |   2.837130178   |
|  `6×6×6`   |     153     |     153      |     153      |   2.807540860   |
|  `6×6×7`   |   183 (?)   |     183      |     183      |   2.826414484   |
|  `6×6×8`   |     203     |     203      |     203      |   2.814714670   |
|  `6×6×9`   |     225     |     225      |     225      |   2.810763211   |
|  `6×6×10`  |   252 (?)   |   252 (?)    |     247      |   2.807997433   |
|  `6×6×11`  |   276 (?)   |   276 (?)    |     268      | **2.804179806** |
|  `6×6×12`  |   294 (?)   |   294 (?)    |     280      | **2.785626776** |
|  `6×6×13`  |   322 (?)   |   322 (?)    |     316      |   2.808378577   |
|  `6×6×14`  |   343 (?)   |   343 (?)    |     336      | **2.804519017** |
|  `6×6×15`  |   371 (?)   |   371 (?)    |     360      | **2.806662647** |
|  `6×6×16`  |   392 (?)   |   392 (?)    |     385      |   2.809853287   |
|  `6×7×7`   |  212 (215)  |  212 (215)   |  212 (215)   |   2.827400948   |
|  `6×7×8`   |  238 (239)  |  238 (239)   |  238 (239)   |   2.822158898   |
|  `6×7×9`   |  268 (270)  |  268 (270)   |  268 (270)   |   2.826160061   |
|  `6×7×10`  |   296 (?)   |     296      |  293 (296)   |   2.821158816   |
|  `6×7×11`  |   322 (?)   |   322 (?)    |     318      |   2.817369624   |
|  `6×7×12`  |   342 (?)   |   342 (?)    |     336      | **2.804519017** |
|  `6×7×13`  |   376 (?)   |   376 (?)    |     372      |   2.817349681   |
|  `6×7×14`  |   403 (?)   |   403 (?)    |     399      |   2.817571522   |
|  `6×7×15`  |   435 (?)   |   435 (?)    |     430      |   2.822238033   |
|  `6×7×16`  |   460 (?)   |   460 (?)    |     457      |   2.822322742   |
|  `6×8×8`   |     266     |     266      |     266      |   2.814904236   |
|  `6×8×9`   |     296     |     296      |     296      |   2.813098408   |
|  `6×8×10`  |   329 (?)   |     329      |     329      |   2.816452167   |
|  `6×8×11`  |   357 (?)   |   357 (?)    |     357      |   2.812719178   |
|  `6×8×12`  |   378 (?)   |   378 (?)    |     378      | **2.801192733** |
|  `6×8×13`  |   418 (?)   |   418 (?)    |     414      |   2.808759412   |
|  `6×8×14`  |   448 (?)   |   448 (?)    |     441      | **2.805900115** |
|  `6×8×15`  |   484 (?)   |   484 (?)    |     480      |   2.815116449   |
|  `6×8×16`  |   511 (?)   |   511 (?)    |     511      |   2.816029634   |
|  `6×9×9`   |   342 (?)   |  341 (342)   |  341 (342)   |   2.828169642   |
|  `6×9×10`  |   371 (?)   |  371 (373)   |  371 (373)   |   2.821014248   |
|  `6×9×11`  |   407 (?)   |   407 (?)    |     407      |   2.822417437   |
|  `6×9×12`  |   433 (?)   |   433 (?)    |  433 (434)   |   2.813178974   |
|  `6×9×13`  |   476 (?)   |   476 (?)    |     474      |   2.820233412   |
|  `6×9×14`  |   508 (?)   |   508 (?)    |     500      |   2.812870837   |
|  `6×9×15`  |   540 (?)   |   540 (?)    |     532      |   2.811681973   |
|  `6×9×16`  |   576 (?)   |   576 (?)    |     556      | **2.804422215** |
| `6×10×10`  |     406     |     406      |     406      |   2.816829393   |
| `6×10×11`  |   446 (?)   |     446      |     446      |   2.818897225   |
| `6×10×12`  |   476 (?)   |     476      |     476      |   2.811300704   |
| `6×10×13`  |   520 (?)   |   520 (?)    |     520      |   2.817338694   |
| `6×10×14`  |   553 (?)   |   553 (?)    |     553      |   2.813744718   |
| `6×10×15`  |   597 (?)   |   597 (?)    |     597      |   2.818970672   |
| `6×10×16`  |   630 (?)   |   630 (?)    |     630      |   2.815981845   |
| `6×11×11`  |   496 (?)   |   496 (?)    |     490      |   2.820960164   |
| `6×11×12`  |   534 (?)   |   534 (?)    |     524      |   2.814338494   |
| `6×11×13`  |   584 (?)   |   584 (?)    |     574      |   2.821466352   |
| `6×11×14`  |   621 (?)   |   621 (?)    |     613      |   2.819725683   |
| `6×11×15`  |   661 (?)   |     661      |     661      |   2.824310648   |
| `6×11×16`  |   701 (?)   |   701 (?)    |     695      |   2.819742751   |
| `6×12×12`  |   570 (?)   |   570 (?)    |     560      |   2.807602758   |
| `6×12×13`  |   624 (?)   |   624 (?)    |     616      |   2.816548366   |
| `6×12×14`  |   666 (?)   |   666 (?)    |     658      |   2.814978785   |
| `6×12×15`  |   705 (?)   |  703 (705)   |  703 (705)   |   2.815586170   |
| `6×12×16`  |   746 (?)   |   746 (?)    |     746      |   2.815074394   |
| `6×13×13`  |   682 (?)   |   682 (?)    |  678 (680)   |   2.825542860   |
| `6×13×14`  |   730 (?)   |   730 (?)    |  726 (730)   |   2.824944345   |
| `6×13×15`  |   771 (?)   |     771      |     771      |   2.822893894   |
| `6×13×16`  |   819 (?)   |   819 (?)    |     819      |   2.822753871   |
| `6×14×14`  |   777 (?)   |   777 (?)    |     777      |   2.824140952   |
| `6×14×15`  |   825 (?)   |   818 (?)    |  818 (825)   |   2.818456628   |
| `6×14×16`  |   880 (?)   |   880 (?)    |     880      |   2.823631915   |
| `6×15×15`  |  868 (870)  |  868 (870)   |  868 (870)   |   2.816172277   |
| `6×15×16`  |   930 (?)   |   930 (?)    |  922 (928)   |   2.816077251   |
| `6×16×16`  |     988     |  985 (988)   |  985 (988)   |   2.818332114   |
|  `7×7×7`   |   250 (?)   |   250 (?)    |     249      |   2.835409898   |
|  `7×7×8`   |   278 (?)   |   278 (?)    |     277      |   2.825542234   |
|  `7×7×9`   |   316 (?)   |  316 (318)   |     315      |   2.834224130   |
|  `7×7×10`  |   346 (?)   |     346      |  345 (346)   |   2.830075228   |
|  `7×7×11`  |   378 (?)   |   378 (?)    |     376      |   2.828230821   |
|  `7×7×12`  |   404 (?)   |   404 (?)    |     402      |   2.821095589   |
|  `7×7×13`  |   443 (?)   |   443 (?)    |     441      |   2.829144541   |
|  `7×7×14`  |   475 (?)   |   475 (?)    |     471      |   2.827273046   |
|  `7×7×15`  |   511 (?)   |   511 (?)    |     508      |   2.832092591   |
|  `7×7×16`  |   540 (?)   |   540 (?)    |     539      |   2.831330828   |
|  `7×8×8`   |   310 (?)   |   310 (?)    |     306      |   2.812667793   |
|  `7×8×9`   |   352 (?)   |   352 (?)    |     350      |   2.824199930   |
|  `7×8×10`  |   385 (?)   |     385      |     385      |   2.822362266   |
|  `7×8×11`  |   423 (?)   |   423 (?)    |     423      |   2.824446365   |
|  `7×8×12`  |   454 (?)   |   454 (?)    |     454      |   2.819287751   |
|  `7×8×13`  |   498 (?)   |   498 (?)    |     496      |   2.825322795   |
|  `7×8×14`  |   532 (?)   |   532 (?)    |     529      |   2.822900761   |
|  `7×8×15`  |   572 (?)   |   572 (?)    |  570 (571)   |   2.827234938   |
|  `7×8×16`  |   603 (?)   |   603 (?)    |     603      |   2.825230941   |
|  `7×9×9`   |   399 (?)   |   399 (?)    |     398      |   2.832545469   |
|  `7×9×10`  |   437 (?)   |     437      |     437      |   2.829753712   |
|  `7×9×11`  |   478 (?)   |   478 (?)    |  478 (480)   |   2.829651018   |
|  `7×9×12`  |   513 (?)   |   513 (?)    |     510      |   2.821833950   |
|  `7×9×13`  |   563 (?)   |   563 (?)    |     562      |   2.831584296   |
|  `7×9×14`  |   600 (?)   |   600 (?)    |     597      |   2.827367786   |
|  `7×9×15`  |   639 (?)   |     639      |  634 (639)   |   2.825226157   |
|  `7×9×16`  |   677 (?)   |   677 (?)    |     667      |   2.820871928   |
| `7×10×10`  |     478     |     478      |     478      |   2.825309911   |
| `7×10×11`  |   526 (?)   |     526      |     526      |   2.827986649   |
| `7×10×12`  |   564 (?)   |     564      |     564      |   2.822520185   |
| `7×10×13`  |   614 (?)   |   614 (?)    |     614      |   2.826761780   |
| `7×10×14`  |   653 (?)   |   653 (?)    |     653      |   2.823169941   |
| `7×10×15`  |   703 (?)   |   703 (?)    |  703 (711)   |   2.826988027   |
| `7×10×16`  |   742 (?)   |   742 (?)    |  742 (752)   |   2.824072156   |
| `7×11×11`  |   580 (?)   |   580 (?)    |     577      |   2.829186234   |
| `7×11×12`  |   624 (?)   |   624 (?)    |     618      |   2.823294520   |
| `7×11×13`  |   680 (?)   |   680 (?)    |     675      |   2.828894453   |
| `7×11×14`  |   725 (?)   |   725 (?)    |     721      |   2.827195395   |
| `7×11×15`  |   778 (?)   |     778      |  777 (778)   |   2.831357038   |
| `7×11×16`  |   822 (?)   |   822 (?)    |  822 (827)   |   2.829413433   |
| `7×12×12`  |   669 (?)   |   669 (?)    |     660      |   2.816295309   |
| `7×12×13`  |   731 (?)   |   731 (?)    |     724      |   2.823761363   |
| `7×12×14`  |   780 (?)   |   780 (?)    |     774      |   2.822499419   |
| `7×12×15`  |   831 (?)   |     831      |     831      |   2.825082662   |
| `7×12×16`  |   884 (?)   |   884 (?)    |     880      |   2.823631915   |
| `7×13×13`  |   798 (?)   |   798 (?)    |  794 (795)   |   2.830948485   |
| `7×13×14`  |   852 (?)   |   852 (?)    |  850 (852)   |   2.830202017   |
| `7×13×15`  |   909 (?)   |     909      |     909      |   2.831041821   |
| `7×13×16`  |   970 (?)   |   970 (?)    |  966 (968)   |   2.831006805   |
| `7×14×14`  |   909 (?)   |   909 (?)    |  909 (912)   |   2.829037251   |
| `7×14×15`  |   969 (?)   |  969 (976)   |  969 (976)   |   2.828567644   |
| `7×14×16`  |  1036 (?)   |   1036 (?)   | 1030 (1034)  |   2.828648763   |
| `7×15×15`  |    1032     |     1032     |     1032     |   2.827727792   |
| `7×15×16`  |  1104 (?)   |   1104 (?)   |     1099     |   2.828563800   |
| `7×16×16`  |  1164 (?)   |   1164 (?)   |     1148     |   2.821663673   |
|  `8×8×8`   |   343 (?)   |   343 (?)    |     336      | **2.797439141** |
|  `8×8×9`   |   391 (?)   |   391 (?)    |     388      |   2.813516852   |
|  `8×8×10`  |     427     |     427      |     427      |   2.812108880   |
|  `8×8×11`  |   475 (?)   |   475 (?)    |     475      |   2.819973988   |
|  `8×8×12`  |   511 (?)   |   511 (?)    |     504      |   2.809801266   |
|  `8×8×13`  |   559 (?)   |   559 (?)    |     559      |   2.822564153   |
|  `8×8×14`  |     595     |     595      |     595      |   2.819336895   |
|  `8×8×15`  |   639 (?)   |   639 (?)    |  628 (635)   |   2.814592730   |
|  `8×8×16`  |   672 (?)   |   672 (?)    |  671 (672)   |   2.817050687   |
|  `8×9×9`   |   435 (?)   |   435 (?)    |     430      |   2.809957177   |
|  `8×9×10`  |     487     |     487      |     487      |   2.821718121   |
|  `8×9×11`  |   531 (?)   |   531 (?)    |  531 (533)   |   2.820303082   |
|  `8×9×12`  |   570 (?)   |   570 (?)    |     560      |   2.807602758   |
|  `8×9×13`  |   624 (?)   |     624      |     624      |   2.822206418   |
|  `8×9×14`  |   666 (?)   |  666 (669)   |  666 (669)   |   2.820221074   |
|  `8×9×15`  |   705 (?)   |  703 (705)   |  703 (705)   |   2.815586170   |
|  `8×9×16`  |   746 (?)   |   746 (?)    |     746      |   2.815074394   |
| `8×10×10`  |     532     |     532      |     532      |   2.816907135   |
| `8×10×11`  |   588 (?)   |     588      |     588      |   2.821593096   |
| `8×10×12`  |   630 (?)   |     630      |  628 (630)   |   2.814592730   |
| `8×10×13`  |   686 (?)   |     686      |     686      |   2.820311011   |
| `8×10×14`  |   728 (?)   |     728      |     728      |   2.815933159   |
| `8×10×15`  |   784 (?)   |  784 (789)   |  784 (789)   |   2.819888631   |
| `8×10×16`  |   826 (?)   |   826 (?)    |  826 (832)   |   2.816333697   |
| `8×11×11`  |   646 (?)   |   646 (?)    |     641      |   2.820135833   |
| `8×11×12`  |   690 (?)   |   690 (?)    |     680      |   2.810341019   |
| `8×11×13`  |   754 (?)   |   754 (?)    |     750      |   2.820138111   |
| `8×11×14`  |   804 (?)   |     804      |     804      |   2.820079580   |
| `8×11×15`  |   859 (?)   |     859      |     859      |   2.820628412   |
| `8×11×16`  |   914 (?)   |   914 (?)    |  914 (920)   |   2.821200247   |
| `8×12×12`  |   735 (?)   |   735 (?)    |     720      | **2.799977314** |
| `8×12×13`  |   807 (?)   |   807 (?)    |     798      |   2.811823417   |
| `8×12×14`  |   861 (?)   |     861      |     861      |   2.814541463   |
| `8×12×15`  |  914 (915)  |  914 (915)   |  914 (915)   |   2.812482294   |
| `8×12×16`  |   980 (?)   |   980 (?)    |     960      |   2.807820225   |
| `8×13×13`  |   885 (?)   |   885 (?)    |     880      |   2.821307498   |
| `8×13×14`  |   945 (?)   |     945      |     945      |   2.821953852   |
| `8×13×15`  |    1005     |     1005     |     1005     |   2.820590900   |
| `8×13×16`  |  1072 (?)   |   1072 (?)   |     1064     |   2.819122214   |
| `8×14×14`  |  1008 (?)   |     1008     |     1008     |   2.819845310   |
| `8×14×15`  |    1080     |     1080     |     1080     |   2.821518953   |
| `8×14×16`  |  1141 (?)   |   1141 (?)   |     1138     |   2.818159924   |
| `8×15×15`  |    1140     | 1137 (1140)  | 1137 (1140)  |   2.816133328   |
| `8×15×16`  |  1217 (?)   |   1217 (?)   |     1198     |   2.812830688   |
| `8×16×16`  |  1274 (?)   |   1274 (?)   |     1248     | **2.805109696** |
|  `9×9×9`   |  486 (498)  |  486 (498)   |  486 (498)   |   2.815464877   |
|  `9×9×10`  |   540 (?)   |   540 (?)    |     534      |   2.813362874   |
|  `9×9×11`  |   594 (?)   |   594 (?)    |     576      | **2.807325686** |
|  `9×9×12`  |   630 (?)   |   630 (?)    |     600      | **2.789620062** |
|  `9×9×13`  |   693 (?)   |   693 (?)    |     681      |   2.812123330   |
|  `9×9×14`  |   735 (?)   |   725 (?)    |  725 (726)   |   2.809198372   |
|  `9×9×15`  |   798 (?)   |   798 (?)    |     783      |   2.814417445   |
|  `9×9×16`  |   840 (?)   |   840 (?)    |     825      |   2.810945122   |
| `9×10×10`  |   597 (?)   |  597 (600)   |  597 (600)   |   2.818970672   |
| `9×10×11`  |   661 (?)   |   661 (?)    |     651      |   2.817680531   |
| `9×10×12`  |   702 (?)   |   702 (?)    |     684      | **2.803818059** |
| `9×10×13`  |   771 (?)   |  771 (772)   |  765 (772)   |   2.819576354   |
| `9×10×14`  |   820 (?)   |     820      |  819 (820)   |   2.818970048   |
| `9×10×15`  |     870     |  866 (870)   |  866 (870)   |   2.815212156   |
| `9×10×16`  |   924 (?)   |   924 (?)    |  924 (939)   |   2.816971116   |
| `9×11×11`  |   721 (?)   |   721 (?)    |  715 (725)   |   2.819505933   |
| `9×11×12`  |   762 (?)   |   762 (?)    |  754 (760)   |   2.807359140   |
| `9×11×13`  |   843 (?)   |  843 (849)   |  835 (849)   |   2.818729064   |
| `9×11×14`  |   900 (?)   |  900 (904)   |  889 (904)   |   2.815840862   |
| `9×11×15`  |   960 (?)   |   960 (?)    |  960 (981)   |   2.820802434   |
| `9×11×16`  |  1024 (?)   | 1024 (1030)  | 1023 (1030)  |   2.821974308   |
| `9×12×12`  |   810 (?)   |   810 (?)    |     800      | **2.798064630** |
| `9×12×13`  |   894 (?)   |   894 (?)    |  884 (900)   |   2.808492461   |
| `9×12×14`  |   960 (?)   |   960 (?)    |     945      |   2.807406833   |
| `9×12×15`  |  1020 (?)   |   1020 (?)   |     1000     | **2.804161987** |
| `9×12×16`  |  1080 (?)   |   1080 (?)   | 1072 (1080)  |   2.807864570   |
| `9×13×13`  |   986 (?)   |  986 (996)   |  981 (996)   |   2.820440786   |
| `9×13×14`  |  1050 (?)   | 1050 (1063)  | 1041 (1063)  |   2.816262654   |
| `9×13×15`  |  1119 (?)   |   1119 (?)   | 1119 (1135)  |   2.819269106   |
| `9×13×16`  |  1188 (?)   | 1188 (1210)  | 1183 (1210)  |   2.817265461   |
| `9×14×14`  |  1125 (?)   | 1125 (1136)  | 1121 (1136)  |   2.818056626   |
| `9×14×15`  |  1185 (?)   |   1185 (?)   | 1182 (1185)  |   2.813355681   |
| `9×14×16`  |  1280 (?)   |   1280 (?)   |     1260     |   2.814688545   |
| `9×15×15`  |  1284 (?)   |   1284 (?)   | 1284 (1290)  |   2.820476797   |
| `9×15×16`  |  1350 (?)   |     1350     | 1341 (1350)  |   2.813740131   |
| `9×16×16`  | 1438 (1444) | 1438 (1444)  | 1431 (1444)  |   2.815455240   |
| `10×10×10` |   651 (?)   |     651      |     651      |   2.813580989   |
| `10×10×11` |   719 (?)   |     719      |     719      |   2.817849439   |
| `10×10×12` |   768 (?)   |  768 (770)   |  768 (770)   |   2.811164062   |
| `10×10×13` |   838 (?)   |     838      |     838      |   2.816278610   |
| `10×10×14` |   889 (?)   |     889      |     889      |   2.811934283   |
| `10×10×15` |   957 (?)   |   957 (?)    |     957      |   2.815641959   |
| `10×10×16` |  1008 (?)   |   1008 (?)   |     1008     |   2.812123655   |
| `10×11×11` |   793 (?)   |     793      |     793      |   2.821415868   |
| `10×11×12` |   850 (?)   |     850      |     850      |   2.816230915   |
| `10×11×13` |   924 (?)   |     924      |     924      |   2.819673026   |
| `10×11×14` |   981 (?)   |     981      |     981      |   2.815670174   |
| `10×11×15` |  1055 (?)   |   1055 (?)   | 1055 (1067)  |   2.818897479   |
| `10×11×16` |  1112 (?)   |   1112 (?)   | 1112 (1136)  |   2.815676689   |
| `10×12×12` |   910 (?)   |     910      |     910      |   2.810672999   |
| `10×12×13` |   990 (?)   |     990      |     990      |   2.814455029   |
| `10×12×14` |  1050 (?)   |     1050     |     1050     |   2.810139154   |
| `10×12×15` | 1130 (1140) | 1122 (1140)  | 1122 (1140)  |   2.810818006   |
| `10×12×16` |  1190 (?)   |   1190 (?)   | 1190 (1216)  |   2.810171910   |
| `10×13×13` |  1082 (?)   |     1082     |     1082     |   2.820012787   |
| `10×13×14` |  1154 (?)   |     1154     |     1154     |   2.817919098   |
| `10×13×15` |  1242 (?)   |     1242     |     1242     |   2.821357792   |
| `10×13×16` |  1326 (?)   | 1326 (1332)  | 1326 (1332)  |   2.823222352   |
| `10×14×14` |  1232 (?)   |     1232     |     1232     |   2.816254849   |
| `10×14×15` |  1327 (?)   |     1327     |     1327     |   2.819986261   |
| `10×14×16` |  1423 (?)   |     1423     |     1423     |   2.823556539   |
| `10×15×15` |  1395 (?)   | 1389 (1395)  | 1389 (1395)  |   2.812527864   |
| `10×15×16` |  1497 (?)   | 1484 (1497)  | 1484 (1497)  |   2.814706248   |
| `10×16×16` | 1585 (1586) | 1585 (1586)  | 1585 (1586)  |   2.816728839   |
| `11×11×11` |   873 (?)   |     873      |     873      |   2.824116479   |
| `11×11×12` |   936 (?)   |     936      |     936      |   2.819077058   |
| `11×11×13` |  1023 (?)   |     1023     |     1023     |   2.824645969   |
| `11×11×14` |  1093 (?)   |     1093     |     1093     |   2.823197571   |
| `11×11×15` |  1169 (?)   | 1169 (1181)  | 1169 (1181)  |   2.824115356   |
| `11×11×16` |  1230 (?)   |   1230 (?)   | 1230 (1236)  |   2.820195393   |
| `11×12×12` |  1002 (?)   |   1002 (?)   |     990      |   2.808622875   |
| `11×12×13` |  1102 (?)   |     1102     | 1092 (1102)  |   2.817937614   |
| `11×12×14` |  1182 (?)   |     1182     |     1182     |   2.821761068   |
| `11×12×15` |  1262 (?)   |   1262 (?)   | 1240 (1264)  |   2.815046272   |
| `11×12×16` |  1322 (?)   |   1322 (?)   |     1312     |   2.813432378   |
| `11×13×13` |  1205 (?)   | 1205 (1210)  | 1205 (1210)  |   2.827216655   |
| `11×13×14` |  1292 (?)   | 1292 (1298)  | 1292 (1298)  |   2.827166171   |
| `11×13×15` |  1377 (?)   |     1377     |     1377     |   2.826656860   |
| `11×13×16` |  1460 (?)   | 1460 (1472)  | 1452 (1472)  |   2.823641623   |
| `11×14×14` |  1376 (?)   | 1376 (1388)  | 1376 (1388)  |   2.824489318   |
| `11×14×15` |  1460 (?)   | 1460 (1471)  | 1460 (1471)  |   2.822281114   |
| `11×14×16` |  1564 (?)   |   1564 (?)   | 1548 (1571)  |   2.821440626   |
| `11×15×15` |  1548 (?)   |   1548 (?)   |     1540     |   2.817843009   |
| `11×15×16` |  1657 (?)   |   1657 (?)   |     1656     |   2.822413466   |
| `11×16×16` |  1752 (?)   |   1752 (?)   |     1724     |   2.814679929   |
| `12×12×12` |  1071 (?)   |   1071 (?)   |     1040     | **2.795668800** |
| `12×12×13` |  1188 (?)   |   1188 (?)   |     1152     | **2.806692856** |
| `12×12×14` |  1271 (?)   |   1271 (?)   | 1234 (1250)  | **2.806467563** |
| `12×12×15` |  1344 (?)   |   1344 (?)   |     1280     | **2.795549318** |
| `12×12×16` |  1404 (?)   |   1404 (?)   |     1392     | **2.804748508** |
| `12×13×13` |  1298 (?)   |   1298 (?)   |     1274     |   2.816848164   |
| `12×13×14` |  1389 (?)   |   1389 (?)   |     1382     |   2.821446941   |
| `12×13×15` |  1470 (?)   |   1470 (?)   |     1460     |   2.817586931   |
| `12×13×16` |  1548 (?)   |   1548 (?)   | 1548 (1556)  |   2.816786558   |
| `12×14×14` |  1484 (?)   |   1484 (?)   |     1481     |   2.821249301   |
| `12×14×15` |  1560 (?)   |   1560 (?)   | 1538 (1540)  |   2.810862435   |
| `12×14×16` |  1664 (?)   |   1664 (?)   |     1638     |   2.811821137   |
| `12×15×15` |  1650 (?)   |   1650 (?)   |     1600     | **2.801323500** |
| `12×15×16` |  1769 (?)   |   1769 (?)   |     1728     |   2.807611813   |
| `12×16×16` |  1862 (?)   |   1862 (?)   |     1824     | **2.805246028** |
| `13×13×13` |  1426 (?)   |   1426 (?)   | 1421 (1426)  |   2.830120644   |
| `13×13×14` |  1511 (?)   | 1511 (1524)  | 1511 (1524)  |   2.826838093   |
| `13×13×15` |  1605 (?)   |     1605     |     1605     |   2.825055042   |
| `13×13×16` |  1711 (?)   |   1711 (?)   | 1704 (1713)  |   2.824705676   |
| `13×14×14` |  1614 (?)   | 1614 (1625)  | 1614 (1625)  |   2.825351482   |
| `13×14×15` |  1698 (?)   | 1698 (1714)  | 1698 (1714)  |   2.819951805   |
| `13×14×16` |  1820 (?)   |   1820 (?)   | 1806 (1825)  |   2.820327226   |
| `13×15×15` |  1803 (?)   |     1803     |     1803     |   2.818128235   |
| `13×15×16` |  1926 (?)   | 1926 (1932)  | 1908 (1932)  |   2.816628414   |
| `13×16×16` |  2038 (?)   |   2038 (?)   |     2022     |   2.815680662   |
| `14×14×14` |  1725 (?)   |   1725 (?)   |     1719     |   2.822787486   |
| `14×14×15` |  1813 (?)   |     1813     |     1813     |   2.818400950   |
| `14×14×16` |  1943 (?)   |   1943 (?)   | 1938 (1939)  |   2.820652346   |
| `14×15×15` |  1905 (?)   | 1895 (1905)  | 1895 (1905)  |   2.810736066   |
| `14×15×16` |  2043 (?)   |   2043 (?)   |     2016     |   2.811264261   |
| `14×16×16` |  2170 (?)   |   2170 (?)   |     2142     |   2.811317904   |
| `15×15×15` |  2058 (?)   |   2058 (?)   |     2058     |   2.817336958   |
| `15×15×16` |  2160 (?)   |   2132 (?)   | 2132 (2173)  |   2.808074285   |
| `15×16×16` |  2302 (?)   |   2302 (?)   |     2262     |   2.807630537   |
| `16×16×16` |  2401 (?)   |   2401 (?)   |     2304     | **2.792481250** |

### Coefficient set status
* total schemes: 680 (31 better Strassen)
* `ZT` schemes: 360 (52.94%)
* `Z` schemes: 37 (5.44%)
* `Q` schemes: 283 (41.62%)


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

```bibtex
@article{perminov202558,
    title={Fast Matrix Multiplication in Small Formats: Discovering New Schemes with an Open-Source Flip Graph Framework},
    author={Perminov, Andrew I},
    journal={arXiv preprint arXiv:2603.02398},
    url={https://arxiv.org/abs/2603.02398},
    year={2026}
}
```
