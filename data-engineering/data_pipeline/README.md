<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [data pipeline principles](#data-pipeline-principles)
  - [6 concepts of data pipeline](#6-concepts-of-data-pipeline)
- [pipeline architecture](#pipeline-architecture)
- [storage](#storage)
- [docs](#docs)

<!-- /code_chunk_output -->

## data pipeline principles

### 6 concepts of data pipeline

data pipeline이라는 것은 A에서 데이터를 이동시키되 데이터를 조작하는 과정(Transform)을 거쳐 B로 이동 시키는 것을 말한다.  
간단하게 들리지만 그렇게 간단한 개념이 아니다. one-time script로 작성되는 것이 아니라 지속적으로 운영되어야 한다.
따라서 아래 6가지 개념에 근거하여 파이프라인을 설계해야 한다. 외우자!

> 💡 what is pipeline?
> Facilitating the (1)movement, (2)storage, and (3)access to data in a (4)repeatable, (5)resilient, and (6)scalable manner.

1. Movement
   streaming(real time), batch, micro batching(near real time)
   processing 방법에 따라 downstream 인프라와 코드 설계에 큰 영향을 미치기 때문에 신중해야 한다.
2. Storage & File Types
   스토리지와 저장하고자 하는 파일의 형식은 시간과 비용에 영향을 준다. 단순히 쉬운 형식이라고 JSON으로 데이터를 저장했다가, 데이터의 양이 증가하면서 그것을 처리하고자 치루는 비용이 훨씬 커지는 경우가 있다.
3. Access
   데이터 파이프라인 과정 중 데이터에 접근하여 그 값을 볼 수 있어야 한다.
4. Repeatable
   작성자를 제외한 사람은 읽을 수 없는 죽은 코드를 생산하지 말라는 일반적인 소프트웨어 원칙에 가깝다.  
   추가로, 파이프라인 idempotent한 결과를 내어야 한다는 조건이 추가된다.
5. Resilient
   일반 백엔드에서 말하는 resiliency와 비슷한 의미이다.
   파이프라인에도 방어 코드와 견고한 구조가 필요하며 low coupling, high cohesion과 같은 소프트웨어 설계 원칙 적용도 예외가 아니다.
6. Scalable
   pipeline을 작성한 코드 자체의 퍼포먼스도 좋아야 하며, 인프라 구성도 고려해야 한다.

## pipeline architecture

## storage

## docs

- https://medium.com/@synabreu/how-to-load-data-efficiently-in-bigquery-7af8cb5bee33
- https://www.apexon.com/blog/architecture-for-high-throughput-low-latency-big-data-pipeline-on-cloud/
