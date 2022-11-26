<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [01 확률이란 무엇인가](#01-확률이란-무엇인가)
  - [확률의 일반화된 덧셈법칙, 배반](#확률의-일반화된-덧셈법칙-배반)
  - [조건부 법칙과 곱셈법칙, 독립](#조건부-법칙과-곱셈법칙-독립)
  - [MECE한 partition(분할)](#mece한-partition분할)
  - [Naive Bayesian](#naive-bayesian)
  - [일반화된 Naive Bayesian](#일반화된-naive-bayesian)
  - [독립(independent)과 배반(mutually exclusive)](#독립independent과-배반mutually-exclusive)
- [02 이항공식](#02-이항공식)
- [03 평균의 법칙](#03-평균의-법칙)
- [04 기대값과 표준오차](#04-기대값과-표준오차)
- [05 정규분포곡선과 확률히스토그램](#05-정규분포곡선과-확률히스토그램)
- [glossary](#glossary)

<!-- /code_chunk_output -->

## 01 확률이란 무엇인가

확률은 크게 두 가지 관점이 있다.

1. 하나의 시행을 동일 조건 하 독립 시행으로 무한히 반복해서 측정하는 도수 이론 내지는 frequentism(빈도 주의)
2. 인간의 주관적인 감각 내지는 직관으로 얻는 주관적 확률 (subjective view)
3. 새로운 정보를 토대로 어떤 사건이 발생했다는 주장에 대한 신뢰도를 갱신해 나가는 방법으로서의 통계 (Bayesian view)
   - 이는 연역적인 빈도 주의가 아닌 통계를 귀납적으로 바라보는 패러다임 전환을 의미한다.

### 확률의 일반화된 덧셈법칙, 배반

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

여기서 A와 B가 상호 배반적인 사건(disjoint, mutex)일 경우 $P(A \cap B) = \emptyset$ 이므로 아래처럼 정리할 수 있다. 아래 섹션에서 좀 더 자세히 설명한다.

$$
P(A \cup B) = P(A) + P(B)
$$

### 조건부 법칙과 곱셈법칙, 독립

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)} \\
P(A \cap B) = P(A)P(B \mid A) = P(B)P(A \mid B)
$$

후술하지만, 독립이라면 $P(A \mid B) = P(A)$ 이므로 아래처럼 정리할 수 있다. 아래 섹션에서 좀 더 자세히 설명한다.

$$
P(A \mid B) = P(A)P(B)
$$

### MECE한 partition(분할)

사건이 전체를 포괄하고(collectively exhaustive) 상호 배반적(mutual exclusive)일 때,
컨설팅 업계에서는 흔히 이를 'MECE'하다라고 표현한다. 통계학에서는 이를 전체를 '분할'(partition)한다고 표현한다.
통계학에서 MECE가 중요한 이유는 여기에 기반하여 베이즈 정리를 이해할 수 있기 때문이다.

### Naive Bayesian

베이즈 정리에 이르는 정의는 생략하고, 단순한 형태의 베이즈 정리는 아래와 같다.
$P(A \mid B)$는 posterior(사후 확률), P(A)는 prior(사전 확률), $P(B \mid A)$는 likelihood(우도)라고 부른다.

$$
P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}
$$

문제는 이를 받아들이는 직관인데, `구하려는 사건과 주어진 사건의 순서를 뒤집어 계산할 수 있다는 것`이다.

### 일반화된 Naive Bayesian

특정 사건 S를 MECE하게 $A_1, A_2, \cdots, A_m$으로 분할(partition)했다고 하자.
여기서 우리는 S라는 공간 내에 B라는 새로운 사건이 발생했을 때, A_1이라는 사건이 발생할 확률을 구해낼 수 있습니다.

$$
P(A_1 \mid B) = \frac{P(B \mid A_1)}{P(B)} = \frac{P(A_1)P(B \mid A_1)}{P(A_1)P(B \mid A_1) + \cdot P(A_m)P(B \mid A_m)}
$$

- https://junpyopark.github.io/bayes/
- https://angeloyeo.github.io/2020/01/09/Bayes_rule.html

### 독립(independent)과 배반(mutually exclusive)

- A 이거나 B = or($ \cup $) 조건 = 덧셈 법칙 = 배반인지 고려해야 함
  - 배반 : $P(A) \cap P(B) = 0$ 즉, A와 B가 별개의 조건. 벤 다이어그램으로 표현하면 교집합이 없는 경우다.
  - 확률간 덧셈을 할 때 사건들이 배반인지 고려해야 함. 이는 본능적으로 이뤄져야 함.
- A 이고 B = and ($ \cap $) 조건 = 곱셈 법칙 = 독립인지 고려해야 함
  - 독립 : $P(A \mid B) = P(A)$ 즉, B가 일어나건 말건 A 확률은 그대로임. 풀어 쓰자면 A가 B 혹은 B가 A의 서로의 확률에 영향을 주지 않음.
  - 확률간 곱셈을 할 떄 사건들이 독립인지 고려해야 함. 이는 본능적으로 이뤄져야 함.

배반

$$
P(A) \cap P(B) = 0
$$

독립

$$
P(A \mid B) = P(A) \\
P(B \mid A) = P(B) \\
P(A \cap B) = P(A)P(B)
$$

## 02 이항공식

## 03 평균의 법칙

## 04 기대값과 표준오차

## 05 정규분포곡선과 확률히스토그램

## glossary

- 복원추출과 비복원추출
- 조건부확률과 비조건부확률
