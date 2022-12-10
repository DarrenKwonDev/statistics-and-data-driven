<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [01 표본 추출(sampling)](#01-표본-추출sampling)
  - [quota sampling이 왜 안되는가](#quota-sampling이-왜-안되는가)
  - [확률적 방법에 의한 표본 추출 (probability sampling)](#확률적-방법에-의한-표본-추출-probability-sampling)
  - [샘플링에 의해 발생할 수 있는 bias](#샘플링에-의해-발생할-수-있는-bias)
  - [비확률적 샘플링 (Non-probability sampling)](#비확률적-샘플링-non-probability-sampling)
- [02 샘플링에서의 확률 오차](#02-샘플링에서의-확률-오차)

<!-- /code_chunk_output -->

## 01 표본 추출(sampling)

우리가 왜 통계를 내려고 하는가? 추론(inference)하려고.
추론이 뭔데? population에서 표본을 추출하여 모집단의 특성(모수, parameter) 을 추정하는 것

그런데 이 추론의 전제에는 `표본이 모집단을 대표해야 한다`는 가정이 필요하고, 그래서 표본 추출에는 기술이 필요하다.

### quota sampling이 왜 안되는가

모집단은 다양한 집단으로 이루어져 있다. 그리고 이 집단들의 크기는 저마다 다르다. `집단에서 표본을 추출할 때 해당 집단들의 크기 별로 추출 확률을 보정해주어야 한다.` 이 과정에서 우리는 표본의 구성비를 모집단의 구성비로 맞추기 위해서 quota sampling(할당 추출)을 하고 싶은 욕망에 빠진다.

quota sampling을 근본적으로 잘못되어 있다. 만약 성비라는 기준으로 모집단을 나눠서 그 비중이 7/3이라 표본에도 이를 반영해서 7/3으로 샘플링을 한다면, 성비외에의 나머지 특성에 대해서는 자의적으로 표본을 추출하게 된다. 성비를 맞추다보니 그 과정에서 자의가 개입된 것이다. 이는 표본이 모집단을 대표하지 못하게 된다.

표본을 추출할 때는 잘 해보겠다고 노력하는게 아니라 무작위, 확률적으로 추출해야 한다. 확률을 도구로써 이용해야 한다.

그렇다면 위의 성비는 아무 이득이 없는 정보였나? 그건 아니다. 확률적 방법에 의해 표본 추출한 후 가중치 부여를 통해서 집단별로 표본의 구성비를 모집단의 구성비와 같도록 조절할 수 있다.

### 확률적 방법에 의한 표본 추출 (probability sampling)

- 왜 확률적으로 샘플링을 해야 하는 가?

  - 표본추출편의(sample selection bias) 때문이다. 그러니까 샘플링을 잘못해서 전제 조건인 `표본이 모집단을 대표해야 한다`는 가정이 깨지는 것이다. 앞서 살펴본 quota sampling이 이러한 표본추출편의를 일으키는 방식이다.
  - literary digest 잡지사의 실수 사례. 잘못된 샘플링으로 대선 결과를 잘못 예측하고 회사가 휘청임.
  - 잘못된 방식) quota sampling -> 모집단의 구성비를 가늠해서 표본로 그러한 구성비를 가지게끔 샘플링하는 것인데 이는 처음부터 실험자의 주관이 개입된 잘못된 방식. 모든 것을 확률에 맡겨야 한다.

- 확률적 샘플링의 특징

  - 확률적 샘플링은 모집단을 이루는 개개의 구성원이 표본으로 선택될 확률을 계산할 수 있게 해준다. 그래서 `관측치별로 추출 확률의 역수로 가중치를 부여하여 표본의 구성비를 모집단의 구성비와 같게 만들 수 있다`
  - 표본추출확률을 정할 때 집단별로 그 크기에 따라 추출 확률을 조절해주어야 한다.
  - 가중치 부여를 통해 집단별로 표본의 구성비를 모집단의 구성비와 같도록 조절할 수 있다.

- 확률적 샘플링
  - Simple random sampling (단순 무작위 추출)
  - Stratified sampling (계층적 샘플링)
    - 모집단의 데이터 분포 비율을 유지하면서 데이터를 샘플링
  - Systematic sampling (계통 추출)
  - Cluster sampling
    - multistage cluster sampling (다단계 군집 추출)

### 샘플링에 의해 발생할 수 있는 bias

- sample selection bias 표본추출편의
- non-response bias 무응답편의
- response bias 응답편의
- household bias 가구편의

### 비확률적 샘플링 (Non-probability sampling)

- Convenience sampling
- Quota sampling
- Self-selection (volunteer) sampling
- Snowball sampling
- Purposive (judgmental) sampling

## 02 샘플링에서의 확률 오차

샘플링을 통해 확률의 세계에 존재했던 추정량은 실제값인 추정치가 되었다. 그리고 이 추정치는 bias와 확률오차로 인해 실제 모수와 다르다. 아래처럼 도식화할 수 있다.

```text
추정치 = 모수 + bias + 확률오차
```
