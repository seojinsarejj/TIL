# 기본 RDD 변환

## map()

구문 : 
`RDD.map(<function>, preservesPartitioning=False)`

- 데이터 집합 파티션 내의 각 요소에 대해 명명된 함수나 익명의 함수를 평가

```
['loremipsumdolor',
 'sitametconsectetur',
 'adipiscingelitnullam',
  ... ]

  ===== .map(lambda x : x.split()) ====>

[
    ['lorem','ipsum','dolor'],
    ['sit','amet','consectetur'],
    ['adipsiscing','elit','nullam']
... ]
```


## flatMap()

구문:
`RDD.flatMap(<function>,preservesPartitioning=False)`

- 입력 데이터세트의 각 레코드에 대한 함수를 실행한다는 점에서 map()과 비슷
- 그러나 map()과 달리 중첩된 수준을 제거한다.

```
['loremipsumdolor',
 'sitametconsectetur',
 'adipiscingelitnullam',
  ... ]

  ===== .flatMap(lambda x : x.split()) ====>

['lorem','ipsum','dolor',
 'sit','amet','consectetur',
 'adipsiscing','elit','nullam'
... ]

```