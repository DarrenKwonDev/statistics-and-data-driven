<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [statistics-and-data-driven](#statistics-and-data-driven)
  - [ch00. basic math](#ch00-basic-math)
    - [01 numpy와 선형대수](#01-numpy와-선형대수)
    - [02 sympy와 미적분](#02-sympy와-미적분)
    - [03 scipy와 최적화](#03-scipy와-최적화)
    - [04 확률변수와 상관관계](#04-확률변수와-상관관계)
    - [05 확률 분포](#05-확률-분포)
    - [06 추정과 검정](#06-추정과-검정)
    - [07 엔트로피](#07-엔트로피)
    - [ref](#ref)
  - [ch01. basic statistics](#ch01-basic-statistics)
    - [01 자료의 정리](#01-자료의-정리)
    - [02 상관관계와 회귀 분석](#02-상관관계와-회귀-분석)
    - [03 확률과 변동성](#03-확률과-변동성)
    - [04 표본추출](#04-표본추출)
    - [05 유의성 검정](#05-유의성-검정)
    - [ref](#ref-1)
  - [ch02. bayesian statistics](#ch02-bayesian-statistics)
    - [ref](#ref-2)
  - [ch03. controlled experiments](#ch03-controlled-experiments)
    - [ref](#ref-3)
  - [ch04. machine learning](#ch04-machine-learning)
    - [ref](#ref-4)
  - [ch05. database internal](#ch05-database-internal)
    - [ref](#ref-5)
  - [ch06. RDBMS design & relationship theory](#ch06-rdbms-design--relationship-theory)
    - [ref](#ref-6)
  - [ch07. general data engineering & self-service](#ch07-general-data-engineering--self-service)
    - [ref](#ref-7)
  - [ch08. doc-culture](#ch08-doc-culture)
  - [ch09. financial engineering](#ch09-financial-engineering)
    - [ref](#ref-8)
  - [etc](#etc)
    - [disclaimer](#disclaimer)
    - [pre-commit hook](#pre-commit-hook)
    - [glossary](#glossary)

<!-- /code_chunk_output -->

# statistics-and-data-driven

데이터 관련 직군 현업자들과 함께한 스터디 + 문서 주도 문화를 도입하기 위한 시도와 그 기록

## ch00. basic math

### 01 numpy와 선형대수

### 02 sympy와 미적분

### 03 scipy와 최적화

### 04 확률변수와 상관관계

### 05 확률 분포

### 06 추정과 검정

### 07 엔트로피

### ref

> 김도형. (김도형의) 데이터 사이언스 스쿨 : 수학편 / 김도형 지음 (2019). Print.

## ch01. basic statistics

### [01 자료의 정리](./ch01-basic-statistics/01_자료의_정리/README.md)

### [02 상관관계와 회귀 분석](./ch01-basic-statistics/02_상관관계와_회귀분석/README.md)

### [03 확률과 변동성](./ch01-basic-statistics/03_확률과_변동성/README.md)

### 04 표본추출

### 05 유의성 검정

### ref

> 류근관. 통계학 / 저자: 류근관 (2013).
> Bruce, Gedeck, 이준용, Bruce, Andrew, and Gedeck, Peter. 데이터 과학을 위한 통계 / 피터 브루스, 앤드루 브루스, 피터 게데크 지음 ; 이준용 옮김. (2021). Print.

## ch02. bayesian statistics

### ref

## ch03. controlled experiments

### ref

> Kohavi, Ron, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, and Ya Xu. "Trustworthy Online Controlled Experiments."

## ch04. machine learning

### ref

## ch05. database internal

### ref

> Petrov, 이우현, and 이태휘. 데이터베이스 인터널스 : 분산 데이터베이스 시스템 심층 분석 / 알렉스 페트로프 지음 ; 이우현 옮김 (2021). Print.

## ch06. RDBMS design & relationship theory

### ref

> Date, 이기홍, and 곽승주. 데이터베이스 설계와 관계형 이론 : 정규화와 탈정규화를 중심으로 / C. J. 데이트 지음 ; 이기홍, 곽승주 옮김 (2021). Print.

## ch07. general data engineering & self-service

### ref

## ch08. doc-culture

조직에 문서 주도 문화를 도입하기 위한 자료들입니다.
비효율적인 회의를 줄이고, 문서를 통해 효율적인 의사소통을 할 수 있도록 도와줍니다.

사실 문서 주도에 대한 제 생각들은 처음부터 있었던 것은 아닙니다.
조직에 data-driven한 조직 문화를 만들고자 했지만 data를 제공해도 구성원이 해당 내용을 읽지 않으면 아무 소용이 없다는 경험 이후에 생각하게 된 개인적인 문화, 방법론입니다.

즉, data-driven 이전에 문서 위주의 문화를 조성해야 한다는 생각입니다.

[바로가기](./ch06-doc-culture/README.md)

## ch09. financial engineering

### ref

## etc

### disclaimer

no typing

### pre-commit hook

```bash
pre-commit install
pre-commit run --all-files # in case you want to run it on all files
```

### glossary
