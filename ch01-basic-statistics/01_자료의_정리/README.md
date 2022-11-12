<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->
<!-- /code_chunk_output -->

## 01 자료의 정리

### 관측 자료의 종류

- 횡단면 자료(cross-section data) : 한 시점 여러 개체
- 시계열 자료(time-series data) : 한 개체 여러 시점
- 종작 자료, 패널 자료(longitudinal data, panel data) : 여러 개체 여러 시점

### 변수

- 양적 변수(quantitative variable)
  - 이산적(discrete)
  - 연속적(continuous)
- 질적 변수(qualitative variable)
  - categorial 하게 나누어 분석함. (ex. 성별, 종교, 직업, 국적 등) 따라서 이산적 변수에 해당 됨

### 실험연구와 경험적 연구

- 실험연구(experimental research)
  - treatment group(처리 집단), control group(통제 집단)
  - 집단 간 무작위 배정(random assignment) 필요
  - double blindness(이중 블라인드) : 실험자와 대상자 모두 실험의 목적을 알지 못하는 상태
  - randomized controlled double blind experiment(랜덤화된 통제된 이중 블라인드 실험)위 두 요소를 둘다 갖춘 실험 방법
- 경험적 연구(observation research)
  - 자연적으로 발생하는 현상을 연구자가 임의로 분석하는 것으로, 관련성은 알 수 있지만 그것이 causation(인과관계)인지 알 수 없음
  - 혼동 요인(confounding factor) : 결과에 영향을 미치는 제 3의 요인
  - 혼동 요인에 대한 통제를 위해서 작고 동질적인 하위 집단으로 나누어 연구하는 것이 필요

## 02 히스토그램

### 개괄

- 경계값에 대한 처리는 보통 좌폐구간 우개구간 형태 [a,b), 즉, a 이상 b 미만 꼴로 처리함.
- 블록의 밑변을 이루고 있는 구간을 계급구간(class interval)이라고 함.
- 히스토그램에서는 블록의 `면적`이 비율을 나타냄

### 히스토그램 작성과 해석

- 구간별 자료의 분포를 테이블로 그린 후 시각화하면 됨
  - distribution table -> 계급 구간에 속하는 자료의 갯수를 표로 나타냄
- 구간별 자료의 수를 frequency, 비율로는 relative frequency라 함
- 계급 구간은 자료가 많은 곳에는 좁게 잡고 듬성듬성한 곳에는 넓게 잡는 것이 좋음
- 가로축을 실제 구간의 폭에 비례하도록 그려야 함. 값의 차이에 비례하지 않고 동일한 간격으로 그릴 경우 혼동을 줄 수 있음
- 각 계급 구간의 부분 구간(계급 구간의 가장 작은 단위, sub-interval)으로 frequency을 나눠서 높이를 그려야 블록의 `면적`이 실제 데이터의 크기를 나타나게 됨
  - 이 때, 높이는 부분 구간에 속한 자료의 비율, 즉, `밀도(density scale)`를 나타냄. 걍 직관적으로 일상 용어처럼 받아들이면 이해됨.

$$
density = \frac{frequency}{sub\_interval}  \\
\sum{density * class\_interval} = 1
$$

## glossary

- 모집단(population)
- 모수(parameter) 모집단의 수치적 요약값. 모집단의 모SD, 모평균 값 등이 모수임. 그냥 무의미하게 전체 수를 ‘모수'라 부르는 경우가 있는데 이는 틀린 것임
- 표본(sample) 모집단으로부터 sampling
- 통계량(statistic) 표본으로부터의 수치적 요약값
- 추론(inference) 표본으로 부터 모집단의 특성을 추론하는 것으로 표본이 충분히 크기 때문에 근사한다는 `큰 수의 법칙`에 의하여 추론 가능
- 렉시스 도표(Lexis diagram) : 출생집단별로 시간에 따른 나이 변화를 보여주는 도표
