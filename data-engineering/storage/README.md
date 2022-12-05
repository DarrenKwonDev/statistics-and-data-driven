<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [storage](#storage)
  - [access pattern(storage layer에 어떤 방식으로 access 하는가)](#access-patternstorage-layer에-어떤-방식으로-access-하는가)
  - [SQL/NoSQL vs files](#sqlnosql-vs-files)
  - [file types](#file-types)
    - [Row vs Columnar Storage](#row-vs-columnar-storage)
  - [compression](#compression)
  - [storage location](#storage-location)
  - [partitions](#partitions)

## storage

### access pattern(storage layer에 어떤 방식으로 access 하는가)

어떤 서비스가 storage layer에 어떤 방식으로 access 하는가에 대한 이야기이다.

• How many system(s) will need access to the data storage layer?  
• How often will the above system(s) be accessing the data storage?  
• How much data will these system(s) be reading?  
• How much logic will be applied by those systems to the data?  
• How does the system technically access the data?

### SQL/NoSQL vs files

<img src="./db_select.png" />

### file types

Choosing Parquet vs Avro vs JSON vs CSV vs HDF5 vs RDBMS. These decisions should be driven by the data needs and access patterns

#### Row vs Columnar Storage

- 행 기반 스토리지
  - 일반 RDBMS
  - OLTP, Online transaction processing (온라인 트랜잭션, insert, update, delete)
  - 서비스를 위한 DB
  - 쿼리 → 적은 양의 데이터를 가져오고 변형하는 일이 잦다.
- 열 기반 스토리지
  - snowflake, big query, redshift
  - OLAP, online analytical processing. (select)
  - 사용자의 의사결정에 도움을 주는 것으로 데이터 분석, 데이터 마이닝에 주로 사용된다.
  - 분석 → 많은 양의 데이터를 가져오고 그걸 활용하지, 여러번 요청하지 않는다.
  - 결론적으로 데이터 웨어 하우스에서 대규모 데이터셋을 다루기에 좋다는 것이다.

### compression

### storage location

### partitions
