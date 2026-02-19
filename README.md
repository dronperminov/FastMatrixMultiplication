# FastMatrixMultiplication

[![arXiv:2511.20317](https://img.shields.io/badge/arXiv-2511.20317-b31b1b.svg)](https://arxiv.org/abs/2511.20317)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.13365-b31b1b.svg)](https://arxiv.org/abs/2512.13365)
[![arXiv:2512.13365](https://img.shields.io/badge/arXiv-2512.21980-b31b1b.svg)](https://arxiv.org/abs/2512.21980)

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

## Key results

### New best ranks
New schemes have been discovered that improve the state-of-the-art for matrix multiplication achieving lower ranks than previously known.

|   Format   |  Prev rank  |                          New rank                          |        ω        |
|:----------:|:-----------:|:----------------------------------------------------------:|:---------------:|
|  `4×4×10`  |  120 (`Q`)  |    [115](schemes/results/ZT/4x4x10_m115_ZT.json) (`ZT`)    | **2.804789925** |
|  `4×4×12`  |  142 (`Q`)  |    [141](schemes/results/ZT/4x4x12_m141_ZT.json) (`ZT`)    |   2.823831239   |
|  `4×4×14`  |  165 (`Q`)  |     [163](schemes/results/Q/4x4x14_m163_Q.json) (`Q`)      |   2.823771262   |
|  `4×4×15`  |  177 (`Q`)  |    [176](schemes/results/ZT/4x4x15_m176_ZT.json) (`ZT`)    |   2.830226950   |
|  `4×4×16`  |  189 (`Q`)  |    [188](schemes/results/ZT/4x4x16_m188_ZT.json) (`ZT`)    |   2.832970819   |
|  `4×5×9`   |  136 (`Q`)  |    [132](schemes/results/ZT/4x5x9_m132_ZT.json) (`ZT`)     |   2.820821776   |
|  `4×5×10`  |  151 (`Z`)  |    [146](schemes/results/ZT/4x5x10_m146_ZT.json) (`ZT`)    |   2.821805270   |
|  `4×5×11`  |  165 (`Z`)  |    [160](schemes/results/ZT/4x5x11_m160_ZT.json) (`ZT`)    |   2.822872235   |
|  `4×5×12`  |  180 (`Z`)  |    [175](schemes/results/ZT/4x5x12_m175_ZT.json) (`ZT`)    |   2.827107959   |
|  `4×5×13`  |  194 (`Z`)  |    [192](schemes/results/ZT/4x5x13_m192_ZT.json) (`ZT`)    |   2.836430345   |
|  `4×5×14`  |  208 (`Z`)  |    [207](schemes/results/ZT/4x5x14_m207_ZT.json) (`ZT`)    |   2.839175463   |
|  `4×5×15`  |  226 (`Z`)  |    [221](schemes/results/ZT/4x5x15_m221_ZT.json) (`ZT`)    |   2.839254157   |
|  `4×5×16`  |  240 (`Q`)  |    [236](schemes/results/ZT/4x5x16_m236_ZT.json) (`ZT`)    |   2.841640648   |
|  `4×6×13`  |  228 (`Z`)  |    [227](schemes/results/ZT/4x6x13_m227_ZT.json) (`ZT`)    |   2.833857047   |
|  `4×7×11`  |  227 (`Z`)  |    [226](schemes/results/ZT/4x7x11_m226_ZT.json) (`ZT`)    |   2.837927019   |
|  `4×9×11`  | 280 (`ZT`)  |    [279](schemes/results/ZT/4x9x11_m279_ZT.json) (`ZT`)    |   2.824354701   |
|  `5×5×9`   |  167 (`Z`)  |    [163](schemes/results/ZT/5x5x9_m163_ZT.json) (`ZT`)     |   2.821448915   |
|  `5×6×10`  |  218 (`Z`)  |    [217](schemes/results/ZT/5x6x10_m217_ZT.json) (`ZT`)    |   2.829647192   |
|  `5×7×8`   |  205 (`Q`)  |    [204](schemes/results/ZT/5x7x8_m204_ZT.json) (`ZT`)     |   2.831402964   |
| `5×13×13`  |  588 (`Q`)  |     [587](schemes/results/Q/5x13x13_m587_Q.json) (`Q`)     |   2.837827448   |
| `5×13×14`  |  630 (`Q`)  |     [628](schemes/results/Q/5x13x14_m628_Q.json) (`Q`)     |   2.836688582   |
| `5×14×14`  |  676 (`Q`)  |     [672](schemes/results/Z/5x14x14_m672_Z.json) (`Z`)     |   2.835662569   |
|  `6×7×7`   | 215 (`ZT`)  |    [212](schemes/results/ZT/6x7x7_m212_ZT.json) (`ZT`)     |   2.827400948   |
|  `6×7×8`   | 239 (`ZT`)  |    [238](schemes/results/ZT/6x7x8_m238_ZT.json) (`ZT`)     |   2.822158898   |
|  `6×7×9`   | 270 (`ZT`)  |    [268](schemes/results/ZT/6x7x9_m268_ZT.json) (`ZT`)     |   2.826160061   |
|  `6×7×10`  |  296 (`Z`)  |     [293](schemes/results/Q/6x7x10_m293_Q.json) (`Q`)      |   2.821158816   |
| `6×13×13`  |  680 (`Q`)  |     [678](schemes/results/Q/6x13x13_m678_Q.json) (`Q`)     |   2.825542860   |
| `6×13×14`  |  730 (`Q`)  |     [726](schemes/results/Q/6x13x14_m726_Q.json) (`Q`)     |   2.824944345   |
|  `7×7×10`  |  346 (`Z`)  |     [345](schemes/results/Q/7x7x10_m345_Q.json) (`Q`)      |   2.830075228   |
|  `7×8×15`  |  571 (`Q`)  |     [570](schemes/results/Q/7x8x15_m570_Q.json) (`Q`)      |   2.827234938   |
|  `7×9×11`  |  480 (`Q`)  |    [479](schemes/results/ZT/7x9x11_m479_ZT.json) (`ZT`)    |   2.830609521   |
|  `7×9×15`  |  639 (`Z`)  |     [634](schemes/results/Q/7x9x15_m634_Q.json) (`Q`)      |   2.825226157   |
| `7×14×15`  |  976 (`Z`)  |     [969](schemes/results/Z/7x14x15_m969_Z.json) (`Z`)     |   2.828567644   |
|  `8×8×16`  |  672 (`Q`)  |     [671](schemes/results/Q/8x8x16_m671_Q.json) (`Q`)      |   2.817050687   |
|  `8×9×11`  |  533 (`Q`)  |    [532](schemes/results/ZT/8x9x11_m532_ZT.json) (`ZT`)    |   2.821148741   |
|  `8×9×14`  |  669 (`Z`)  |    [666](schemes/results/ZT/8x9x14_m666_ZT.json) (`ZT`)    |   2.820221074   |
| `9×10×10`  |  600 (`Z`)  |   [598](schemes/results/ZT/9x10x10_m598_ZT.json) (`ZT`)    |   2.819708783   |
| `9×10×13`  |  772 (`Z`)  |     [765](schemes/results/Q/9x10x13_m765_Q.json) (`Q`)     |   2.819576354   |
| `9×10×14`  |  820 (`Z`)  |     [819](schemes/results/Q/9x10x14_m819_Q.json) (`Q`)     |   2.818970048   |
| `9×11×11`  |  725 (`Q`)  |     [715](schemes/results/Q/9x11x11_m715_Q.json) (`Q`)     |   2.819505933   |
| `9×11×12`  |  760 (`Q`)  |     [754](schemes/results/Q/9x11x12_m754_Q.json) (`Q`)     |   2.807359140   |
| `9×11×13`  |  849 (`Z`)  |     [835](schemes/results/Q/9x11x13_m835_Q.json) (`Q`)     |   2.818729064   |
| `9×11×14`  |  904 (`Z`)  |     [889](schemes/results/Q/9x11x14_m889_Q.json) (`Q`)     |   2.815840862   |
| `9×11×15`  |  981 (`Q`)  |     [960](schemes/results/Z/9x11x15_m960_Z.json) (`Z`)     |   2.820802434   |
| `9×11×16`  | 1030 (`Z`)  |    [1023](schemes/results/Q/9x11x16_m1023_Q.json) (`Q`)    |   2.821974308   |
| `9×12×13`  |  900 (`Q`)  |     [884](schemes/results/Q/9x12x13_m884_Q.json) (`Q`)     |   2.808492461   |
| `9×12×16`  | 1080 (`Q`)  |    [1072](schemes/results/Q/9x12x16_m1072_Q.json) (`Q`)    |   2.807864570   |
| `9×13×13`  |  996 (`Z`)  |     [981](schemes/results/Q/9x13x13_m981_Q.json) (`Q`)     |   2.820440786   |
| `9×13×14`  | 1063 (`Z`)  |    [1041](schemes/results/Q/9x13x14_m1041_Q.json) (`Q`)    |   2.816262654   |
| `9×13×15`  | 1135 (`Q`)  |    [1119](schemes/results/Z/9x13x15_m1119_Z.json) (`Z`)    |   2.819269106   |
| `9×13×16`  | 1210 (`Z`)  |    [1183](schemes/results/Q/9x13x16_m1183_Q.json) (`Q`)    |   2.817265461   |
| `9×14×14`  | 1136 (`Z`)  |    [1121](schemes/results/Q/9x14x14_m1121_Q.json) (`Q`)    |   2.818056626   |
| `9×15×15`  | 1290 (`Q`)  |    [1284](schemes/results/Z/9x15x15_m1284_Z.json) (`Z`)    |   2.820476797   |
| `9×15×16`  | 1350 (`Z`)  |    [1341](schemes/results/Q/9x15x16_m1341_Q.json) (`Q`)    |   2.813740131   |
| `9×16×16`  | 1444 (`ZT`) |    [1431](schemes/results/Q/9x16x16_m1431_Q.json) (`Q`)    |   2.815455240   |
| `10×11×15` | 1067 (`Q`)  |  [1055](schemes/results/ZT/10x11x15_m1055_ZT.json) (`ZT`)  |   2.818897479   |
| `10×13×16` | 1332 (`Z`)  |  [1326](schemes/results/ZT/10x13x16_m1326_ZT.json) (`ZT`)  |   2.823222352   |
| `11×12×13` | 1102 (`Z`)  |   [1092](schemes/results/Q/11x12x13_m1092_Q.json) (`Q`)    |   2.817937614   |
| `11×12×15` | 1264 (`Q`)  |   [1240](schemes/results/Q/11x12x15_m1240_Q.json) (`Q`)    |   2.815046272   |
| `11×13×13` | 1210 (`Z`)  |  [1205](schemes/results/ZT/11x13x13_m1205_ZT.json) (`ZT`)  |   2.827216655   |
| `11×13×14` | 1298 (`Z`)  |  [1292](schemes/results/ZT/11x13x14_m1292_ZT.json) (`ZT`)  |   2.827166171   |
| `11×13×16` | 1472 (`Z`)  |   [1452](schemes/results/Q/11x13x16_m1452_Q.json) (`Q`)    |   2.823641623   |
| `11×14×14` | 1388 (`Z`)  |  [1376](schemes/results/ZT/11x14x14_m1376_ZT.json) (`ZT`)  |   2.824489318   |
| `11×14×15` | 1471 (`Z`)  |   [1460](schemes/results/Z/11x14x15_m1460_Z.json) (`Z`)    |   2.822281114   |
| `11×14×16` | 1571 (`Q`)  |   [1548](schemes/results/Q/11x14x16_m1548_Q.json) (`Q`)    |   2.821440626   |
| `12×12×14` | 1250 (`Q`)  |   [1240](schemes/results/Q/12x12x14_m1240_Q.json) (`Q`)    |   2.808379984   |
| `12×13×16` | 1556 (`Q`)  | [1548](schemes/results/ZT/12x13x16_m1548_ZT.json) (`ZT/Q`) |   2.816786558   |
| `13×13×13` | 1426 (`Q`)  |   [1421](schemes/results/Q/13x13x13_m1421_Q.json) (`Q`)    |   2.830120644   |
| `13×13×14` | 1524 (`Z`)  |  [1511](schemes/results/ZT/13x13x14_m1511_ZT.json) (`ZT`)  |   2.826838093   |
| `13×13×16` | 1713 (`Q`)  |   [1704](schemes/results/Q/13x13x16_m1704_Q.json) (`Q`)    |   2.824705676   |
| `13×14×14` | 1625 (`Z`)  |  [1614](schemes/results/ZT/13x14x14_m1614_ZT.json) (`ZT`)  |   2.825351482   |
| `13×14×15` | 1714 (`Z`)  |  [1698](schemes/results/ZT/13x14x15_m1698_ZT.json) (`ZT`)  |   2.819951805   |
| `13×14×16` | 1825 (`Q`)  |   [1806](schemes/results/Q/13x14x16_m1806_Q.json) (`Q`)    |   2.820327226   |
| `13×15×16` | 1932 (`Z`)  |   [1908](schemes/results/Q/13x15x16_m1908_Q.json) (`Q`)    |   2.816628414   |
| `14×14×16` | 1939 (`Q`)  |   [1938](schemes/results/Q/14x14x16_m1938_Q.json) (`Q`)    |   2.820652346   |
| `15×15×16` | 2173 (`Q`)  |   [2155](schemes/results/Q/15x15x16_m2155_Q.json) (`Q`)    |   2.812005396   |


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
|  `2×5×9`   |     [72](schemes/results/ZT/2x5x9_m72_ZT.json)     |    `Q`     |
|  `2×6×9`   |     [86](schemes/results/ZT/2x6x9_m86_ZT.json)     |    `Z`     |
|  `2×7×8`   |     [88](schemes/results/ZT/2x7x8_m88_ZT.json)     |    `Z`     |
|  `2×8×15`  |   [188](schemes/results/ZT/2x8x15_m188_ZT.json)    |    `Z`     |
|  `3×3×7`   |     [49](schemes/results/ZT/3x3x7_m49_ZT.json)     |    `Q`     |
|  `3×3×9`   |     [63](schemes/results/ZT/3x3x9_m63_ZT.json)     |    `Q`     |
|  `3×4×5`   |     [47](schemes/results/ZT/3x4x5_m47_ZT.json)     |    `Z`     |
|  `3×4×6`   |     [54](schemes/results/ZT/3x4x6_m54_ZT.json)     |   `Z/Q`    |
|  `3×4×9`   |     [83](schemes/results/ZT/3x4x9_m83_ZT.json)     |    `Q`     |
|  `3×4×10`  |    [92](schemes/results/ZT/3x4x10_m92_ZT.json)     |    `Q`     |
|  `3×4×11`  |   [101](schemes/results/ZT/3x4x11_m101_ZT.json)    |    `Q`     |
|  `3×4×12`  |   [108](schemes/results/ZT/3x4x12_m108_ZT.json)    |    `Q`     |
|  `3×4×16`  |   [146](schemes/results/ZT/3x4x16_m146_ZT.json)    |    `Q`     |
|  `3×5×10`  |   [115](schemes/results/ZT/3x5x10_m115_ZT.json)    |    `Z`     |
|  `3×6×8`   |    [108](schemes/results/ZT/3x6x8_m108_ZT.json)    |   `Z/Q`    |
|  `3×8×12`  |   [216](schemes/results/ZT/3x8x12_m216_ZT.json)    |    `Q`     |
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
|  `5×5×6`   |    [110](schemes/results/ZT/5x5x6_m110_ZT.json)    |   `Z/Q`    |
|  `5×5×7`   |    [127](schemes/results/ZT/5x5x7_m127_ZT.json)    |   `Z/Q`    |
|  `5×5×8`   |    [144](schemes/results/ZT/5x5x8_m144_ZT.json)    |   `Z/Q`    |
|  `5×5×10`  |   [184](schemes/results/ZT/5x5x10_m184_ZT.json)    |    `Q`     |
|  `5×5×11`  |   [202](schemes/results/ZT/5x5x11_m202_ZT.json)    |    `Q`     |
|  `5×5×12`  |   [220](schemes/results/ZT/5x5x12_m220_ZT.json)    |    `Z`     |
|  `5×5×13`  |   [237](schemes/results/ZT/5x5x13_m237_ZT.json)    |    `Z`     |
|  `5×5×14`  |   [254](schemes/results/ZT/5x5x14_m254_ZT.json)    |    `Z`     |
|  `5×5×15`  |   [271](schemes/results/ZT/5x5x15_m271_ZT.json)    |    `Q`     |
|  `5×5×16`  |   [288](schemes/results/ZT/5x5x16_m288_ZT.json)    |    `Q`     |
|  `5×6×6`   |    [130](schemes/results/ZT/5x6x6_m130_ZT.json)    |   `Z/Q`    |
|  `5×6×7`   |    [150](schemes/results/ZT/5x6x7_m150_ZT.json)    |   `Z/Q`    |
|  `5×6×8`   |    [170](schemes/results/ZT/5x6x8_m170_ZT.json)    |   `Z/Q`    |
|  `5×6×9`   |    [197](schemes/results/ZT/5x6x9_m197_ZT.json)    |    `Z`     |
|  `5×6×16`  |   [340](schemes/results/ZT/5x6x16_m340_ZT.json)    |    `Q`     |
|  `5×7×7`   |    [176](schemes/results/ZT/5x7x7_m176_ZT.json)    |   `Z/Q`    |
|  `5×7×10`  |   [254](schemes/results/ZT/5x7x10_m254_ZT.json)    |    `Z`     |
|  `5×7×11`  |   [277](schemes/results/ZT/5x7x11_m277_ZT.json)    |    `Z`     |
|  `5×7×13`  |   [325](schemes/results/ZT/5x7x13_m325_ZT.json)    |    `Q`     |
|  `5×8×12`  |   [333](schemes/results/ZT/5x8x12_m333_ZT.json)    |    `Q`     |
|  `5×9×15`  |   [474](schemes/results/ZT/5x9x15_m474_ZT.json)    |    `Z`     |
|  `6×6×7`   |    [183](schemes/results/ZT/6x6x7_m183_ZT.json)    |   `Z/Q`    |
|  `6×8×10`  |   [329](schemes/results/ZT/6x8x10_m329_ZT.json)    |    `Z`     |
|  `6×8×11`  |   [357](schemes/results/ZT/6x8x11_m357_ZT.json)    |    `Q`     |
|  `6×8×12`  |   [378](schemes/results/ZT/6x8x12_m378_ZT.json)    |    `Q`     |
|  `6×9×9`   |    [342](schemes/results/ZT/6x9x9_m342_ZT.json)    |    `Z`     |
|  `6×9×10`  |   [373](schemes/results/ZT/6x9x10_m373_ZT.json)    |    `Z`     |
| `6×11×15`  |   [661](schemes/results/ZT/6x11x15_m661_ZT.json)   |    `Z`     |
| `6×12×15`  |   [705](schemes/results/ZT/6x12x15_m705_ZT.json)   |    `Z`     |
| `6×12×16`  |   [746](schemes/results/ZT/6x12x16_m746_ZT.json)   |    `Q`     |
| `6×13×15`  |   [771](schemes/results/ZT/6x13x15_m771_ZT.json)   |    `Z`     |
|  `7×8×10`  |   [385](schemes/results/ZT/7x8x10_m385_ZT.json)    |    `Z`     |
|  `7×8×11`  |   [423](schemes/results/ZT/7x8x11_m423_ZT.json)    |    `Q`     |
|  `7×8×12`  |   [454](schemes/results/ZT/7x8x12_m454_ZT.json)    |    `Q`     |
|  `7×9×10`  |   [437](schemes/results/ZT/7x9x10_m437_ZT.json)    |    `Z`     |
| `7×12×15`  |   [831](schemes/results/ZT/7x12x15_m831_ZT.json)   |    `Z`     |
| `7×13×15`  |   [909](schemes/results/ZT/7x13x15_m909_ZT.json)   |    `Z`     |
|  `8×8×11`  |   [475](schemes/results/ZT/8x8x11_m475_ZT.json)    |    `Q`     |
|  `8×8×13`  |   [559](schemes/results/ZT/8x8x13_m559_ZT.json)    |    `Q`     |
|  `8×9×13`  |   [624](schemes/results/ZT/8x9x13_m624_ZT.json)    |    `Z`     |
|  `8×9×15`  |   [705](schemes/results/ZT/8x9x15_m705_ZT.json)    |    `Z`     |
|  `8×9×16`  |   [746](schemes/results/ZT/8x9x16_m746_ZT.json)    |    `Q`     |
| `8×10×11`  |   [588](schemes/results/ZT/8x10x11_m588_ZT.json)   |    `Z`     |
| `8×10×12`  |   [630](schemes/results/ZT/8x10x12_m630_ZT.json)   |    `Z`     |
| `8×10×13`  |   [686](schemes/results/ZT/8x10x13_m686_ZT.json)   |    `Z`     |
| `8×10×14`  |   [728](schemes/results/ZT/8x10x14_m728_ZT.json)   |    `Z`     |
| `8×11×14`  |   [804](schemes/results/ZT/8x11x14_m804_ZT.json)   |    `Z`     |
| `8×11×15`  |   [859](schemes/results/ZT/8x11x15_m859_ZT.json)   |    `Z`     |
| `8×12×14`  |   [861](schemes/results/ZT/8x12x14_m861_ZT.json)   |    `Z`     |
| `8×13×14`  |   [945](schemes/results/ZT/8x13x14_m945_ZT.json)   |    `Z`     |
| `8×14×14`  |  [1008](schemes/results/ZT/8x14x14_m1008_ZT.json)  |    `Z`     |
| `10×10×10` |  [651](schemes/results/ZT/10x10x10_m651_ZT.json)   |    `Z`     |
| `10×10×11` |  [719](schemes/results/ZT/10x10x11_m719_ZT.json)   |    `Z`     |
| `10×10×12` |  [770](schemes/results/ZT/10x10x12_m770_ZT.json)   |    `Z`     |
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
| `10×15×15` | [1395](schemes/results/ZT/10x15x15_m1395_ZT.json)  |    `Z`     |
| `10×15×16` | [1497](schemes/results/ZT/10x15x16_m1497_ZT.json)  |    `Z`     |
| `11×11×11` |  [873](schemes/results/ZT/11x11x11_m873_ZT.json)   |    `Z`     |
| `11×11×12` |  [936](schemes/results/ZT/11x11x12_m936_ZT.json)   |    `Z`     |
| `11×11×13` | [1023](schemes/results/ZT/11x11x13_m1023_ZT.json)  |    `Z`     |
| `11×11×14` | [1093](schemes/results/ZT/11x11x14_m1093_ZT.json)  |    `Z`     |
| `11×12×14` | [1182](schemes/results/ZT/11x12x14_m1182_ZT.json)  |    `Z`     |
| `11×13×15` | [1377](schemes/results/ZT/11x13x15_m1377_ZT.json)  |    `Z`     |
| `13×13×15` | [1605](schemes/results/ZT/13x13x15_m1605_ZT.json)  |    `Z`     |
| `13×15×15` | [1803](schemes/results/ZT/13x15x15_m1803_ZT.json)  |    `Z`     |
| `14×14×15` | [1813](schemes/results/ZT/14x14x15_m1813_ZT.json)  |    `Z`     |
| `14×15×15` | [1905](schemes/results/ZT/14x15x15_m1905_ZT.json)  |    `Z`     |
| `15×15×15` | [2058](schemes/results/ZT/15x15x15_m2058_ZT.json)  |    `Q`     |


### Rediscovery in the integer ring (`Z`)
The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).
Implementations restricted to integer coefficients were previously unknown.

|   Format   |                       Rank                       |
|:----------:|:------------------------------------------------:|
|  `2×5×7`   |     [55](schemes/results/Z/2x5x7_m55_Z.json)     |
|  `2×5×8`   |     [63](schemes/results/Z/2x5x8_m63_Z.json)     |
|  `2×5×13`  |   [102](schemes/results/Z/2x5x13_m102_Z.json)    |
|  `2×5×14`  |   [110](schemes/results/Z/2x5x14_m110_Z.json)    |
|  `2×5×15`  |   [118](schemes/results/Z/2x5x15_m118_Z.json)    |
|  `2×5×16`  |   [126](schemes/results/Z/2x5x16_m126_Z.json)    |
|  `2×6×8`   |     [75](schemes/results/Z/2x6x8_m75_Z.json)     |
|  `2×6×13`  |   [122](schemes/results/Z/2x6x13_m122_Z.json)    |
|  `2×6×14`  |   [131](schemes/results/Z/2x6x14_m131_Z.json)    |
|  `2×7×7`   |     [76](schemes/results/Z/2x7x7_m76_Z.json)     |
|  `2×7×9`   |     [99](schemes/results/Z/2x7x9_m99_Z.json)     |
|  `2×7×12`  |   [131](schemes/results/Z/2x7x12_m131_Z.json)    |
|  `2×7×13`  |   [142](schemes/results/Z/2x7x13_m142_Z.json)    |
|  `2×7×14`  |   [152](schemes/results/Z/2x7x14_m152_Z.json)    |
|  `2×7×15`  |   [164](schemes/results/Z/2x7x15_m164_Z.json)    |
|  `2×7×16`  |   [175](schemes/results/Z/2x7x16_m175_Z.json)    |
|  `2×8×9`   |    [113](schemes/results/Z/2x8x9_m113_Z.json)    |
|  `2×8×14`  |   [175](schemes/results/Z/2x8x14_m175_Z.json)    |
| `2×11×12`  |   [204](schemes/results/Z/2x11x12_m204_Z.json)   |
| `2×11×13`  |   [221](schemes/results/Z/2x11x13_m221_Z.json)   |
| `2×11×14`  |   [238](schemes/results/Z/2x11x14_m238_Z.json)   |
| `2×13×15`  |   [300](schemes/results/Z/2x13x15_m300_Z.json)   |
| `2×13×16`  |   [320](schemes/results/Z/2x13x16_m320_Z.json)   |
| `2×15×16`  |   [368](schemes/results/Z/2x15x16_m368_Z.json)   |
|  `3×4×8`   |     [73](schemes/results/Z/3x4x8_m73_Z.json)     |
|  `3×5×7`   |     [79](schemes/results/Z/3x5x7_m79_Z.json)     |
|  `3×5×13`  |   [147](schemes/results/Z/3x5x13_m147_Z.json)    |
|  `3×5×14`  |   [158](schemes/results/Z/3x5x14_m158_Z.json)    |
|  `3×5×15`  |   [169](schemes/results/Z/3x5x15_m169_Z.json)    |
|  `3×7×7`   |    [111](schemes/results/Z/3x7x7_m111_Z.json)    |
|  `3×8×9`   |    [163](schemes/results/Z/3x8x9_m163_Z.json)    |
|  `3×8×11`  |   [198](schemes/results/Z/3x8x11_m198_Z.json)    |
|  `3×8×16`  |   [288](schemes/results/Z/3x8x16_m288_Z.json)    |
| `3×10×16`  |   [360](schemes/results/Z/3x10x16_m360_Z.json)   |
| `4×10×13`  |   [361](schemes/results/Z/4x10x13_m361_Z.json)   |
| `4×10×14`  |   [385](schemes/results/Z/4x10x14_m385_Z.json)   |
| `4×10×15`  |   [417](schemes/results/Z/4x10x15_m417_Z.json)   |
| `4×10×16`  |   [441](schemes/results/Z/4x10x16_m441_Z.json)   |
| `4×11×14`  |   [429](schemes/results/Z/4x11x14_m429_Z.json)   |
| `4×11×16`  |   [489](schemes/results/Z/4x11x16_m489_Z.json)   |
| `4×14×14`  |   [532](schemes/results/Z/4x14x14_m532_Z.json)   |
|  `5×7×9`   |    [229](schemes/results/Z/5x7x9_m229_Z.json)    |
|  `5×8×9`   |    [260](schemes/results/Z/5x8x9_m260_Z.json)    |
|  `5×8×16`  |   [445](schemes/results/Z/5x8x16_m445_Z.json)    |
|  `5×9×11`  |   [353](schemes/results/Z/5x9x11_m353_Z.json)    |
|  `5×9×12`  |   [377](schemes/results/Z/5x9x12_m377_Z.json)    |
| `5×10×13`  |   [451](schemes/results/Z/5x10x13_m451_Z.json)   |
| `5×10×14`  |   [481](schemes/results/Z/5x10x14_m481_Z.json)   |
| `5×10×15`  |   [519](schemes/results/Z/5x10x15_m519_Z.json)   |
| `5×10×16`  |   [549](schemes/results/Z/5x10x16_m549_Z.json)   |
| `5×11×16`  |   [609](schemes/results/Z/5x11x16_m609_Z.json)   |
|  `6×8×16`  |   [511](schemes/results/Z/6x8x16_m511_Z.json)    |
|  `6×9×11`  |   [407](schemes/results/Z/6x9x11_m407_Z.json)    |
|  `6×9×12`  |   [434](schemes/results/Z/6x9x12_m434_Z.json)    |
| `6×10×13`  |   [520](schemes/results/Z/6x10x13_m520_Z.json)   |
| `6×10×14`  |   [553](schemes/results/Z/6x10x14_m553_Z.json)   |
| `6×10×15`  |   [597](schemes/results/Z/6x10x15_m597_Z.json)   |
| `6×10×16`  |   [630](schemes/results/Z/6x10x16_m630_Z.json)   |
| `6×13×14`  |   [730](schemes/results/Z/6x13x14_m730_Z.json)   |
| `6×13×16`  |   [819](schemes/results/Z/6x13x16_m819_Z.json)   |
| `6×14×14`  |   [777](schemes/results/Z/6x14x14_m777_Z.json)   |
| `6×14×15`  |   [825](schemes/results/Z/6x14x15_m825_Z.json)   |
| `6×14×16`  |   [880](schemes/results/Z/6x14x16_m880_Z.json)   |
|  `7×8×16`  |   [603](schemes/results/Z/7x8x16_m603_Z.json)    |
| `7×10×13`  |   [614](schemes/results/Z/7x10x13_m614_Z.json)   |
| `7×10×14`  |   [653](schemes/results/Z/7x10x14_m653_Z.json)   |
| `7×13×14`  |   [852](schemes/results/Z/7x13x14_m852_Z.json)   |
| `9×14×15`  |  [1185](schemes/results/Z/9x14x15_m1185_Z.json)  |

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
```


## Research Findings & Status

The table below summarizes the current state of researched matrix multiplication schemes. It highlights where ternary schemes (ZT) match or approximate the known minimal ranks
from other fields. The best ranks of previously known schemes are given in brackets.

|   Format   |  `ZT` rank  |   `Z` rank   |   `Q` rank   |  `Z2` rank  |
|:----------:|:-----------:|:------------:|:------------:|:-----------:|
|  `2×2×2`   |      7      |      7       |      7       |      7      |
|  `2×2×3`   |     11      |      11      |      11      |     11      |
|  `2×2×4`   |     14      |      14      |      14      |     14      |
|  `2×2×5`   |     18      |      18      |      18      |     18      |
|  `2×2×6`   |     21      |      21      |      21      |     21      |
|  `2×2×7`   |     25      |      25      |      25      |     25      |
|  `2×2×8`   |     28      |      28      |      28      |     28      |
|  `2×2×9`   |     32      |      32      |      32      |     32      |
|  `2×2×10`  |     35      |      35      |      35      |     35      |
|  `2×2×11`  |     39      |      39      |      39      |     39      |
|  `2×2×12`  |     42      |      42      |      42      |     42      |
|  `2×2×13`  |     46      |      46      |      46      |     46      |
|  `2×2×14`  |     49      |      49      |      49      |     49      |
|  `2×2×15`  |     53      |      53      |      53      |     53      |
|  `2×2×16`  |     56      |      56      |      56      |     56      |
|  `2×3×3`   |     15      |      15      |      15      |     15      |
|  `2×3×4`   |     20      |      20      |      20      |     20      |
|  `2×3×5`   |     25      |      25      |      25      |     25      |
|  `2×3×6`   |     30      |      30      |      30      |     30      |
|  `2×3×7`   |     35      |      35      |      35      |     35      |
|  `2×3×8`   |     40      |      40      |      40      |     40      |
|  `2×3×9`   |     45      |      45      |      45      |     45      |
|  `2×3×10`  |   50 (?)    |      50      |      50      |     50      |
|  `2×3×11`  |     55      |      55      |      55      |     55      |
|  `2×3×12`  |     60      |      60      |      60      |     60      |
|  `2×3×13`  |   65 (?)    |      65      |      65      |     65      |
|  `2×3×14`  |     70      |      70      |      70      |     70      |
|  `2×3×15`  |   75 (?)    |      75      |      75      |     75      |
|  `2×3×16`  |     80      |      80      |      80      |     80      |
|  `2×4×4`   |     26      |      26      |      26      |     26      |
|  `2×4×5`   |   33 (?)    |      33      |      32      |     33      |
|  `2×4×6`   |   39 (?)    |      39      |      39      |     39      |
|  `2×4×7`   |     45      |      45      |      45      |     45      |
|  `2×4×8`   |     51      |      51      |      51      |     51      |
|  `2×4×9`   |   59 (?)    |    59 (?)    |      58      |   59 (?)    |
|  `2×4×10`  |   65 (?)    |    65 (?)    |      64      |   65 (?)    |
|  `2×4×11`  |   71 (?)    |    71 (?)    |      71      |   71 (?)    |
|  `2×4×12`  |   77 (?)    |    77 (?)    |      77      |   77 (?)    |
|  `2×4×13`  |   84 (?)    |    84 (?)    |      83      |   84 (?)    |
|  `2×4×14`  |     90      |      90      |      90      |     90      |
|  `2×4×15`  |   96 (?)    |    96 (?)    |      96      |   96 (?)    |
|  `2×4×16`  |     102     |     102      |     102      |     102     |
|  `2×5×5`   |     40      |      40      |      40      |     40      |
|  `2×5×6`   |     47      |      47      |      47      |     47      |
|  `2×5×7`   |   57 (?)    |    55 (?)    |      55      |     55      |
|  `2×5×8`   |   65 (?)    |    63 (?)    |      63      |     63      |
|  `2×5×9`   |   72 (?)    |    72 (?)    |      72      |   72 (?)    |
|  `2×5×10`  |   80 (?)    |    80 (?)    |      79      |   80 (?)    |
|  `2×5×11`  |     87      |      87      |      87      |     87      |
|  `2×5×12`  |     94      |      94      |      94      |     94      |
|  `2×5×13`  |   104 (?)   |   102 (?)    |     102      |     102     |
|  `2×5×14`  |   112 (?)   |   110 (?)    |     110      |     110     |
|  `2×5×15`  |   119 (?)   |   118 (?)    |     118      |     118     |
|  `2×5×16`  |   127 (?)   |   126 (?)    |     126      |   126 (?)   |
|  `2×6×6`   |   57 (?)    |      56      |      56      |     56      |
|  `2×6×7`   |   67 (?)    |      66      |      66      |     66      |
|  `2×6×8`   |   77 (?)    |    75 (?)    |      75      |     75      |
|  `2×6×9`   |   86 (?)    |      86      |      86      |     86      |
|  `2×6×10`  |     94      |      94      |      94      |     94      |
|  `2×6×11`  |   104 (?)   |     103      |     103      |     103     |
|  `2×6×12`  |   114 (?)   |     112      |     112      |     112     |
|  `2×6×13`  |   124 (?)   |   122 (?)    |     122      |     122     |
|  `2×6×14`  |   133 (?)   |   131 (?)    |     131      |     131     |
|  `2×6×15`  |     141     |     141      |     141      |     141     |
|  `2×6×16`  |   151 (?)   |     150      |     150      |     150     |
|  `2×7×7`   |   77 (?)    |    76 (?)    |      76      |     76      |
|  `2×7×8`   |   88 (?)    |      88      |      88      |     88      |
|  `2×7×9`   |   102 (?)   |    99 (?)    |      99      |   99 (?)    |
|  `2×7×10`  |   112 (?)   |     110      |     110      |     110     |
|  `2×7×11`  |   122 (?)   |     121      |     121      |     121     |
|  `2×7×12`  |   133 (?)   |   131 (?)    |     131      |     131     |
|  `2×7×13`  |   144 (?)   |   142 (?)    |     142      |     142     |
|  `2×7×14`  |   154 (?)   |   152 (?)    |     152      |     152     |
|  `2×7×15`  |   165 (?)   |   164 (?)    |     164      |     164     |
|  `2×7×16`  |   176 (?)   |   175 (?)    |     175      |     175     |
|  `2×8×8`   |     100     |     100      |     100      |     100     |
|  `2×8×9`   |   116 (?)   |   113 (?)    |     113      |   113 (?)   |
|  `2×8×10`  |   128 (?)   |     125      |     125      |     125     |
|  `2×8×11`  |   139 (?)   |     138      |     138      |     138     |
|  `2×8×12`  |   151 (?)   |     150      |     150      |     150     |
|  `2×8×13`  |   165 (?)   |   163 (?)    |  163 (164)   |   163 (?)   |
|  `2×8×14`  |   176 (?)   |   175 (?)    |     175      |   175 (?)   |
|  `2×8×15`  |   188 (?)   |     188      |     188      |     188     |
|  `2×8×16`  |     200     |     200      |     200      |     200     |
|  `2×9×9`   |     126     |     126      |     126      |     126     |
|  `2×9×10`  |   144 (?)   |     140      |     140      |     140     |
|  `2×9×11`  |   158 (?)   |     154      |     154      |     154     |
|  `2×9×12`  |   171 (?)   |     168      |     168      |     168     |
|  `2×9×13`  |   185 (?)   |   185 (?)    |     182      |   185 (?)   |
|  `2×9×14`  |   198 (?)   |   198 (?)    |     196      |   198 (?)   |
|  `2×9×15`  |   212 (?)   |   212 (?)    |     210      |   212 (?)   |
|  `2×9×16`  |   228 (?)   |   225 (?)    |     224      |   225 (?)   |
| `2×10×10`  |     155     |     155      |     155      |     155     |
| `2×10×11`  |   174 (?)   |     171      |     171      |     171     |
| `2×10×12`  |   188 (?)   |     186      |     186      |     186     |
| `2×10×13`  |   205 (?)   |     202      |     202      |     202     |
| `2×10×14`  |   220 (?)   |   219 (?)    |     217      |   219 (?)   |
| `2×10×15`  |     235     |  234 (235)   |  234 (235)   |  234 (235)  |
| `2×10×16`  |     249     |     249      |     249      |     249     |
| `2×11×11`  |     187     |     187      |     187      |     187     |
| `2×11×12`  |   208 (?)   |   204 (?)    |     204      |   204 (?)   |
| `2×11×13`  |   226 (?)   |   221 (?)    |     221      |   221 (?)   |
| `2×11×14`  |   242 (?)   |   238 (?)    |     238      |   238 (?)   |
| `2×11×15`  |   258 (?)   |   257 (?)    |     255      |   257 (?)   |
| `2×11×16`  |   274 (?)   |   274 (?)    |     272      |   274 (?)   |
| `2×12×12`  |     222     |     222      |     222      |     222     |
| `2×12×13`  |   245 (?)   |     241      |     241      |     241     |
| `2×12×14`  |   264 (?)   |     259      |     259      |     259     |
| `2×12×15`  |   282 (?)   |     278      |     278      |     278     |
| `2×12×16`  |   299 (?)   |   298 (?)    |  298 (300)   |   298 (?)   |
| `2×13×13`  |     260     |     260      |     260      |     260     |
| `2×13×14`  |   286 (?)   |   283 (?)    |     280      |   283 (?)   |
| `2×13×15`  |   306 (?)   |   300 (?)    |     300      |   300 (?)   |
| `2×13×16`  |   325 (?)   |   320 (?)    |     320      |   320 (?)   |
| `2×14×14`  |     301     |     301      |     301      |     301     |
| `2×14×15`  |   329 (?)   |     323      |     323      |     323     |
| `2×14×16`  |   350 (?)   |     344      |     344      |     344     |
| `2×15×15`  |     345     |     345      |     345      |     345     |
| `2×15×16`  |   375 (?)   |   368 (?)    |     368      |   368 (?)   |
| `2×16×16`  |     392     |     392      |     392      |     392     |
|  `3×3×3`   |     23      |      23      |      23      |     23      |
|  `3×3×4`   |     29      |      29      |      29      |     29      |
|  `3×3×5`   |     36      |      36      |      36      |     36      |
|  `3×3×6`   |   42 (?)    |      42      |      40      |     42      |
|  `3×3×7`   |   49 (?)    |    49 (?)    |      49      |   49 (?)    |
|  `3×3×8`   |   56 (?)    |    56 (?)    |      55      |   55 (?)    |
|  `3×3×9`   |   63 (?)    |    63 (?)    |      63      |   63 (?)    |
|  `3×3×10`  |   71 (?)    |    71 (?)    |      69      |   71 (?)    |
|  `3×3×11`  |   78 (?)    |    78 (?)    |      76      |   78 (?)    |
|  `3×3×12`  |   84 (?)    |    84 (?)    |      80      |   84 (?)    |
|  `3×3×13`  |   91 (?)    |    91 (?)    |      89      |   91 (?)    |
|  `3×3×14`  |   98 (?)    |    98 (?)    |      95      |   98 (?)    |
|  `3×3×15`  |   105 (?)   |   105 (?)    |     103      |   105 (?)   |
|  `3×3×16`  |   112 (?)   |   112 (?)    |     109      |   112 (?)   |
|  `3×4×4`   |     38      |      38      |      38      |     38      |
|  `3×4×5`   |   47 (?)    |      47      |      47      |     47      |
|  `3×4×6`   |   54 (?)    |      54      |      54      |     54      |
|  `3×4×7`   |   64 (?)    |      64      |      63      |     64      |
|  `3×4×8`   |     74      |   73 (74)    |      73      |     73      |
|  `3×4×9`   |   83 (?)    |    83 (?)    |      83      |   83 (?)    |
|  `3×4×10`  |   92 (?)    |    92 (?)    |      92      |   92 (?)    |
|  `3×4×11`  |   101 (?)   |   101 (?)    |     101      |   101 (?)   |
|  `3×4×12`  |   108 (?)   |   108 (?)    |     108      |   108 (?)   |
|  `3×4×13`  |   118 (?)   |   118 (?)    |     117      |   118 (?)   |
|  `3×4×14`  |   128 (?)   |   127 (?)    |     126      |   127 (?)   |
|  `3×4×15`  |   137 (?)   |   137 (?)    |     136      |   137 (?)   |
|  `3×4×16`  |   146 (?)   |   146 (?)    |     146      |   146 (?)   |
|  `3×5×5`   |     58      |      58      |      58      |     58      |
|  `3×5×6`   |   70 (?)    |      68      |      68      |     68      |
|  `3×5×7`   |   81 (?)    |   79 (80)    |      79      |     79      |
|  `3×5×8`   |   92 (?)    |      90      |      90      |     90      |
|  `3×5×9`   |   105 (?)   |     104      |     104      |     104     |
|  `3×5×10`  |   115 (?)   |     115      |     115      |     115     |
|  `3×5×11`  |   128 (?)   |     126      |     126      |     126     |
|  `3×5×12`  |   139 (?)   |     136      |     136      |     136     |
|  `3×5×13`  |   150 (?)   |   147 (?)    |     147      |     147     |
|  `3×5×14`  |   162 (?)   |   158 (?)    |     158      |     158     |
|  `3×5×15`  |   173 (?)   |   169 (?)    |     169      |     169     |
|  `3×5×16`  |   184 (?)   |     180      |     180      |     180     |
|  `3×6×6`   |   83 (?)    |    83 (?)    |      80      |   83 (86)   |
|  `3×6×7`   |   96 (?)    |    96 (?)    |      94      |   96 (?)    |
|  `3×6×8`   |   108 (?)   |     108      |     108      |     108     |
|  `3×6×9`   |   124 (?)   |   122 (?)    |     120      |   122 (?)   |
|  `3×6×10`  |   137 (?)   |   136 (?)    |     134      |   136 (?)   |
|  `3×6×11`  |   150 (?)   |   150 (?)    |     148      |   150 (?)   |
|  `3×6×12`  |   162 (?)   |   162 (?)    |     160      |   162 (?)   |
|  `3×6×13`  |   178 (?)   |   176 (?)    |     174      |   176 (?)   |
|  `3×6×14`  |   191 (?)   |   190 (?)    |     188      |   190 (?)   |
|  `3×6×15`  |   204 (?)   |   204 (?)    |     200      |   204 (?)   |
|  `3×6×16`  |   216 (?)   |   216 (?)    |     214      |   216 (?)   |
|  `3×7×7`   |   113 (?)   |   111 (?)    |     111      |     111     |
|  `3×7×8`   |   128 (?)   |   128 (?)    |     126      |   128 (?)   |
|  `3×7×9`   |   145 (?)   |   143 (?)    |     142      |   143 (?)   |
|  `3×7×10`  |   160 (?)   |   158 (?)    |     157      |   158 (?)   |
|  `3×7×11`  |   177 (?)   |   175 (?)    |     173      |   175 (?)   |
|  `3×7×12`  |   192 (?)   |   190 (?)    |     188      |   190 (?)   |
|  `3×7×13`  |   209 (?)   |   207 (?)    |     205      |   207 (?)   |
|  `3×7×14`  |   224 (?)   |   222 (?)    |     220      |   222 (?)   |
|  `3×7×15`  |   241 (?)   |   237 (?)    |     236      |   237 (?)   |
|  `3×7×16`  |   256 (?)   |   254 (?)    |     251      |   254 (?)   |
|  `3×8×8`   |   148 (?)   |   146 (?)    |     145      |   145 (?)   |
|  `3×8×9`   |   164 (?)   |   163 (?)    |     163      |   163 (?)   |
|  `3×8×10`  |   182 (?)   |     180      |     180      |     180     |
|  `3×8×11`  |   200 (?)   |   198 (?)    |     198      |   198 (?)   |
|  `3×8×12`  |   216 (?)   |   216 (?)    |     216      |   216 (?)   |
|  `3×8×13`  |   236 (?)   |   236 (?)    |     234      |   236 (?)   |
|  `3×8×14`  |   256 (?)   |   253 (?)    |     252      |   253 (?)   |
|  `3×8×15`  |   272 (?)   |     270      |     270      |     270     |
|  `3×8×16`  |   290 (?)   |   288 (?)    |     288      |   288 (?)   |
|  `3×9×9`   |   187 (?)   |   185 (?)    |     183      |   185 (?)   |
|  `3×9×10`  |   207 (?)   |   205 (?)    |     203      |   205 (?)   |
|  `3×9×11`  |   227 (?)   |   226 (?)    |     224      |   226 (?)   |
|  `3×9×12`  |   246 (?)   |   244 (?)    |     240      |   244 (?)   |
|  `3×9×13`  |   268 (?)   |   265 (?)    |     262      |   265 (?)   |
|  `3×9×14`  |   288 (?)   |   285 (?)    |     283      |   285 (?)   |
|  `3×9×15`  |   309 (?)   |   306 (?)    |     303      |   306 (?)   |
|  `3×9×16`  |   328 (?)   |   326 (?)    |     323      |   326 (?)   |
| `3×10×10`  |   229 (?)   |   228 (?)    |     226      |   228 (?)   |
| `3×10×11`  |   251 (?)   |   250 (?)    |     249      |   250 (?)   |
| `3×10×12`  |   270 (?)   |   270 (?)    |     268      |   270 (?)   |
| `3×10×13`  |   296 (?)   |   294 (?)    |     291      |   294 (?)   |
| `3×10×14`  |   319 (?)   |   316 (?)    |     314      |   316 (?)   |
| `3×10×15`  |   341 (?)   |   338 (?)    |     336      |   338 (?)   |
| `3×10×16`  |   362 (?)   |   360 (?)    |     360      |   360 (?)   |
| `3×11×11`  |   278 (?)   |   276 (?)    |     274      |   276 (?)   |
| `3×11×12`  |   300 (?)   |   298 (?)    |     296      |   298 (?)   |
| `3×11×13`  |   327 (?)   |   323 (?)    |     321      |   323 (?)   |
| `3×11×14`  |   350 (?)   |   348 (?)    |     346      |   348 (?)   |
| `3×11×15`  |   377 (?)   |   373 (?)    |     369      |   373 (?)   |
| `3×11×16`  |   400 (?)   |   396 (?)    |     394      |   396 (?)   |
| `3×12×12`  |   324 (?)   |   324 (?)    |     320      |   324 (?)   |
| `3×12×13`  |   354 (?)   |   352 (?)    |     348      |   352 (?)   |
| `3×12×14`  |   378 (?)   |   378 (?)    |     376      |   378 (?)   |
| `3×12×15`  |   408 (?)   |   406 (?)    |     400      |   406 (?)   |
| `3×12×16`  |   432 (?)   |   432 (?)    |     428      |   432 (?)   |
| `3×13×13`  |   386 (?)   |   383 (?)    |     379      |   383 (?)   |
| `3×13×14`  |   414 (?)   |   411 (?)    |     408      |   411 (?)   |
| `3×13×15`  |   445 (?)   |   439 (?)    |     436      |   439 (?)   |
| `3×13×16`  |   472 (?)   |   468 (?)    |     465      |   468 (?)   |
| `3×14×14`  |   447 (?)   |   443 (?)    |     440      |   443 (?)   |
| `3×14×15`  |   476 (?)   |   474 (?)    |     470      |   474 (?)   |
| `3×14×16`  |   506 (?)   |   504 (?)    |     502      |   504 (?)   |
| `3×15×15`  |   510 (?)   |   507 (?)    |     503      |   507 (?)   |
| `3×15×16`  |   544 (?)   |   540 (?)    |     536      |   540 (?)   |
| `3×16×16`  |   576 (?)   |   576 (?)    |     574      |   576 (?)   |
|  `4×4×4`   |     49      |      49      |      48      |     47      |
|  `4×4×5`   |     61      |      61      |      61      |     60      |
|  `4×4×6`   |   73 (?)    |      73      |      73      |     73      |
|  `4×4×7`   |     85      |      85      |      85      |     85      |
|  `4×4×8`   |   96 (?)    |    96 (?)    |      96      |   94 (?)    |
|  `4×4×9`   |   107 (?)   |   107 (?)    |     104      |   107 (?)   |
|  `4×4×10`  |   115 (?)   |   115 (?)    |  115 (120)   |   115 (?)   |
|  `4×4×11`  |   130 (?)   |   130 (?)    |     130      |   130 (?)   |
|  `4×4×12`  |   141 (?)   |   141 (?)    |  141 (142)   |   141 (?)   |
|  `4×4×13`  |   153 (?)   |   153 (?)    |     152      |   153 (?)   |
|  `4×4×14`  |   164 (?)   |   164 (?)    |  163 (165)   |   164 (?)   |
|  `4×4×15`  |   176 (?)   |   176 (?)    |  176 (177)   |   176 (?)   |
|  `4×4×16`  |   188 (?)   |   188 (?)    |  188 (189)   |   188 (?)   |
|  `4×5×5`   |     76      |      76      |      76      |     73      |
|  `4×5×6`   |   90 (?)    |      90      |      90      |   89 (90)   |
|  `4×5×7`   |   104 (?)   |     104      |     104      |     104     |
|  `4×5×8`   |  118 (122)  |     118      |     118      |     118     |
|  `4×5×9`   |   132 (?)   |  132 (139)   |  132 (136)   |  132 (139)  |
|  `4×5×10`  |  146 (152)  |  146 (151)   |  146 (151)   |  146 (151)  |
|  `4×5×11`  |   160 (?)   |  160 (165)   |  160 (165)   |  160 (165)  |
|  `4×5×12`  |   175 (?)   |  175 (180)   |  175 (180)   |  175 (180)  |
|  `4×5×13`  |   192 (?)   |  192 (194)   |  192 (194)   |  192 (194)  |
|  `4×5×14`  |   207 (?)   |  207 (208)   |  207 (208)   |  207 (208)  |
|  `4×5×15`  |   221 (?)   |  221 (226)   |  221 (226)   |  221 (226)  |
|  `4×5×16`  |   236 (?)   |   236 (?)    |  236 (240)   |   236 (?)   |
|  `4×6×6`   |     105     |     105      |     105      |     105     |
|  `4×6×7`   |   123 (?)   |     123      |     123      |     123     |
|  `4×6×8`   |     140     |     140      |     140      |     140     |
|  `4×6×9`   |   159 (?)   |   159 (?)    |     159      |   159 (?)   |
|  `4×6×10`  |   175 (?)   |     175      |     175      |     175     |
|  `4×6×11`  |   194 (?)   |   194 (?)    |     194      |   194 (?)   |
|  `4×6×12`  |     210     |     210      |     210      |     210     |
|  `4×6×13`  |   227 (?)   |  227 (228)   |  227 (228)   |  227 (228)  |
|  `4×6×14`  |     245     |     245      |     245      |     245     |
|  `4×6×15`  |   263 (?)   |     263      |     263      |     263     |
|  `4×6×16`  |     280     |     280      |     280      |     280     |
|  `4×7×7`   |   144 (?)   |     144      |     144      |     144     |
|  `4×7×8`   |     164     |     164      |     164      |     164     |
|  `4×7×9`   |   187 (?)   |   187 (?)    |     186      |   187 (?)   |
|  `4×7×10`  |   206 (?)   |   206 (?)    |     203      |   206 (?)   |
|  `4×7×11`  |   226 (?)   |  226 (227)   |  226 (227)   |  226 (227)  |
|  `4×7×12`  |   246 (?)   |     246      |     246      |     246     |
|  `4×7×13`  |   267 (?)   |   267 (?)    |     266      |   267 (?)   |
|  `4×7×14`  |     285     |     285      |     285      |     285     |
|  `4×7×15`  |   307 (?)   |   307 (?)    |     307      |   307 (?)   |
|  `4×7×16`  |     324     |     324      |     324      |     324     |
|  `4×8×8`   |     182     |     182      |     182      |     182     |
|  `4×8×9`   |   209 (?)   |   209 (?)    |     206      |   209 (?)   |
|  `4×8×10`  |   230 (?)   |   230 (?)    |     224      |   230 (?)   |
|  `4×8×11`  |   255 (?)   |   255 (?)    |     252      |   255 (?)   |
|  `4×8×12`  |     272     |     272      |     272      |     272     |
|  `4×8×13`  |   297 (?)   |     297      |     297      |     297     |
|  `4×8×14`  |     315     |     315      |     315      |     315     |
|  `4×8×15`  |     339     |     339      |     339      |     339     |
|  `4×8×16`  |     357     |     357      |     357      |     357     |
|  `4×9×9`   |     225     |     225      |     225      |     225     |
|  `4×9×10`  |     255     |     255      |     255      |     255     |
|  `4×9×11`  |  279 (280)  |  279 (280)   |  279 (280)   |  279 (280)  |
|  `4×9×12`  |     300     |     300      |     300      |     300     |
|  `4×9×13`  |   330 (?)   |   330 (?)    |     329      |   330 (?)   |
|  `4×9×14`  |   355 (?)   |     355      |     355      |     355     |
|  `4×9×15`  |   375 (?)   |     375      |     375      |     375     |
|  `4×9×16`  |     400     |     400      |     400      |     400     |
| `4×10×10`  |     280     |     280      |     280      |     280     |
| `4×10×11`  |     308     |     308      |     308      |     308     |
| `4×10×12`  |     329     |     329      |     329      |     329     |
| `4×10×13`  |   369 (?)   |   361 (?)    |     361      |   361 (?)   |
| `4×10×14`  |   394 (?)   |   385 (?)    |     385      |   385 (?)   |
| `4×10×15`  |   421 (?)   |   417 (?)    |     417      |   417 (?)   |
| `4×10×16`  |   444 (?)   |   441 (?)    |     441      |   441 (?)   |
| `4×11×11`  |   342 (?)   |     340      |     340      |     340     |
| `4×11×12`  |   366 (?)   |     365      |     365      |     365     |
| `4×11×13`  |   404 (?)   |   401 (?)    |     400      |   401 (?)   |
| `4×11×14`  |   437 (?)   |   429 (?)    |     429      |   429 (?)   |
| `4×11×15`  |   463 (?)   |   463 (?)    |     452      |   463 (?)   |
| `4×11×16`  |   490 (?)   |   489 (?)    |     489      |   489 (?)   |
| `4×12×12`  |     390     |     390      |     390      |     390     |
| `4×12×13`  |   430 (?)   |   430 (?)    |     426      |   430 (?)   |
| `4×12×14`  |   465 (?)   |   462 (?)    |     456      |   462 (?)   |
| `4×12×15`  |   495 (?)   |   495 (?)    |     480      |   495 (?)   |
| `4×12×16`  |     520     |     520      |     520      |     520     |
| `4×13×13`  |   472 (?)   |   472 (?)    |     466      |   472 (?)   |
| `4×13×14`  |   509 (?)   |   502 (?)    |     500      |   502 (?)   |
| `4×13×15`  |   537 (?)   |   537 (?)    |     528      |   537 (?)   |
| `4×13×16`  |     568     |     568      |     568      |     568     |
| `4×14×14`  |   539 (?)   |   532 (?)    |     532      |   532 (?)   |
| `4×14×15`  |   572 (?)   |   572 (?)    |     568      |   572 (?)   |
| `4×14×16`  |     610     |     610      |     610      |     610     |
| `4×15×15`  |     600     |     600      |     600      |     600     |
| `4×15×16`  |   642 (?)   |   642 (?)    |     640      |   642 (?)   |
| `4×16×16`  |     676     |     676      |     676      |     676     |
|  `5×5×5`   |     93      |      93      |      93      |     93      |
|  `5×5×6`   |   110 (?)   |     110      |     110      |     110     |
|  `5×5×7`   |  127 (134)  |     127      |     127      |     127     |
|  `5×5×8`   |   144 (?)   |     144      |     144      |     144     |
|  `5×5×9`   |   163 (?)   |  163 (167)   |  163 (167)   |  163 (167)  |
|  `5×5×10`  |   184 (?)   |   184 (?)    |     184      |  183 (184)  |
|  `5×5×11`  |   202 (?)   |   202 (?)    |     202      |  200 (202)  |
|  `5×5×12`  |   220 (?)   |     220      |     220      |  217 (220)  |
|  `5×5×13`  |   237 (?)   |     237      |     237      |     237     |
|  `5×5×14`  |   254 (?)   |     254      |     254      |     254     |
|  `5×5×15`  |   271 (?)   |   271 (?)    |     271      |     271     |
|  `5×5×16`  |   288 (?)   |   288 (?)    |     288      |     288     |
|  `5×6×6`   |   130 (?)   |     130      |     130      |     130     |
|  `5×6×7`   |   150 (?)   |     150      |     150      |     150     |
|  `5×6×8`   |  170 (176)  |     170      |     170      |     170     |
|  `5×6×9`   |   197 (?)   |     197      |     197      |     197     |
|  `5×6×10`  |   217 (?)   |  217 (218)   |  217 (218)   |  217 (218)  |
|  `5×6×11`  |   240 (?)   |   238 (?)    |     236      |   238 (?)   |
|  `5×6×12`  |   258 (?)   |   258 (?)    |     250      |   258 (?)   |
|  `5×6×13`  |   280 (?)   |   280 (?)    |     278      |   280 (?)   |
|  `5×6×14`  |   300 (?)   |   300 (?)    |     297      |   300 (?)   |
|  `5×6×15`  |   320 (?)   |   320 (?)    |     318      |   320 (?)   |
|  `5×6×16`  |   340 (?)   |   340 (?)    |     340      |   340 (?)   |
|  `5×7×7`   |   176 (?)   |     176      |     176      |     176     |
|  `5×7×8`   |   204 (?)   |   204 (?)    |  204 (205)   |  204 (205)  |
|  `5×7×9`   |   231 (?)   |  229 (234)   |     229      |     229     |
|  `5×7×10`  |   254 (?)   |     254      |     254      |     254     |
|  `5×7×11`  |   277 (?)   |     277      |     277      |     277     |
|  `5×7×12`  |   300 (?)   |   300 (?)    |     296      |   300 (?)   |
|  `5×7×13`  |   325 (?)   |   325 (?)    |     325      |   325 (?)   |
|  `5×7×14`  |   351 (?)   |   351 (?)    |     349      |   351 (?)   |
|  `5×7×15`  |   379 (?)   |   378 (?)    |     375      |   378 (?)   |
|  `5×7×16`  |   402 (?)   |   400 (?)    |     398      |   400 (?)   |
|  `5×8×8`   |     230     |     230      |     230      |     230     |
|  `5×8×9`   |   262 (?)   |   260 (?)    |     260      |   260 (?)   |
|  `5×8×10`  |   287 (?)   |   287 (?)    |     284      |   287 (?)   |
|  `5×8×11`  |   313 (?)   |   313 (?)    |     312      |   313 (?)   |
|  `5×8×12`  |   333 (?)   |   333 (?)    |     333      |   333 (?)   |
|  `5×8×13`  |   365 (?)   |   365 (?)    |     363      |   365 (?)   |
|  `5×8×14`  |   391 (?)   |   391 (?)    |     387      |   391 (?)   |
|  `5×8×15`  |   423 (?)   |   421 (?)    |     419      |   421 (?)   |
|  `5×8×16`  |   449 (?)   |   445 (?)    |     445      |     445     |
|  `5×9×9`   |   295 (?)   |   295 (?)    |     294      |   295 (?)   |
|  `5×9×10`  |   323 (?)   |   323 (?)    |     322      |   323 (?)   |
|  `5×9×11`  |   355 (?)   |   353 (?)    |     353      |   353 (?)   |
|  `5×9×12`  |   381 (?)   |   377 (?)    |     377      |   377 (?)   |
|  `5×9×13`  |   417 (?)   |   412 (?)    |     411      |   412 (?)   |
|  `5×9×14`  |   448 (?)   |   441 (?)    |     439      |   441 (?)   |
|  `5×9×15`  |   474 (?)   |     474      |     474      |     474     |
|  `5×9×16`  |   507 (?)   |   503 (?)    |     497      |   503 (?)   |
| `5×10×10`  |     352     |     352      |     352      |     352     |
| `5×10×11`  |   390 (?)   |     386      |     386      |     386     |
| `5×10×12`  |   421 (?)   |     413      |     413      |     413     |
| `5×10×13`  |   463 (?)   |   451 (?)    |     451      |   451 (?)   |
| `5×10×14`  |   495 (?)   |   481 (?)    |     481      |   481 (?)   |
| `5×10×15`  |   531 (?)   |   519 (?)    |     519      |   519 (?)   |
| `5×10×16`  |   563 (?)   |   549 (?)    |     549      |   549 (?)   |
| `5×11×11`  |   432 (?)   |   427 (?)    |     424      |   427 (?)   |
| `5×11×12`  |   465 (?)   |   461 (?)    |     455      |   461 (?)   |
| `5×11×13`  |   509 (?)   |   503 (?)    |     498      |   503 (?)   |
| `5×11×14`  |   545 (?)   |   537 (?)    |     533      |   537 (?)   |
| `5×11×15`  |   580 (?)   |   577 (?)    |     575      |   577 (?)   |
| `5×11×16`  |   617 (?)   |   609 (?)    |     609      |   609 (?)   |
| `5×12×12`  |   498 (?)   |   498 (?)    |     488      |   498 (?)   |
| `5×12×13`  |   546 (?)   |   546 (?)    |     536      |   546 (?)   |
| `5×12×14`  |   585 (?)   |   582 (?)    |     574      |   582 (?)   |
| `5×12×15`  |   621 (?)   |   621 (?)    |     615      |   621 (?)   |
| `5×12×16`  |   659 (?)   |   657 (?)    |     656      |   657 (?)   |
| `5×13×13`  |   596 (?)   |   594 (?)    |  587 (588)   |   594 (?)   |
| `5×13×14`  |   639 (?)   |   632 (?)    |  628 (630)   |   632 (?)   |
| `5×13×15`  |   675 (?)   |   675 (?)    |     672      |   675 (?)   |
| `5×13×16`  |   720 (?)   |   718 (?)    |     717      |   718 (?)   |
| `5×14×14`  |   683 (?)   |   672 (?)    |  672 (676)   |   672 (?)   |
| `5×14×15`  |   722 (?)   |   722 (?)    |     721      |   722 (?)   |
| `5×14×16`  |   773 (?)   |   769 (?)    |     768      |   769 (?)   |
| `5×15×15`  |     762     |     762      |     762      |     762     |
| `5×15×16`  |   819 (?)   |     813      |     813      |     813     |
| `5×16×16`  |     868     |     868      |     868      |     868     |
|  `6×6×6`   |     153     |     153      |     153      |     153     |
|  `6×6×7`   |   183 (?)   |     183      |     183      |     183     |
|  `6×6×8`   |     203     |     203      |     203      |     203     |
|  `6×6×9`   |     225     |     225      |     225      |     225     |
|  `6×6×10`  |   252 (?)   |   252 (?)    |     247      |   252 (?)   |
|  `6×6×11`  |   276 (?)   |   276 (?)    |     268      |   276 (?)   |
|  `6×6×12`  |   294 (?)   |   294 (?)    |     280      |   294 (?)   |
|  `6×6×13`  |   322 (?)   |   322 (?)    |     316      |   322 (?)   |
|  `6×6×14`  |   343 (?)   |   343 (?)    |     336      |   343 (?)   |
|  `6×6×15`  |   371 (?)   |   371 (?)    |     360      |   371 (?)   |
|  `6×6×16`  |   392 (?)   |   392 (?)    |     385      |   392 (?)   |
|  `6×7×7`   |  212 (215)  |  212 (215)   |  212 (215)   |  212 (215)  |
|  `6×7×8`   |  238 (239)  |  238 (239)   |  238 (239)   |  238 (239)  |
|  `6×7×9`   |  268 (270)  |  268 (270)   |  268 (270)   |  268 (270)  |
|  `6×7×10`  |   296 (?)   |     296      |  293 (296)   |     296     |
|  `6×7×11`  |   322 (?)   |   322 (?)    |     318      |   322 (?)   |
|  `6×7×12`  |   342 (?)   |   342 (?)    |     336      |   342 (?)   |
|  `6×7×13`  |   376 (?)   |   376 (?)    |     372      |   376 (?)   |
|  `6×7×14`  |   403 (?)   |   403 (?)    |     399      |   403 (?)   |
|  `6×7×15`  |   437 (?)   |   435 (?)    |     430      |   435 (?)   |
|  `6×7×16`  |   464 (?)   |   460 (?)    |     457      |   460 (?)   |
|  `6×8×8`   |     266     |     266      |     266      |     266     |
|  `6×8×9`   |     296     |     296      |     296      |     296     |
|  `6×8×10`  |   329 (?)   |     329      |     329      |     329     |
|  `6×8×11`  |   357 (?)   |   357 (?)    |     357      |   357 (?)   |
|  `6×8×12`  |   378 (?)   |   378 (?)    |     378      |   378 (?)   |
|  `6×8×13`  |   418 (?)   |   418 (?)    |     414      |   418 (?)   |
|  `6×8×14`  |   448 (?)   |   448 (?)    |     441      |   448 (?)   |
|  `6×8×15`  |   486 (?)   |   484 (?)    |     480      |   484 (?)   |
|  `6×8×16`  |   518 (?)   |   511 (?)    |     511      |     511     |
|  `6×9×9`   |   342 (?)   |     342      |     342      |     342     |
|  `6×9×10`  |   373 (?)   |     373      |     373      |     373     |
|  `6×9×11`  |   410 (?)   |   407 (?)    |     407      |   407 (?)   |
|  `6×9×12`  |   435 (?)   |   434 (?)    |     434      |   434 (?)   |
|  `6×9×13`  |   477 (?)   |   476 (?)    |     474      |   476 (?)   |
|  `6×9×14`  |   511 (?)   |   508 (?)    |     500      |   508 (?)   |
|  `6×9×15`  |   540 (?)   |   540 (?)    |     532      |   540 (?)   |
|  `6×9×16`  |   576 (?)   |   576 (?)    |     556      |   576 (?)   |
| `6×10×10`  |     406     |     406      |     406      |     406     |
| `6×10×11`  |   454 (?)   |     446      |     446      |     446     |
| `6×10×12`  |   489 (?)   |     476      |     476      |     476     |
| `6×10×13`  |   534 (?)   |   520 (?)    |     520      |   520 (?)   |
| `6×10×14`  |   567 (?)   |   553 (?)    |     553      |   553 (?)   |
| `6×10×15`  |   600 (?)   |   597 (?)    |     597      |   597 (?)   |
| `6×10×16`  |   642 (?)   |   630 (?)    |     630      |   630 (?)   |
| `6×11×11`  |   501 (?)   |   496 (?)    |     490      |   496 (?)   |
| `6×11×12`  |   534 (?)   |   534 (?)    |     524      |   534 (?)   |
| `6×11×13`  |   584 (?)   |   584 (?)    |     574      |   584 (?)   |
| `6×11×14`  |   624 (?)   |   621 (?)    |     613      |   621 (?)   |
| `6×11×15`  |   661 (?)   |     661      |     661      |     661     |
| `6×11×16`  |   701 (?)   |   701 (?)    |     695      |   701 (?)   |
| `6×12×12`  |   570 (?)   |   570 (?)    |     560      |   570 (?)   |
| `6×12×13`  |   624 (?)   |   624 (?)    |     616      |   624 (?)   |
| `6×12×14`  |   666 (?)   |   666 (?)    |     658      |   666 (?)   |
| `6×12×15`  |   705 (?)   |     705      |     705      |     705     |
| `6×12×16`  |   746 (?)   |   746 (?)    |     746      |   746 (?)   |
| `6×13×13`  |   682 (?)   |   682 (?)    |  678 (680)   |   682 (?)   |
| `6×13×14`  |   731 (?)   |   730 (?)    |  726 (730)   |   730 (?)   |
| `6×13×15`  |   771 (?)   |     771      |     771      |     771     |
| `6×13×16`  |   823 (?)   |   819 (?)    |     819      |   819 (?)   |
| `6×14×14`  |   784 (?)   |   777 (?)    |     777      |   777 (?)   |
| `6×14×15`  |   826 (?)   |   825 (?)    |     825      |   825 (?)   |
| `6×14×16`  |   888 (?)   |   880 (?)    |     880      |   880 (?)   |
| `6×15×15`  |     870     |     870      |     870      |     870     |
| `6×15×16`  |   940 (?)   |   930 (?)    |     928      |   930 (?)   |
| `6×16×16`  |     988     |     988      |     988      |     988     |
|  `7×7×7`   |   250 (?)   |   250 (?)    |     249      |   248 (?)   |
|  `7×7×8`   |   278 (?)   |   278 (?)    |     277      |   273 (?)   |
|  `7×7×9`   |   316 (?)   |  316 (318)   |     315      |  313 (318)  |
|  `7×7×10`  |   346 (?)   |     346      |  345 (346)   |     346     |
|  `7×7×11`  |   378 (?)   |   378 (?)    |     376      |   378 (?)   |
|  `7×7×12`  |   404 (?)   |   404 (?)    |     402      |   404 (?)   |
|  `7×7×13`  |   443 (?)   |   443 (?)    |     441      |   443 (?)   |
|  `7×7×14`  |   475 (?)   |   475 (?)    |     471      |   475 (?)   |
|  `7×7×15`  |   513 (?)   |   511 (?)    |     508      |   511 (?)   |
|  `7×7×16`  |   544 (?)   |   540 (?)    |     539      |   540 (?)   |
|  `7×8×8`   |   310 (?)   |   310 (?)    |     306      |   302 (?)   |
|  `7×8×9`   |   352 (?)   |   352 (?)    |     350      |   352 (?)   |
|  `7×8×10`  |   385 (?)   |     385      |     385      |     385     |
|  `7×8×11`  |   423 (?)   |   423 (?)    |     423      |   423 (?)   |
|  `7×8×12`  |   454 (?)   |   454 (?)    |     454      |   454 (?)   |
|  `7×8×13`  |   498 (?)   |   498 (?)    |     496      |   498 (?)   |
|  `7×8×14`  |   532 (?)   |   532 (?)    |     529      |   532 (?)   |
|  `7×8×15`  |   574 (?)   |   572 (?)    |  570 (571)   |   572 (?)   |
|  `7×8×16`  |   606 (?)   |   603 (?)    |     603      |   603 (?)   |
|  `7×9×9`   |   399 (?)   |   399 (?)    |     398      |   399 (?)   |
|  `7×9×10`  |   437 (?)   |     437      |     437      |     437     |
|  `7×9×11`  |   479 (?)   |   479 (?)    |  479 (480)   |   479 (?)   |
|  `7×9×12`  |   515 (?)   |   515 (?)    |     510      |   515 (?)   |
|  `7×9×13`  |   564 (?)   |   563 (?)    |     562      |   563 (?)   |
|  `7×9×14`  |   603 (?)   |   600 (?)    |     597      |   600 (?)   |
|  `7×9×15`  |   639 (?)   |     639      |  634 (639)   |     639     |
|  `7×9×16`  |   677 (?)   |   677 (?)    |     667      |   677 (?)   |
| `7×10×10`  |     478     |     478      |     478      |     478     |
| `7×10×11`  |   530 (?)   |     526      |     526      |     526     |
| `7×10×12`  |   570 (?)   |     564      |     564      |     564     |
| `7×10×13`  |   620 (?)   |   614 (?)    |     614      |   614 (?)   |
| `7×10×14`  |   659 (?)   |   653 (?)    |     653      |   653 (?)   |
| `7×10×15`  |   708 (?)   |   703 (?)    |  703 (711)   |   703 (?)   |
| `7×10×16`  |   748 (?)   |   742 (?)    |  742 (752)   |   742 (?)   |
| `7×11×11`  |   584 (?)   |   580 (?)    |     577      |   580 (?)   |
| `7×11×12`  |   626 (?)   |   624 (?)    |     618      |   624 (?)   |
| `7×11×13`  |   682 (?)   |   680 (?)    |     675      |   680 (?)   |
| `7×11×14`  |   727 (?)   |   725 (?)    |     721      |   725 (?)   |
| `7×11×15`  |   778 (?)   |     778      |  777 (778)   |     778     |
| `7×11×16`  |   824 (?)   |   822 (?)    |  822 (827)   |   822 (?)   |
| `7×12×12`  |   669 (?)   |   669 (?)    |     660      |   669 (?)   |
| `7×12×13`  |   731 (?)   |   731 (?)    |     724      |   731 (?)   |
| `7×12×14`  |   780 (?)   |   780 (?)    |     774      |   780 (?)   |
| `7×12×15`  |   831 (?)   |     831      |     831      |     831     |
| `7×12×16`  |   884 (?)   |   884 (?)    |     880      |   884 (?)   |
| `7×13×13`  |   800 (?)   |   798 (?)    |  794 (795)   |   798 (?)   |
| `7×13×14`  |   856 (?)   |   852 (?)    |  850 (852)   |   852 (?)   |
| `7×13×15`  |   909 (?)   |     909      |     909      |     909     |
| `7×13×16`  |   972 (?)   |   971 (?)    |     968      |   971 (?)   |
| `7×14×14`  |   915 (?)   |   909 (?)    |  909 (912)   |   909 (?)   |
| `7×14×15`  |   976 (?)   |  969 (976)   |  969 (976)   |  969 (976)  |
| `7×14×16`  |  1040 (?)   |   1040 (?)   |     1034     |  1040 (?)   |
| `7×15×15`  |    1032     |     1032     |     1032     |    1032     |
| `7×15×16`  |  1108 (?)   |   1104 (?)   |     1099     |  1104 (?)   |
| `7×16×16`  |  1164 (?)   |   1164 (?)   |     1148     |  1164 (?)   |
|  `8×8×8`   |   343 (?)   |   343 (?)    |     336      |   329 (?)   |
|  `8×8×9`   |   391 (?)   |   391 (?)    |     388      |   391 (?)   |
|  `8×8×10`  |     427     |     427      |     427      |     427     |
|  `8×8×11`  |   475 (?)   |   475 (?)    |     475      |   475 (?)   |
|  `8×8×12`  |   511 (?)   |   511 (?)    |     504      |   511 (?)   |
|  `8×8×13`  |   559 (?)   |   559 (?)    |     559      |   559 (?)   |
|  `8×8×14`  |     595     |     595      |     595      |     595     |
|  `8×8×15`  |   639 (?)   |   639 (?)    |     635      |   639 (?)   |
|  `8×8×16`  |   672 (?)   |   672 (?)    |  671 (672)   |   672 (?)   |
|  `8×9×9`   |   435 (?)   |   435 (?)    |     430      |   435 (?)   |
|  `8×9×10`  |     487     |     487      |     487      |     487     |
|  `8×9×11`  |   532 (?)   |   532 (?)    |  532 (533)   |   532 (?)   |
|  `8×9×12`  |   570 (?)   |   570 (?)    |     560      |   570 (?)   |
|  `8×9×13`  |   624 (?)   |     624      |     624      |     624     |
|  `8×9×14`  |   666 (?)   |  666 (669)   |  666 (669)   |  666 (669)  |
|  `8×9×15`  |   705 (?)   |     705      |     705      |     705     |
|  `8×9×16`  |   746 (?)   |   746 (?)    |     746      |   746 (?)   |
| `8×10×10`  |     532     |     532      |     532      |     532     |
| `8×10×11`  |   588 (?)   |     588      |     588      |     588     |
| `8×10×12`  |   630 (?)   |     630      |     630      |     630     |
| `8×10×13`  |   686 (?)   |     686      |     686      |     686     |
| `8×10×14`  |   728 (?)   |     728      |     728      |     728     |
| `8×10×15`  |   784 (?)   |  784 (789)   |  784 (789)   |  784 (789)  |
| `8×10×16`  |   826 (?)   |   826 (?)    |  826 (832)   |   826 (?)   |
| `8×11×11`  |   646 (?)   |   646 (?)    |     641      |   646 (?)   |
| `8×11×12`  |   690 (?)   |   690 (?)    |     680      |   690 (?)   |
| `8×11×13`  |   754 (?)   |   754 (?)    |     750      |   754 (?)   |
| `8×11×14`  |   804 (?)   |     804      |     804      |     804     |
| `8×11×15`  |   859 (?)   |     859      |     859      |     859     |
| `8×11×16`  |   914 (?)   |   914 (?)    |  914 (920)   |   914 (?)   |
| `8×12×12`  |   735 (?)   |   735 (?)    |     720      |   735 (?)   |
| `8×12×13`  |   807 (?)   |   807 (?)    |     798      |   807 (?)   |
| `8×12×14`  |   861 (?)   |     861      |     861      |     861     |
| `8×12×15`  |     915     |     915      |     915      |     915     |
| `8×12×16`  |   980 (?)   |   980 (?)    |     960      |   980 (?)   |
| `8×13×13`  |   885 (?)   |   885 (?)    |     880      |   885 (?)   |
| `8×13×14`  |   945 (?)   |     945      |     945      |     945     |
| `8×13×15`  |    1005     |     1005     |     1005     |    1005     |
| `8×13×16`  |  1076 (?)   |   1076 (?)   |     1064     |  1076 (?)   |
| `8×14×14`  |  1008 (?)   |     1008     |     1008     |    1008     |
| `8×14×15`  |    1080     |     1080     |     1080     |    1080     |
| `8×14×16`  |  1148 (?)   |   1148 (?)   |     1138     |  1148 (?)   |
| `8×15×15`  |    1140     |     1140     |     1140     |    1140     |
| `8×15×16`  |  1219 (?)   |   1219 (?)   |     1198     |  1219 (?)   |
| `8×16×16`  |  1274 (?)   |   1274 (?)   |     1248     |  1274 (?)   |
|  `9×9×9`   |     498     |     498      |     498      |     498     |
|  `9×9×10`  |   540 (?)   |   540 (?)    |     534      |   540 (?)   |
|  `9×9×11`  |   594 (?)   |   594 (?)    |     576      |   594 (?)   |
|  `9×9×12`  |   630 (?)   |   630 (?)    |     600      |   630 (?)   |
|  `9×9×13`  |   693 (?)   |   693 (?)    |     681      |   693 (?)   |
|  `9×9×14`  |   735 (?)   |   735 (?)    |     726      |   735 (?)   |
|  `9×9×15`  |   798 (?)   |   798 (?)    |     783      |   798 (?)   |
|  `9×9×16`  |   840 (?)   |   840 (?)    |     825      |   840 (?)   |
| `9×10×10`  |   598 (?)   |  598 (600)   |  598 (600)   |  598 (600)  |
| `9×10×11`  |   661 (?)   |   661 (?)    |     651      |   661 (?)   |
| `9×10×12`  |   702 (?)   |   702 (?)    |     684      |   702 (?)   |
| `9×10×13`  |   771 (?)   |  771 (772)   |  765 (772)   |  771 (772)  |
| `9×10×14`  |   820 (?)   |     820      |  819 (820)   |     820     |
| `9×10×15`  |     870     |     870      |     870      |     870     |
| `9×10×16`  |   930 (?)   |   930 (?)    |  930 (939)   |   930 (?)   |
| `9×11×11`  |   721 (?)   |   721 (?)    |  715 (725)   |   721 (?)   |
| `9×11×12`  |   762 (?)   |   762 (?)    |  754 (760)   |   762 (?)   |
| `9×11×13`  |   843 (?)   |  843 (849)   |  835 (849)   |  843 (849)  |
| `9×11×14`  |   900 (?)   |  900 (904)   |  889 (904)   |  900 (904)  |
| `9×11×15`  |   972 (?)   |   960 (?)    |  960 (981)   |   960 (?)   |
| `9×11×16`  |  1024 (?)   | 1024 (1030)  | 1023 (1030)  | 1024 (1030) |
| `9×12×12`  |   810 (?)   |   810 (?)    |     800      |   810 (?)   |
| `9×12×13`  |   900 (?)   |   894 (?)    |  884 (900)   |   894 (?)   |
| `9×12×14`  |   960 (?)   |   960 (?)    |     945      |   960 (?)   |
| `9×12×15`  |  1032 (?)   |   1020 (?)   |     1000     |  1020 (?)   |
| `9×12×16`  |  1080 (?)   |   1080 (?)   | 1072 (1080)  |  1080 (?)   |
| `9×13×13`  |   996 (?)   |  987 (996)   |  981 (996)   |  987 (996)  |
| `9×13×14`  |  1062 (?)   | 1050 (1063)  | 1041 (1063)  | 1050 (1063) |
| `9×13×15`  |  1143 (?)   |   1119 (?)   | 1119 (1135)  |  1119 (?)   |
| `9×13×16`  |  1188 (?)   | 1188 (1210)  | 1183 (1210)  | 1188 (1210) |
| `9×14×14`  |  1136 (?)   | 1125 (1136)  | 1121 (1136)  | 1125 (1136) |
| `9×14×15`  |  1215 (?)   |   1185 (?)   |     1185     |  1185 (?)   |
| `9×14×16`  |  1280 (?)   |   1280 (?)   |     1260     |  1280 (?)   |
| `9×15×15`  |  1293 (?)   |   1284 (?)   | 1284 (1290)  |  1284 (?)   |
| `9×15×16`  |  1363 (?)   |     1350     | 1341 (1350)  |    1350     |
| `9×16×16`  | 1438 (1444) | 1438 (1444)  | 1431 (1444)  | 1438 (1444) |
| `10×10×10` |   651 (?)   |     651      |     651      |     651     |
| `10×10×11` |   719 (?)   |     719      |     719      |     719     |
| `10×10×12` |   770 (?)   |     770      |     770      |     770     |
| `10×10×13` |   838 (?)   |     838      |     838      |     838     |
| `10×10×14` |   889 (?)   |     889      |     889      |     889     |
| `10×10×15` |   957 (?)   |   957 (?)    |     957      |   957 (?)   |
| `10×10×16` |  1008 (?)   |   1008 (?)   |     1008     |  1008 (?)   |
| `10×11×11` |   793 (?)   |     793      |     793      |     793     |
| `10×11×12` |   850 (?)   |     850      |     850      |     850     |
| `10×11×13` |   924 (?)   |     924      |     924      |     924     |
| `10×11×14` |   981 (?)   |     981      |     981      |     981     |
| `10×11×15` |  1055 (?)   |   1055 (?)   | 1055 (1067)  |  1055 (?)   |
| `10×11×16` |  1112 (?)   |   1112 (?)   | 1112 (1136)  |  1112 (?)   |
| `10×12×12` |   910 (?)   |     910      |     910      |     910     |
| `10×12×13` |   990 (?)   |     990      |     990      |     990     |
| `10×12×14` |  1050 (?)   |     1050     |     1050     |    1050     |
| `10×12×15` | 1130 (1140) | 1130 (1140)  | 1130 (1140)  | 1130 (1140) |
| `10×12×16` |  1190 (?)   |   1190 (?)   | 1190 (1216)  |  1190 (?)   |
| `10×13×13` |  1082 (?)   |     1082     |     1082     |    1082     |
| `10×13×14` |  1154 (?)   |     1154     |     1154     |    1154     |
| `10×13×15` |  1242 (?)   |     1242     |     1242     |    1242     |
| `10×13×16` |  1326 (?)   | 1326 (1332)  | 1326 (1332)  | 1326 (1332) |
| `10×14×14` |  1232 (?)   |     1232     |     1232     |    1232     |
| `10×14×15` |  1327 (?)   |     1327     |     1327     |    1327     |
| `10×14×16` |  1423 (?)   |     1423     |     1423     |    1423     |
| `10×15×15` |  1395 (?)   |     1395     |     1395     |    1395     |
| `10×15×16` |  1497 (?)   |     1497     |     1497     |    1497     |
| `10×16×16` |    1586     |     1586     |     1586     |    1586     |
| `11×11×11` |   873 (?)   |     873      |     873      |     873     |
| `11×11×12` |   936 (?)   |     936      |     936      |     936     |
| `11×11×13` |  1023 (?)   |     1023     |     1023     |    1023     |
| `11×11×14` |  1093 (?)   |     1093     |     1093     |    1093     |
| `11×11×15` |  1170 (?)   | 1170 (1181)  | 1170 (1181)  | 1170 (1181) |
| `11×11×16` |  1230 (?)   |   1230 (?)   | 1230 (1236)  |  1230 (?)   |
| `11×12×12` |  1002 (?)   |   1002 (?)   |     990      |  1002 (?)   |
| `11×12×13` |  1102 (?)   |     1102     | 1092 (1102)  |    1102     |
| `11×12×14` |  1182 (?)   |     1182     |     1182     |    1182     |
| `11×12×15` |  1262 (?)   |   1262 (?)   | 1240 (1264)  |  1262 (?)   |
| `11×12×16` |  1322 (?)   |   1322 (?)   |     1312     |  1322 (?)   |
| `11×13×13` |  1205 (?)   | 1205 (1210)  | 1205 (1210)  | 1205 (1210) |
| `11×13×14` |  1292 (?)   | 1292 (1298)  | 1292 (1298)  | 1292 (1298) |
| `11×13×15` |  1377 (?)   |     1377     |     1377     |    1377     |
| `11×13×16` |  1460 (?)   | 1460 (1472)  | 1452 (1472)  | 1460 (1472) |
| `11×14×14` |  1376 (?)   | 1376 (1388)  | 1376 (1388)  | 1376 (1388) |
| `11×14×15` |  1468 (?)   | 1460 (1471)  | 1460 (1471)  | 1460 (1471) |
| `11×14×16` |  1564 (?)   |   1564 (?)   | 1548 (1571)  |  1564 (?)   |
| `11×15×15` |  1548 (?)   |   1548 (?)   |     1540     |  1548 (?)   |
| `11×15×16` |  1657 (?)   |   1657 (?)   |     1656     |  1657 (?)   |
| `11×16×16` |  1752 (?)   |   1752 (?)   |     1724     |  1752 (?)   |
| `12×12×12` |  1071 (?)   |   1071 (?)   |     1040     |  1071 (?)   |
| `12×12×13` |  1188 (?)   |   1188 (?)   |     1152     |  1188 (?)   |
| `12×12×14` |  1271 (?)   |   1271 (?)   | 1240 (1250)  |  1271 (?)   |
| `12×12×15` |  1344 (?)   |   1344 (?)   |     1280     |  1344 (?)   |
| `12×12×16` |  1404 (?)   |   1404 (?)   |     1392     |  1404 (?)   |
| `12×13×13` |  1298 (?)   |   1298 (?)   |     1274     |  1298 (?)   |
| `12×13×14` |  1389 (?)   |   1389 (?)   |     1382     |  1389 (?)   |
| `12×13×15` |  1470 (?)   |   1470 (?)   |     1460     |  1470 (?)   |
| `12×13×16` |  1548 (?)   |   1548 (?)   | 1548 (1556)  |  1548 (?)   |
| `12×14×14` |  1484 (?)   |   1484 (?)   |     1481     |  1484 (?)   |
| `12×14×15` |  1560 (?)   |   1560 (?)   |     1540     |  1560 (?)   |
| `12×14×16` |  1664 (?)   |   1664 (?)   |     1638     |  1664 (?)   |
| `12×15×15` |  1650 (?)   |   1650 (?)   |     1600     |  1650 (?)   |
| `12×15×16` |  1769 (?)   |   1769 (?)   |     1728     |  1769 (?)   |
| `12×16×16` |  1862 (?)   |   1862 (?)   |     1824     |  1862 (?)   |
| `13×13×13` |  1426 (?)   |   1426 (?)   | 1421 (1426)  |  1426 (?)   |
| `13×13×14` |  1511 (?)   | 1511 (1524)  | 1511 (1524)  | 1511 (1524) |
| `13×13×15` |  1605 (?)   |     1605     |     1605     |    1605     |
| `13×13×16` |  1711 (?)   |   1711 (?)   | 1704 (1713)  |  1711 (?)   |
| `13×14×14` |  1614 (?)   | 1614 (1625)  | 1614 (1625)  | 1614 (1625) |
| `13×14×15` |  1698 (?)   | 1698 (1714)  | 1698 (1714)  | 1698 (1714) |
| `13×14×16` |  1820 (?)   |   1820 (?)   | 1806 (1825)  |  1820 (?)   |
| `13×15×15` |  1803 (?)   |     1803     |     1803     |    1803     |
| `13×15×16` |  1926 (?)   | 1926 (1932)  | 1908 (1932)  | 1926 (1932) |
| `13×16×16` |  2038 (?)   |   2038 (?)   |     2022     |  2038 (?)   |
| `14×14×14` |  1725 (?)   |   1725 (?)   |     1719     |  1725 (?)   |
| `14×14×15` |  1813 (?)   |     1813     |     1813     |    1813     |
| `14×14×16` |  1943 (?)   |   1943 (?)   | 1938 (1939)  |  1943 (?)   |
| `14×15×15` |  1905 (?)   |     1905     |     1905     |    1905     |
| `14×15×16` |  2043 (?)   |   2043 (?)   |     2016     |  2043 (?)   |
| `14×16×16` |  2170 (?)   |   2170 (?)   |     2142     |  2170 (?)   |
| `15×15×15` |  2058 (?)   |   2058 (?)   |     2058     |  2058 (?)   |
| `15×15×16` |  2160 (?)   |   2160 (?)   | 2155 (2173)  |  2160 (?)   |
| `15×16×16` |  2302 (?)   |   2302 (?)   |     2262     |  2302 (?)   |
| `16×16×16` |  2401 (?)   |   2401 (?)   |     2304     |  2401 (?)   |

### Coefficient set status
* total schemes: 680 (29 better Strassen)
* `ZT` schemes: 275 (40.44%)
* `Z` schemes: 117 (17.21%)
* `Q` schemes: 288 (42.35%)


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
