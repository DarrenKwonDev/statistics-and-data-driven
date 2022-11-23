<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [01 상관관계](#01-상관관계)
  - [상관관계와 인과관계](#상관관계와-인과관계)
  - [correlation coefficient(상관계수, r)](#correlation-coefficient상관계수-r)
  - [상관계수의 의미와 한계](#상관계수의-의미와-한계)
- [02 simple regression analysis (단순회귀분석)](#02-simple-regression-analysis-단순회귀분석)
  - [regression line(회귀 직선)](#regression-line회귀-직선)
  - [regression effect](#regression-effect)
  - [용어의 혼란 주의](#용어의-혼란-주의)
- [03 회귀분석의 오차](#03-회귀분석의-오차)
  - [residual(잔차), RMSE](#residual잔차-rmse)
  - [correlation coefficient(r)를 통한 RMSE 추정](#correlation-coefficientr를-통한-rmse-추정)
  - [homoscedasticity, heteroscedasticity(등분산성과 이분산성)](#homoscedasticity-heteroscedasticity등분산성과-이분산성)
  - [세로띠 안의 분포를 정규 분포로 근사하기](#세로띠-안의-분포를-정규-분포로-근사하기)
- [04 회귀직선](#04-회귀직선)
  - [linear equation](#linear-equation)
  - [multiple regression(중회귀분석)](#multiple-regression중회귀분석)
  - [총변동의 분리와 결정계수(coefficient of determination)](#총변동의-분리와-결정계수coefficient-of-determination)
  - [adjust R^2 (조정된 결정계수)](#adjust-r2-조정된-결정계수)
- [glossary](#glossary)
<!-- /code_chunk_output -->

## 01 상관관계

### 상관관계와 인과관계

상관관계는 역이 성립하지만(원인과 결과가 뒤바뀜) 인과관계는 비대칭이다.

- A라서 B가 발생했다(인과) -> B라서 A가 발생했다(거짓)
- A란 경향이면 B란 경향이다(상관) -> B란 경향을 보이면 A란 경향이다(참)

### correlation coefficient(상관계수, r)

보통 두 변수로 이루어진 자료는 다음과 같은 통계량으로 요약된다.
x, y의 $\mu$와 $\sigma$, 상관관계($r$)
$$ -1 \leq r \leq 1 $$

보통 `피어슨 상관계수`를 가장 많이 사용하고 스피어만 상관계수 등을 사용하기도 한다.

피어슨 상관계수는 다음과 같이 계산된다. 공분산을 각각의 표준편차의 곱으로 나눈 간편한 식이 자주 사용된다.

$$
r = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\cdot{}\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}} \\
  = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y}) / (n-1)}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2 / (n-1)}\dot{}\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2 / (n-1)}} \\
  = \frac{Cov(X, Y)}{SD_x \cdot{} SD_y}
$$

### 상관계수의 의미와 한계

- 상관 계수가 0.8이면 0.4인 관계보다 두 배만큼 강한 관계?
  - 강도가 2배라는 말은 틀렸다. 상관 관계가 0.8이라면 단순히 0.4보다 클 뿐, 강도가 숫자 그대로 표현되는 것은 아니다.
- 변수의 선형 변환(ax+b)은 상관계수를 변화시키지 않는다.
  - 상관계수는 두 변수의 선형 변환에 영향을 받지 않는다. 수학적으로 증명할 수 있으나 지면이 부족하여...
- 상관 계수는 `두 변수간의 scatter plot이 타원형일 경우에 적합하다`. 그렇지 않으면 상관계수의 유용성이 떨어진다.
  - outlier의 존재, 두 변수가 비선형 관계일 경우에는 상관계수가 덜 유용하다.
  - 예를 들어 인간이 느끼는 쾌적함과 온도라는 두 변수는 비선형 관계이다. 단순히 온도가 높거나 낮다고해서 쾌적함이 선형적으로 관계성을 드러내지 않는다.
- 잘못 해석하면 실제의 관계를 과장하게 된다.
  - 지역, 국가 등 집단 단위의 자료의 상관계수는 개개인에게 적용되는 관계를 과장할 수 있다.
- 강한 상관관계를 가진다고해서 그것이 인과관계를 드러내지는 않는다.
  - 발의 크기와 어휘력이란 두 변수 사이의 상관관계는 인과가 아니다. 나이라는 confounding factor를 무시한 것이다.

## 02 simple regression analysis (단순회귀분석)

### regression line(회귀 직선)

y의 x에 대한(x에 대한 y의) 회귀직선은 각각의 x값에 대응하는 y의 평균값을 추정한다.
일반적으로 x, y가 선형적 관계에 놓여있다는 전제 하에, 그들의 평균, 표준편차, 상관계수가 존재한다면 이들을 이용하여 회귀직선을 추정할 수 있다. 왜냐하면 x가 $1 SD_x$가 증가함에 따라 y도 $r SD_y$만큼 증가하는 경향이 있기 때문이다.
이러한 정의에 따라 회귀 직선의 기울기는 $r * \frac{SD_x}{SD_y}$이다. SD_x가 변화할 때마다 r \* SD_y만큼 y가 변화하기 때문이다.

그리고 이 회귀 직선은, 앞서 살펴보았듯, scatter plot을 그려보았을 때 타원형이 아닌 형태라면 무의미해진다.
data의 분포가 타원형이 아니라면, 회귀 직선은 data의 분포를 잘 설명하지 못한다.

뿐만 아니라 기존 자료에 포함되지 않는 경우, 대표적으로 (1) 새로운 개체가 기존 데이터와 성격이 다른 경우 (2) 아웃라이어인 경우에는 회귀 직선을 통한 값 추정이 틀릴 가능성이 높다. 이러한 문제를 extrapolation(외삽)이라고 한다.

### regression effect

평균으로의 회귀.

### 용어의 혼란 주의

- y의 x에 대한 값 = x에 대한 y값 = x 값을 기반으로 y값을 추정하고 싶다 = 기울기는 $r \times \frac{SD_y}{SD_x}$

- x의 y에 대한 값 = y에 대한 x값 = y값을 기반으로 x값을 추정하고 싶다 = 기울기는 $r \times \frac{SD_x}{SD_y}$

## 03 회귀분석의 오차

### residual(잔차), RMSE

실제값과 회귀를 통한 추정치와의 차이를 추정 오차라 한다. 간단히, 실제값과 추정치를 빼면 잔차(residual)가 나온다.
잔차를 기반으로 회귀분석의 전반적 오차를 측정하게 된다.

이 잔차의 제곱합(SSE, sum of squared error)
MSE(mean squared error) = $\frac{SSE}{n - 2}$
RMSE(root mean squared error) = $\sqrt{MSE}$

꼴로 유도하는데 보통 곧장 RMSE를 계산한다. 수식에서 밑변이 자유도인 `n-2`를 사용함에 유의하자.

$$
RMSE = \sqrt{\frac{(x - x_1)^2 + ... + (x - x_n)^2}{n-2}}
$$

RMSE는 표준편차와 같이 해당 직선으로부터 $\pm 1 RMSE$ 떨어진 데이터들이 68%, $\pm 2 RMSE$ 떨어진 데이터들이 95% 존재한다는 것을 의미한다.

### correlation coefficient(r)를 통한 RMSE 추정

x에 관한 y를 회귀 추정할 경우 계산되는 RMSE는 아래와 같이 근사될 수 있다.
RMSE는 정의상 자유도가 -2 이지만 SD를 구할 때는 -1이기 때문에 값이 같지는 않다. 다만 표본의 수가 많으면 그 값에 큰 차이가 없다.

$$
RMSE \approx \sqrt{1 - r^2} \times SD_y
$$

### homoscedasticity, heteroscedasticity(등분산성과 이분산성)

잔차의 분산이 일정한 경우 homoscedasticity, 일정하지 않은 경우 heteroscedasticity라고 한다.

풀어쓰자면, scatter plot으로 데이터를 그린 후에 세로띠를 그려 특정 x에 속한 (x, y) 순서쌍들이 가지는 y가 퍼져 있는 정도(분산, 표준편차)를 확인할 수 있을 것이다. 이 정도가 x에 따라 일관된다면 해당 데이터는 homoscedasticity를 가지고 있다고 할 수 있으며 RMSE의 추정 오차가 어느 곳에서나 적용될 수 있다고 볼 수 있다.

그러나 x에 따라 퍼져있는 정도가 일정하지 않다면 RMSE를 일관되게 적용할 수 없으며 해당 데이터는 heteroscedasticity를 가지고 있다고 할 수 있다.

단순하게 생각하면 scatter plot이 타원형이라면 등분산성을 가정하고 회귀분석을 진행할 수 있다.

### 세로띠 안의 분포를 정규 분포로 근사하기

데이터가 homoscedasticity를 가지고 있다고 가정하고 회귀분석을 진행할 경우, 세로띠 안의 분포를 정규 분포로 근사할 수 있다. 이 때, 해당 분포의 평균은 0이고 표준편차는 RMSE가 된다.

이를 통해서 세로 띠 안의 정규 분포 분석을 위해 새로운 평균과 새로운 표준편차를 가지는 정규 분포를 만들 수 있다.

구체적인 방법은 류근관. 통계학 / 저자: 류근관 (2013), p.154의 2번 문제를 참고하라.

## 04 회귀직선

### linear equation

y 절편은 x = 0일 때인데, 이는 단위당 x의 가치를 역으로 제거하는 방향으로 구할 수 있다.
구체적인 방법은 류근관. 통계학 / 저자: 류근관 (2013), p.162를 참고하라.

$$
y = \Delta{t} + \bar{y} - (\bar{x} \times \Delta{t}) \\
\Delta{t} = r \times \frac{SD_y}{SD_x}
$$

### multiple regression(중회귀분석)

x_n 요소의 순수효과는 b_n으로 표시함.

$$
y = a + b_1x_1 + b_2x_2 + \cdots + b_nx_n + 오차
$$

### 총변동의 분리와 결정계수(coefficient of determination)

단순 회귀 직선을 가정했을 때, 총변동 ($y_i - \bar{y}$)은 원인으로 여겨지는 x가 미친 효과와 그 외의 변수가 미친 효과로 분리할 수 있다.

예를 들어, 인플레이션 증가량(y)을 설명하고자 통화 증가량(x)으로 회귀 분석을 시도하였고, 도출된 값과 평균 사이의 차이를 온전히 통화 증가량(x)로만 설명할 수 있는 부분과 그 외의 변수가 미친 영향으로 분리할 수 있다는 것이다.

$a + bx_i$를 회귀식이라 할 때, 총 변동 $y_i - \bar{y}$는 아래와 같이 분리될 수 있다.

$$
y_i - \bar{y} = [(a+bx_i) - \bar{y}] + [y_i - (a+bx_i)] \\
T(total) = R(regression) + E(error)
$$

R은 변수 x에 대해 설명되는 부분이고 E는 그 외의 변수에 대해 설명되는 부분이다. 보통 E보다 R이 더 클 경우 변수 x가 y에 대해서 잘 설명한다고 할 수 있다.

이를 한 변수 $y_i$에 대한 변동이 아니라 전체로 확대하면 다음과 같이 일반화할 수 있다.

$$
\sum{(y_i - \bar{y})^2} = \sum{[(a+bx_i) - \bar{y}]^2} + \sum{[y_i - (a+bx_i)]^2} \\
SST = SSR + SSE
$$

여기서 SST는 총 변동(total sum of squares), SSR(regression sum of squares)은 회귀 제곱합, SSE는 오차제곱합(error sum of squares)이다.

그런데 여기서 SSR에 의해 SST를 더 잘 설명할수록 회귀 직선의 설명력이 좋다고 할 수 있으므로 위 식을 변형하여 수치화 하자면
결정계수 R^2는 다음과 같이 정의할 수 있다.

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST} \\
(0 \leq R^2 \leq 1)
$$

- 참고로 단순 회귀 분석에 한하여 결정계수는 상관계수의 제곱과 같다. $R^2 = r^2$
- 중회귀분석일 경우 변수가 늘어날수록 SSR가 늘어나므로 결정계수는 1에 가까워진다. -> 그러면 단순히 독립 변수(설명 변수)만 잔뜩 넣으면 되는거 아닌가? -> 그래서 조정된 결정계수를 활용해야

### adjust R^2 (조정된 결정계수)

위에서 살펴본 결정 계수는 독립 변수만 추가하면 증가한다는 문제가 있으므로 이를 조정한 값을 쓴다.

n을 표본 크기, k를 독립 변수의 갯수로 할 때 조정된 결정계수는 다음과 같다.

$$
\bar{R^2} = 1 - \frac{SSE / (n-k-1)}{SST / (n-1)}
$$

## glossary

- 독립변수(independent variable): x. 설명 변수로 x -> y의 관계를 설명한다.
- 종속변수(dependent variable): y. 피설명변수로 x에 의한 영향을 받는다.
