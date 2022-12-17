<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [01 유의성 검정(significance test)](#01-유의성-검정significance-test)
  - [귀무 가설과 대립 가설](#귀무-가설과-대립-가설)
  - [z검정과 p값](#z검정과-p값)
  - [ASA(American Statistical Association) Statement on Statistical Significance and P-Values](#asaamerican-statistical-association-statement-on-statistical-significance-and-p-values)

<!-- /code_chunk_output -->

## 01 유의성 검정(significance test)

유의성 검정(significance test)은 단순히 어떤 결과가 우연의 산물인지, 아니면 통계적으로 유의한 결과인지를 판단하는 것이다.

### 귀무 가설과 대립 가설

- 귀무가설(null hypothesis): $H_0$, 관측된 차이가 우연의 산물이다.
- 대립가설(alternative hypothesis): $H_1$, 관측된 차이가 통계적으로 유의미하다.

보통 귀무 가설은 보수적이고 대립 가설은 진취적이다. 일반적으로 가설 검증은 귀무 가설을 기각해서 결과가 통계적으로 유의미하다는 것을 증명하려는 방식으로 진행된다.

### z검정과 p값

### ASA(American Statistical Association) Statement on Statistical Significance and P-Values

p값으로 정의되는 확률이 0.05 미만이면 통계적으로 유의한 결과를 얻었다고 관행적으로 생각하지만 그게 아니라는 미국 통계 학회(ASA)의 글이다.

[원문](https://amstat.tandfonline.com/doi/full/10.1080/00031305.2016.1154108?scroll=top&needAccess=true#.Y53lGuxBz9B)

1. P-values can indicate how incompatible the data are with a specified statistical model. (p값은 데이터가 특정 통계모델과 얼마나 양립할 수 없는지 보여줄 수 있다.)

2. P-alues do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone. (p값은 연구된 가설이 참일 확률을 나타낼 수 없다. 또한 p값은 데이터가 우연히 발생할 확률을 나타낼 수도 없다.)

3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold. (과학적 결론과 사업 또는 정책 결정은 p값이 임계값을 넘었느냐 아닌가를 근거로 해서는 안된다.)

4. Proper inference requires full reporting and transparency (적절한 추론은 전부 보고하는 것과 투명성을 필요로 한다.)

5. A p-alue, or statistical significance, does not measure the size of an effect or the importance of a result. (p값이나 통계적 유의성은 효과의 크기나 결과의 중요성을 판단하지 못한다.)

6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis. (p값 그 자체로는 모델이나 가설에 대한 좋은 판단의 근거가 되지 못한다.)
