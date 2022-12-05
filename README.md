<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [statistics-and-data-driven](#statistics-and-data-driven)
  - [basic math](#basic-math)
    - [01 numpy와 선형대수](#01-numpy와-선형대수)
    - [02 sympy와 미적분](#02-sympy와-미적분)
    - [03 scipy와 Optimization Problem](#03-scipy와-optimization-problem)
    - [04 확률변수와 상관관계](#04-확률변수와-상관관계)
    - [05 확률 분포](#05-확률-분포)
    - [06 추정과 검정](#06-추정과-검정)
    - [07 엔트로피](#07-엔트로피)
  - [basic statistics](#basic-statistics)
    - [01 자료의 정리](#01-자료의-정리)
    - [02 상관관계와 회귀 분석](#02-상관관계와-회귀-분석)
    - [03 확률과 변동성](#03-확률과-변동성)
    - [04 표본추출](#04-표본추출)
    - [05 유의성 검정](#05-유의성-검정)
  - [bayesian statistics](#bayesian-statistics)
  - [controlled experiments](#controlled-experiments)
  - [machine learning](#machine-learning)
  - [database internal](#database-internal)
  - [RDBMS design \& relationship theory](#rdbms-design--relationship-theory)
    - [RDBMS Modeling](#rdbms-modeling)
  - [general data engineering \& self-service](#general-data-engineering--self-service)
    - [data pipeline](#data-pipeline)
    - [SQL](#sql)
  - [distribution computing](#distribution-computing)
  - [financial engineering](#financial-engineering)
  - [doc-culture](#doc-culture)
  - [etc](#etc)
    - [disclaimer](#disclaimer)
    - [highschool math](#highschool-math)
    - [pre-commit hook](#pre-commit-hook)
    - [ref](#ref)
    - [glossary](#glossary)

<!-- /code_chunk_output -->

# statistics-and-data-driven

데이터 관련 직군 현업자들과 함께한 스터디 + 문서 주도 문화를 도입하기 위한 시도와 그 기록

---

## basic math

### 01 numpy와 선형대수

### 02 sympy와 미적분

### 03 scipy와 Optimization Problem

### 04 확률변수와 상관관계

### 05 확률 분포

### 06 추정과 검정

### 07 엔트로피

<details open>
<summary>references</summary>

> 김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.  
> Hiraoka, Hori, 이창신, and Hori, Gen. 프로그래머를 위한 선형대수 = Linear Algebra for Programmer / 히라오카 카즈유키, 호리 겐 [공]지음 ; 이창신 옮김 (2017). Print.  
> Nagano, and 장진희. 다시 미분 적분 = Try Again, Calculas! / 나가노 히로유키 지음 ; 장진희 옮김 (2019). Print.  
> Nakai, and 이기홍. 프로그래머를 위한 기초 해석학 = Basic Analysis for Programmers / 나카이 에츠지 지음 ; 이기홍 옮김 (2018). Print.

</details>

## basic statistics

### [01 자료의 정리](./ch01-basic-statistics/01_자료의_정리/README.md)

### [02 상관관계와 회귀 분석](./ch01-basic-statistics/02_상관관계와_회귀분석/README.md)

### [03 확률과 변동성](./ch01-basic-statistics/03_확률과_변동성/README.md)

### [04 표본추출](./ch01-basic-statistics/04_표본추출/README.md)

### 05 유의성 검정

<details open>

<summary>references</summary>

> 류근관. 통계학 / 저자: 류근관 (2013).  
> Bruce, Gedeck, 이준용, Bruce, Andrew, and Gedeck, Peter. 데이터 과학을 위한 통계 / 피터 브루스, 앤드루 브루스, 피터 게데크 지음 ; 이준용 옮김. (2021). Print.

</details>

## bayesian statistics

<details open>
<summary>references</summary>

</details>

## controlled experiments

<details open>
<summary>references</summary>

> Kohavi, Ron, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, and Ya Xu. "Trustworthy Online Controlled Experiments."

</details>

## machine learning

<details open>
<summary>references</summary>

</details>

---

## database internal

<details open>
<summary>references</summary>

> Petrov, 이우현, and 이태휘. 데이터베이스 인터널스 : 분산 데이터베이스 시스템 심층 분석 / 알렉스 페트로프 지음 ; 이우현 옮김 (2021). Print.

</details>

## RDBMS design & relationship theory

### RDBMS Modeling

<details open>
<summary>references</summary>

> Introduction to Data Engineering / Daniel Beach (2022)
> 이기홍, and 곽승주. 데이터베이스 설계와 관계형 이론 : 정규화와 탈정규화를 중심으로 / C. J. 데이트 지음 ; 이기홍, 곽승주 옮김 (2021). Print.

</details>

## general data engineering & self-service

### data pipeline

### SQL

<details open>
<summary>references</summary>

> Introduction to Data Engineering / Daniel Beach (2022)

</details>

## distribution computing

<details open>
<summary>references</summary>

> Travis Jeffrey. Distributed Services with Go: Your Guide to Reliable, Scalable, and Maintainable Systems

</details>

---

## financial engineering

<details open>
<summary>references</summary>

</details>

---

## doc-culture

조직에 문서 주도 문화를 도입하기 위한 자료들입니다.
비효율적인 회의를 줄이고, 문서를 통해 효율적인 의사소통을 할 수 있도록 도와줍니다.

사실 문서 주도에 대한 제 생각들은 처음부터 있었던 것은 아닙니다.
조직에 data-driven한 조직 문화를 만들고자 했지만 data를 제공해도 구성원이 해당 내용을 읽지 않으면 아무 소용이 없다는 경험 이후에 생각하게 된 개인적인 문화, 방법론입니다.

즉, data-driven 이전에 문서 위주의 문화를 조성해야 한다는 생각입니다.

[digital gardening?](https://github.com/MaggieAppleton/digital-gardeners)  
[바로가기](./ch06-doc-culture/README.md)

---

## etc

### disclaimer

no typing

### highschool math

별도로 설명하지는 않겠지만 아래 내용을 알고 있어야 한다.

- 고1) 다항식, 인수분해, 이차함수, 복소수, 원, 직선의 이동, 집합론
- 수1) 제곱, 로그, 삼각함수, 수열
- 수2) 극한, 기초 미적분
- 확통) 기초 확률론, 정규 분포

### pre-commit hook

```bash
pre-commit install
pre-commit run --all-files # in case you want to run it on all files
```

### ref

> http://norman3.github.io/prml/docs/chapter02/3_1

### glossary
