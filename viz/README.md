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
