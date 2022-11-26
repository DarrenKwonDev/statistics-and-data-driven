<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [01 확률이란 무엇인가](#01-확률이란-무엇인가)
  - [확률의 일반화된 덧셈법칙, 배반](#확률의-일반화된-덧셈법칙-배반)
  - [조건부 법칙과 곱셈법칙, 독립](#조건부-법칙과-곱셈법칙-독립)
  - [MECE한 partition(분할)](#mece한-partition분할)
  - [Naive Bayesian](#naive-bayesian)
  - [일반화된 Naive Bayesian](#일반화된-naive-bayesian)
  - [독립(independent)과 배반(mutually exclusive)](#독립independent과-배반mutually-exclusive)
  - [배반 -\> 독립, 독립 -\> 배반 두 명제 모두 거짓](#배반---독립-독립---배반-두-명제-모두-거짓)
- [02 binomial formula (이항공식)](#02-binomial-formula-이항공식)
  - [이항 공식](#이항-공식)
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
  - 직관적으로 이해하면 두 사건은 독립이다 = 두 사건은 연관 없다로 이해하자.
  - 증명하려면 그냥 $P(A) \cap P(B) = P(A) \times P(B)$ 로 증명하는게 빠르다.
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

### 배반 -> 독립, 독립 -> 배반 두 명제 모두 거짓

독립사건과 배반사건은 서로 전혀 연관이 없는 개념이다.  
교집합이 있을 때(사건이 배반이 아니더라도) 사건들은 상호 독립적일 수 있다. 잘 생각해보면 상식적인 것이다. 주사위 짝수일 확률이 주사위 눈이 3이상일 확률과 무슨 상관이 있는가? 예시로 이해해보자면 https://kenadams.tistory.com/38 참고
따라서 `독립 -> 배반` 명제는 거짓이다.

또한 `배반 -> 독립`도 거짓이다. 배반 사건이라면 $P(A) \cap P(B) = 0$ 인데 독립을 증명하기 위한 공식인 $P(A \cap B) = P(A)P(B)$ 가 애초에 0이 되어버림. 독립 사건의 전제 조건은 적어도 각 A, B에 대한 확률이 0은 아니어야 함.
따라서 `배반 -> 독립` 명제는 거짓이다.  
예시로 이해해보려면 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=parkhc1992&logNo=220587985603 참고

## 02 binomial formula (이항공식)

[이산확률분포(discrete probability distribution)](https://namu.wiki/w/%ED%99%95%EB%A5%A0%EB%B6%84%ED%8F%AC)에는 이항분포, 푸아송분포, 기하 분포 등 다양한 분포가 존재한다. 여기서는 이항 분포를 다루는 이항공식에 대해 알아보자.

이항 분포를 따르는 이항확률 변수 X는 $X \sim B(n, p)$ 로 표기할 수 있다.

### 이항 공식

- n번의 독립시행 (독립이 아니라면 한 사건의 발생이 다른 사건에 영향을 미치므로 이항공식 적용 불가)
- 관심사건 A에 대해 P(A) = p이고, P(A') = 1-p (베르누이 시행)
- n번중 A가 k번 발생

일 때 아래와 같이 이항 공식이 적용된다.

$$
P(X=k) = _{n}C_{k} p^k (1-p)^{n-k}
$$

또한, 이항 공식을 합하면 사건 전체의 확률이므로 1이 된다.

$$
\sum_{k=0}^{n} P(X=k) = 1
$$

## 03 평균의 법칙

## 04 기대값과 표준오차

## 05 정규분포곡선과 확률히스토그램

## glossary

- 복원추출과 비복원추출
- 조건부확률과 비조건부확률
