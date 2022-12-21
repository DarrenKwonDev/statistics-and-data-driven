<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

- [doc-culture](#doc-culture)
  - [why doc culture?](#why-doc-culture)
    - [main point](#main-point)
    - [doc culture system references](#doc-culture-system-references)
  - [how to organize doc?](#how-to-organize-doc)
    - [서본결](#서본결)
    - [셀프 데이터 서비스와 문서의 연결](#셀프-데이터-서비스와-문서의-연결)
  - [doc make tech](#doc-make-tech)
    - [doc system research](#doc-system-research)
      - [large size doc systems](#large-size-doc-systems)
      - [static site generator(SSG) 적극 활용 권장](#static-site-generatorssg-적극-활용-권장)
      - [code-interactive](#code-interactive)
      - [code sandbox](#code-sandbox)
    - [how to deal with biblio](#how-to-deal-with-biblio)
    - [doc parse, processing](#doc-parse-processing)

<!-- code_chunk_output -->
<!-- /code_chunk_output -->

---

# doc-culture

## why doc culture?

조직에 문서 주도 문화를 도입하기 위한 자료들입니다.
비효율적인 회의를 줄이고, 문서를 통해 효율적인 의사소통을 할 수 있도록 도와줍니다.

사실 문서 주도에 대한 제 생각들은 처음부터 있었던 것은 아닙니다.
조직에 data-driven한 조직 문화를 만들고자 했지만 data를 제공해도 구성원이 해당 내용을 읽지 않으면 아무 소용이 없다는 경험 이후에 생각하게 된 개인적인 문화, 방법론입니다.

즉, data-driven 이전에 문서 위주의 문화를 조성해야 한다는 생각입니다.

### main point

- 문서를 미리 읽지 않고 회의가 시작하면 문서를 모두가 읽기 시작합니다. 어차피 아무도 안 읽어 옵니다.
- 화려한 이미지와 차트는 오히려 내용에 대한 본질을 흐릴 수 있습니다. IR과 같은 외부 피칭이 아니라면 내부 문서는 텍스트 위주로 문서를 작성합니다.
  - 문장에서 미사여구와 형용사를 제거해야 합니다.
  - 단문 위주로 문장을 작성합니다.
    - 문장이 길어지면 주술관계가 모호해져 문장을 이해하는 비용이 증가합니다.
  - 1 pager에 집착할 필요는 없지만 분량을 줄이려고 노력합니다.
    - 아마존과 같은 큰 회사라고 하더라도 6 page를 넘어가지 않습니다.
- speaker가 아닌 content를 중심으로 회의를 진행합니다.
- 문서 문화를 정착하면 자연스레 의사결정에 대한 히스토리를 남기게 됩니다.
- 문화를 정착시키기 위해서는 여러 tech를 통해 자동화에 힘써야 합니다.

### doc culture system references

[Eng)The Document Culture of Amazon](https://www.justingarrison.com/blog/2021-03-15-the-document-culture-of-amazon/)
[Kor)The Document Culture of Amazon](https://news.hada.io/topic?id=4479)

[Eng)It's time to start writing](https://alexnixon.github.io/2019/12/10/writing.html)
[Kor)It's time to start writing](https://news.hada.io/topic?id=2504)

## how to organize doc?

### 서본결

- BDD(Behavior-Driven Development)에서 given, when, then이란 테스트 프레임을 통해 테스트를 작성하는 것과 비슷한 방식으로 문서를 작성합니다.
  - given(서)
  - when(본)
  - then(결)

### 셀프 데이터 서비스와 문서의 연결

작성 예정

## doc make tech

### doc system research

#### large size doc systems

[TC39](https://github.com/tc39)

#### static site generator(SSG) 적극 활용 권장

[hugo](https://gohugo.io/)  
[nextra(experimental)](https://nextra.vercel.app/)

학습은 불가피함. build 속도가 제일 빠른 hugo를 권장함.

#### code-interactive

highly interactive doc is similar to programming learn sites, like [exercism](https://exercism.org/) or [datacamp](https://www.datacamp.com/)

[MDN](https://github.com/mdn/mdn)

- 출력물이 콘솔에 출력되는 것으로 보아 사용자의 브라우저 런타임에서 실행되는 것 같다.

[edge db tutorial](https://www.edgedb.com/tutorial)

- code-interactive should use its interpreter or at least its parser

#### code sandbox

https://blog.pronus.io/en/posts/programe-pelo-navegador-com-code-lab/

### how to deal with biblio

markdown에서 지원을 안 한다. script를 짜거나, 지원하는 포맷을 써야 한다.

- use pandoc
- https://github.com/parksb/handmade-blog

### doc parse, processing

[parsr](https://github.com/axa-group/Parsr)  
[hwp.js](https://github.com/hahnlee/hwp.js)  
[hwp-rs](https://github.com/hahnlee/hwp-rs)  
[docconv](https://github.com/sajari/docconv)  
[wkhtmltopdf](https://wkhtmltopdf.org/)  
[wkhtmltopdf-go](https://github.com/andrewcharlton/wkhtmltopdf-go)  
[unioffice](https://github.com/unidoc/unioffice)  
[@webtoon/psd](https://d2.naver.com/helloworld/6631477)

[Kotlin으로 DSL 만들기](https://toss.tech/article/kotlin-dsl-restdocs)
