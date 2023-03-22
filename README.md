## 🚨 this document is in progress

![logo](./images/logo.svg)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

-   [math](#math)
    -   [linear algebra](#linear-algebra)
    -   [calculus](#calculus)
    -   [optimization problem](#optimization-problem)
    -   [엔트로피](#엔트로피)
    -   [basic statistics](#basic-statistics)
    -   [bayesian and intermediate statistics](#bayesian-and-intermediate-statistics)
    -   [forecasting](#forecasting)
    -   [etc](#etc)
-   [engineering](#engineering)
    -   [general data engineering](#general-data-engineering)
        -   [data pipeline](#data-pipeline)
        -   [storage and file types](#storage-and-file-types)
        -   [database internal](#database-internal)
    -   [RDBMS](#rdbms)
        -   [RDBMS Modeling](#rdbms-modeling)
        -   [SQL](#sql)
    -   [scalability](#scalability)
    -   [distribution computing](#distribution-computing)
-   [machine learning](#machine-learning)
-   [MLOps](#mlops)
-   [applied](#applied)
    -   [controlled experiments(대조 실험, A/B 테스팅)](#controlled-experiments대조-실험-ab-테스팅)
        -   [design of experiments(실험 설계)](#design-of-experiments실험-설계)
        -   [online A/B testing](#online-ab-testing)
    -   [causal inference](#causal-inference)
    -   [product growth strategies](#product-growth-strategies)
    -   [financial engineering](#financial-engineering)
-   [etc](#etc-1)
    -   [disclaimer](#disclaimer)
    -   [pre-commit hook](#pre-commit-hook)
    -   [ref](#ref)

![math](./images/math.svg)

# math

## linear algebra

-   [주재걸 교수의 <인공지능을 위한 선형대수> - 노트 필기](./basic-math/linear_algebra/주재걸_선형대수/README.md)
-   [알고리즘으로 배우는 선형대수](./basic-math/linear_algebra/알고리즘으로_배우는_선형대수/README.md)

<details open>
<summary>references</summary>

> -   김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.
> -   Hiraoka, Hori, 이창신, and Hori, Gen. 프로그래머를 위한 선형대수 = Linear Algebra for Programmer / 히라오카 카즈유키, 호리 겐 [공]지음 ; 이창신 옮김 (2017). Print.
> -   인공지능을 위한 선형대수 (https://www.boostcourse.org/ai251)
> -   [Introduction to Linear Algebra for Applied Machine Learning with Python](https://pabloinsente.github.io/intro-linear-algebra)

</details>

## calculus

| Chapter | 요약 |
| ------- | ---- |

<details open>
<summary>references</summary>

> -   김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.
> -   Nagano, and 장진희. 다시 미분 적분 = Try Again, Calculas! / 나가노 히로유키 지음 ; 장진희 옮김 (2019). Print.

</details>

## optimization problem

| Chapter | 요약 |
| ------- | ---- |

<details open>
<summary>references</summary>

> -   -   김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.

</details>

## 엔트로피

<details open>
<summary>references</summary>

> -   김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.

</details>

## basic statistics

| Chapter                                                                     | 요약                                                                                                                |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [자료의 정리](./basic-statistics/01_자료의_정리/README.md)                  | 대표값, skewness, ND, standardization, 기본 통계학의 멘탈 모델에 대해서 배웁니다                                    |
| [상관관계와 회귀 분석](./basic-statistics/02_상관관계와_회귀분석/README.md) | regression equation과 coefficient of determination(결정계수, R)에 대해서 배웁니다                                   |
| [확률과 변동성](./basic-statistics/03_확률과_변동성/README.md)              | 확률, box-model, 기대값과 합의 표준오차, CLT(중심극한정리), 확률적 히스토그램의 정규분포로의 근사에 대해서 배웁니다 |
| [표본추출](./basic-statistics/04_표본추출/README.md)                        | 표본 추출과 표본합, 표본 평균, 표본 합/평균/개수/비율 표준 오차, 신뢰구간에 대해서 배웁니다                         |
| [유의성 검정](./basic-statistics/05_유의성검정/README.md)                   | z-검정, t-검정, p값, run검정, $\chi^2$-검정에 대해서 배웁니다.                                                      |

<details open>

<summary>references</summary>

> -   류근관. 통계학 / 저자: 류근관 (2013).
> -   Bruce, Gedeck, 이준용, Bruce, Andrew, and Gedeck, Peter. 데이터 과학을 위한 통계 / 피터 브루스, 앤드루 브루스, 피터 게데크 지음 ; 이준용 옮김. (2021). Print.
> -   https://dlsun.github.io/probability/

</details>

## bayesian and intermediate statistics

| Chapter                 | 요약                                                                                                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 베이즈 정리             | [링크](./bayesian-statistics/bayes_theorem/bayes.ipynb)                                                                                                    |
| 다양한 분포             | [링크](./bayesian-statistics/distributions/distributions.ipynb)                                                                                            |
| 비율과 수량에 대한 추정 | [비율](./bayesian-statistics/estimating_proportions/estimating_proportions.ipynb), [수량](./bayesian-statistics/estimating_counts/estimating_counts.ipynb) |
| 공산과 가산             | ...                                                                                                                                                        |
| 포아송 과정             | ...                                                                                                                                                        |
| 의사결정분석            | ...                                                                                                                                                        |
| 검정                    | ...                                                                                                                                                        |
| 비교                    | ...                                                                                                                                                        |
| 분류                    | ...                                                                                                                                                        |
| 추론                    | ...                                                                                                                                                        |

<details open>
<summary>references</summary>

> -   Downey, and 권정민. 파이썬을 활용한 베이지안 통계 / 앨런 B. 다우니 지음 ; 권정민 옮김 (2014). Print.
> -   https://allendowney.github.io/ThinkBayes2

</details>

## forecasting

| Chapter | 요약 |
| ------- | ---- |

<details open>
<summary>references</summary>

> -   https://otexts.com/fppkr/

</details>

## etc

| Chapter         | 요약 |
| --------------- | ---- |
| 주성분분석(PCA) | ---- |
| MTS             | ---- |

![engineering](./images/engineering.svg)

# engineering

## general data engineering

### [data pipeline](data-engineering/data_pipeline/README.md)

### [storage and file types](data-engineering/storage/README.md)

### database internal

<details open>
<summary>references</summary>

> -   Densmore, James. Data Pipelines Pocket Reference : Moving and Processing Data for Analytics / James Densmore. 1st ed. 2021. Web.
> -   Introduction to Data Engineering / Daniel Beach (2022)
> -   Petrov, 이우현, and 이태휘. 데이터베이스 인터널스 : 분산 데이터베이스 시스템 심층 분석 / 알렉스 페트로프 지음 ; 이우현 옮김 (2021). Print.

</details>

## RDBMS

### [RDBMS Modeling](rdbms/rdbms/README.md)

### SQL

<details open>
<summary>references</summary>

> -   Introduction to Data Engineering / Daniel Beach (2022)
> -   이기홍, and 곽승주. 데이터베이스 설계와 관계형 이론 : 정규화와 탈정규화를 중심으로 / C. J. 데이트 지음 ; 이기홍, 곽승주 옮김 (2021). Print.
> -   https://www.linkedin.com/pulse/internals-postgresql-chapter-1-urooj-fatima-raza/

</details>

## scalability

<details open>
<summary>references</summary>

> -   https://github.com/binhnguyennus/awesome-scalability

</details>

## distribution computing

<details open>
<summary>references</summary>

> -   Travis Jeffrey. Distributed Services with Go: Your Guide to Reliable, Scalable, and Maintainable Systems

</details>

![ml](./images/ml.svg)

# machine learning

| Chapter                          | 요약         |
| -------------------------------- | ------------ |
| 파이썬 머신러닝 완벽 가이드      | sklearn 활용 |
| 모두를 위한 머신러닝/딥러닝 강의 | 🤡           |
| 모두를 위한 딥러닝 시즌 2        | 🤡           |
| 딥러닝 파이토치 교과서           | 🤡           |

<details open>
<summary>references</summary>

> -   권철민. 파이썬 머신러닝 완벽 가이드 : 다양한 캐글 예제와 함께 기초 알고리즘부터 최신 기법까지 배우 / 권철민 지음 (2022). Print.
> -   서지영. 딥러닝 파이토치 교과서 = Deep Learning with PyTorch / 서지영 지음 (2022). Print.
> -   AI/딥러닝 입문자 학습 가이드. https://www.edwith.org/hellodl101/lecture/103151?isDesc=false.

</details>

# MLOps

| Chapter                                                            | 요약 |
| ------------------------------------------------------------------ | ---- |
| Machine Learning Engineering for Production (MLOps) Specialization | 🤡   |

<details open>
<summary>references</summary>

> -   https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops

</details>

![applied](./images/applied.svg)

# applied

## controlled experiments(대조 실험, A/B 테스팅)

| Chapter | 요약 |
| ------- | ---- |

### [design of experiments(실험 설계)](./controlled-experiments/experiments-design/README.md)

### [online A/B testing](./controlled-experiments/ab-testing/README.md)

<details open>
<summary>references</summary>

> -   Kohavi, Ron, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, and Ya Xu. "Trustworthy Online Controlled Experiments."

</details>

## causal inference

| Chapter | 요약 |
| ------- | ---- |

<details open>
<summary>references</summary>

> -   https://github.com/CausalInferenceLab/Causal-Inference-with-Python

</details>

## product growth strategies

<details open>
<summary>references</summary>

> -   Gold, and 정현지. 고객 리텐션의 전략 : 데이터를 통해 고객 이탈을 막아라 / 칼 골드 ; 정현지 옮김 (2022). Print.

</details>

## financial engineering

<details open>
<summary>references</summary>

</details>

# etc

<details>
<summary>etc</summary>

### disclaimer

no typing

### pre-commit hook

```bash
pre-commit install
pre-commit run --all-files # in case you want to run it on all files
```

### ref

> -   http://norman3.github.io/prml/docs/chapter02/3_1

</details>
