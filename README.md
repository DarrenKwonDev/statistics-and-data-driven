## 🚨 this document is in progress

![logo](./images/logo.svg)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [math](#math)
  - [basic math](#basic-math)
    - [선형대수](#선형대수)
    - [미적분](#미적분)
    - [Optimization Problem](#optimization-problem)
    - [엔트로피](#엔트로피)
  - [basic statistics](#basic-statistics)
    - [자료의 정리](#자료의-정리)
    - [상관관계와 회귀 분석](#상관관계와-회귀-분석)
    - [확률과 변동성](#확률과-변동성)
    - [표본추출](#표본추출)
    - [유의성 검정](#유의성-검정)
  - [bayesian statistics](#bayesian-statistics)
  - [controlled experiments(대조 실험, A/B 테스팅)](#controlled-experiments대조-실험-ab-테스팅)
    - [design of experiments(실험 설계)](#design-of-experiments실험-설계)
    - [online A/B testing](#online-ab-testing)
  - [causal inference](#causal-inference)
  - [forecasting](#forecasting)
  - [machine learning](#machine-learning)
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
- [applied](#applied)
  - [product growth strategies](#product-growth-strategies)
  - [financial engineering](#financial-engineering)
  - [doc-culture](#doc-culture)
- [etc](#etc)
  - [disclaimer](#disclaimer)
  - [pre-commit hook](#pre-commit-hook)
  - [ref](#ref)

![math](./images/math.svg)

# math

## basic math

### 선형대수

### 미적분

### Optimization Problem

### 엔트로피

<details open>
<summary>references</summary>

> 김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.  
> Hiraoka, Hori, 이창신, and Hori, Gen. 프로그래머를 위한 선형대수 = Linear Algebra for Programmer / 히라오카 카즈유키, 호리 겐 [공]지음 ; 이창신 옮김 (2017). Print.  
> Nagano, and 장진희. 다시 미분 적분 = Try Again, Calculas! / 나가노 히로유키 지음 ; 장진희 옮김 (2019). Print.  
> Nakai, and 이기홍. 프로그래머를 위한 기초 해석학 = Basic Analysis for Programmers / 나카이 에츠지 지음 ; 이기홍 옮김 (2018). Print.  
> https://sites.google.com/mensakorea.org/math/%EC%B7%A8%EB%AF%B8%EB%A1%9C-%EC%88%98%ED%95%99%ED%95%98%EC%9E%90?authuser=0  
> https://dlsun.github.io/probability/

</details>

## basic statistics

### [자료의 정리](./ch01-basic-statistics/01_자료의_정리/README.md)

대표값, skewness, ND, standardization, 기본 통계학의 멘탈 모델에 대해서 배웁니다

### [상관관계와 회귀 분석](./ch01-basic-statistics/02_상관관계와_회귀분석/README.md)

regression equation과 coefficient of determination(결정계수, R)에 대해서 배웁니다

### [확률과 변동성](./ch01-basic-statistics/03_확률과_변동성/README.md)

확률, box-model, 기대값과 합의 표준오차, CLT(중심극한정리), 확률적 히스토그램의 정규분포로의 근사에 대해서 배웁니다

### [표본추출](./ch01-basic-statistics/04_표본추출/README.md)

표본 추출과 표본합, 표본 평균, 표본 합/평균/개수/비율 표준 오차, 신뢰구간에 대해서 배웁니다

### [유의성 검정](./ch01-basic-statistics/05_유의성검정/README.md)

z-검정, t-검정, p값, run검정, $\chi^2$-검정에 대해서 배웁니다.

<details open>

<summary>references</summary>

> 류근관. 통계학 / 저자: 류근관 (2013).  
> Bruce, Gedeck, 이준용, Bruce, Andrew, and Gedeck, Peter. 데이터 과학을 위한 통계 / 피터 브루스, 앤드루 브루스, 피터 게데크 지음 ; 이준용 옮김. (2021). Print.  
> https://dlsun.github.io/probability/

</details>

## bayesian statistics

<details open>
<summary>references</summary>

</details>

## controlled experiments(대조 실험, A/B 테스팅)

### [design of experiments(실험 설계)](./controlled-experiments/experiments-design/README.md)

### [online A/B testing](./controlled-experiments/ab-testing/README.md)

<details open>
<summary>references</summary>

> Kohavi, Ron, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, and Ya Xu. "Trustworthy Online Controlled Experiments."

</details>

## causal inference

<details open>
<summary>references</summary>

> https://github.com/CausalInferenceLab/Causal-Inference-with-Python

</details>

## forecasting

<details open>
<summary>references</summary>

> https://otexts.com/fppkr/

</details>

## machine learning

<details open>
<summary>references</summary>

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
> Petrov, 이우현, and 이태휘. 데이터베이스 인터널스 : 분산 데이터베이스 시스템 심층 분석 / 알렉스 페트로프 지음 ; 이우현 옮김 (2021). Print.

</details>

## RDBMS

### [RDBMS Modeling](rdbms/rdbms/README.md)

### SQL

<details open>
<summary>references</summary>

> Introduction to Data Engineering / Daniel Beach (2022)  
> 이기홍, and 곽승주. 데이터베이스 설계와 관계형 이론 : 정규화와 탈정규화를 중심으로 / C. J. 데이트 지음 ; 이기홍, 곽승주 옮김 (2021). Print.  
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

![applied](./images/applied.svg)

# applied

모두 DDDM(Data driven decision making)의 일부입니다.

## product growth strategies

<details open>
<summary>references</summary>

> Gold, and 정현지. 고객 리텐션의 전략 : 데이터를 통해 고객 이탈을 막아라 / 칼 골드 ; 정현지 옮김 (2022). Print.

</details>

## financial engineering

<details open>
<summary>references</summary>

</details>

## doc-culture

조직에 문서 주도 문화를 도입하기 위한 자료들입니다.
비효율적인 회의를 줄이고, 문서를 통해 효율적인 의사소통을 할 수 있도록 도와줍니다.

사실 문서 주도에 대한 제 생각들은 처음부터 있었던 것은 아닙니다.
조직에 data-driven한 조직 문화를 만들고자 했지만 data를 제공해도 구성원이 해당 내용을 읽지 않으면 아무 소용이 없다는 경험 이후에 생각하게 된 개인적인 문화, 방법론입니다.

즉, data-driven 이전에 문서 위주의 문화를 조성해야 한다는 생각입니다.

[digital gardening](https://github.com/MaggieAppleton/digital-gardeners)  
[바로가기](./ch06-doc-culture/README.md)

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
