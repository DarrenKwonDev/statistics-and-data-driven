## ๐จ this document is in progress

![logo](./images/logo.svg)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [math](#math)
  - [linear algebra](#linear-algebra)
  - [calculus](#calculus)
  - [optimization problem](#optimization-problem)
  - [์ํธ๋กํผ](#์ํธ๋กํผ)
  - [basic statistics](#basic-statistics)
  - [bayesian and intermediate statistics](#bayesian-and-intermediate-statistics)
  - [forecasting](#forecasting)
- [engineering](#engineering)
  - [general data engineering](#general-data-engineering)
    - [data pipeline](#data-pipeline)
    - [storage and file types](#storage-and-file-types)
    - [database internal](#database-internal)
  - [RDBMS](#rdbms)
    - [RDBMS Modeling](#rdbms-modeling)
    - [SQL](#sql)
  - [scalability](#scalability)
  - [distribution computing](#distribution-computing)
- [machine learning](#machine-learning)
- [applied](#applied)
  - [controlled experiments(๋์กฐ ์คํ, A/B ํ์คํ)](#controlled-experiments๋์กฐ-์คํ-ab-ํ์คํ)
    - [design of experiments(์คํ ์ค๊ณ)](#design-of-experiments์คํ-์ค๊ณ)
    - [online A/B testing](#online-ab-testing)
  - [causal inference](#causal-inference)
  - [product growth strategies](#product-growth-strategies)
  - [financial engineering](#financial-engineering)
- [etc](#etc)
    - [disclaimer](#disclaimer)
    - [pre-commit hook](#pre-commit-hook)
    - [ref](#ref)

![math](./images/math.svg)

# math

## linear algebra

-   [์ฃผ์ฌ๊ฑธ ๊ต์์ <์ธ๊ณต์ง๋ฅ์ ์ํ ์ ํ๋์> ๋ธํธ ํ๊ธฐ](./basic-math/linear_algebra/์ฃผ์ฌ๊ฑธ_์ ํ๋์/README.md)

<details open>
<summary>references</summary>

> ๊น๋ํ. (๊น๋ํ์) ๋ฐ์ดํฐ ์ฌ์ด์ธ์ค ์ค์ฟจ : ์ํํธ / ๊น๋ํ ์ง์ (2019). Print.  
> Hiraoka, Hori, ์ด์ฐฝ์ , and Hori, Gen. ํ๋ก๊ทธ๋๋จธ๋ฅผ ์ํ ์ ํ๋์ = Linear Algebra for Programmer / ํ๋ผ์ค์นด ์นด์ฆ์ ํค, ํธ๋ฆฌ ๊ฒ [๊ณต]์ง์ ; ์ด์ฐฝ์  ์ฎ๊น (2017). Print.
> ์ธ๊ณต์ง๋ฅ์ ์ํ ์ ํ๋์ (https://www.boostcourse.org/ai251)

</details>

## calculus

| Chapter | ์์ฝ |
| ------- | ---- |

<details open>
<summary>references</summary>

> ๊น๋ํ. (๊น๋ํ์) ๋ฐ์ดํฐ ์ฌ์ด์ธ์ค ์ค์ฟจ : ์ํํธ / ๊น๋ํ ์ง์ (2019). Print.  
> Nagano, and ์ฅ์งํฌ. ๋ค์ ๋ฏธ๋ถ ์ ๋ถ = Try Again, Calculas! / ๋๊ฐ๋ธ ํ๋ก์ ํค ์ง์ ; ์ฅ์งํฌ ์ฎ๊น (2019). Print.

</details>

## optimization problem

| Chapter | ์์ฝ |
| ------- | ---- |

<details open>
<summary>references</summary>

> ๊น๋ํ. (๊น๋ํ์) ๋ฐ์ดํฐ ์ฌ์ด์ธ์ค ์ค์ฟจ : ์ํํธ / ๊น๋ํ ์ง์ (2019). Print.

</details>

## ์ํธ๋กํผ

<details open>
<summary>references</summary>

> ๊น๋ํ. (๊น๋ํ์) ๋ฐ์ดํฐ ์ฌ์ด์ธ์ค ์ค์ฟจ : ์ํํธ / ๊น๋ํ ์ง์ (2019). Print.

</details>

## basic statistics

| Chapter                                                                     | ์์ฝ                                                                                                                |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [์๋ฃ์ ์ ๋ฆฌ](./basic-statistics/01_์๋ฃ์_์ ๋ฆฌ/README.md)                  | ๋ํ๊ฐ, skewness, ND, standardization, ๊ธฐ๋ณธ ํต๊ณํ์ ๋ฉํ ๋ชจ๋ธ์ ๋ํด์ ๋ฐฐ์๋๋ค                                    |
| [์๊ด๊ด๊ณ์ ํ๊ท ๋ถ์](./basic-statistics/02_์๊ด๊ด๊ณ์_ํ๊ท๋ถ์/README.md) | regression equation๊ณผ coefficient of determination(๊ฒฐ์ ๊ณ์, R)์ ๋ํด์ ๋ฐฐ์๋๋ค                                   |
| [ํ๋ฅ ๊ณผ ๋ณ๋์ฑ](./basic-statistics/03_ํ๋ฅ ๊ณผ_๋ณ๋์ฑ/README.md)              | ํ๋ฅ , box-model, ๊ธฐ๋๊ฐ๊ณผ ํฉ์ ํ์ค์ค์ฐจ, CLT(์ค์ฌ๊ทนํ์ ๋ฆฌ), ํ๋ฅ ์  ํ์คํ ๊ทธ๋จ์ ์ ๊ท๋ถํฌ๋ก์ ๊ทผ์ฌ์ ๋ํด์ ๋ฐฐ์๋๋ค |
| [ํ๋ณธ์ถ์ถ](./basic-statistics/04_ํ๋ณธ์ถ์ถ/README.md)                        | ํ๋ณธ ์ถ์ถ๊ณผ ํ๋ณธํฉ, ํ๋ณธ ํ๊ท , ํ๋ณธ ํฉ/ํ๊ท /๊ฐ์/๋น์จ ํ์ค ์ค์ฐจ, ์ ๋ขฐ๊ตฌ๊ฐ์ ๋ํด์ ๋ฐฐ์๋๋ค                         |
| [์ ์์ฑ ๊ฒ์ ](./basic-statistics/05_์ ์์ฑ๊ฒ์ /README.md)                   | z-๊ฒ์ , t-๊ฒ์ , p๊ฐ, run๊ฒ์ , $\chi^2$-๊ฒ์ ์ ๋ํด์ ๋ฐฐ์๋๋ค.                                                      |

<details open>

<summary>references</summary>

> ๋ฅ๊ทผ๊ด. ํต๊ณํ / ์ ์: ๋ฅ๊ทผ๊ด (2013).  
> Bruce, Gedeck, ์ด์ค์ฉ, Bruce, Andrew, and Gedeck, Peter. ๋ฐ์ดํฐ ๊ณผํ์ ์ํ ํต๊ณ / ํผํฐ ๋ธ๋ฃจ์ค, ์ค๋๋ฃจ ๋ธ๋ฃจ์ค, ํผํฐ ๊ฒ๋ฐํฌ ์ง์ ; ์ด์ค์ฉ ์ฎ๊น. (2021). Print.  
> https://dlsun.github.io/probability/

</details>

## bayesian and intermediate statistics

| Chapter                 | ์์ฝ |
| ----------------------- | ---- |
| ๋ฒ ์ด์ฆ ์ ๋ฆฌ             | ...  |
| ๋ค์ํ ๋ถํฌ             | ...  |
| ๋น์จ๊ณผ ์๋์ ๋ํ ์ถ์  | ...  |
| ๊ณต์ฐ๊ณผ ๊ฐ์ฐ             | ...  |
| ํฌ์์ก ๊ณผ์              | ...  |
| ์์ฌ๊ฒฐ์ ๋ถ์            | ...  |
| ๊ฒ์                     | ...  |
| ๋น๊ต                    | ...  |
| ๋ถ๋ฅ                    | ...  |
| ์ถ๋ก                     | ...  |

<details open>
<summary>references</summary>

> Downey, and ๊ถ์ ๋ฏผ. ํ์ด์ฌ์ ํ์ฉํ ๋ฒ ์ด์ง์ ํต๊ณ / ์จ๋ฐ B. ๋ค์ฐ๋ ์ง์ ; ๊ถ์ ๋ฏผ ์ฎ๊น (2014). Print.  
> https://allendowney.github.io/ThinkBayes2

</details>

## forecasting

| Chapter | ์์ฝ |
| ------- | ---- |

<details open>
<summary>references</summary>

> https://otexts.com/fppkr/

</details>

![engineering](./images/engineering.svg)

# engineering

## general data engineering

### [data pipeline](data-engineering/data_pipeline/README.md)

### [storage and file types](data-engineering/storage/README.md)

### database internal

<details open>
<summary>references</summary>

> Densmore, James. Data Pipelines Pocket Reference : Moving and Processing Data for Analytics / James Densmore. 1st ed. 2021. Web.  
> Introduction to Data Engineering / Daniel Beach (2022)  
> Petrov, ์ด์ฐํ, and ์ดํํ. ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ธํฐ๋์ค : ๋ถ์ฐ ๋ฐ์ดํฐ๋ฒ ์ด์ค ์์คํ ์ฌ์ธต ๋ถ์ / ์๋ ์ค ํํธ๋กํ ์ง์ ; ์ด์ฐํ ์ฎ๊น (2021). Print.

</details>

## RDBMS

### [RDBMS Modeling](rdbms/rdbms/README.md)

### SQL

<details open>
<summary>references</summary>

> Introduction to Data Engineering / Daniel Beach (2022)  
> ์ด๊ธฐํ, and ๊ณฝ์น์ฃผ. ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ค๊ณ์ ๊ด๊ณํ ์ด๋ก  : ์ ๊ทํ์ ํ์ ๊ทํ๋ฅผ ์ค์ฌ์ผ๋ก / C. J. ๋ฐ์ดํธ ์ง์ ; ์ด๊ธฐํ, ๊ณฝ์น์ฃผ ์ฎ๊น (2021). Print.  
> https://www.linkedin.com/pulse/internals-postgresql-chapter-1-urooj-fatima-raza/

</details>

## scalability

<details open>
<summary>references</summary>

> https://github.com/binhnguyennus/awesome-scalability

</details>

## distribution computing

<details open>
<summary>references</summary>

> Travis Jeffrey. Distributed Services with Go: Your Guide to Reliable, Scalable, and Maintainable Systems

</details>

![ml](./images/ml.svg)

# machine learning

| Chapter | ์์ฝ |
| ------- | ---- |

<details open>
<summary>references</summary>

</details>

![applied](./images/applied.svg)

# applied

## controlled experiments(๋์กฐ ์คํ, A/B ํ์คํ)

| Chapter | ์์ฝ |
| ------- | ---- |

### [design of experiments(์คํ ์ค๊ณ)](./controlled-experiments/experiments-design/README.md)

### [online A/B testing](./controlled-experiments/ab-testing/README.md)

<details open>
<summary>references</summary>

> Kohavi, Ron, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, and Ya Xu. "Trustworthy Online Controlled Experiments."

</details>

## causal inference

| Chapter | ์์ฝ |
| ------- | ---- |

<details open>
<summary>references</summary>

> https://github.com/CausalInferenceLab/Causal-Inference-with-Python

</details>

## product growth strategies

<details open>
<summary>references</summary>

> Gold, and ์ ํ์ง. ๊ณ ๊ฐ ๋ฆฌํ์์ ์ ๋ต : ๋ฐ์ดํฐ๋ฅผ ํตํด ๊ณ ๊ฐ ์ดํ์ ๋ง์๋ผ / ์นผ ๊ณจ๋ ; ์ ํ์ง ์ฎ๊น (2022). Print.

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

> http://norman3.github.io/prml/docs/chapter02/3_1

</details>
