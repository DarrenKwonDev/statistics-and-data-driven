# viz

## Overview

-   dataset의 종류에 따른 적합한 시각화가 다름.
    -   정형(structure), 시계열, 지리, 관계형(network), 계층형, 비정형 등.
-   정형 데이터
    -   csv, tsv 파일로 제공됨. col이 feature, row가 item에 해당
    -   가장 쉽게 시각화할 수 있는 종류.
-   시계열
    -   시간 흐름에 따른 추세(trend), 계절성(seasonality), 주기성(cycle) 파악이 주
-   지리, 지도
    -   거리, 경로, 분포
-   관계형
    -   객체와 객체 간의 관계. Node와 Link
    -   크기, 색, 수 등으로 가중치 표현
-   계층형
    -   관계 중에서도 포함 관계가 분명함
    -   tree, treemap, sunburst

## 데이터의 종류

-   수치형(numeric)
    -   연속형(continuous) : 길이, 무게, 온도
    -   이산형(discrete) : 횟수, 개수
-   범주형(categorical)
    -   명목형(nominal) : 혈액형, 종교 등
    -   순서형(ordinal) : 학년, 별점, 등급

## 데이터 정렬

-   시계열 : 시간순
-   수치형 : 크기순
-   순서형 : 범주의 순서대로
-   명목형 : 범주의 값에 따라 정렬

## 기타 tips

-   bar chart의 x축 시작은 0 강추
-   line chart는 가급적 5개 이하의 선을 사용할 것을 추천. 너무 많으면 시각으로 혼란스러움
-   line chart는 추세를 보므로 x축의 간격이 중요함. x축의 간격이 규칙적이지 않다면 관측값에 점을 찍어야. 왜? 실제로 관측된 값이 아닌데 선으로 그려서 실제로도 있다고 오해할 수 있기 때문임.
-   line chart 그리는데 데이터에 노이즈가 너무 많다면 smoothing을 해. [matplotlib plot smooth curve](https://www.delftstack.com/howto/matplotlib/matplotlib-plot-smooth-curve/)
-   scatter plot의 목적 : 군집, 값 사이의 차이, 이상치
