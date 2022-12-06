<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [data pipeline principles](#data-pipeline-principles)
  - [6 concepts of data pipeline](#6-concepts-of-data-pipeline)
- [pipeline architecture 고려사항](#pipeline-architecture-고려사항)
  - [`Calculating data size and velocity`](#calculating-data-size-and-velocity)
  - [`Calculating compute/storage requirements based on data size`](#calculating-computestorage-requirements-based-on-data-size)
    - [latency, cost numbers](#latency-cost-numbers)
    - [RAM](#ram)
    - [CPU](#cpu)
    - [storage](#storage)
    - [cluster, node, pod, etc...](#cluster-node-pod-etc)
  - [`Understanding the end result`](#understanding-the-end-result)
  - [`Complexity vs simplicity tradeoffs`](#complexity-vs-simplicity-tradeoffs)
  - [`Understanding cost`](#understanding-cost)
- [etc](#etc)

<!-- /code_chunk_output -->

## data pipeline principles

### 6 concepts of data pipeline

data pipeline이라는 것은 A에서 데이터를 이동시키되 데이터를 조작하는 과정(Transform)을 거쳐 B로 이동 시키는 것을 말한다.  
간단하게 들리지만 그렇게 간단한 개념이 아니다. one-time script로 작성되는 것이 아니라 지속적으로 운영되어야 한다.
따라서 아래 6가지 개념에 근거하여 파이프라인을 설계해야 한다. 외우자!

> 💡 what is pipeline?  
> Facilitating the (1)movement, (2)storage, and (3)access to data in a (4)repeatable, (5)resilient, and (6)scalable manner.

1. `Movement`  
   streaming(real time), batch, micro batching(near real time)
   processing 방법에 따라 downstream 인프라와 코드 설계에 큰 영향을 미치기 때문에 신중해야 한다.
   - 높은 velocity에 data size가 작은 경우 streaming이 적합하다. (Kafka, Pulsar, Spark streaming)
   - 그 외의 일반적인 경우 batch processing이 적합하다.
2. `Storage & File Types`  
   스토리지와 저장하고자 하는 파일의 형식은 시간과 비용에 영향을 준다. 단순히 쉬운 형식이라고 JSON으로 데이터를 저장했다가, 데이터의 양이 증가하면서 그것을 처리하고자 치루는 비용이 훨씬 커지는 경우가 있다.
3. `Access`  
   데이터 파이프라인 과정 중 데이터에 접근하여 그 값을 볼 수 있어야 한다.
4. `Repeatable`  
   작성자를 제외한 사람은 읽을 수 없는 죽은 코드를 생산하지 말라는 일반적인 소프트웨어 원칙에 가깝다.  
   추가로, 파이프라인 idempotent한 결과를 내어야 한다는 조건이 추가된다.
5. `Resilient`  
   일반 백엔드에서 말하는 resiliency와 비슷한 의미이다.  
   파이프라인에도 방어 코드와 견고한 구조가 필요하며 low coupling, high cohesion과 같은 소프트웨어 설계 원칙 적용도 예외가 아니다.
6. `Scalable`  
   pipeline을 작성한 코드 자체의 퍼포먼스도 좋아야 하며, 인프라 구성도 고려해야 한다.  
   연산에 소요되는 컴퓨팅 리소스를 파악해야 한다.

## pipeline architecture 고려사항

코드에 달려들기 전에 아키텍처를 먼저 고려해야 한다. (Architecture First)
생각의 흐름은 현실에서 시니어의 사고 흐름을 따라가며 도제식으로 학습해야 하는 것으로 보이지만, 내가 생각하는 사고 흐름은

- 해결하고자 하는 문제와 final expectations.

  - 내가 생각하는 결과가 아니라 요구한 사람의 final expectations을 이해해야 한다.
  - final expectations에 기반하여 다음과 같은 사항을 고려한다.

### `Calculating data size and velocity`

- `data size`
  - KB 수준의 json이 하루에 자잘하게 온다면 streaming 방식이 적합할 것이고, GB 수준의 CSV가 하루에 1번 온다면 배칭이 적합한 방식일 것이다. 생성되는 데이터의 포맷과 양에 기반하여 기술을 고려한다.
- `velocity`(amount of incoming data)
  - 데이터가 들어오는 빈도가 어떠한지 고려한다. 하루에 한 두번 들어오는 수준이면 별다른 조치가 필요 없을 것이나 유저 행동 로그와 같은 데이터는 velocity가 높은 것으로 예상되어 compaction이나 aggregation 단계가 필요할 것이다.

### `Calculating compute/storage requirements based on data size`

보통 이 문제를 해결하게 위해서는 CS 일반에 대한 지식과 리눅스 경험이 요구된다.

- Calculating Compute Requirements
  - OOM 문제와 퍼포먼스 이슈를 방지하기 위해 필요한 리소스를 계산해야 한다.
  - 컴퓨팅 리소스가 얼마나 필요한지 Back Of The Envelope Calculation을 해야 한다.
  - Resource Requirement = (processing unit size x (number of CPU + RAM)) x number of batches
  - <ins>가용 가능한 자원의 usage를 최대한으로 활용해야 한다.</ins> cpu usage가 peak을 쳤을 때도 2% 정도에서만 머문다면 비싼 인스턴스를 쓸 이유가 없다.
- Understanding the end result
  - 용량 x 저장 기간 x 저장 방식(compression으로 용량 일부 절약)에 따라 저장소의 용량이 결정된다.

#### latency, cost numbers

- https://gist.github.com/jboner/2841832
- https://colin-scott.github.io/personal_website/research/interactive_latency.html
- https://github.com/sirupsen/napkin-math

#### RAM

- in memory 연산으로 처리하고 끝내면 되는데 불필요하게 disk에 읽고 쓰는 작업은 없나?
  - 물론 in memory 연산이 빠르지만 잘못하면 OOM 에러를 만나게 된다. 가용 가능한 정도를 계산에 두고 있어야
  - 현재 인스턴스에서 메모리가 얼마나 되지?
  - os를 구동하기 위한 메모리를 제외하고 정말로 사용할 수 있는 메모리가 얼마나 되지?
  - peak를 칠 때 얼마나 메모리를 써야 하지? 인스턴스 한계를 넘는다면 어떻게 대응하지?
  - 기존 data의 양에 기반하여 memory 소비량을 계산할 수 있나? 해봐야지
- 기존 코드에서 불필요하게 메모리를 많이 잡아 먹는 부분은 없나?
  - memory leak이 발생하는 부분은 없나?
  - clean up이 안되는 부분은 없나?

#### CPU

- 가급적 multi-threading, multi-processing 처리를 하라
- 노는 core가 있지 않은가?

#### storage

- 대부분 cloud 기반으로 넘어가 size에는 신경을 덜 쓴다
  - azure blob, aws s3, gcp gcs, etc...
- Reading and writing directly to cloud storage is best but creates network bottlenecks.
  - network io도 io긴 하다

#### cluster, node, pod, etc...

- 어떤 시스템을 사용하건 띄우는 인스턴스의 갯수를 늘려서 처리할 수 있다.
- 인스턴스당 처리량을 어림잡아 계산하고 기억해두자

### `Understanding the end result`

- 큰 그림을 잘 그리라는 것

### `Complexity vs simplicity tradeoffs`

- Too complex and the pipeline will be unmanageable
- Too simple and the pipeline won’t scale
- 이 아키텍처를 가용 가능한 인적, 물적 리소스로 유지할 수 있는가? 개발자는 보통 새로운 기술에 끌리기 마련이므로 이를 자제할 필요가 있다.

### `Understanding cost`

- 비용 절감

## etc

일반 소프트웨어 개발에 적용되는 각종 원칙들(OOP, function approach, clean code, DRY, etc) 또한 적용될 수 있음.

위의 결정 사항들은 상황에 따라 언제든지 변경될 수 있고, 히스토리를 남겨야 현재 시스템이 만들어진 이유를 알 수 있기 때문에 [architecture decision record(ADR)](https://github.com/joelparkerhenderson/architecture-decision-record) 문서화를 꼭 해두어야 한다.

추가로, [람다 아키텍처 카파 아키텍처](https://towardsdatascience.com/a-brief-introduction-to-two-data-processing-architectures-lambda-and-kappa-for-big-data-4f35c28005bb)에 대해 공부해두자

- data pipeline도 테스트를 짜야한다.
- Diving into writing code right away without working through the architecture first is a big mistake
- https://medium.com/@synabreu/how-to-load-data-efficiently-in-bigquery-7af8cb5bee33
- https://www.apexon.com/blog/architecture-for-high-throughput-low-latency-big-data-pipeline-on-cloud/
