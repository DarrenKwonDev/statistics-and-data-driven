<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->
<!-- /code_chunk_output -->

## 01 자료의 정리

### 관측 자료의 종류

- 횡단면 자료(cross-section data) : 한 시점 여러 개체
- 시계열 자료(time-series data) : 한 개체 여러 시점

  - 시계열 데이터 분석은 크게 ‘추세', ‘주기', ‘계절성'으로 구분하여 분석함
    - 추세 : 장기적으로 늘어나거나 줄어드는 형태
    - 주기 : 고정된 시간 단위로 나타나는 유사한 변동 형태
    - 계절성 : 주기적으로 반복되는 때에 어떤 사건이 발생하는 것 (ex 빼빼로데이)

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
density = \frac{frequency}{sub\,interval} \\
\sum{density \times class\,interval} = 1
$$

## 평균과 표준편차(SD)

### 평균과 분포

중심 -> mean(평균), median(중앙값)
분포 -> SD(standard deviation), 사분위수 범위(interquartile range)

이 두 지표만 가지고 히스토그램을 분석할 수는 없다. peak이 2개란 히스토그램의 형태도 존재하는 등.
그러나 이 둘이 제일 잘 활용되는 지표

### 평균, 중앙값, 최빈값, RMS : 무엇이 대표값인가?

1. 평균(mean)

$$
\overline{X}={X_1+X_2+...+X_n \over n}={1 \over n}\sum_{i=1}^{n}X_i
$$

2. 중앙값(median) -> sorting한 후의 중앙값

3. 최빈값(mode)

- 평균값과 중앙값은 같은 값일 될수도 아닐수도 있다. 보통 아니지.
- 평균과 중앙값의 차이가 크면 분석 목적과 자료 특성에 맞게 적당한 대표값을 선택해야 함.

4. root mean square(RMS) -> 통계학자들이 쓰는 대표값

$$
\sqrt{\frac{\sum_{i=1}^{k}{(x_i - mean)^2}}{k}}
$$

- 수학적으로 모든 숫자가 같은 경우 제외하곤 mean < RMS
- 개별 값 - mean 을 '편차'(deviation)이라 함

### SD : 평균으로 부터 퍼진 정도

앞서 편차(deviation)을 `개별 값 - mean`이라 정의함
표준편차(standard deviation)은 편차의 정도를 측정하는 값이다.

$$
S=\sqrt{\frac{\sum_{i=1}^{n}(X_i-\overline{X})^2}{n-1}}
$$

- RMS와 비슷하지만 분모가 n-1이다. 이는 표준편차를 구할 때의 자유도(degrees of freedom)이다.
- 표준 편차는 원래 자료들의 RMS가 아니라 평균으로부터 떨어진 편차들의 대략적 RMS를 의미한다.
- 분산(variance)

  - 편차(deviation)의 제곱의 합
  - 분산에 루트 씌우면 그게 SD임. 제곱했으니까 값이 너무 커졌으니 루트를 씌운 것. 반대로, 표준 편차 제곱하면 그게 분산임
  - 계산에 표준편차가 더 편하다. 그래서 표준편차를 많이 씀.

- 68-95 법칙
  - mean $\pm$ 1SD : 68%
  - mean $\pm$ 2SD : 95%
  - 대부분의 숫자가 평균에서 2SD 범위 안에 있음을 의미

## 측정 오차

(개별 관측치) = (실제의 값) + (편의, bias) + (측정오차)

- 실제 값이 상수이므로 bias가 없다는 전제 하에는 반복 측정을 통한 관측치의 SD는 측정오차의 SD와 같게 된다. 즉, SD는 측정오차의 정도를 나타내기도 한다.
- bias가 없다면 반복 측정을 통해 얻어진 측정치들의 평균은 실제값에 수렴한다.
- 그러나 bias가 존재한다면 지속적으로 측정을 반복하더라도 실제값에 수렴하지 않는다.

## glossary

- 모집단(population)
- 모수(parameter) 모집단의 수치적 요약값. 모집단의 모SD, 모평균 값 등이 모수임. 그냥 무의미하게 전체 수를 ‘모수'라 부르는 경우가 있는데 이는 틀린 것임
- 표본(sample) 모집단으로부터 sampling
- 통계량(statistic) 표본으로부터의 수치적 요약값
- 추론(inference) 표본으로 부터 모집단의 특성을 추론하는 것으로 표본이 충분히 크기 때문에 근사한다는 `큰 수의 법칙`에 의하여 추론 가능
- 렉시스 도표(Lexis diagram) : 출생집단별로 시간에 따른 나이 변화를 보여주는 도표
