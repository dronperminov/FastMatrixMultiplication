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

* [Fast Matrix Multiplication via Ternary Meta Flip Graphs](https://arxiv.org/abs/2511.20317) (arxiv)
* [Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication](https://arxiv.org/abs/2512.13365) (arxiv)
* [A 58-Addition, Rank-23 Scheme for General 3x3 Matrix Multiplication](https://arxiv.org/abs/2512.21980) (arxiv)
* [Fast Matrix Multiplication in Small Formats: Discovering New Schemes with an Open-Source Flip Graph Framework](https://arxiv.org/abs/2603.02398) (arxiv)

## Key results

### New best ranks
New schemes have been discovered that improve the state-of-the-art for matrix multiplication achieving lower ranks than previously known.

|   Format   |  Prev rank  |                          New rank                          |        ω        |
|:----------:|:-----------:|:----------------------------------------------------------:|:---------------:|
|  `2x4x11`  |  71 (`Q`)   |     [70](schemes/results/ZT/2x4x11_m70_ZT.json) (`ZT`)     |   2.846666725   |
|  `3x5x9`   |  104 (`Z`)  |   [102](schemes/results/ZT/3x5x9_m102_ZT.json) (`ZT/Z`)    |   2.828571093   |
|  `3x5x10`  |  115 (`Z`)  |    [114](schemes/results/ZT/3x5x10_m114_ZT.json) (`ZT`)    |   2.835687395   |
|  `3x7x9`   |  142 (`Q`)  |    [141](schemes/results/ZT/3x7x9_m141_ZT.json) (`ZT`)     |   2.832315186   |
|  `3x7x13`  |  205 (`Q`)  |   [204](schemes/results/ZT/3x7x13_m204_ZT.json) (`ZT/Q`)   |   2.844182227   |
|  `3x7x14`  |  220 (`Q`)  |    [219](schemes/results/ZT/3x7x14_m219_ZT.json) (`ZT`)    |   2.844547952   |
|  `3x7x15`  |  236 (`Q`)  |     [235](schemes/results/Q/3x7x15_m235_Q.json) (`Q`)      |   2.847205515   |
|  `3x9x11`  |  224 (`Q`)  |     [222](schemes/results/Q/3x9x11_m222_Q.json) (`Q`)      |   2.846644652   |
|  `3x9x13`  |  262 (`Q`)  |     [261](schemes/results/Q/3x9x13_m261_Q.json) (`Q`)      |   2.848348427   |
|  `3x9x14`  |  283 (`Q`)  |    [281](schemes/results/ZT/3x9x14_m281_ZT.json) (`ZT`)    |   2.850103717   |
| `3x10x11`  |  249 (`Q`)  |     [248](schemes/results/Q/3x10x11_m248_Q.json) (`Q`)     |   2.852219687   |
| `3x10x14`  |  314 (`Q`)  |   [312](schemes/results/ZT/3x10x14_m312_ZT.json) (`ZT`)    |   2.852364741   |
| `3x10x15`  |  336 (`Q`)  |   [335](schemes/results/ZT/3x10x15_m335_ZT.json) (`ZT`)    |   2.855080165   |
| `3x10x16`  |  360 (`Q`)  |   [355](schemes/results/ZT/3x10x16_m355_ZT.json) (`ZT`)    |   2.853411678   |
| `3x11x14`  |  346 (`Q`)  |     [345](schemes/results/Q/3x11x14_m345_Q.json) (`Q`)     |   2.857215849   |
| `3x13x13`  |  379 (`Q`)  |     [378](schemes/results/Q/3x13x13_m378_Q.json) (`Q`)     |   2.858577688   |
| `3x13x14`  |  408 (`Q`)  |     [407](schemes/results/Q/3x13x14_m407_Q.json) (`Q`)     |   2.860150618   |
| `3x13x15`  |  436 (`Q`)  |     [435](schemes/results/Q/3x13x15_m435_Q.json) (`Q`)     |   2.860506655   |
| `3x13x16`  |  465 (`Q`)  |     [464](schemes/results/Q/3x13x16_m464_Q.json) (`Q`)     |   2.861905425   |
| `3x14x14`  |  440 (`Q`)  |  [438](schemes/results/ZT/3x14x14_m438_ZT.json) (`ZT/Q`)   |   2.861445516   |
| `3x14x15`  |  470 (`Q`)  |     [469](schemes/results/Q/3x14x15_m469_Q.json) (`Q`)     |   2.862645108   |
| `3x14x16`  |  502 (`Q`)  |  [500](schemes/results/ZT/3x14x16_m500_ZT.json) (`ZT/Q`)   |   2.863761055   |
| `3x15x16`  |  536 (`Q`)  |   [534](schemes/results/ZT/3x15x16_m534_ZT.json) (`ZT`)    |   2.863728243   |
| `3x16x16`  |  574 (`Q`)  |     [569](schemes/results/Q/3x16x16_m569_Q.json) (`Q`)     |   2.864576103   |
|  `4x4x10`  |  120 (`Q`)  |    [115](schemes/results/ZT/4x4x10_m115_ZT.json) (`ZT`)    | **2.804789925** |
|  `4x4x11`  |  130 (`Q`)  |    [129](schemes/results/ZT/4x4x11_m129_ZT.json) (`ZT`)    |   2.819743225   |
|  `4x4x12`  |  142 (`Q`)  |    [141](schemes/results/ZT/4x4x12_m141_ZT.json) (`ZT`)    |   2.823831239   |
|  `4x4x14`  |  165 (`Q`)  |     [163](schemes/results/Q/4x4x14_m163_Q.json) (`Q`)      |   2.823771262   |
|  `4x4x15`  |  177 (`Q`)  |    [176](schemes/results/ZT/4x4x15_m176_ZT.json) (`ZT`)    |   2.830226950   |
|  `4x4x16`  |  189 (`Q`)  |    [188](schemes/results/ZT/4x4x16_m188_ZT.json) (`ZT`)    |   2.832970819   |
|  `4x5x9`   |  136 (`Q`)  |    [132](schemes/results/ZT/4x5x9_m132_ZT.json) (`ZT`)     |   2.820821776   |
|  `4x5x10`  |  151 (`Z`)  |    [146](schemes/results/ZT/4x5x10_m146_ZT.json) (`ZT`)    |   2.821805270   |
|  `4x5x11`  |  165 (`Z`)  |    [160](schemes/results/ZT/4x5x11_m160_ZT.json) (`ZT`)    |   2.822872235   |
|  `4x5x12`  |  180 (`Z`)  |    [174](schemes/results/ZT/4x5x12_m174_ZT.json) (`ZT`)    |   2.823971094   |
|  `4x5x13`  |  194 (`Z`)  |    [191](schemes/results/ZT/4x5x13_m191_ZT.json) (`ZT`)    |   2.833613095   |
|  `4x5x14`  |  208 (`Z`)  |     [206](schemes/results/Q/4x5x14_m206_Q.json) (`Q`)      |   2.836597217   |
|  `4x5x15`  |  226 (`Z`)  |    [221](schemes/results/ZT/4x5x15_m221_ZT.json) (`ZT`)    |   2.839254157   |
|  `4x5x16`  |  240 (`Q`)  |    [235](schemes/results/ZT/4x5x16_m235_ZT.json) (`ZT`)    |   2.839432229   |
|  `4x6x13`  |  228 (`Z`)  |    [227](schemes/results/ZT/4x6x13_m227_ZT.json) (`ZT`)    |   2.833857047   |
|  `4x6x16`  | 280 (`ZT`)  |    [276](schemes/results/ZT/4x6x16_m276_ZT.json) (`ZT`)    |   2.833509566   |
|  `4x7x8`   | 164 (`ZT`)  |    [161](schemes/results/ZT/4x7x8_m161_ZT.json) (`ZT`)     |   2.816927225   |
|  `4x7x11`  |  227 (`Z`)  |     [224](schemes/results/Q/4x7x11_m224_Q.json) (`Q`)      |   2.833273201   |
|  `4x7x12`  |  246 (`Z`)  |    [242](schemes/results/ZT/4x7x12_m242_ZT.json) (`ZT`)    |   2.830754429   |
|  `4x7x13`  |  266 (`Q`)  |    [265](schemes/results/ZT/4x7x13_m265_ZT.json) (`ZT`)    |   2.838520048   |
|  `4x7x14`  | 285 (`ZT`)  |    [284](schemes/results/ZT/4x7x14_m284_ZT.json) (`ZT`)    |   2.838080655   |
|  `4x7x15`  |  307 (`Q`)  |   [305](schemes/results/ZT/4x7x15_m305_ZT.json) (`ZT/Q`)   |   2.841094648   |
|  `4x7x16`  | 324 (`ZT`)  |    [322](schemes/results/ZT/4x7x16_m322_ZT.json) (`ZT`)    |   2.837713576   |
|  `4x8x8`   | 182 (`ZT`)  |    [180](schemes/results/ZT/4x8x8_m180_ZT.json) (`ZT`)     |   2.809444911   |
|  `4x9x10`  | 255 (`ZT`)  |    [250](schemes/results/ZT/4x9x10_m250_ZT.json) (`ZT`)    |   2.814150526   |
|  `4x9x11`  | 280 (`ZT`)  |    [275](schemes/results/ZT/4x9x11_m275_ZT.json) (`ZT`)    |   2.817111923   |
|  `4x9x13`  |  329 (`Q`)  |    [325](schemes/results/ZT/4x9x13_m325_ZT.json) (`ZT`)    |   2.822080998   |
|  `4x9x14`  |  355 (`Z`)  |   [350](schemes/results/ZT/4x9x14_m350_ZT.json) (`ZT/Z`)   |   2.824199930   |
|  `4x9x16`  | 400 (`ZT`)  |    [398](schemes/results/ZT/4x9x16_m398_ZT.json) (`ZT`)    |   2.825527347   |
| `4x10x15`  |  417 (`Q`)  |     [413](schemes/results/Q/4x10x15_m413_Q.json) (`Q`)     |   2.824846255   |
| `4x11x12`  |  365 (`Z`)  |  [362](schemes/results/ZT/4x11x12_m362_ZT.json) (`ZT/Q`)   |   2.819374888   |
| `4x11x15`  |  452 (`Q`)  |     [449](schemes/results/Q/4x11x15_m449_Q.json) (`Q`)     |   2.821995048   |
| `4x11x16`  |  489 (`Q`)  |   [480](schemes/results/ZT/4x11x16_m480_ZT.json) (`ZT`)    |   2.824765046   |
| `4x12x12`  | 390 (`ZT`)  |   [389](schemes/results/ZT/4x12x12_m389_ZT.json) (`ZT`)    |   2.814731749   |
| `4x12x13`  |  426 (`Q`)  |     [422](schemes/results/Q/4x12x13_m422_Q.json) (`Q`)     |   2.817680586   |
| `4x12x14`  |  456 (`Q`)  |     [452](schemes/results/Q/4x12x14_m452_Q.json) (`Q`)     |   2.817253261   |
| `4x12x16`  | 520 (`ZT`)  |   [513](schemes/results/ZT/4x12x16_m513_ZT.json) (`ZT`)    |   2.817793502   |
| `4x13x15`  |  528 (`Q`)  |     [520](schemes/results/Q/4x13x15_m520_Q.json) (`Q`)     |   2.817338694   |
| `4x13x16`  | 568 (`ZT`)  |  [560](schemes/results/ZT/4x13x16_m560_ZT.json) (`ZT/Z`)   |   2.823361605   |
| `4x14x15`  |  568 (`Q`)  |     [557](schemes/results/Q/4x14x15_m557_Q.json) (`Q`)     |   2.816955831   |
| `4x14x16`  | 610 (`ZT`)  |   [598](schemes/results/ZT/4x14x16_m598_ZT.json) (`ZT`)    |   2.821556397   |
| `4x15x15`  | 600 (`ZT`)  |     [596](schemes/results/Q/4x15x15_m596_Q.json) (`Q`)     |   2.818231324   |
| `4x15x16`  |  640 (`Q`)  |     [632](schemes/results/Q/4x15x16_m632_Q.json) (`Q`)     |   2.817366557   |
| `4x16x16`  | 676 (`ZT`)  |   [666](schemes/results/ZT/4x16x16_m666_ZT.json) (`ZT`)    |   2.813813510   |
|  `5x5x9`   |  167 (`Z`)  |    [161](schemes/results/ZT/5x5x9_m161_ZT.json) (`ZT`)     |   2.814610506   |
|  `5x5x10`  |  184 (`Q`)  |    [178](schemes/results/ZT/5x5x10_m178_ZT.json) (`ZT`)    |   2.815441580   |
|  `5x5x11`  |  202 (`Q`)  |    [195](schemes/results/ZT/5x5x11_m195_ZT.json) (`ZT`)    |   2.816386568   |
|  `5x5x12`  |  220 (`Z`)  |    [204](schemes/results/ZT/5x5x12_m204_ZT.json) (`ZT`)    | **2.797154354** |
|  `5x5x13`  |  237 (`Z`)  |    [227](schemes/results/ZT/5x5x13_m227_ZT.json) (`ZT`)    |   2.813855803   |
|  `5x5x14`  |  254 (`Z`)  |    [244](schemes/results/ZT/5x5x14_m244_ZT.json) (`ZT`)    |   2.815242892   |
|  `5x5x15`  |  271 (`Q`)  |    [262](schemes/results/ZT/5x5x15_m262_ZT.json) (`ZT`)    |   2.818498736   |
|  `5x5x16`  |  288 (`Q`)  |    [280](schemes/results/ZT/5x5x16_m280_ZT.json) (`ZT`)    |   2.821408468   |
|  `5x6x9`   |  197 (`Z`)  |    [193](schemes/results/ZT/5x6x9_m193_ZT.json) (`ZT`)     |   2.820092998   |
|  `5x6x10`  |  218 (`Z`)  |    [216](schemes/results/ZT/5x6x10_m216_ZT.json) (`ZT`)    |   2.827217780   |
|  `5x7x8`   |  205 (`Q`)  |    [204](schemes/results/ZT/5x7x8_m204_ZT.json) (`ZT`)     |   2.831402964   |
|  `5x9x9`   |  294 (`Q`)  |    [293](schemes/results/ZT/5x9x9_m293_ZT.json) (`ZT`)     |   2.838247561   |
|  `5x9x15`  |  474 (`Z`)  |     [463](schemes/results/Q/5x9x15_m463_Q.json) (`Q`)      |   2.826399572   |
| `5x10x12`  |  413 (`Z`)  |   [408](schemes/results/ZT/5x10x12_m408_ZT.json) (`ZT`)    |   2.819133943   |
| `5x11x12`  |  455 (`Q`)  |     [454](schemes/results/Q/5x11x12_m454_Q.json) (`Q`)     |   2.827112377   |
| `5x12x15`  |  615 (`Q`)  |   [612](schemes/results/ZT/5x12x15_m612_ZT.json) (`ZT`)    |   2.829914687   |
| `5x12x16`  |  656 (`Q`)  |     [655](schemes/results/Q/5x12x16_m655_Q.json) (`Q`)     |   2.832983066   |
| `5x13x13`  |  588 (`Q`)  |     [587](schemes/results/Q/5x13x13_m587_Q.json) (`Q`)     |   2.837827448   |
| `5x13x14`  |  630 (`Q`)  |     [628](schemes/results/Q/5x13x14_m628_Q.json) (`Q`)     |   2.836688582   |
| `5x14x14`  |  676 (`Q`)  |  [672](schemes/results/ZT/5x14x14_m672_ZT.json) (`ZT/Z`)   |   2.835662569   |
| `5x15x15`  | 762 (`ZT`)  |   [761](schemes/results/ZT/5x15x15_m761_ZT.json) (`ZT`)    |   2.833078290   |
|  `6x6x13`  |  316 (`Q`)  |     [315](schemes/results/Q/6x6x13_m315_Q.json) (`Q`)      | **2.806832057** |
|  `6x7x7`   | 215 (`ZT`)  |    [212](schemes/results/ZT/6x7x7_m212_ZT.json) (`ZT`)     |   2.827400948   |
|  `6x7x8`   | 239 (`ZT`)  |    [238](schemes/results/ZT/6x7x8_m238_ZT.json) (`ZT`)     |   2.822158898   |
|  `6x7x9`   | 270 (`ZT`)  |    [264](schemes/results/ZT/6x7x9_m264_ZT.json) (`ZT`)     |   2.818558639   |
|  `6x7x10`  |  296 (`Z`)  |     [293](schemes/results/Q/6x7x10_m293_Q.json) (`Q`)      |   2.821158816   |
|  `6x8x10`  |  329 (`Z`)  |    [327](schemes/results/ZT/6x8x10_m327_ZT.json) (`ZT`)    |   2.813489198   |
|  `6x8x16`  |  511 (`Q`)  |    [510](schemes/results/ZT/6x8x16_m510_ZT.json) (`ZT`)    |   2.815145110   |
|  `6x9x9`   |  342 (`Z`)  |      [332](schemes/results/Q/6x9x9_m332_Q.json) (`Q`)      |   2.815198446   |
|  `6x9x10`  |  373 (`Z`)  |     [367](schemes/results/Q/6x9x10_m367_Q.json) (`Q`)      |   2.815845324   |
|  `6x9x11`  |  407 (`Q`)  |     [404](schemes/results/Q/6x9x11_m404_Q.json) (`Q`)      |   2.818942356   |
|  `6x9x12`  |  434 (`Q`)  |     [429](schemes/results/Q/6x9x12_m429_Q.json) (`Q`)      |   2.808878248   |
|  `6x9x13`  |  474 (`Q`)  |     [468](schemes/results/Q/6x9x13_m468_Q.json) (`Q`)      |   2.814402245   |
|  `6x9x14`  |  500 (`Q`)  |     [494](schemes/results/Q/6x9x14_m494_Q.json) (`Q`)      |   2.807406517   |
|  `6x9x15`  |  532 (`Q`)  |     [529](schemes/results/Q/6x9x15_m529_Q.json) (`Q`)      |   2.809148737   |
|  `6x9x16`  |  556 (`Q`)  |     [552](schemes/results/Q/6x9x16_m552_Q.json) (`Q`)      | **2.801218708** |
| `6x10x15`  |  597 (`Q`)  |   [594](schemes/results/ZT/6x10x15_m594_ZT.json) (`ZT`)    |   2.816748899   |
| `6x11x12`  |  524 (`Q`)  |   [521](schemes/results/ZT/6x11x12_m521_ZT.json) (`ZT`)    |   2.811757811   |
| `6x11x15`  |  661 (`Z`)  |   [653](schemes/results/ZT/6x11x15_m653_ZT.json) (`ZT`)    |   2.819014665   |
| `6x11x16`  |  695 (`Q`)  |  [684](schemes/results/ZT/6x11x16_m684_ZT.json) (`ZT/Q`)   |   2.812868273   |
| `6x12x13`  |  616 (`Q`)  |   [615](schemes/results/ZT/6x12x13_m615_ZT.json) (`ZT`)    |   2.815835948   |
| `6x12x14`  |  658 (`Q`)  |     [645](schemes/results/Q/6x12x14_m645_Q.json) (`Q`)     | **2.806322591** |
| `6x12x15`  |  705 (`Z`)  |     [686](schemes/results/Q/6x12x15_m686_Q.json) (`Q`)     | **2.805072101** |
| `6x12x16`  |  746 (`Q`)  |  [736](schemes/results/ZT/6x12x16_m736_ZT.json) (`ZT/Z`)   |   2.809331029   |
| `6x13x13`  |  680 (`Q`)  |     [678](schemes/results/Q/6x13x13_m678_Q.json) (`Q`)     |   2.825542860   |
| `6x13x14`  |  730 (`Q`)  |     [726](schemes/results/Q/6x13x14_m726_Q.json) (`Q`)     |   2.824944345   |
| `6x13x15`  |  771 (`Z`)  |  [763](schemes/results/ZT/6x13x15_m763_ZT.json) (`ZT/Z`)   |   2.818464723   |
| `6x13x16`  |  819 (`Q`)  |     [798](schemes/results/Q/6x13x16_m798_Q.json) (`Q`)     |   2.811823417   |
| `6x14x14`  |  777 (`Q`)  |     [776](schemes/results/Q/6x14x14_m776_Q.json) (`Q`)     |   2.823594480   |
| `6x14x15`  |  825 (`Q`)  |  [814](schemes/results/ZT/6x14x15_m814_ZT.json) (`ZT/Z`)   |   2.816396649   |
| `6x14x16`  |  880 (`Q`)  |   [864](schemes/results/ZT/6x14x16_m864_ZT.json) (`ZT`)    |   2.815990055   |
| `6x15x15`  | 870 (`ZT`)  |     [859](schemes/results/Q/6x15x15_m859_Q.json) (`Q`)     |   2.811834182   |
| `6x15x16`  |  928 (`Q`)  |  [920](schemes/results/ZT/6x15x16_m920_ZT.json) (`ZT/Z`)   |   2.815181444   |
| `6x16x16`  | 988 (`ZT`)  |   [972](schemes/results/ZT/6x16x16_m972_ZT.json) (`ZT`)    |   2.812899669   |
|  `7x7x10`  |  346 (`Z`)  |     [345](schemes/results/Q/7x7x10_m345_Q.json) (`Q`)      |   2.830075228   |
|  `7x8x9`   |  350 (`Q`)  |   [347](schemes/results/ZT/7x8x9_m347_ZT.json) (`ZT/Z`)    |   2.820049700   |
|  `7x8x12`  |  454 (`Q`)  |   [452](schemes/results/ZT/7x8x12_m452_ZT.json) (`ZT/Z`)   |   2.817253261   |
|  `7x8x15`  |  571 (`Q`)  |     [557](schemes/results/Q/7x8x15_m557_Q.json) (`Q`)      |   2.816955831   |
|  `7x8x16`  |  603 (`Q`)  |    [598](schemes/results/ZT/7x8x16_m598_ZT.json) (`ZT`)    |   2.821556397   |
|  `7x9x9`   |  398 (`Q`)  |    [396](schemes/results/ZT/7x9x9_m396_ZT.json) (`ZT`)     |   2.830161790   |
|  `7x9x10`  |  437 (`Z`)  |   [433](schemes/results/ZT/7x9x10_m433_ZT.json) (`ZT/Z`)   |   2.825473910   |
|  `7x9x11`  |  480 (`Q`)  |    [478](schemes/results/ZT/7x9x11_m478_ZT.json) (`ZT`)    |   2.829651018   |
|  `7x9x12`  |  510 (`Q`)  |     [508](schemes/results/Q/7x9x12_m508_Q.json) (`Q`)      |   2.820055471   |
|  `7x9x15`  |  639 (`Z`)  |     [634](schemes/results/Q/7x9x15_m634_Q.json) (`Q`)      |   2.825226157   |
| `7x10x12`  |  564 (`Z`)  |     [557](schemes/results/Q/7x10x12_m557_Q.json) (`Q`)     |   2.816955831   |
| `7x10x15`  |  711 (`Q`)  |  [694](schemes/results/ZT/7x10x15_m694_ZT.json) (`ZT/Z`)   |   2.821431419   |
| `7x10x16`  |  752 (`Q`)  |     [736](schemes/results/Q/7x10x16_m736_Q.json) (`Q`)     |   2.820602981   |
| `7x11x15`  |  778 (`Z`)  |     [777](schemes/results/Q/7x11x15_m777_Q.json) (`Q`)     |   2.831357038   |
| `7x11x16`  |  827 (`Q`)  |  [822](schemes/results/ZT/7x11x16_m822_ZT.json) (`ZT/Z`)   |   2.829413433   |
| `7x12x15`  |  831 (`Z`)  |  [815](schemes/results/ZT/7x12x15_m815_ZT.json) (`ZT/Z`)   |   2.816912591   |
| `7x12x16`  |  880 (`Q`)  |  [878](schemes/results/ZT/7x12x16_m878_ZT.json) (`ZT/Z`)   |   2.822684315   |
| `7x13x13`  |  795 (`Q`)  |     [794](schemes/results/Q/7x13x13_m794_Q.json) (`Q`)     |   2.830948485   |
| `7x13x14`  |  852 (`Q`)  |     [850](schemes/results/Q/7x13x14_m850_Q.json) (`Q`)     |   2.830202017   |
| `7x13x16`  |  968 (`Q`)  |     [962](schemes/results/Q/7x13x16_m962_Q.json) (`Q`)     |   2.829297704   |
| `7x14x14`  |  912 (`Q`)  |  [909](schemes/results/ZT/7x14x14_m909_ZT.json) (`ZT/Z`)   |   2.829037251   |
| `7x14x15`  |  976 (`Z`)  |  [952](schemes/results/ZT/7x14x15_m952_ZT.json) (`ZT/Z`)   |   2.821286881   |
| `7x14x16`  | 1034 (`Q`)  |    [1022](schemes/results/Q/7x14x16_m1022_Q.json) (`Q`)    |   2.825469455   |
| `7x15x16`  | 1099 (`Q`)  |    [1083](schemes/results/Q/7x15x16_m1083_Q.json) (`Q`)    |   2.822639497   |
|  `8x8x15`  |  635 (`Q`)  |     [628](schemes/results/Q/8x8x15_m628_Q.json) (`Q`)      |   2.814592730   |
|  `8x8x16`  |  672 (`Q`)  |    [666](schemes/results/ZT/8x8x16_m666_ZT.json) (`ZT`)    |   2.813813510   |
|  `8x9x10`  | 487 (`ZT`)  |   [482](schemes/results/ZT/8x9x10_m482_ZT.json) (`ZT/Z`)   |   2.817012414   |
|  `8x9x11`  |  533 (`Q`)  |    [521](schemes/results/ZT/8x9x11_m521_ZT.json) (`ZT`)    |   2.811757811   |
|  `8x9x13`  |  624 (`Z`)  |    [615](schemes/results/ZT/8x9x13_m615_ZT.json) (`ZT`)    |   2.815835948   |
|  `8x9x14`  |  669 (`Z`)  |   [654](schemes/results/ZT/8x9x14_m654_ZT.json) (`ZT/Z`)   |   2.812333691   |
|  `8x9x15`  |  705 (`Z`)  |   [699](schemes/results/ZT/8x9x15_m699_ZT.json) (`ZT/Z`)   |   2.813135327   |
|  `8x9x16`  |  746 (`Q`)  |    [735](schemes/results/ZT/8x9x16_m735_ZT.json) (`ZT`)    |   2.808752406   |
| `8x10x10`  | 532 (`ZT`)  |   [528](schemes/results/ZT/8x10x10_m528_ZT.json) (`ZT`)    |   2.813520009   |
| `8x10x12`  |  630 (`Z`)  |     [624](schemes/results/Q/8x10x12_m624_Q.json) (`Q`)     |   2.811801179   |
| `8x10x14`  |  728 (`Z`)  |   [726](schemes/results/ZT/8x10x14_m726_ZT.json) (`ZT`)    |   2.814757685   |
| `8x10x15`  |  789 (`Z`)  |     [778](schemes/results/Q/8x10x15_m778_Q.json) (`Q`)     |   2.816637962   |
| `8x10x16`  |  832 (`Q`)  |     [822](schemes/results/Q/8x10x16_m822_Q.json) (`Q`)     |   2.814298209   |
| `8x11x12`  |  680 (`Q`)  |     [676](schemes/results/Q/8x11x12_m676_Q.json) (`Q`)     |   2.807798855   |
| `8x11x15`  |  859 (`Z`)  |     [848](schemes/results/Q/8x11x15_m848_Q.json) (`Q`)     |   2.815247371   |
| `8x11x16`  |  920 (`Q`)  |     [904](schemes/results/Q/8x11x16_m904_Q.json) (`Q`)     |   2.816647975   |
| `8x12x13`  |  798 (`Q`)  |     [781](schemes/results/Q/8x12x13_m781_Q.json) (`Q`)     | **2.802762167** |
| `8x12x14`  |  861 (`Z`)  |     [843](schemes/results/Q/8x12x14_m843_Q.json) (`Q`)     | **2.805742480** |
| `8x12x15`  | 915 (`ZT`)  |     [904](schemes/results/Q/8x12x15_m904_Q.json) (`Q`)     |   2.807944089   |
| `8x13x14`  |  945 (`Z`)  |     [944](schemes/results/Q/8x13x14_m944_Q.json) (`Q`)     |   2.821517755   |
| `8x13x15`  | 1005 (`ZT`) |   [991](schemes/results/ZT/8x13x15_m991_ZT.json) (`ZT`)    |   2.814866970   |
| `8x13x16`  | 1064 (`Q`)  |    [1054](schemes/results/Q/8x13x16_m1054_Q.json) (`Q`)    |   2.815302758   |
| `8x14x14`  | 1008 (`Z`)  |    [1004](schemes/results/Q/8x14x14_m1004_Q.json) (`Q`)    |   2.818224059   |
| `8x14x15`  | 1080 (`ZT`) | [1063](schemes/results/ZT/8x14x15_m1063_ZT.json) (`ZT/Q`)  |   2.815109808   |
| `8x14x16`  | 1138 (`Q`)  |    [1104](schemes/results/Q/8x14x16_m1104_Q.json) (`Q`)    | **2.806012534** |
| `8x15x15`  | 1140 (`ZT`) |    [1130](schemes/results/Q/8x15x15_m1130_Q.json) (`Q`)    |   2.813661626   |
| `8x15x16`  | 1198 (`Q`)  |    [1185](schemes/results/Q/8x15x16_m1185_Q.json) (`Q`)    |   2.808501081   |
| `8x16x16`  | 1248 (`Q`)  |    [1230](schemes/results/Q/8x16x16_m1230_Q.json) (`Q`)    | **2.799393436** |
|  `9x9x9`   | 498 (`ZT`)  |    [486](schemes/results/ZT/9x9x9_m486_ZT.json) (`ZT`)     |   2.815464877   |
|  `9x9x14`  |  726 (`Q`)  |     [720](schemes/results/Q/9x9x14_m720_Q.json) (`Q`)      | **2.806246597** |
|  `9x9x15`  |  783 (`Q`)  |     [760](schemes/results/Q/9x9x15_m760_Q.json) (`Q`)      | **2.801824302** |
|  `9x9x16`  |  825 (`Q`)  |     [822](schemes/results/Q/9x9x16_m822_Q.json) (`Q`)      |   2.809420228   |
| `9x10x10`  |  600 (`Z`)  |   [597](schemes/results/ZT/9x10x10_m597_ZT.json) (`ZT`)    |   2.818970672   |
| `9x10x12`  |  684 (`Q`)  |     [668](schemes/results/Q/9x10x12_m668_Q.json) (`Q`)     | **2.793651686** |
| `9x10x13`  |  772 (`Z`)  |     [758](schemes/results/Q/9x10x13_m758_Q.json) (`Q`)     |   2.815672846   |
| `9x10x14`  |  820 (`Z`)  |     [808](schemes/results/Q/9x10x14_m808_Q.json) (`Q`)     |   2.813287623   |
| `9x10x15`  | 870 (`ZT`)  |   [864](schemes/results/ZT/9x10x15_m864_ZT.json) (`ZT`)    |   2.814249815   |
| `9x10x16`  |  939 (`Q`)  |     [916](schemes/results/Q/9x10x16_m916_Q.json) (`Q`)     |   2.813383975   |
| `9x11x11`  |  725 (`Q`)  |     [715](schemes/results/Q/9x11x11_m715_Q.json) (`Q`)     |   2.819505933   |
| `9x11x12`  |  760 (`Q`)  |     [738](schemes/results/Q/9x11x12_m738_Q.json) (`Q`)     | **2.798270808** |
| `9x11x13`  |  849 (`Z`)  |     [835](schemes/results/Q/9x11x13_m835_Q.json) (`Q`)     |   2.818729064   |
| `9x11x14`  |  904 (`Z`)  |     [882](schemes/results/Q/9x11x14_m882_Q.json) (`Q`)     |   2.812562599   |
| `9x11x15`  |  981 (`Q`)  |   [956](schemes/results/ZT/9x11x15_m956_ZT.json) (`ZT`)    |   2.819087272   |
| `9x11x16`  | 1030 (`Z`)  |  [996](schemes/results/ZT/9x11x16_m996_ZT.json) (`ZT/Z`)   |   2.811083198   |
| `9x12x13`  |  900 (`Q`)  |  [878](schemes/results/ZT/9x12x13_m878_ZT.json) (`ZT/Q`)   | **2.805673201** |
| `9x12x14`  |  945 (`Q`)  |     [940](schemes/results/Q/9x12x14_m940_Q.json) (`Q`)     | **2.805232985** |
| `9x12x15`  | 1000 (`Q`)  |     [996](schemes/results/Q/9x12x15_m996_Q.json) (`Q`)     | **2.802534955** |
| `9x12x16`  | 1080 (`Q`)  |    [1035](schemes/results/Q/9x12x16_m1035_Q.json) (`Q`)    | **2.793729377** |
| `9x13x13`  |  996 (`Z`)  |     [981](schemes/results/Q/9x13x13_m981_Q.json) (`Q`)     |   2.820440786   |
| `9x13x14`  | 1063 (`Z`)  |    [1024](schemes/results/Q/9x13x14_m1024_Q.json) (`Q`)    |   2.809588658   |
| `9x13x15`  | 1135 (`Q`)  | [1119](schemes/results/ZT/9x13x15_m1119_ZT.json) (`ZT/Z`)  |   2.819269106   |
| `9x13x16`  | 1210 (`Z`)  |  [1167](schemes/results/ZT/9x13x16_m1167_ZT.json) (`ZT`)   |   2.811843698   |
| `9x14x14`  | 1136 (`Z`)  |    [1101](schemes/results/Q/9x14x14_m1101_Q.json) (`Q`)    |   2.810831956   |
| `9x14x15`  | 1185 (`Q`)  |    [1175](schemes/results/Q/9x14x15_m1175_Q.json) (`Q`)    |   2.810993734   |
| `9x14x16`  | 1260 (`Q`)  |    [1254](schemes/results/Q/9x14x16_m1254_Q.json) (`Q`)    |   2.812806553   |
| `9x15x15`  | 1290 (`Q`)  |    [1236](schemes/results/Q/9x15x15_m1236_Q.json) (`Q`)    | **2.805463706** |
| `9x15x16`  | 1350 (`Z`)  | [1320](schemes/results/ZT/9x15x16_m1320_ZT.json) (`ZT/Z`)  |   2.807572842   |
| `9x16x16`  | 1444 (`ZT`) | [1380](schemes/results/ZT/9x16x16_m1380_ZT.json) (`ZT/Z`)  | **2.801393711** |
| `10x10x12` |  770 (`Z`)  |   [766](schemes/results/ZT/10x10x12_m766_ZT.json) (`ZT`)   |   2.810060733   |
| `10x11x12` |  850 (`Z`)  |    [849](schemes/results/Q/10x11x12_m849_Q.json) (`Q`)     |   2.815739433   |
| `10x11x15` | 1067 (`Q`)  | [1050](schemes/results/ZT/10x11x15_m1050_ZT.json) (`ZT/Z`) |   2.816973777   |
| `10x11x16` | 1136 (`Q`)  |  [1112](schemes/results/ZT/10x11x16_m1112_ZT.json) (`ZT`)  |   2.815676689   |
| `10x12x12` |  910 (`Z`)  |  [902](schemes/results/ZT/10x12x12_m902_ZT.json) (`ZT/Z`)  | **2.807030426** |
| `10x12x15` | 1140 (`ZT`) | [1122](schemes/results/ZT/10x12x15_m1122_ZT.json) (`ZT/Z`) |   2.810818006   |
| `10x12x16` | 1216 (`Q`)  |   [1176](schemes/results/Q/10x12x16_m1176_Q.json) (`Q`)    | **2.805475746** |
| `10x13x15` | 1242 (`Z`)  | [1230](schemes/results/ZT/10x13x15_m1230_ZT.json) (`ZT/Z`) |   2.817513014   |
| `10x13x16` | 1332 (`Z`)  |   [1318](schemes/results/Q/10x13x16_m1318_Q.json) (`Q`)    |   2.820846164   |
| `10x14x15` | 1327 (`Z`)  | [1314](schemes/results/ZT/10x14x15_m1314_ZT.json) (`ZT/Z`) |   2.816125387   |
| `10x14x16` | 1423 (`Z`)  |   [1398](schemes/results/Q/10x14x16_m1398_Q.json) (`Q`)    |   2.816663561   |
| `10x15x15` | 1395 (`Z`)  |   [1385](schemes/results/Q/10x15x15_m1385_Q.json) (`Q`)    |   2.811406977   |
| `10x15x16` | 1497 (`Z`)  |   [1482](schemes/results/Q/10x15x16_m1482_Q.json) (`Q`)    |   2.814186431   |
| `10x16x16` | 1586 (`ZT`) |   [1560](schemes/results/Q/10x16x16_m1560_Q.json) (`Q`)    |   2.810651214   |
| `11x11x12` |  936 (`Z`)  |    [922](schemes/results/Q/11x11x12_m922_Q.json) (`Q`)     |   2.812867384   |
| `11x11x15` | 1181 (`Z`)  |  [1169](schemes/results/ZT/11x11x15_m1169_ZT.json) (`ZT`)  |   2.824115356   |
| `11x11x16` | 1236 (`Q`)  |  [1230](schemes/results/ZT/11x11x16_m1230_ZT.json) (`ZT`)  |   2.820195393   |
| `11x12x12` |  990 (`Q`)  |    [968](schemes/results/Q/11x12x12_m968_Q.json) (`Q`)     | **2.799472327** |
| `11x12x13` | 1102 (`Z`)  |   [1082](schemes/results/Q/11x12x13_m1082_Q.json) (`Q`)    |   2.814231919   |
| `11x12x14` | 1182 (`Z`)  |   [1153](schemes/results/Q/11x12x14_m1153_Q.json) (`Q`)    |   2.811853672   |
| `11x12x15` | 1264 (`Q`)  | [1234](schemes/results/ZT/11x12x15_m1234_ZT.json) (`ZT/Z`) |   2.813129312   |
| `11x12x16` | 1312 (`Q`)  |   [1278](schemes/results/Q/11x12x16_m1278_Q.json) (`Q`)    | **2.803143027** |
| `11x13x13` | 1210 (`Z`)  |  [1205](schemes/results/ZT/11x13x13_m1205_ZT.json) (`ZT`)  |   2.827216655   |
| `11x13x14` | 1298 (`Z`)  |  [1292](schemes/results/ZT/11x13x14_m1292_ZT.json) (`ZT`)  |   2.827166171   |
| `11x13x15` | 1377 (`Z`)  |   [1371](schemes/results/Q/11x13x15_m1371_Q.json) (`Q`)    |   2.824949046   |
| `11x13x16` | 1472 (`Z`)  |   [1446](schemes/results/Q/11x13x16_m1446_Q.json) (`Q`)    |   2.822035717   |
| `11x14x14` | 1388 (`Z`)  |  [1376](schemes/results/ZT/11x14x14_m1376_ZT.json) (`ZT`)  |   2.824489318   |
| `11x14x15` | 1471 (`Z`)  | [1432](schemes/results/ZT/11x14x15_m1432_ZT.json) (`ZT/Z`) |   2.814780394   |
| `11x14x16` | 1571 (`Q`)  |   [1520](schemes/results/Q/11x14x16_m1520_Q.json) (`Q`)    |   2.814428649   |
| `11x15x16` | 1656 (`Q`)  |   [1605](schemes/results/Q/11x15x16_m1605_Q.json) (`Q`)    |   2.810502126   |
| `12x12x13` | 1152 (`Q`)  |   [1144](schemes/results/Q/12x12x13_m1144_Q.json) (`Q`)    | **2.803918249** |
| `12x12x14` | 1250 (`Q`)  |   [1234](schemes/results/Q/12x12x14_m1234_Q.json) (`Q`)    | **2.806467563** |
| `12x12x16` | 1392 (`Q`)  | [1380](schemes/results/ZT/12x12x16_m1380_ZT.json) (`ZT/Z`) | **2.801393711** |
| `12x13x14` | 1382 (`Q`)  |   [1370](schemes/results/Q/12x13x14_m1370_Q.json) (`Q`)    |   2.818044255   |
| `12x13x15` | 1460 (`Q`)  |   [1442](schemes/results/Q/12x13x15_m1442_Q.json) (`Q`)    |   2.812789736   |
| `12x13x16` | 1556 (`Q`)  |   [1509](schemes/results/Q/12x13x16_m1509_Q.json) (`Q`)    | **2.807000642** |
| `12x14x14` | 1481 (`Q`)  |   [1449](schemes/results/Q/12x14x14_m1449_Q.json) (`Q`)    |   2.812807792   |
| `12x14x15` | 1540 (`Q`)  |   [1538](schemes/results/Q/12x14x15_m1538_Q.json) (`Q`)    |   2.810862435   |
| `12x14x16` | 1638 (`Q`)  |   [1617](schemes/results/Q/12x14x16_m1617_Q.json) (`Q`)    | **2.806918970** |
| `12x15x16` | 1728 (`Q`)  | [1725](schemes/results/ZT/12x15x16_m1725_ZT.json) (`ZT/Z`) | **2.806957387** |
| `12x16x16` | 1824 (`Q`)  |   [1815](schemes/results/Q/12x16x16_m1815_Q.json) (`Q`)    | **2.803398069** |
| `13x13x13` | 1426 (`Q`)  |   [1421](schemes/results/Q/13x13x13_m1421_Q.json) (`Q`)    |   2.830120644   |
| `13x13x14` | 1524 (`Z`)  |  [1511](schemes/results/ZT/13x13x14_m1511_ZT.json) (`ZT`)  |   2.826838093   |
| `13x13x16` | 1713 (`Q`)  |   [1704](schemes/results/Q/13x13x16_m1704_Q.json) (`Q`)    |   2.824705676   |
| `13x14x14` | 1625 (`Z`)  |  [1614](schemes/results/ZT/13x14x14_m1614_ZT.json) (`ZT`)  |   2.825351482   |
| `13x14x15` | 1714 (`Z`)  | [1681](schemes/results/ZT/13x14x15_m1681_ZT.json) (`ZT/Z`) |   2.816136526   |
| `13x14x16` | 1825 (`Q`)  |   [1796](schemes/results/Q/13x14x16_m1796_Q.json) (`Q`)    |   2.818238934   |
| `13x15x15` | 1803 (`Z`)  | [1797](schemes/results/ZT/13x15x15_m1797_ZT.json) (`ZT/Z`) |   2.816875265   |
| `13x15x16` | 1932 (`Z`)  |  [1885](schemes/results/ZT/13x15x16_m1885_ZT.json) (`ZT`)  |   2.812106276   |
| `14x14x15` | 1813 (`Z`)  | [1798](schemes/results/ZT/14x14x15_m1798_ZT.json) (`ZT/Z`) |   2.815280055   |
| `14x14x16` | 1939 (`Q`)  |   [1931](schemes/results/Q/14x14x16_m1931_Q.json) (`Q`)    |   2.819303950   |
| `14x15x15` | 1905 (`Z`)  |   [1890](schemes/results/Q/14x15x15_m1890_Q.json) (`Q`)    |   2.809752096   |
| `14x16x16` | 2142 (`Q`)  |   [2128](schemes/results/Q/14x16x16_m2128_Q.json) (`Q`)    |   2.808914234   |
| `15x15x16` | 2173 (`Q`)  | [2132](schemes/results/ZT/15x15x16_m2132_ZT.json) (`ZT/Z`) |   2.808074285   |


### Rediscovery in the ternary coefficient set (`ZT`)
The following schemes have been rediscovered in the `ZT` format. Originally known over the rational (`Q`) or integer (`Z`) fields, implementations
with coefficients restricted to the ternary set were previously unknown.

|   Format   |                        Rank                        | Known ring |
|:----------:|:--------------------------------------------------:|:----------:|
|  `2x3x10`  |    [50](schemes/results/ZT/2x3x10_m50_ZT.json)     |    `Z`     |
|  `2x3x13`  |    [65](schemes/results/ZT/2x3x13_m65_ZT.json)     |    `Z`     |
|  `2x3x15`  |    [75](schemes/results/ZT/2x3x15_m75_ZT.json)     |    `Z`     |
|  `2x4x6`   |     [39](schemes/results/ZT/2x4x6_m39_ZT.json)     |    `Z`     |
|  `2x4x9`   |     [58](schemes/results/ZT/2x4x9_m58_ZT.json)     |    `Q`     |
|  `2x4x10`  |    [64](schemes/results/ZT/2x4x10_m64_ZT.json)     |    `Q`     |
|  `2x4x12`  |    [77](schemes/results/ZT/2x4x12_m77_ZT.json)     |    `Q`     |
|  `2x4x13`  |    [83](schemes/results/ZT/2x4x13_m83_ZT.json)     |    `Q`     |
|  `2x4x15`  |    [96](schemes/results/ZT/2x4x15_m96_ZT.json)     |    `Q`     |
|  `2x5x7`   |     [55](schemes/results/ZT/2x5x7_m55_ZT.json)     |    `Q`     |
|  `2x5x8`   |     [63](schemes/results/ZT/2x5x8_m63_ZT.json)     |    `Q`     |
|  `2x5x9`   |     [72](schemes/results/ZT/2x5x9_m72_ZT.json)     |    `Q`     |
|  `2x5x10`  |    [79](schemes/results/ZT/2x5x10_m79_ZT.json)     |    `Q`     |
|  `2x5x13`  |   [102](schemes/results/ZT/2x5x13_m102_ZT.json)    |    `Q`     |
|  `2x5x14`  |   [110](schemes/results/ZT/2x5x14_m110_ZT.json)    |    `Q`     |
|  `2x5x15`  |   [118](schemes/results/ZT/2x5x15_m118_ZT.json)    |    `Q`     |
|  `2x5x16`  |   [126](schemes/results/ZT/2x5x16_m126_ZT.json)    |    `Q`     |
|  `2x6x6`   |     [56](schemes/results/ZT/2x6x6_m56_ZT.json)     |    `Z`     |
|  `2x6x7`   |     [66](schemes/results/ZT/2x6x7_m66_ZT.json)     |   `Z/Q`    |
|  `2x6x8`   |     [75](schemes/results/ZT/2x6x8_m75_ZT.json)     |    `Q`     |
|  `2x6x9`   |     [86](schemes/results/ZT/2x6x9_m86_ZT.json)     |    `Z`     |
|  `2x6x11`  |   [103](schemes/results/ZT/2x6x11_m103_ZT.json)    |    `Z`     |
|  `2x6x12`  |   [112](schemes/results/ZT/2x6x12_m112_ZT.json)    |    `Z`     |
|  `2x6x13`  |   [122](schemes/results/ZT/2x6x13_m122_ZT.json)    |    `Q`     |
|  `2x6x14`  |   [131](schemes/results/ZT/2x6x14_m131_ZT.json)    |    `Q`     |
|  `2x6x16`  |   [150](schemes/results/ZT/2x6x16_m150_ZT.json)    |    `Z`     |
|  `2x7x7`   |     [76](schemes/results/ZT/2x7x7_m76_ZT.json)     |    `Q`     |
|  `2x7x8`   |     [88](schemes/results/ZT/2x7x8_m88_ZT.json)     |    `Z`     |
|  `2x7x9`   |     [99](schemes/results/ZT/2x7x9_m99_ZT.json)     |    `Q`     |
|  `2x7x10`  |   [110](schemes/results/ZT/2x7x10_m110_ZT.json)    |    `Z`     |
|  `2x7x11`  |   [121](schemes/results/ZT/2x7x11_m121_ZT.json)    |    `Z`     |
|  `2x7x12`  |   [131](schemes/results/ZT/2x7x12_m131_ZT.json)    |    `Q`     |
|  `2x7x13`  |   [142](schemes/results/ZT/2x7x13_m142_ZT.json)    |    `Q`     |
|  `2x7x14`  |   [152](schemes/results/ZT/2x7x14_m152_ZT.json)    |    `Q`     |
|  `2x7x15`  |   [164](schemes/results/ZT/2x7x15_m164_ZT.json)    |    `Q`     |
|  `2x7x16`  |   [175](schemes/results/ZT/2x7x16_m175_ZT.json)    |    `Q`     |
|  `2x8x9`   |    [113](schemes/results/ZT/2x8x9_m113_ZT.json)    |    `Q`     |
|  `2x8x10`  |   [125](schemes/results/ZT/2x8x10_m125_ZT.json)    |    `Z`     |
|  `2x8x11`  |   [138](schemes/results/ZT/2x8x11_m138_ZT.json)    |    `Z`     |
|  `2x8x12`  |   [150](schemes/results/ZT/2x8x12_m150_ZT.json)    |    `Z`     |
|  `2x8x14`  |   [175](schemes/results/ZT/2x8x14_m175_ZT.json)    |    `Q`     |
|  `2x8x15`  |   [188](schemes/results/ZT/2x8x15_m188_ZT.json)    |    `Z`     |
|  `2x9x13`  |   [182](schemes/results/ZT/2x9x13_m182_ZT.json)    |   `Z/Q`    |
|  `2x9x14`  |   [196](schemes/results/ZT/2x9x14_m196_ZT.json)    |   `Z/Q`    |
|  `2x9x15`  |   [210](schemes/results/ZT/2x9x15_m210_ZT.json)    |   `Z/Q`    |
|  `2x9x16`  |   [224](schemes/results/ZT/2x9x16_m224_ZT.json)    |   `Z/Q`    |
| `2x10x15`  |   [233](schemes/results/ZT/2x10x15_m233_ZT.json)   |   `Z/Q`    |
| `2x12x16`  |   [296](schemes/results/ZT/2x12x16_m296_ZT.json)   |   `Z/Q`    |
|  `3x3x7`   |     [49](schemes/results/ZT/3x3x7_m49_ZT.json)     |    `Q`     |
|  `3x3x9`   |     [63](schemes/results/ZT/3x3x9_m63_ZT.json)     |    `Q`     |
|  `3x3x10`  |    [69](schemes/results/ZT/3x3x10_m69_ZT.json)     |    `Q`     |
|  `3x3x11`  |    [76](schemes/results/ZT/3x3x11_m76_ZT.json)     |    `Q`     |
|  `3x4x5`   |     [47](schemes/results/ZT/3x4x5_m47_ZT.json)     |    `Z`     |
|  `3x4x6`   |     [54](schemes/results/ZT/3x4x6_m54_ZT.json)     |   `Z/Q`    |
|  `3x4x8`   |     [73](schemes/results/ZT/3x4x8_m73_ZT.json)     |    `Q`     |
|  `3x4x9`   |     [83](schemes/results/ZT/3x4x9_m83_ZT.json)     |    `Q`     |
|  `3x4x10`  |    [92](schemes/results/ZT/3x4x10_m92_ZT.json)     |    `Q`     |
|  `3x4x11`  |   [101](schemes/results/ZT/3x4x11_m101_ZT.json)    |    `Q`     |
|  `3x4x12`  |   [108](schemes/results/ZT/3x4x12_m108_ZT.json)    |    `Q`     |
|  `3x4x16`  |   [146](schemes/results/ZT/3x4x16_m146_ZT.json)    |    `Q`     |
|  `3x5x6`   |     [68](schemes/results/ZT/3x5x6_m68_ZT.json)     |    `Z`     |
|  `3x5x7`   |     [79](schemes/results/ZT/3x5x7_m79_ZT.json)     |    `Q`     |
|  `3x5x8`   |     [90](schemes/results/ZT/3x5x8_m90_ZT.json)     |   `Z/Q`    |
|  `3x5x11`  |   [126](schemes/results/ZT/3x5x11_m126_ZT.json)    |    `Z`     |
|  `3x5x12`  |   [136](schemes/results/ZT/3x5x12_m136_ZT.json)    |    `Z`     |
|  `3x5x13`  |   [147](schemes/results/ZT/3x5x13_m147_ZT.json)    |    `Q`     |
|  `3x5x14`  |   [158](schemes/results/ZT/3x5x14_m158_ZT.json)    |    `Q`     |
|  `3x5x15`  |   [169](schemes/results/ZT/3x5x15_m169_ZT.json)    |    `Q`     |
|  `3x5x16`  |   [180](schemes/results/ZT/3x5x16_m180_ZT.json)    |    `Z`     |
|  `3x6x8`   |    [108](schemes/results/ZT/3x6x8_m108_ZT.json)    |   `Z/Q`    |
|  `3x7x7`   |    [111](schemes/results/ZT/3x7x7_m111_ZT.json)    |    `Q`     |
|  `3x8x9`   |    [163](schemes/results/ZT/3x8x9_m163_ZT.json)    |    `Q`     |
|  `3x8x10`  |   [180](schemes/results/ZT/3x8x10_m180_ZT.json)    |    `Z`     |
|  `3x8x11`  |   [198](schemes/results/ZT/3x8x11_m198_ZT.json)    |    `Q`     |
|  `3x8x12`  |   [216](schemes/results/ZT/3x8x12_m216_ZT.json)    |    `Q`     |
|  `3x8x15`  |   [270](schemes/results/ZT/3x8x15_m270_ZT.json)    |    `Z`     |
|  `3x8x16`  |   [288](schemes/results/ZT/3x8x16_m288_ZT.json)    |    `Q`     |
| `3x11x11`  |   [274](schemes/results/ZT/3x11x11_m274_ZT.json)   |    `Q`     |
|  `4x4x6`   |     [73](schemes/results/ZT/4x4x6_m73_ZT.json)     |   `Z/Q`    |
|  `4x4x8`   |     [96](schemes/results/ZT/4x4x8_m96_ZT.json)     |    `Q`     |
|  `4x5x6`   |     [90](schemes/results/ZT/4x5x6_m90_ZT.json)     |    `Z`     |
|  `4x5x7`   |    [104](schemes/results/ZT/4x5x7_m104_ZT.json)    |   `Z/Q`    |
|  `4x5x8`   |    [118](schemes/results/ZT/4x5x8_m118_ZT.json)    |   `Z/Q`    |
|  `4x6x7`   |    [123](schemes/results/ZT/4x6x7_m123_ZT.json)    |   `Z/Q`    |
|  `4x6x9`   |    [159](schemes/results/ZT/4x6x9_m159_ZT.json)    |    `Q`     |
|  `4x6x10`  |   [175](schemes/results/ZT/4x6x10_m175_ZT.json)    |    `Z`     |
|  `4x6x11`  |   [194](schemes/results/ZT/4x6x11_m194_ZT.json)    |    `Q`     |
|  `4x6x15`  |   [263](schemes/results/ZT/4x6x15_m263_ZT.json)    |    `Z`     |
|  `4x7x7`   |    [144](schemes/results/ZT/4x7x7_m144_ZT.json)    |   `Z/Q`    |
|  `4x8x13`  |   [297](schemes/results/ZT/4x8x13_m297_ZT.json)    |    `Z`     |
|  `4x9x15`  |   [375](schemes/results/ZT/4x9x15_m375_ZT.json)    |    `Z`     |
| `4x10x13`  |   [361](schemes/results/ZT/4x10x13_m361_ZT.json)   |    `Q`     |
| `4x10x14`  |   [385](schemes/results/ZT/4x10x14_m385_ZT.json)   |    `Q`     |
| `4x10x16`  |   [441](schemes/results/ZT/4x10x16_m441_ZT.json)   |    `Q`     |
| `4x11x11`  |   [340](schemes/results/ZT/4x11x11_m340_ZT.json)   |    `Z`     |
| `4x11x14`  |   [429](schemes/results/ZT/4x11x14_m429_ZT.json)   |    `Q`     |
| `4x14x14`  |   [532](schemes/results/ZT/4x14x14_m532_ZT.json)   |    `Q`     |
|  `5x5x6`   |    [110](schemes/results/ZT/5x5x6_m110_ZT.json)    |   `Z/Q`    |
|  `5x5x7`   |    [127](schemes/results/ZT/5x5x7_m127_ZT.json)    |   `Z/Q`    |
|  `5x5x8`   |    [144](schemes/results/ZT/5x5x8_m144_ZT.json)    |   `Z/Q`    |
|  `5x6x6`   |    [130](schemes/results/ZT/5x6x6_m130_ZT.json)    |   `Z/Q`    |
|  `5x6x7`   |    [150](schemes/results/ZT/5x6x7_m150_ZT.json)    |   `Z/Q`    |
|  `5x6x8`   |    [170](schemes/results/ZT/5x6x8_m170_ZT.json)    |   `Z/Q`    |
|  `5x6x16`  |   [340](schemes/results/ZT/5x6x16_m340_ZT.json)    |    `Q`     |
|  `5x7x7`   |    [176](schemes/results/ZT/5x7x7_m176_ZT.json)    |   `Z/Q`    |
|  `5x7x9`   |    [229](schemes/results/ZT/5x7x9_m229_ZT.json)    |    `Q`     |
|  `5x7x10`  |   [254](schemes/results/ZT/5x7x10_m254_ZT.json)    |    `Z`     |
|  `5x7x11`  |   [277](schemes/results/ZT/5x7x11_m277_ZT.json)    |    `Z`     |
|  `5x7x13`  |   [325](schemes/results/ZT/5x7x13_m325_ZT.json)    |    `Q`     |
|  `5x8x9`   |    [260](schemes/results/ZT/5x8x9_m260_ZT.json)    |    `Q`     |
|  `5x8x12`  |   [333](schemes/results/ZT/5x8x12_m333_ZT.json)    |    `Q`     |
|  `5x8x16`  |   [445](schemes/results/ZT/5x8x16_m445_ZT.json)    |    `Q`     |
|  `5x9x10`  |   [322](schemes/results/ZT/5x9x10_m322_ZT.json)    |    `Q`     |
|  `5x9x11`  |   [353](schemes/results/ZT/5x9x11_m353_ZT.json)    |    `Q`     |
|  `5x9x12`  |   [377](schemes/results/ZT/5x9x12_m377_ZT.json)    |    `Q`     |
| `5x10x11`  |   [386](schemes/results/ZT/5x10x11_m386_ZT.json)   |    `Z`     |
| `5x10x13`  |   [451](schemes/results/ZT/5x10x13_m451_ZT.json)   |    `Q`     |
| `5x10x14`  |   [481](schemes/results/ZT/5x10x14_m481_ZT.json)   |    `Q`     |
| `5x10x15`  |   [519](schemes/results/ZT/5x10x15_m519_ZT.json)   |    `Q`     |
| `5x10x16`  |   [549](schemes/results/ZT/5x10x16_m549_ZT.json)   |    `Q`     |
| `5x11x16`  |   [609](schemes/results/ZT/5x11x16_m609_ZT.json)   |    `Q`     |
| `5x15x16`  |   [813](schemes/results/ZT/5x15x16_m813_ZT.json)   |    `Z`     |
|  `6x6x7`   |    [183](schemes/results/ZT/6x6x7_m183_ZT.json)    |   `Z/Q`    |
|  `6x8x11`  |   [357](schemes/results/ZT/6x8x11_m357_ZT.json)    |    `Q`     |
|  `6x8x12`  |   [378](schemes/results/ZT/6x8x12_m378_ZT.json)    |    `Q`     |
| `6x10x11`  |   [446](schemes/results/ZT/6x10x11_m446_ZT.json)   |    `Z`     |
| `6x10x12`  |   [476](schemes/results/ZT/6x10x12_m476_ZT.json)   |    `Z`     |
| `6x10x13`  |   [520](schemes/results/ZT/6x10x13_m520_ZT.json)   |    `Q`     |
| `6x10x14`  |   [553](schemes/results/ZT/6x10x14_m553_ZT.json)   |    `Q`     |
| `6x10x16`  |   [630](schemes/results/ZT/6x10x16_m630_ZT.json)   |    `Q`     |
|  `7x8x10`  |   [385](schemes/results/ZT/7x8x10_m385_ZT.json)    |    `Z`     |
|  `7x8x11`  |   [423](schemes/results/ZT/7x8x11_m423_ZT.json)    |    `Q`     |
| `7x10x11`  |   [526](schemes/results/ZT/7x10x11_m526_ZT.json)   |    `Z`     |
| `7x10x13`  |   [614](schemes/results/ZT/7x10x13_m614_ZT.json)   |    `Q`     |
| `7x10x14`  |   [653](schemes/results/ZT/7x10x14_m653_ZT.json)   |    `Q`     |
| `7x13x15`  |   [909](schemes/results/ZT/7x13x15_m909_ZT.json)   |    `Z`     |
|  `8x8x11`  |   [475](schemes/results/ZT/8x8x11_m475_ZT.json)    |    `Q`     |
|  `8x8x13`  |   [559](schemes/results/ZT/8x8x13_m559_ZT.json)    |    `Q`     |
| `8x10x11`  |   [588](schemes/results/ZT/8x10x11_m588_ZT.json)   |    `Z`     |
| `8x10x13`  |   [686](schemes/results/ZT/8x10x13_m686_ZT.json)   |    `Z`     |
| `8x11x14`  |   [804](schemes/results/ZT/8x11x14_m804_ZT.json)   |    `Z`     |
| `8x12x16`  |   [960](schemes/results/ZT/8x12x16_m960_ZT.json)   |    `Q`     |
| `10x10x10` |  [651](schemes/results/ZT/10x10x10_m651_ZT.json)   |    `Z`     |
| `10x10x11` |  [719](schemes/results/ZT/10x10x11_m719_ZT.json)   |    `Z`     |
| `10x10x13` |  [838](schemes/results/ZT/10x10x13_m838_ZT.json)   |    `Z`     |
| `10x10x14` |  [889](schemes/results/ZT/10x10x14_m889_ZT.json)   |    `Z`     |
| `10x10x15` |  [957](schemes/results/ZT/10x10x15_m957_ZT.json)   |    `Q`     |
| `10x10x16` | [1008](schemes/results/ZT/10x10x16_m1008_ZT.json)  |    `Q`     |
| `10x11x11` |  [793](schemes/results/ZT/10x11x11_m793_ZT.json)   |    `Z`     |
| `10x11x13` |  [924](schemes/results/ZT/10x11x13_m924_ZT.json)   |    `Z`     |
| `10x11x14` |  [981](schemes/results/ZT/10x11x14_m981_ZT.json)   |    `Z`     |
| `10x12x13` |  [990](schemes/results/ZT/10x12x13_m990_ZT.json)   |    `Z`     |
| `10x12x14` | [1050](schemes/results/ZT/10x12x14_m1050_ZT.json)  |    `Z`     |
| `10x13x13` | [1082](schemes/results/ZT/10x13x13_m1082_ZT.json)  |    `Z`     |
| `10x13x14` | [1154](schemes/results/ZT/10x13x14_m1154_ZT.json)  |    `Z`     |
| `10x14x14` | [1232](schemes/results/ZT/10x14x14_m1232_ZT.json)  |    `Z`     |
| `11x11x11` |  [873](schemes/results/ZT/11x11x11_m873_ZT.json)   |    `Z`     |
| `11x11x13` | [1023](schemes/results/ZT/11x11x13_m1023_ZT.json)  |    `Z`     |
| `11x11x14` | [1093](schemes/results/ZT/11x11x14_m1093_ZT.json)  |    `Z`     |
| `13x13x15` | [1605](schemes/results/ZT/13x13x15_m1605_ZT.json)  |    `Z`     |
| `15x15x15` | [2058](schemes/results/ZT/15x15x15_m2058_ZT.json)  |    `Q`     |


### Rediscovery in the integer ring (`Z`)
The following schemes, originally known over the rational field (`Q`), have now been rediscovered in the integer ring (`Z`).
Implementations restricted to integer coefficients were previously unknown.

|   Format   |                       Rank                       |
|:----------:|:------------------------------------------------:|
| `2x11x12`  |   [204](schemes/results/Z/2x11x12_m204_Z.json)   |
| `2x11x13`  |   [221](schemes/results/Z/2x11x13_m221_Z.json)   |
| `2x11x14`  |   [238](schemes/results/Z/2x11x14_m238_Z.json)   |
| `2x13x15`  |   [300](schemes/results/Z/2x13x15_m300_Z.json)   |
| `2x13x16`  |   [320](schemes/results/Z/2x13x16_m320_Z.json)   |
| `2x15x16`  |   [368](schemes/results/Z/2x15x16_m368_Z.json)   |

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
| MMC — Matrix Multiplication Catalog | Large catalog tracking history and fields, maintained by @blacelle ([matmulcatalog](https://solven.eu/matmulcatalog)).                                                                           |
| Alpha Tensor                        | Schemes from DeepMind's AlphaTensor project ([https://github.com/google-deepmind/alphatensor/tree/main/algorithms](https://github.com/google-deepmind/alphatensor/tree/main/algorithms)).        |
| Alpha Evolve                        | Schemes from DeepMind's AlphaEvolve project ([mathematical_results.ipynb](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)). |
| Original Flip Graph                 | Foundational work by Jakob Moosbauer ([flips](https://github.com/jakobmoosbauer/flips/tree/main/solutions)).                                                                                     |
| Adaptive flip graph                 | Improved flip graph approach ([adap](https://github.com/Yamato-Arai/adap)).                                                                                                                      |
| Symmetric flip graph                | Flip graphs with symmetry ([symmetric-flips](https://github.com/jakobmoosbauer/symmetric-flips)).                                                                                                |
| Meta Flip Graph                     | Advanced flip graph techniques by M. Kauers et al. ([matrix-multiplication](https://github.com/mkauers/matrix-multiplication)).                                                                  |
| FMM Add Reduction                   | Work on additive reductions by @werekorren ([fmm_add_reduction](https://github.com/werekorren/fmm_add_reduction/tree/main/algorithms)).                                                          |

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


## Research Findings & Status

The table below summarizes the current state of researched matrix multiplication schemes. It highlights where ternary schemes (ZT) match or approximate the known minimal ranks
from other fields. The best ranks of previously known schemes are given in brackets.

|   Format   |  `ZT` rank  |   `Z` rank   |   `Q` rank   |        ω        |
|:----------:|:-----------:|:------------:|:------------:|:---------------:|
|  `2x2x2`   |      7      |      7       |      7       |   2.807354922   |
|  `2x2x3`   |     11      |      11      |      11      |   2.894952138   |
|  `2x2x4`   |     14      |      14      |      14      |   2.855516192   |
|  `2x2x5`   |     18      |      18      |      18      |   2.894489388   |
|  `2x2x6`   |     21      |      21      |      21      |   2.873949845   |
|  `2x2x7`   |     25      |      25      |      25      |   2.897969631   |
|  `2x2x8`   |     28      |      28      |      28      |   2.884412953   |
|  `2x2x9`   |     32      |      32      |      32      |   2.901396054   |
|  `2x2x10`  |     35      |      35      |      35      |   2.891404915   |
|  `2x2x11`  |     39      |      39      |      39      |   2.904369496   |
|  `2x2x12`  |     42      |      42      |      42      |   2.896519407   |
|  `2x2x13`  |     46      |      46      |      46      |   2.906913622   |
|  `2x2x14`  |     49      |      49      |      49      |   2.900482192   |
|  `2x2x15`  |     53      |      53      |      53      |   2.909104390   |
|  `2x2x16`  |     56      |      56      |      56      |   2.903677461   |
|  `2x3x3`   |     15      |      15      |      15      |   2.810763211   |
|  `2x3x4`   |     20      |      20      |      20      |   2.827893201   |
|  `2x3x5`   |     25      |      25      |      25      |   2.839184673   |
|  `2x3x6`   |     30      |      30      |      30      |   2.847366603   |
|  `2x3x7`   |     35      |      35      |      35      |   2.853661579   |
|  `2x3x8`   |     40      |      40      |      40      |   2.858709308   |
|  `2x3x9`   |     45      |      45      |      45      |   2.862881209   |
|  `2x3x10`  |   50 (?)    |      50      |      50      |   2.866409712   |
|  `2x3x11`  |     55      |      55      |      55      |   2.869448748   |
|  `2x3x12`  |     60      |      60      |      60      |   2.872104893   |
|  `2x3x13`  |   65 (?)    |      65      |      65      |   2.874454619   |
|  `2x3x14`  |     70      |      70      |      70      |   2.876554438   |
|  `2x3x15`  |   75 (?)    |      75      |      75      |   2.878447154   |
|  `2x3x16`  |     80      |      80      |      80      |   2.880165875   |
|  `2x4x4`   |     26      |      26      |      26      |   2.820263831   |
|  `2x4x5`   |   33 (?)    |      33      |      32      |   2.818527371   |
|  `2x4x6`   |   39 (?)    |      39      |      39      |   2.839089189   |
|  `2x4x7`   |     45      |      45      |      45      |   2.837016079   |
|  `2x4x8`   |     51      |      51      |      51      |   2.836212671   |
|  `2x4x9`   |   58 (?)    |    58 (?)    |      58      |   2.848323599   |
|  `2x4x10`  |   64 (?)    |    64 (?)    |      64      |   2.847232637   |
|  `2x4x11`  |   70 (?)    |    70 (?)    |   70 (71)    |   2.846666725   |
|  `2x4x12`  |   77 (?)    |    77 (?)    |      77      |   2.855044295   |
|  `2x4x13`  |   83 (?)    |    83 (?)    |      83      |   2.854307941   |
|  `2x4x14`  |     90      |      90      |      90      |   2.860958406   |
|  `2x4x15`  |   96 (?)    |    96 (?)    |      96      |   2.860170902   |
|  `2x4x16`  |     102     |     102      |     102      |   2.859610861   |
|  `2x5x5`   |     40      |      40      |      40      |   2.828878651   |
|  `2x5x6`   |     47      |      47      |      47      |   2.821072489   |
|  `2x5x7`   |   55 (?)    |    55 (?)    |      55      |   2.829707666   |
|  `2x5x8`   |   63 (?)    |    63 (?)    |      63      |   2.836451080   |
|  `2x5x9`   |   72 (?)    |    72 (?)    |      72      |   2.851231340   |
|  `2x5x10`  |   79 (?)    |    79 (?)    |      79      |   2.846440637   |
|  `2x5x11`  |     87      |      87      |      87      |   2.850288335   |
|  `2x5x12`  |     94      |      94      |      94      |   2.846978142   |
|  `2x5x13`  |   102 (?)   |   102 (?)    |     102      |   2.850502360   |
|  `2x5x14`  |   110 (?)   |   110 (?)    |     110      |   2.853593986   |
|  `2x5x15`  |   118 (?)   |   118 (?)    |     118      |   2.856335182   |
|  `2x5x16`  |   126 (?)   |   126 (?)    |     126      |   2.858787945   |
|  `2x6x6`   |   56 (?)    |      56      |      56      |   2.823707705   |
|  `2x6x7`   |   66 (?)    |      66      |      66      |   2.836714944   |
|  `2x6x8`   |   75 (?)    |    75 (?)    |      75      |   2.837746771   |
|  `2x6x9`   |   86 (?)    |      86      |      86      |   2.854051123   |
|  `2x6x10`  |     94      |      94      |      94      |   2.846978142   |
|  `2x6x11`  |   103 (?)   |     103      |     103      |   2.847583659   |
|  `2x6x12`  |   112 (?)   |     112      |     112      |   2.848295451   |
|  `2x6x13`  |   122 (?)   |   122 (?)    |     122      |   2.853955264   |
|  `2x6x14`  |   131 (?)   |   131 (?)    |     131      |   2.854351051   |
|  `2x6x15`  |     141     |     141      |     141      |   2.858926060   |
|  `2x6x16`  |   150 (?)   |     150      |     150      |   2.859138205   |
|  `2x7x7`   |   76 (?)    |    76 (?)    |      76      |   2.833651510   |
|  `2x7x8`   |   88 (?)    |      88      |      88      |   2.846670267   |
|  `2x7x9`   |   99 (?)    |    99 (?)    |      99      |   2.850404467   |
|  `2x7x10`  |   110 (?)   |     110      |     110      |   2.853593986   |
|  `2x7x11`  |   121 (?)   |     121      |     121      |   2.856364308   |
|  `2x7x12`  |   131 (?)   |   131 (?)    |     131      |   2.854351051   |
|  `2x7x13`  |   142 (?)   |   142 (?)    |     142      |   2.856929683   |
|  `2x7x14`  |   152 (?)   |   152 (?)    |     152      |   2.855497187   |
|  `2x7x15`  |   164 (?)   |   164 (?)    |     164      |   2.861285133   |
|  `2x7x16`  |   175 (?)   |   175 (?)    |     175      |   2.863150652   |
|  `2x8x8`   |     100     |     100      |     100      |   2.847366938   |
|  `2x8x9`   |   113 (?)   |   113 (?)    |     113      |   2.853661214   |
|  `2x8x10`  |   125 (?)   |     125      |     125      |   2.854077858   |
|  `2x8x11`  |   138 (?)   |     138      |     138      |   2.858873767   |
|  `2x8x12`  |   150 (?)   |     150      |     150      |   2.859138205   |
|  `2x8x13`  |   163 (?)   |   163 (?)    |  163 (164)   |   2.862977345   |
|  `2x8x14`  |   175 (?)   |   175 (?)    |     175      |   2.863150652   |
|  `2x8x15`  |   188 (?)   |     188      |     188      |   2.866331117   |
|  `2x8x16`  |     200     |     200      |     200      |   2.866446071   |
|  `2x9x9`   |     126     |     126      |     126      |   2.851807566   |
|  `2x9x10`  |   143 (?)   |     140      |     140      |   2.854814260   |
|  `2x9x11`  |   157 (?)   |     154      |     154      |   2.857430935   |
|  `2x9x12`  |   171 (?)   |     168      |     168      |   2.859738747   |
|  `2x9x13`  |   182 (?)   |     182      |     182      |   2.861796718   |
|  `2x9x14`  |   196 (?)   |     196      |     196      |   2.863648982   |
|  `2x9x15`  |   210 (?)   |     210      |     210      |   2.865329321   |
|  `2x9x16`  |   224 (?)   |     224      |     224      |   2.866864110   |
| `2x10x10`  |     155     |     155      |     155      |   2.855675548   |
| `2x10x11`  |   173 (?)   |     171      |     171      |   2.859854622   |
| `2x10x12`  |   188 (?)   |     186      |     186      |   2.860476715   |
| `2x10x13`  |   204 (?)   |     202      |     202      |   2.863822126   |
| `2x10x14`  |   219 (?)   |     217      |     217      |   2.864293647   |
| `2x10x15`  |  233 (235)  |     233      |     233      |   2.867065046   |
| `2x10x16`  |     249     |     248      |     248      |   2.867435125   |
| `2x11x11`  |     187     |     187      |     187      |   2.859082510   |
| `2x11x12`  |   206 (?)   |   204 (?)    |     204      |   2.861281494   |
| `2x11x13`  |   224 (?)   |   221 (?)    |     221      |   2.863244617   |
| `2x11x14`  |   241 (?)   |   238 (?)    |     238      |   2.865013288   |
| `2x11x15`  |   257 (?)   |     255      |     255      |   2.866619250   |
| `2x11x16`  |   274 (?)   |     272      |     272      |   2.868087316   |
| `2x12x12`  |     222     |     222      |     222      |   2.862112883   |
| `2x12x13`  |   243 (?)   |     241      |     241      |   2.865119566   |
| `2x12x14`  |   262 (?)   |     259      |     259      |   2.865766826   |
| `2x12x15`  |   281 (?)   |     278      |     278      |   2.868257722   |
| `2x12x16`  |   296 (?)   |     296      |     296      |   2.868778995   |
| `2x13x13`  |     260     |     260      |     260      |   2.864831429   |
| `2x13x14`  |   283 (?)   |     280      |     280      |   2.866530057   |
| `2x13x15`  |   305 (?)   |   300 (?)    |     300      |   2.868073511   |
| `2x13x16`  |   325 (?)   |   320 (?)    |     320      |   2.869485347   |
| `2x14x14`  |     301     |     301      |     301      |   2.867288565   |
| `2x14x15`  |   327 (?)   |     323      |     323      |   2.869573850   |
| `2x14x16`  |   350 (?)   |     344      |     344      |   2.870191390   |
| `2x15x15`  |     345     |     345      |     345      |   2.869524113   |
| `2x15x16`  |   375 (?)   |   368 (?)    |     368      |   2.870888061   |
| `2x16x16`  |     392     |     392      |     392      |   2.871569948   |
|  `3x3x3`   |     23      |      23      |      23      |   2.854049830   |
|  `3x3x4`   |     29      |      29      |      29      |   2.818985378   |
|  `3x3x5`   |     36      |      36      |      36      |   2.824142367   |
|  `3x3x6`   |   42 (?)    |      42      |      40      | **2.774299980** |
|  `3x3x7`   |   49 (?)    |    49 (?)    |      49      |   2.818025883   |
|  `3x3x8`   |   56 (?)    |    56 (?)    |      55      |   2.811068066   |
|  `3x3x9`   |   63 (?)    |    63 (?)    |      63      |   2.828432812   |
|  `3x3x10`  |   69 (?)    |    69 (?)    |      69      |   2.822857064   |
|  `3x3x11`  |   76 (?)    |    76 (?)    |      76      |   2.827390894   |
|  `3x3x12`  |   84 (?)    |    84 (?)    |      80      |   2.807712827   |
|  `3x3x13`  |   91 (?)    |    91 (?)    |      89      |   2.827681075   |
|  `3x3x14`  |   98 (?)    |    98 (?)    |      95      |   2.824820996   |
|  `3x3x15`  |   105 (?)   |   105 (?)    |     103      |   2.834537838   |
|  `3x3x16`  |   111 (?)   |   111 (?)    |     109      |   2.831905908   |
|  `3x4x4`   |     38      |      38      |      38      |   2.818959400   |
|  `3x4x5`   |   47 (?)    |      47      |      47      |   2.821072489   |
|  `3x4x6`   |   54 (?)    |      54      |      54      | **2.798196494** |
|  `3x4x7`   |   64 (?)    |      64      |      63      | **2.805217355** |
|  `3x4x8`   |   73 (74)   |   73 (74)    |      73      |   2.819981689   |
|  `3x4x9`   |   83 (?)    |    83 (?)    |      83      |   2.831300786   |
|  `3x4x10`  |   92 (?)    |    92 (?)    |      92      |   2.833501646   |
|  `3x4x11`  |   101 (?)   |   101 (?)    |     101      |   2.835536188   |
|  `3x4x12`  |   108 (?)   |   108 (?)    |     108      |   2.826342326   |
|  `3x4x13`  |   118 (?)   |   118 (?)    |     117      |   2.829094886   |
|  `3x4x14`  |   127 (?)   |   127 (?)    |     126      |   2.831566689   |
|  `3x4x15`  |   137 (?)   |   137 (?)    |     136      |   2.838067999   |
|  `3x4x16`  |   146 (?)   |   146 (?)    |     146      |   2.843715269   |
|  `3x5x5`   |     58      |      58      |      58      |   2.821392604   |
|  `3x5x6`   |   68 (?)    |      68      |      68      |   2.813124119   |
|  `3x5x7`   |   79 (?)    |   79 (80)    |      79      |   2.816599750   |
|  `3x5x8`   |   90 (?)    |      90      |      90      |   2.819728939   |
|  `3x5x9`   |   102 (?)   |  102 (104)   |  102 (104)   |   2.828571093   |
|  `3x5x10`  |   114 (?)   |  114 (115)   |  114 (115)   |   2.835687395   |
|  `3x5x11`  |   126 (?)   |     126      |     126      |   2.841559080   |
|  `3x5x12`  |   136 (?)   |     136      |     136      |   2.838067999   |
|  `3x5x13`  |   147 (?)   |   147 (?)    |     147      |   2.839237439   |
|  `3x5x14`  |   158 (?)   |   158 (?)    |     158      |   2.840373980   |
|  `3x5x15`  |   169 (?)   |   169 (?)    |     169      |   2.841471724   |
|  `3x5x16`  |   180 (?)   |     180      |     180      |   2.842528174   |
|  `3x6x6`   |   83 (?)    |    83 (?)    |      80      |   2.807712827   |
|  `3x6x7`   |   96 (?)    |    96 (?)    |      94      |   2.818256795   |
|  `3x6x8`   |   108 (?)   |     108      |     108      |   2.826342326   |
|  `3x6x9`   |   122 (?)   |   122 (?)    |     120      |   2.823037498   |
|  `3x6x10`  |   136 (?)   |   136 (?)    |     134      |   2.829509241   |
|  `3x6x11`  |   150 (?)   |   150 (?)    |     148      |   2.834886501   |
|  `3x6x12`  |   162 (?)   |   162 (?)    |     160      |   2.832508438   |
|  `3x6x13`  |   176 (?)   |   176 (?)    |     174      |   2.837076970   |
|  `3x6x14`  |   190 (?)   |   190 (?)    |     188      |   2.841039398   |
|  `3x6x15`  |   204 (?)   |   204 (?)    |     200      |   2.839184366   |
|  `3x6x16`  |   216 (?)   |   216 (?)    |     214      |   2.842670031   |
|  `3x7x7`   |   111 (?)   |   111 (?)    |     111      |   2.831135449   |
|  `3x7x8`   |   128 (?)   |   128 (?)    |     126      |   2.831566689   |
|  `3x7x9`   |   141 (?)   |   141 (?)    |  141 (142)   |   2.832315186   |
|  `3x7x10`  |   158 (?)   |   158 (?)    |     157      |   2.836811740   |
|  `3x7x11`  |   175 (?)   |   175 (?)    |     173      |   2.840626282   |
|  `3x7x12`  |   190 (?)   |   190 (?)    |     188      |   2.841039398   |
|  `3x7x13`  |   204 (?)   |   204 (?)    |  204 (205)   |   2.844182227   |
|  `3x7x14`  |   219 (?)   |   219 (?)    |  219 (220)   |   2.844547952   |
|  `3x7x15`  |   236 (?)   |   236 (?)    |  235 (236)   |   2.847205515   |
|  `3x7x16`  |   252 (?)   |   252 (?)    |     251      |   2.849586051   |
|  `3x8x8`   |   146 (?)   |   146 (?)    |     145      |   2.839793508   |
|  `3x8x9`   |   163 (?)   |   163 (?)    |     163      |   2.842876116   |
|  `3x8x10`  |   180 (?)   |     180      |     180      |   2.842528174   |
|  `3x8x11`  |   198 (?)   |   198 (?)    |     198      |   2.845219854   |
|  `3x8x12`  |   216 (?)   |   216 (?)    |     216      |   2.847598050   |
|  `3x8x13`  |   236 (?)   |   236 (?)    |     234      |   2.849722142   |
|  `3x8x14`  |   253 (?)   |   253 (?)    |     252      |   2.851636630   |
|  `3x8x15`  |   270 (?)   |     270      |     270      |   2.853375643   |
|  `3x8x16`  |   288 (?)   |   288 (?)    |     288      |   2.854965878   |
|  `3x9x9`   |   185 (?)   |   185 (?)    |     183      |   2.845127188   |
|  `3x9x10`  |   204 (?)   |   204 (?)    |     203      |   2.847162657   |
|  `3x9x11`  |   224 (?)   |   224 (?)    |  222 (224)   |   2.846644652   |
|  `3x9x12`  |   243 (?)   |   243 (?)    |     240      |   2.844256405   |
|  `3x9x13`  |   263 (?)   |   263 (?)    |  261 (262)   |   2.848348427   |
|  `3x9x14`  |   281 (?)   |   281 (?)    |  281 (283)   |   2.850103717   |
|  `3x9x15`  |   304 (?)   |   304 (?)    |     303      |   2.855016796   |
|  `3x9x16`  |   326 (?)   |   326 (?)    |     323      |   2.856252700   |
| `3x10x10`  |   227 (?)   |   227 (?)    |     226      |   2.851021242   |
| `3x10x11`  |   249 (?)   |   249 (?)    |  248 (249)   |   2.852219687   |
| `3x10x12`  |   270 (?)   |   270 (?)    |     268      |   2.849586221   |
| `3x10x13`  |   294 (?)   |   294 (?)    |     291      |   2.852757491   |
| `3x10x14`  |   312 (?)   |   312 (?)    |  312 (314)   |   2.852364741   |
| `3x10x15`  |   335 (?)   |   335 (?)    |  335 (336)   |   2.855080165   |
| `3x10x16`  |   355 (?)   |   355 (?)    |  355 (360)   |   2.853411678   |
| `3x11x11`  |   274 (?)   |   274 (?)    |     274      |   2.856843143   |
| `3x11x12`  |   298 (?)   |   298 (?)    |     296      |   2.854020431   |
| `3x11x13`  |   322 (?)   |   322 (?)    |     321      |   2.856462333   |
| `3x11x14`  |   346 (?)   |   346 (?)    |  345 (346)   |   2.857215849   |
| `3x11x15`  |   373 (?)   |   373 (?)    |     369      |   2.857961939   |
| `3x11x16`  |   396 (?)   |   396 (?)    |     394      |   2.859910251   |
| `3x12x12`  |   324 (?)   |   324 (?)    |     320      |   2.851639645   |
| `3x12x13`  |   351 (?)   |   351 (?)    |     348      |   2.855444087   |
| `3x12x14`  |   377 (?)   |   377 (?)    |     376      |   2.858746388   |
| `3x12x15`  |   405 (?)   |   405 (?)    |     400      |   2.856901552   |
| `3x12x16`  |   432 (?)   |   432 (?)    |     428      |   2.859827202   |
| `3x13x13`  |   380 (?)   |   380 (?)    |  378 (379)   |   2.858577688   |
| `3x13x14`  |   408 (?)   |   408 (?)    |  407 (408)   |   2.860150618   |
| `3x13x15`  |   439 (?)   |   439 (?)    |  435 (436)   |   2.860506655   |
| `3x13x16`  |   466 (?)   |   466 (?)    |  464 (465)   |   2.861905425   |
| `3x14x14`  |   438 (?)   |   438 (?)    |  438 (440)   |   2.861445516   |
| `3x14x15`  |   470 (?)   |   470 (?)    |  469 (470)   |   2.862645108   |
| `3x14x16`  |   500 (?)   |   500 (?)    |  500 (502)   |   2.863761055   |
| `3x15x15`  |   504 (?)   |   504 (?)    |     503      |   2.864557717   |
| `3x15x16`  |   534 (?)   |   534 (?)    |  534 (536)   |   2.863728243   |
| `3x16x16`  |   571 (?)   |   571 (?)    |  569 (574)   |   2.864576103   |
|  `4x4x4`   |     49      |      49      |      48      | **2.792481250** |
|  `4x4x5`   |     61      |      61      |      61      |   2.814364818   |
|  `4x4x6`   |   73 (?)    |      73      |      73      |   2.819981689   |
|  `4x4x7`   |     85      |      85      |      85      |   2.824617348   |
|  `4x4x8`   |   96 (?)    |    96 (?)    |      96      |   2.822126786   |
|  `4x4x9`   |   107 (?)   |   107 (?)    |     104      | **2.803560588** |
|  `4x4x10`  |   115 (?)   |   115 (?)    |  115 (120)   | **2.804789925** |
|  `4x4x11`  |   129 (?)   |   129 (?)    |  129 (130)   |   2.819743225   |
|  `4x4x12`  |   141 (?)   |   141 (?)    |  141 (142)   |   2.823831239   |
|  `4x4x13`  |   153 (?)   |   153 (?)    |     152      |   2.823706611   |
|  `4x4x14`  |   164 (?)   |   164 (?)    |  163 (165)   |   2.823771262   |
|  `4x4x15`  |   176 (?)   |   176 (?)    |  176 (177)   |   2.830226950   |
|  `4x4x16`  |   188 (?)   |   188 (?)    |  188 (189)   |   2.832970819   |
|  `4x5x5`   |     76      |      76      |      76      |   2.821220388   |
|  `4x5x6`   |   90 (?)    |      90      |      90      |   2.819728939   |
|  `4x5x7`   |   104 (?)   |     104      |     104      |   2.819542878   |
|  `4x5x8`   |  118 (122)  |     118      |     118      |   2.820012554   |
|  `4x5x9`   |   132 (?)   |  132 (139)   |  132 (136)   |   2.820821776   |
|  `4x5x10`  |  146 (152)  |  146 (151)   |  146 (151)   |   2.821805270   |
|  `4x5x11`  |   160 (?)   |  160 (165)   |  160 (165)   |   2.822872235   |
|  `4x5x12`  |   174 (?)   |  174 (180)   |  174 (180)   |   2.823971094   |
|  `4x5x13`  |   191 (?)   |  191 (194)   |  191 (194)   |   2.833613095   |
|  `4x5x14`  |   207 (?)   |  207 (208)   |  206 (208)   |   2.836597217   |
|  `4x5x15`  |   221 (?)   |  221 (226)   |  221 (226)   |   2.839254157   |
|  `4x5x16`  |   235 (?)   |   235 (?)    |  235 (240)   |   2.839432229   |
|  `4x6x6`   |     105     |     105      |     105      |   2.809337134   |
|  `4x6x7`   |   123 (?)   |     123      |     123      |   2.817457953   |
|  `4x6x8`   |     140     |     140      |     140      |   2.819769913   |
|  `4x6x9`   |   159 (?)   |   159 (?)    |     159      |   2.829009300   |
|  `4x6x10`  |   175 (?)   |     175      |     175      |   2.827107959   |
|  `4x6x11`  |   194 (?)   |   194 (?)    |     194      |   2.834239371   |
|  `4x6x12`  |     210     |     210      |     210      |   2.832674296   |
|  `4x6x13`  |   227 (?)   |  227 (228)   |  227 (228)   |   2.833857047   |
|  `4x6x14`  |     245     |     245      |     245      |   2.837108348   |
|  `4x6x15`  |   263 (?)   |     263      |     263      |   2.839987538   |
|  `4x6x16`  |  276 (280)  |  276 (280)   |  276 (280)   |   2.833509566   |
|  `4x7x7`   |   144 (?)   |     144      |     144      |   2.824766202   |
|  `4x7x8`   |  161 (164)  |  161 (164)   |  161 (164)   |   2.816927225   |
|  `4x7x9`   |   187 (?)   |   187 (?)    |     186      |   2.835236653   |
|  `4x7x10`  |   206 (?)   |   206 (?)    |     203      |   2.828786709   |
|  `4x7x11`  |   225 (?)   |  225 (227)   |  224 (227)   |   2.833273201   |
|  `4x7x12`  |   242 (?)   |  242 (246)   |  242 (246)   |   2.830754429   |
|  `4x7x13`  |   265 (?)   |   265 (?)    |  265 (266)   |   2.838520048   |
|  `4x7x14`  |  284 (285)  |  284 (285)   |  284 (285)   |   2.838080655   |
|  `4x7x15`  |   305 (?)   |   305 (?)    |  305 (307)   |   2.841094648   |
|  `4x7x16`  |  322 (324)  |  322 (324)   |  322 (324)   |   2.837713576   |
|  `4x8x8`   |  180 (182)  |  180 (182)   |  180 (182)   |   2.809444911   |
|  `4x8x9`   |   209 (?)   |   209 (?)    |     206      |   2.822486324   |
|  `4x8x10`  |   230 (?)   |   230 (?)    |     224      |   2.814499777   |
|  `4x8x11`  |   253 (?)   |   253 (?)    |     252      |   2.829012734   |
|  `4x8x12`  |     272     |     272      |     272      |   2.826149622   |
|  `4x8x13`  |   297 (?)   |     297      |     297      |   2.832380680   |
|  `4x8x14`  |     315     |     315      |     315      |   2.826912765   |
|  `4x8x15`  |     339     |     339      |     339      |   2.831001921   |
|  `4x8x16`  |     357     |     357      |     357      |   2.826593421   |
|  `4x9x9`   |     225     |     225      |     225      |   2.810763211   |
|  `4x9x10`  |  250 (255)  |  250 (255)   |  250 (255)   |   2.814150526   |
|  `4x9x11`  |  275 (280)  |  275 (280)   |  275 (280)   |   2.817111923   |
|  `4x9x12`  |     300     |     300      |     300      |   2.819734242   |
|  `4x9x13`  |   325 (?)   |   325 (?)    |  325 (329)   |   2.822080998   |
|  `4x9x14`  |   350 (?)   |  350 (355)   |  350 (355)   |   2.824199930   |
|  `4x9x15`  |   375 (?)   |     375      |     375      |   2.826127741   |
|  `4x9x16`  |  398 (400)  |  398 (400)   |  398 (400)   |   2.825527347   |
| `4x10x10`  |     280     |     280      |     280      |   2.821408468   |
| `4x10x11`  |     308     |     308      |     308      |   2.824204956   |
| `4x10x12`  |     329     |     329      |     329      |   2.816452167   |
| `4x10x13`  |   361 (?)   |   361 (?)    |     361      |   2.824930840   |
| `4x10x14`  |   385 (?)   |   385 (?)    |     385      |   2.822362266   |
| `4x10x15`  |   417 (?)   |   417 (?)    |  413 (417)   |   2.824846255   |
| `4x10x16`  |   441 (?)   |   441 (?)    |     441      |   2.827087301   |
| `4x11x11`  |   340 (?)   |     340      |     340      |   2.828630974   |
| `4x11x12`  |   362 (?)   |  362 (365)   |  362 (365)   |   2.819374888   |
| `4x11x13`  |   401 (?)   |   401 (?)    |     400      |   2.830997032   |
| `4x11x14`  |   429 (?)   |   429 (?)    |     429      |   2.831024692   |
| `4x11x15`  |   458 (?)   |   458 (?)    |  449 (452)   |   2.821995048   |
| `4x11x16`  |   480 (?)   |   480 (?)    |  480 (489)   |   2.824765046   |
| `4x12x12`  |  389 (390)  |  389 (390)   |  389 (390)   |   2.814731749   |
| `4x12x13`  |   430 (?)   |   430 (?)    |  422 (426)   |   2.817680586   |
| `4x12x14`  |   455 (?)   |   455 (?)    |  452 (456)   |   2.817253261   |
| `4x12x15`  |   488 (?)   |   488 (?)    |     480      |   2.815116449   |
| `4x12x16`  |  513 (520)  |  513 (520)   |  513 (520)   |   2.817793502   |
| `4x13x13`  |   472 (?)   |   472 (?)    |     466      |   2.828730930   |
| `4x13x14`  |   502 (?)   |   502 (?)    |     500      |   2.828979156   |
| `4x13x15`  |   536 (?)   |   536 (?)    |  520 (528)   |   2.817338694   |
| `4x13x16`  |  560 (568)  |  560 (568)   |  560 (568)   |   2.823361605   |
| `4x14x14`  |   532 (?)   |   532 (?)    |     532      |   2.825446399   |
| `4x14x15`  |   572 (?)   |   572 (?)    |  557 (568)   |   2.816955831   |
| `4x14x16`  |  598 (610)  |  598 (610)   |  598 (610)   |   2.821556397   |
| `4x15x15`  |  599 (600)  |  599 (600)   |  596 (600)   |   2.818231324   |
| `4x15x16`  |   640 (?)   |   640 (?)    |  632 (640)   |   2.817366557   |
| `4x16x16`  |  666 (676)  |  666 (676)   |  666 (676)   |   2.813813510   |
|  `5x5x5`   |     93      |      93      |      93      |   2.816262409   |
|  `5x5x6`   |   110 (?)   |     110      |     110      |   2.814302034   |
|  `5x5x7`   |  127 (134)  |     127      |     127      |   2.813778022   |
|  `5x5x8`   |   144 (?)   |     144      |     144      |   2.813995249   |
|  `5x5x9`   |   161 (?)   |  161 (167)   |  161 (167)   |   2.814610506   |
|  `5x5x10`  |   178 (?)   |   178 (?)    |  178 (184)   |   2.815441580   |
|  `5x5x11`  |   195 (?)   |   195 (?)    |  195 (202)   |   2.816386568   |
|  `5x5x12`  |   204 (?)   |  204 (220)   |  204 (220)   | **2.797154354** |
|  `5x5x13`  |   227 (?)   |  227 (237)   |  227 (237)   |   2.813855803   |
|  `5x5x14`  |   244 (?)   |  244 (254)   |  244 (254)   |   2.815242892   |
|  `5x5x15`  |   262 (?)   |   262 (?)    |  262 (271)   |   2.818498736   |
|  `5x5x16`  |   280 (?)   |   280 (?)    |  280 (288)   |   2.821408468   |
|  `5x6x6`   |   130 (?)   |     130      |     130      |   2.812001673   |
|  `5x6x7`   |   150 (?)   |     150      |     150      |   2.811221917   |
|  `5x6x8`   |  170 (176)  |     170      |     170      |   2.811240720   |
|  `5x6x9`   |   193 (?)   |  193 (197)   |  193 (197)   |   2.820092998   |
|  `5x6x10`  |   216 (?)   |  216 (218)   |  216 (218)   |   2.827217780   |
|  `5x6x11`  |   238 (?)   |   238 (?)    |     236      |   2.826562083   |
|  `5x6x12`  |   258 (?)   |   258 (?)    |     250      |   2.814150526   |
|  `5x6x13`  |   280 (?)   |   280 (?)    |     278      |   2.829776752   |
|  `5x6x14`  |   300 (?)   |   300 (?)    |     297      |   2.827893397   |
|  `5x6x15`  |   320 (?)   |   320 (?)    |     318      |   2.829506239   |
|  `5x6x16`  |   340 (?)   |   340 (?)    |     340      |   2.832433220   |
|  `5x7x7`   |   176 (?)   |     176      |     176      |   2.819618966   |
|  `5x7x8`   |   204 (?)   |   204 (?)    |  204 (205)   |   2.831402964   |
|  `5x7x9`   |   229 (?)   |  229 (234)   |     229      |   2.833717544   |
|  `5x7x10`  |   254 (?)   |     254      |     254      |   2.835812967   |
|  `5x7x11`  |   277 (?)   |     277      |     277      |   2.834094219   |
|  `5x7x12`  |   298 (?)   |   298 (?)    |     296      |   2.826218294   |
|  `5x7x13`  |   325 (?)   |   325 (?)    |     325      |   2.835070644   |
|  `5x7x14`  |   351 (?)   |   351 (?)    |     349      |   2.835658091   |
|  `5x7x15`  |   377 (?)   |   377 (?)    |     375      |   2.838838811   |
|  `5x7x16`  |   400 (?)   |   400 (?)    |     398      |   2.838106105   |
|  `5x8x8`   |     230     |     230      |     230      |   2.828247238   |
|  `5x8x9`   |   260 (?)   |   260 (?)    |     260      |   2.834140342   |
|  `5x8x10`  |   286 (?)   |   286 (?)    |     284      |   2.828510889   |
|  `5x8x11`  |   313 (?)   |   313 (?)    |     312      |   2.830564681   |
|  `5x8x12`  |   333 (?)   |   333 (?)    |     333      |   2.822324450   |
|  `5x8x13`  |   365 (?)   |   365 (?)    |     363      |   2.827581156   |
|  `5x8x14`  |   391 (?)   |   391 (?)    |     387      |   2.824818687   |
|  `5x8x15`  |   421 (?)   |   421 (?)    |     419      |   2.831610434   |
|  `5x8x16`  |   445 (?)   |   445 (?)    |     445      |   2.831279571   |
|  `5x9x9`   |   293 (?)   |   293 (?)    |  293 (294)   |   2.838247561   |
|  `5x9x10`  |   322 (?)   |   322 (?)    |     322      |   2.835644554   |
|  `5x9x11`  |   353 (?)   |   353 (?)    |     353      |   2.836528379   |
|  `5x9x12`  |   377 (?)   |   377 (?)    |     377      |   2.828664069   |
|  `5x9x13`  |   412 (?)   |   412 (?)    |     411      |   2.833785246   |
|  `5x9x14`  |   441 (?)   |   441 (?)    |     439      |   2.831878945   |
|  `5x9x15`  |   468 (?)   |  468 (474)   |  463 (474)   |   2.826399572   |
|  `5x9x16`  |   503 (?)   |   503 (?)    |     497      |   2.830986305   |
| `5x10x10`  |     352     |     352      |     352      |   2.830571654   |
| `5x10x11`  |   386 (?)   |     386      |     386      |   2.831655074   |
| `5x10x12`  |   408 (?)   |  408 (413)   |  408 (413)   |   2.819133943   |
| `5x10x13`  |   451 (?)   |   451 (?)    |     451      |   2.830705612   |
| `5x10x14`  |   481 (?)   |   481 (?)    |     481      |   2.828175028   |
| `5x10x15`  |   519 (?)   |   519 (?)    |     519      |   2.833157741   |
| `5x10x16`  |   549 (?)   |   549 (?)    |     549      |   2.831023864   |
| `5x11x11`  |   427 (?)   |   427 (?)    |     424      |   2.833497741   |
| `5x11x12`  |   461 (?)   |   461 (?)    |  454 (455)   |   2.827112377   |
| `5x11x13`  |   503 (?)   |   503 (?)    |     498      |   2.834905546   |
| `5x11x14`  |   537 (?)   |   537 (?)    |     533      |   2.833953893   |
| `5x11x15`  |   577 (?)   |   577 (?)    |     575      |   2.838722531   |
| `5x11x16`  |   609 (?)   |   609 (?)    |     609      |   2.837120407   |
| `5x12x12`  |   498 (?)   |   498 (?)    |     488      |   2.822653463   |
| `5x12x13`  |   537 (?)   |   537 (?)    |     536      |   2.830991200   |
| `5x12x14`  |   581 (?)   |   581 (?)    |     574      |   2.830350615   |
| `5x12x15`  |   612 (?)   |   612 (?)    |  612 (615)   |   2.829914687   |
| `5x12x16`  |   657 (?)   |   657 (?)    |  655 (656)   |   2.832983066   |
| `5x13x13`  |   592 (?)   |   592 (?)    |  587 (588)   |   2.837827448   |
| `5x13x14`  |   632 (?)   |   632 (?)    |  628 (630)   |   2.836688582   |
| `5x13x15`  |   675 (?)   |   675 (?)    |     672      |   2.837770064   |
| `5x13x16`  |   718 (?)   |   718 (?)    |     717      |   2.839397681   |
| `5x14x14`  |   672 (?)   |   672 (?)    |  672 (676)   |   2.835662569   |
| `5x14x15`  |   722 (?)   |   722 (?)    |     721      |   2.837890958   |
| `5x14x16`  |   769 (?)   |   769 (?)    |     768      |   2.838788042   |
| `5x15x15`  |  761 (762)  |  761 (762)   |  761 (762)   |   2.833078290   |
| `5x15x16`  |   813 (?)   |     813      |     813      |   2.835257472   |
| `5x16x16`  |     868     |     868      |     868      |   2.837130178   |
|  `6x6x6`   |     153     |     153      |     153      |   2.807540860   |
|  `6x6x7`   |   183 (?)   |     183      |     183      |   2.826414484   |
|  `6x6x8`   |     203     |     203      |     203      |   2.814714670   |
|  `6x6x9`   |     225     |     225      |     225      |   2.810763211   |
|  `6x6x10`  |   252 (?)   |   252 (?)    |     247      |   2.807997433   |
|  `6x6x11`  |   276 (?)   |   276 (?)    |     268      | **2.804179806** |
|  `6x6x12`  |   294 (?)   |   294 (?)    |     280      | **2.785626776** |
|  `6x6x13`  |   322 (?)   |   322 (?)    |  315 (316)   | **2.806832057** |
|  `6x6x14`  |   343 (?)   |   343 (?)    |     336      | **2.804519017** |
|  `6x6x15`  |   371 (?)   |   371 (?)    |     360      | **2.806662647** |
|  `6x6x16`  |   392 (?)   |   392 (?)    |     385      |   2.809853287   |
|  `6x7x7`   |  212 (215)  |  212 (215)   |  212 (215)   |   2.827400948   |
|  `6x7x8`   |  238 (239)  |  238 (239)   |  238 (239)   |   2.822158898   |
|  `6x7x9`   |  264 (270)  |  264 (270)   |  264 (270)   |   2.818558639   |
|  `6x7x10`  |   296 (?)   |     296      |  293 (296)   |   2.821158816   |
|  `6x7x11`  |   322 (?)   |   322 (?)    |     318      |   2.817369624   |
|  `6x7x12`  |   342 (?)   |   342 (?)    |     336      | **2.804519017** |
|  `6x7x13`  |   376 (?)   |   376 (?)    |     372      |   2.817349681   |
|  `6x7x14`  |   403 (?)   |   403 (?)    |     399      |   2.817571522   |
|  `6x7x15`  |   435 (?)   |   435 (?)    |     430      |   2.822238033   |
|  `6x7x16`  |   460 (?)   |   460 (?)    |     457      |   2.822322742   |
|  `6x8x8`   |     266     |     266      |     266      |   2.814904236   |
|  `6x8x9`   |     296     |     296      |     296      |   2.813098408   |
|  `6x8x10`  |   327 (?)   |  327 (329)   |  327 (329)   |   2.813489198   |
|  `6x8x11`  |   357 (?)   |   357 (?)    |     357      |   2.812719178   |
|  `6x8x12`  |   378 (?)   |   378 (?)    |     378      | **2.801192733** |
|  `6x8x13`  |   418 (?)   |   418 (?)    |     414      |   2.808759412   |
|  `6x8x14`  |   448 (?)   |   448 (?)    |     441      | **2.805900115** |
|  `6x8x15`  |   484 (?)   |   484 (?)    |     480      |   2.815116449   |
|  `6x8x16`  |   510 (?)   |   510 (?)    |  510 (511)   |   2.815145110   |
|  `6x9x9`   |   341 (?)   |  341 (342)   |  332 (342)   |   2.815198446   |
|  `6x9x10`  |   371 (?)   |  371 (373)   |  367 (373)   |   2.815845324   |
|  `6x9x11`  |   407 (?)   |   407 (?)    |  404 (407)   |   2.818942356   |
|  `6x9x12`  |   433 (?)   |   433 (?)    |  429 (434)   |   2.808878248   |
|  `6x9x13`  |   476 (?)   |   472 (?)    |  468 (474)   |   2.814402245   |
|  `6x9x14`  |   507 (?)   |   507 (?)    |  494 (500)   |   2.807406517   |
|  `6x9x15`  |   538 (?)   |   538 (?)    |  529 (532)   |   2.809148737   |
|  `6x9x16`  |   572 (?)   |   572 (?)    |  552 (556)   | **2.801218708** |
| `6x10x10`  |     406     |     406      |     406      |   2.816829393   |
| `6x10x11`  |   446 (?)   |     446      |     446      |   2.818897225   |
| `6x10x12`  |   476 (?)   |     476      |     476      |   2.811300704   |
| `6x10x13`  |   520 (?)   |   520 (?)    |     520      |   2.817338694   |
| `6x10x14`  |   553 (?)   |   553 (?)    |     553      |   2.813744718   |
| `6x10x15`  |   594 (?)   |   594 (?)    |  594 (597)   |   2.816748899   |
| `6x10x16`  |   630 (?)   |   630 (?)    |     630      |   2.815981845   |
| `6x11x11`  |   496 (?)   |   496 (?)    |     490      |   2.820960164   |
| `6x11x12`  |   521 (?)   |   521 (?)    |  521 (524)   |   2.811757811   |
| `6x11x13`  |   584 (?)   |   584 (?)    |     574      |   2.821466352   |
| `6x11x14`  |   621 (?)   |   621 (?)    |     613      |   2.819725683   |
| `6x11x15`  |   653 (?)   |  653 (661)   |  653 (661)   |   2.819014665   |
| `6x11x16`  |   684 (?)   |   684 (?)    |  684 (695)   |   2.812868273   |
| `6x12x12`  |   564 (?)   |   564 (?)    |     560      |   2.807602758   |
| `6x12x13`  |   615 (?)   |   615 (?)    |  615 (616)   |   2.815835948   |
| `6x12x14`  |   666 (?)   |   654 (?)    |  645 (658)   | **2.806322591** |
| `6x12x15`  |   704 (?)   |  703 (705)   |  686 (705)   | **2.805072101** |
| `6x12x16`  |   736 (?)   |   736 (?)    |  736 (746)   |   2.809331029   |
| `6x13x13`  |   682 (?)   |   682 (?)    |  678 (680)   |   2.825542860   |
| `6x13x14`  |   730 (?)   |   730 (?)    |  726 (730)   |   2.824944345   |
| `6x13x15`  |   763 (?)   |  763 (771)   |  763 (771)   |   2.818464723   |
| `6x13x16`  |   816 (?)   |   816 (?)    |  798 (819)   |   2.811823417   |
| `6x14x14`  |   777 (?)   |   777 (?)    |  776 (777)   |   2.823594480   |
| `6x14x15`  |   814 (?)   |   814 (?)    |  814 (825)   |   2.816396649   |
| `6x14x16`  |   864 (?)   |   864 (?)    |  864 (880)   |   2.815990055   |
| `6x15x15`  |  868 (870)  |  868 (870)   |  859 (870)   |   2.811834182   |
| `6x15x16`  |   920 (?)   |   920 (?)    |  920 (928)   |   2.815181444   |
| `6x16x16`  |  972 (988)  |  972 (988)   |  972 (988)   |   2.812899669   |
|  `7x7x7`   |   250 (?)   |   250 (?)    |     249      |   2.835409898   |
|  `7x7x8`   |   278 (?)   |   278 (?)    |     277      |   2.825542234   |
|  `7x7x9`   |   316 (?)   |  316 (318)   |     315      |   2.834224130   |
|  `7x7x10`  |   346 (?)   |     346      |  345 (346)   |   2.830075228   |
|  `7x7x11`  |   378 (?)   |   378 (?)    |     376      |   2.828230821   |
|  `7x7x12`  |   404 (?)   |   404 (?)    |     402      |   2.821095589   |
|  `7x7x13`  |   443 (?)   |   443 (?)    |     441      |   2.829144541   |
|  `7x7x14`  |   475 (?)   |   475 (?)    |     471      |   2.827273046   |
|  `7x7x15`  |   511 (?)   |   511 (?)    |     508      |   2.832092591   |
|  `7x7x16`  |   540 (?)   |   540 (?)    |     539      |   2.831330828   |
|  `7x8x8`   |   310 (?)   |   310 (?)    |     306      |   2.812667793   |
|  `7x8x9`   |   347 (?)   |   347 (?)    |  347 (350)   |   2.820049700   |
|  `7x8x10`  |   385 (?)   |     385      |     385      |   2.822362266   |
|  `7x8x11`  |   423 (?)   |   423 (?)    |     423      |   2.824446365   |
|  `7x8x12`  |   452 (?)   |   452 (?)    |  452 (454)   |   2.817253261   |
|  `7x8x13`  |   498 (?)   |   498 (?)    |     496      |   2.825322795   |
|  `7x8x14`  |   532 (?)   |   532 (?)    |     529      |   2.822900761   |
|  `7x8x15`  |   572 (?)   |   572 (?)    |  557 (571)   |   2.816955831   |
|  `7x8x16`  |   598 (?)   |   598 (?)    |  598 (603)   |   2.821556397   |
|  `7x9x9`   |   396 (?)   |   396 (?)    |  396 (398)   |   2.830161790   |
|  `7x9x10`  |   433 (?)   |  433 (437)   |  433 (437)   |   2.825473910   |
|  `7x9x11`  |   478 (?)   |   478 (?)    |  478 (480)   |   2.829651018   |
|  `7x9x12`  |   513 (?)   |   513 (?)    |  508 (510)   |   2.820055471   |
|  `7x9x13`  |   563 (?)   |   563 (?)    |     562      |   2.831584296   |
|  `7x9x14`  |   600 (?)   |   600 (?)    |     597      |   2.827367786   |
|  `7x9x15`  |   639 (?)   |     639      |  634 (639)   |   2.825226157   |
|  `7x9x16`  |   677 (?)   |   677 (?)    |     667      |   2.820871928   |
| `7x10x10`  |     478     |     478      |     478      |   2.825309911   |
| `7x10x11`  |   526 (?)   |     526      |     526      |   2.827986649   |
| `7x10x12`  |   564 (?)   |     564      |  557 (564)   |   2.816955831   |
| `7x10x13`  |   614 (?)   |   614 (?)    |     614      |   2.826761780   |
| `7x10x14`  |   653 (?)   |   653 (?)    |     653      |   2.823169941   |
| `7x10x15`  |   694 (?)   |   694 (?)    |  694 (711)   |   2.821431419   |
| `7x10x16`  |   742 (?)   |   742 (?)    |  736 (752)   |   2.820602981   |
| `7x11x11`  |   580 (?)   |   580 (?)    |     577      |   2.829186234   |
| `7x11x12`  |   624 (?)   |   624 (?)    |     618      |   2.823294520   |
| `7x11x13`  |   680 (?)   |   680 (?)    |     675      |   2.828894453   |
| `7x11x14`  |   725 (?)   |   725 (?)    |     721      |   2.827195395   |
| `7x11x15`  |   778 (?)   |     778      |  777 (778)   |   2.831357038   |
| `7x11x16`  |   822 (?)   |   822 (?)    |  822 (827)   |   2.829413433   |
| `7x12x12`  |   669 (?)   |   669 (?)    |     660      |   2.816295309   |
| `7x12x13`  |   731 (?)   |   731 (?)    |     724      |   2.823761363   |
| `7x12x14`  |   780 (?)   |   780 (?)    |     774      |   2.822499419   |
| `7x12x15`  |   815 (?)   |  815 (831)   |  815 (831)   |   2.816912591   |
| `7x12x16`  |   878 (?)   |   878 (?)    |  878 (880)   |   2.822684315   |
| `7x13x13`  |   798 (?)   |   798 (?)    |  794 (795)   |   2.830948485   |
| `7x13x14`  |   852 (?)   |   852 (?)    |  850 (852)   |   2.830202017   |
| `7x13x15`  |   909 (?)   |     909      |     909      |   2.831041821   |
| `7x13x16`  |   966 (?)   |   966 (?)    |  962 (968)   |   2.829297704   |
| `7x14x14`  |   909 (?)   |   909 (?)    |  909 (912)   |   2.829037251   |
| `7x14x15`  |   952 (?)   |  952 (976)   |  952 (976)   |   2.821286881   |
| `7x14x16`  |  1028 (?)   |   1028 (?)   | 1022 (1034)  |   2.825469455   |
| `7x15x15`  |    1032     |     1032     |     1032     |   2.827727792   |
| `7x15x16`  |  1089 (?)   |   1089 (?)   | 1083 (1099)  |   2.822639497   |
| `7x16x16`  |  1158 (?)   |   1158 (?)   |     1148     |   2.821663673   |
|  `8x8x8`   |   343 (?)   |   343 (?)    |     336      | **2.797439141** |
|  `8x8x9`   |   391 (?)   |   391 (?)    |     388      |   2.813516852   |
|  `8x8x10`  |     427     |     427      |     427      |   2.812108880   |
|  `8x8x11`  |   475 (?)   |   475 (?)    |     475      |   2.819973988   |
|  `8x8x12`  |   508 (?)   |   508 (?)    |     504      |   2.809801266   |
|  `8x8x13`  |   559 (?)   |   559 (?)    |     559      |   2.822564153   |
|  `8x8x14`  |     595     |     595      |     595      |   2.819336895   |
|  `8x8x15`  |   639 (?)   |   639 (?)    |  628 (635)   |   2.814592730   |
|  `8x8x16`  |   666 (?)   |   666 (?)    |  666 (672)   |   2.813813510   |
|  `8x9x9`   |   432 (?)   |   432 (?)    |     430      |   2.809957177   |
|  `8x9x10`  |  482 (487)  |  482 (487)   |  482 (487)   |   2.817012414   |
|  `8x9x11`  |   521 (?)   |   521 (?)    |  521 (533)   |   2.811757811   |
|  `8x9x12`  |   564 (?)   |   564 (?)    |     560      |   2.807602758   |
|  `8x9x13`  |   615 (?)   |  615 (624)   |  615 (624)   |   2.815835948   |
|  `8x9x14`  |   654 (?)   |  654 (669)   |  654 (669)   |   2.812333691   |
|  `8x9x15`  |   699 (?)   |  699 (705)   |  699 (705)   |   2.813135327   |
|  `8x9x16`  |   735 (?)   |   735 (?)    |  735 (746)   |   2.808752406   |
| `8x10x10`  |  528 (532)  |  528 (532)   |  528 (532)   |   2.813520009   |
| `8x10x11`  |   588 (?)   |     588      |     588      |   2.821593096   |
| `8x10x12`  |   630 (?)   |     630      |  624 (630)   |   2.811801179   |
| `8x10x13`  |   686 (?)   |     686      |     686      |   2.820311011   |
| `8x10x14`  |   726 (?)   |  726 (728)   |  726 (728)   |   2.814757685   |
| `8x10x15`  |   784 (?)   |  784 (789)   |  778 (789)   |   2.816637962   |
| `8x10x16`  |   826 (?)   |   826 (?)    |  822 (832)   |   2.814298209   |
| `8x11x11`  |   646 (?)   |   646 (?)    |     641      |   2.820135833   |
| `8x11x12`  |   690 (?)   |   690 (?)    |  676 (680)   |   2.807798855   |
| `8x11x13`  |   754 (?)   |   754 (?)    |     750      |   2.820138111   |
| `8x11x14`  |   804 (?)   |     804      |     804      |   2.820079580   |
| `8x11x15`  |   859 (?)   |     859      |  848 (859)   |   2.815247371   |
| `8x11x16`  |   914 (?)   |   914 (?)    |  904 (920)   |   2.816647975   |
| `8x12x12`  |   735 (?)   |   735 (?)    |     720      | **2.799977314** |
| `8x12x13`  |   807 (?)   |   807 (?)    |  781 (798)   | **2.802762167** |
| `8x12x14`  |   861 (?)   |     861      |  843 (861)   | **2.805742480** |
| `8x12x15`  |  914 (915)  |  914 (915)   |  904 (915)   |   2.807944089   |
| `8x12x16`  |   960 (?)   |   960 (?)    |     960      |   2.807820225   |
| `8x13x13`  |   885 (?)   |   885 (?)    |     880      |   2.821307498   |
| `8x13x14`  |   945 (?)   |     945      |  944 (945)   |   2.821517755   |
| `8x13x15`  | 991 (1005)  |  991 (1005)  |  991 (1005)  |   2.814866970   |
| `8x13x16`  |  1064 (?)   |   1064 (?)   | 1054 (1064)  |   2.815302758   |
| `8x14x14`  |  1008 (?)   |     1008     | 1004 (1008)  |   2.818224059   |
| `8x14x15`  | 1063 (1080) | 1063 (1080)  | 1063 (1080)  |   2.815109808   |
| `8x14x16`  |  1127 (?)   |   1127 (?)   | 1104 (1138)  | **2.806012534** |
| `8x15x15`  | 1137 (1140) | 1137 (1140)  | 1130 (1140)  |   2.813661626   |
| `8x15x16`  |  1203 (?)   |   1203 (?)   | 1185 (1198)  |   2.808501081   |
| `8x16x16`  |  1260 (?)   |   1260 (?)   | 1230 (1248)  | **2.799393436** |
|  `9x9x9`   |  486 (498)  |  486 (498)   |  486 (498)   |   2.815464877   |
|  `9x9x10`  |   537 (?)   |   537 (?)    |     534      |   2.813362874   |
|  `9x9x11`  |   594 (?)   |   594 (?)    |     576      | **2.807325686** |
|  `9x9x12`  |   626 (?)   |   626 (?)    |     600      | **2.789620062** |
|  `9x9x13`  |   683 (?)   |   683 (?)    |     681      |   2.812123330   |
|  `9x9x14`  |   725 (?)   |   725 (?)    |  720 (726)   | **2.806246597** |
|  `9x9x15`  |   794 (?)   |   794 (?)    |  760 (783)   | **2.801824302** |
|  `9x9x16`  |   824 (?)   |   824 (?)    |  822 (825)   |   2.809420228   |
| `9x10x10`  |   597 (?)   |  597 (600)   |  597 (600)   |   2.818970672   |
| `9x10x11`  |   661 (?)   |   661 (?)    |     651      |   2.817680531   |
| `9x10x12`  |   702 (?)   |   702 (?)    |  668 (684)   | **2.793651686** |
| `9x10x13`  |   771 (?)   |  763 (772)   |  758 (772)   |   2.815672846   |
| `9x10x14`  |   820 (?)   |     820      |  808 (820)   |   2.813287623   |
| `9x10x15`  |  864 (870)  |  864 (870)   |  864 (870)   |   2.814249815   |
| `9x10x16`  |   924 (?)   |   920 (?)    |  916 (939)   |   2.813383975   |
| `9x11x11`  |   721 (?)   |   721 (?)    |  715 (725)   |   2.819505933   |
| `9x11x12`  |   762 (?)   |   762 (?)    |  738 (760)   | **2.798270808** |
| `9x11x13`  |   843 (?)   |  843 (849)   |  835 (849)   |   2.818729064   |
| `9x11x14`  |   900 (?)   |  900 (904)   |  882 (904)   |   2.812562599   |
| `9x11x15`  |   956 (?)   |   956 (?)    |  956 (981)   |   2.819087272   |
| `9x11x16`  |   996 (?)   |  996 (1030)  |  996 (1030)  |   2.811083198   |
| `9x12x12`  |   810 (?)   |   810 (?)    |     800      | **2.798064630** |
| `9x12x13`  |   878 (?)   |   878 (?)    |  878 (900)   | **2.805673201** |
| `9x12x14`  |   960 (?)   |   960 (?)    |  940 (945)   | **2.805232985** |
| `9x12x15`  |  1012 (?)   |   1012 (?)   |  996 (1000)  | **2.802534955** |
| `9x12x16`  |  1074 (?)   |   1074 (?)   | 1035 (1080)  | **2.793729377** |
| `9x13x13`  |   986 (?)   |  986 (996)   |  981 (996)   |   2.820440786   |
| `9x13x14`  |  1050 (?)   | 1050 (1063)  | 1024 (1063)  |   2.809588658   |
| `9x13x15`  |  1119 (?)   |   1119 (?)   | 1119 (1135)  |   2.819269106   |
| `9x13x16`  |  1167 (?)   | 1167 (1210)  | 1167 (1210)  |   2.811843698   |
| `9x14x14`  |  1125 (?)   | 1125 (1136)  | 1101 (1136)  |   2.810831956   |
| `9x14x15`  |  1179 (?)   |   1179 (?)   | 1175 (1185)  |   2.810993734   |
| `9x14x16`  |  1270 (?)   |   1270 (?)   | 1254 (1260)  |   2.812806553   |
| `9x15x15`  |  1276 (?)   |   1276 (?)   | 1236 (1290)  | **2.805463706** |
| `9x15x16`  |  1320 (?)   | 1320 (1350)  | 1320 (1350)  |   2.807572842   |
| `9x16x16`  | 1380 (1444) | 1380 (1444)  | 1380 (1444)  | **2.801393711** |
| `10x10x10` |   651 (?)   |     651      |     651      |   2.813580989   |
| `10x10x11` |   719 (?)   |     719      |     719      |   2.817849439   |
| `10x10x12` |   766 (?)   |  766 (770)   |  766 (770)   |   2.810060733   |
| `10x10x13` |   838 (?)   |     838      |     838      |   2.816278610   |
| `10x10x14` |   889 (?)   |     889      |     889      |   2.811934283   |
| `10x10x15` |   957 (?)   |   957 (?)    |     957      |   2.815641959   |
| `10x10x16` |  1008 (?)   |   1008 (?)   |     1008     |   2.812123655   |
| `10x11x11` |   793 (?)   |     793      |     793      |   2.821415868   |
| `10x11x12` |   850 (?)   |     850      |  849 (850)   |   2.815739433   |
| `10x11x13` |   924 (?)   |     924      |     924      |   2.819673026   |
| `10x11x14` |   981 (?)   |     981      |     981      |   2.815670174   |
| `10x11x15` |  1050 (?)   |   1050 (?)   | 1050 (1067)  |   2.816973777   |
| `10x11x16` |  1112 (?)   |   1112 (?)   | 1112 (1136)  |   2.815676689   |
| `10x12x12` |   902 (?)   |  902 (910)   |  902 (910)   | **2.807030426** |
| `10x12x13` |   990 (?)   |     990      |     990      |   2.814455029   |
| `10x12x14` |  1050 (?)   |     1050     |     1050     |   2.810139154   |
| `10x12x15` | 1122 (1140) | 1122 (1140)  | 1122 (1140)  |   2.810818006   |
| `10x12x16` |  1190 (?)   |   1190 (?)   | 1176 (1216)  | **2.805475746** |
| `10x13x13` |  1082 (?)   |     1082     |     1082     |   2.820012787   |
| `10x13x14` |  1154 (?)   |     1154     |     1154     |   2.817919098   |
| `10x13x15` |  1230 (?)   | 1230 (1242)  | 1230 (1242)  |   2.817513014   |
| `10x13x16` |  1326 (?)   | 1326 (1332)  | 1318 (1332)  |   2.820846164   |
| `10x14x14` |  1232 (?)   |     1232     |     1232     |   2.816254849   |
| `10x14x15` |  1314 (?)   | 1314 (1327)  | 1314 (1327)  |   2.816125387   |
| `10x14x16` |  1418 (?)   | 1418 (1423)  | 1398 (1423)  |   2.816663561   |
| `10x15x15` |  1395 (?)   | 1389 (1395)  | 1385 (1395)  |   2.811406977   |
| `10x15x16` |  1488 (?)   | 1484 (1497)  | 1482 (1497)  |   2.814186431   |
| `10x16x16` | 1585 (1586) | 1578 (1586)  | 1560 (1586)  |   2.810651214   |
| `11x11x11` |   873 (?)   |     873      |     873      |   2.824116479   |
| `11x11x12` |   936 (?)   |     936      |  922 (936)   |   2.812867384   |
| `11x11x13` |  1023 (?)   |     1023     |     1023     |   2.824645969   |
| `11x11x14` |  1093 (?)   |     1093     |     1093     |   2.823197571   |
| `11x11x15` |  1169 (?)   | 1169 (1181)  | 1169 (1181)  |   2.824115356   |
| `11x11x16` |  1230 (?)   |   1230 (?)   | 1230 (1236)  |   2.820195393   |
| `11x12x12` |  1002 (?)   |   1002 (?)   |  968 (990)   | **2.799472327** |
| `11x12x13` |  1102 (?)   |     1102     | 1082 (1102)  |   2.814231919   |
| `11x12x14` |  1182 (?)   |     1182     | 1153 (1182)  |   2.811853672   |
| `11x12x15` |  1234 (?)   |   1234 (?)   | 1234 (1264)  |   2.813129312   |
| `11x12x16` |  1306 (?)   |   1306 (?)   | 1278 (1312)  | **2.803143027** |
| `11x13x13` |  1205 (?)   | 1205 (1210)  | 1205 (1210)  |   2.827216655   |
| `11x13x14` |  1292 (?)   | 1292 (1298)  | 1292 (1298)  |   2.827166171   |
| `11x13x15` |  1377 (?)   |     1377     | 1371 (1377)  |   2.824949046   |
| `11x13x16` |  1458 (?)   | 1458 (1472)  | 1446 (1472)  |   2.822035717   |
| `11x14x14` |  1376 (?)   | 1376 (1388)  | 1376 (1388)  |   2.824489318   |
| `11x14x15` |  1432 (?)   | 1432 (1471)  | 1432 (1471)  |   2.814780394   |
| `11x14x16` |  1550 (?)   |   1550 (?)   | 1520 (1571)  |   2.814428649   |
| `11x15x15` |  1548 (?)   |   1548 (?)   |     1540     |   2.817843009   |
| `11x15x16` |  1657 (?)   |   1629 (?)   | 1605 (1656)  |   2.810502126   |
| `11x16x16` |  1752 (?)   |   1752 (?)   |     1724     |   2.814679929   |
| `12x12x12` |  1068 (?)   |   1068 (?)   |     1040     | **2.795668800** |
| `12x12x13` |  1168 (?)   |   1168 (?)   | 1144 (1152)  | **2.803918249** |
| `12x12x14` |  1260 (?)   |   1260 (?)   | 1234 (1250)  | **2.806467563** |
| `12x12x15` |  1332 (?)   |   1332 (?)   |     1280     | **2.795549318** |
| `12x12x16` |  1380 (?)   |   1380 (?)   | 1380 (1392)  | **2.801393711** |
| `12x13x13` |  1298 (?)   |   1298 (?)   |     1274     |   2.816848164   |
| `12x13x14` |  1389 (?)   |   1389 (?)   | 1370 (1382)  |   2.818044255   |
| `12x13x15` |  1470 (?)   |   1470 (?)   | 1442 (1460)  |   2.812789736   |
| `12x13x16` |  1548 (?)   |   1544 (?)   | 1509 (1556)  | **2.807000642** |
| `12x14x14` |  1484 (?)   |   1484 (?)   | 1449 (1481)  |   2.812807792   |
| `12x14x15` |  1546 (?)   |   1546 (?)   | 1538 (1540)  |   2.810862435   |
| `12x14x16` |  1663 (?)   |   1663 (?)   | 1617 (1638)  | **2.806918970** |
| `12x15x15` |  1650 (?)   |   1650 (?)   |     1600     | **2.801323500** |
| `12x15x16` |  1725 (?)   |   1725 (?)   | 1725 (1728)  | **2.806957387** |
| `12x16x16` |  1862 (?)   |   1862 (?)   | 1815 (1824)  | **2.803398069** |
| `13x13x13` |  1426 (?)   |   1426 (?)   | 1421 (1426)  |   2.830120644   |
| `13x13x14` |  1511 (?)   | 1511 (1524)  | 1511 (1524)  |   2.826838093   |
| `13x13x15` |  1605 (?)   |     1605     |     1605     |   2.825055042   |
| `13x13x16` |  1711 (?)   |   1711 (?)   | 1704 (1713)  |   2.824705676   |
| `13x14x14` |  1614 (?)   | 1614 (1625)  | 1614 (1625)  |   2.825351482   |
| `13x14x15` |  1681 (?)   | 1681 (1714)  | 1681 (1714)  |   2.816136526   |
| `13x14x16` |  1820 (?)   |   1820 (?)   | 1796 (1825)  |   2.818238934   |
| `13x15x15` |  1797 (?)   | 1797 (1803)  | 1797 (1803)  |   2.816875265   |
| `13x15x16` |  1885 (?)   | 1885 (1932)  | 1885 (1932)  |   2.812106276   |
| `13x16x16` |  2038 (?)   |   2038 (?)   |     2022     |   2.815680662   |
| `14x14x14` |  1725 (?)   |   1725 (?)   |     1719     |   2.822787486   |
| `14x14x15` |  1798 (?)   | 1798 (1813)  | 1798 (1813)  |   2.815280055   |
| `14x14x16` |  1943 (?)   |   1943 (?)   | 1931 (1939)  |   2.819303950   |
| `14x15x15` |  1905 (?)   | 1895 (1905)  | 1890 (1905)  |   2.809752096   |
| `14x15x16` |  2043 (?)   |   2043 (?)   |     2016     |   2.811264261   |
| `14x16x16` |  2170 (?)   |   2170 (?)   | 2128 (2142)  |   2.808914234   |
| `15x15x15` |  2058 (?)   |   2058 (?)   |     2058     |   2.817336958   |
| `15x15x16` |  2132 (?)   |   2132 (?)   | 2132 (2173)  |   2.808074285   |
| `15x16x16` |  2302 (?)   |   2302 (?)   |     2262     |   2.807630537   |
| `16x16x16` |  2401 (?)   |   2401 (?)   |     2304     | **2.792481250** |

### Coefficient set status
* total schemes: 680 (52 better Strassen)
* `ZT` schemes: 378 (55.59%)
* `Z` schemes: 22 (3.24%)
* `Q` schemes: 280 (41.18%)


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
