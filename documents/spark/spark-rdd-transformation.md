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

## filter()

구문:
`RDD.filter(<function>)`

- 데이터세트의 각 요소에 대해 일반적으로 익명의 함수로 표현된 부울 표현식을 평가한다.

## distinct()

구문:
`RDD.distinct(numPartitons=None)`

- 입력 RDD에 특정 요소를 포함해 만들어진 새로운 RDD를 반환한다.
- 이는 중복을 제거하는 데 이용한다. 
- numPartitions 인수는 타깃 파티션 수만큼 데이터를 재분산할 수 있다.


## groupBy()

구문:
`RDD.groupBy(<function>, numPartitions=None)`

- 지정 함수로 그룹화된 항목의 RDD를 반환한다.
- numPartitions 인수를 사용하면, 그룹화 함수의 출력에서 키 공간의 해시를 계산해 지정된 수의 파티션을 자동으로 생성할 수 있다.

## sortBy()

구문:
`RDD.sortBy(<keyfunc>, ascending=True, numPartitions=None)`

- 주어진 데이터세트에 대해 키를 지정하는 <keyfunc>인수로 RDD를 정렬한다.
