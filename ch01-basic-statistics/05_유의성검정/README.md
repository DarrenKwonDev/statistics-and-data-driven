<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [01 유의성 검정(significance test) 일반](#01-유의성-검정significance-test-일반)
  - [귀무 가설(영 가설)과 대립 가설](#귀무-가설영-가설과-대립-가설)
  - [z검정과 p값](#z검정과-p값)
    - [z-test가 유의미한 경우](#z-test가-유의미한-경우)
  - [p-value에 대한 이야기들](#p-value에-대한-이야기들)
  - [ASA(American Statistical Association) Statement on Statistical Significance and P-Values](#asaamerican-statistical-association-statement-on-statistical-significance-and-p-values)
  - [t-test](#t-test)
- [02 복수표본 z-검정(two-sample z-test)](#02-복수표본-z-검정two-sample-z-test)
- [03 회귀분석의 런검정](#03-회귀분석의-런검정)
- [04 카이제곱검정](#04-카이제곱검정)

<!-- /code_chunk_output -->

## 01 유의성 검정(significance test) 일반

유의성 검정(significance test)은 단순히 어떤 결과가 우연의 산물인지, 아니면 통계적으로 유의한 결과인지(statistically significant)를 판단하는 것이다.

유의성 검정은 모집단에 대한 논쟁에만 의미가 있다. 표본을 가지고 통계 실험을 하지만 유의성 검정의 대상은 표본이 아니라 모집단이다.

### 귀무 가설(영 가설)과 대립 가설

- 귀무가설(null hypothesis): $H_0$, 관측된 차이가 우연의 산물이다. 영 가설이라고도 한다.
- 대립가설(alternative hypothesis): $H_1$, 관측된 차이가 통계적으로 유의미하다.

보통 귀무 가설은 보수적이고 대립 가설은 진취적이다. 일반적으로 가설 검증은 귀무 가설을 기각해서 결과가 통계적으로 유의미하다는 것을 증명하려는 방식으로 진행된다.

### z검정과 p값

귀무 가설이 참이라는 가정 하에 z-통계량(z-statistic)를 구한다.

$$
z = \frac{통계량 - 기대값}{통계량의\ 표준오차}
$$

이 z-통계량은 결국 기대값으로 부터 해당 값이 어느 SE 단위로 떨어져있는 가에 대한 값이고, 정규분포에 근사하여 (통계량이 합, 평균이라면 CLT에 의해 정규분포를 보일테니) 해당 데이터 혹은 더 극단적인 상황이 일어날 가능성인 p-value를 계산할 수 있게 된다.

p-value는 유의수준(significance level, $\alpha$, 검정의 크기)을 기준으로 아래와 같이 판단한다.
양측 검정인지, 단측 검정인지는 실험에 따라 자율적으로 판단한다.

- $p \le \alpha$ : $H_0$ 귀무 가설 기각. 그렇지만 대립 가설이 맞다는 증거는 아니다.
- $p \gt \alpha$ : $H_0$ 귀무 가설 기각 못함.

p-value를 정규분포표 보면서 계산해도 되지만 보통 p-value가 유의 수준보다 같거나 작아지게 하는 검정 통계량의 영역, 즉, 기각역(critical region, rejection region)을 외워 판단하는 것이 훨씬 빠르다

단측 검정인 경우 아래 값을 그대로 쓰면 되고 양측 검정인 경우 $z_{\alpha/2}$를 쓰면 된다

$$
z_{5\%} = 1.65 \
z_{2.5\%} = 1.96 \
z_{1\%} = 2.33 \
z_{0.5\%} = 2.56 \
$$

관습적으로 유의 수준은 0.05(5%)로 두고 이하일 경우 통계적으로 유의미하다고 기계적으로 판단하는 경우가 많다.
보통 $\pm 2SE$ 바깥이면 p값이 5% 이하이므로 귀무가설을 기각한다.

그런데 ASA에서는 꼭 그렇지는 않다는 의견을 내었다. <ins>p값은 연구된 가설이 참일 확률을 나타낼 수 없다.</ins> 좋은 것은, p값 자체를 알려주는 것이다.

#### z-test가 유의미한 경우

앞서 CLT에 의해 표본의 합, 평균이 정규분포를 따라간다는 가정를 하였다. 만약 표본이 적다면 z-test는 할 수 없다. 정규 분포를 따르는 모양이 되지 못할 것이기 때문이다.

표본이 적은 경우에는 t-test나 sign-test를 해야 한다.

### p-value에 대한 이야기들

p값이 유의 수준을 넘느냐 마느냐로 의사결정을 하는 것 자체가 부적절한 것일 수 있다. p-value hacking으로 어떻게든 값을 내리려는 편법도 많다. 후술하겠지만 p값은 연구된 가설이 참일 확률을 나타낼 수 없다.

p값이 크다는 것은 어떤 효과 또는 연관성이 있다고 할 증거가 부족하다는 (inconclusive) 뜻이지 효과가 없다는 의미가 아니다.

p값이 크다는 것은 우연에 의한 변동이라고 보기에는 일어날 수 있는 확률이 적다는 것이지 확실성을 보장하는 것은 아니다.

### ASA(American Statistical Association) Statement on Statistical Significance and P-Values

p값으로 정의되는 확률이 0.05 미만이면 통계적으로 유의한 결과를 얻었다고 관행적으로 생각하지만 그게 아니라는 미국 통계 학회(ASA)의 글이다.

[원문](https://amstat.tandfonline.com/doi/full/10.1080/00031305.2016.1154108?scroll=top&needAccess=true#.Y53lGuxBz9B)

1. P-values can indicate how incompatible the data are with a specified statistical model. (p값은 데이터가 특정 통계모델과 얼마나 양립할 수 없는지 보여줄 수 있다.)

2. P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone. (p값은 연구된 가설이 참일 확률을 나타낼 수 없다. 또한 p값은 데이터가 우연히 발생할 확률을 나타낼 수도 없다.)

3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold. (과학적 결론과 사업 또는 정책 결정은 p값이 임계값을 넘었느냐 아닌가를 근거로 해서는 안된다.)

4. Proper inference requires full reporting and transparency (적절한 추론은 전부 보고하는 것과 투명성을 필요로 한다.)

5. A p-value, or statistical significance, does not measure the size of an effect or the importance of a result. (p값이나 통계적 유의성은 효과의 크기나 결과의 중요성을 판단하지 못한다.)

6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis. (p값 그 자체로는 모델이나 가설에 대한 좋은 판단의 근거가 되지 못한다.)

### t-test

표본의 크기가 적다면 정규분포에 근사할 수 없다. 그래서 t-분포 곡선을 기반으로 p-value를 계산한다. t-분포곡선은 자유도에 따라 그 모양이 달라진다. 자유도가 증가할 수록 정규분포곡선과 가까워진다.

$$
자유도 = 측정횟수 - 1
$$

## 02 복수표본 z-검정(two-sample z-test)

## 03 회귀분석의 런검정

## 04 카이제곱검정
