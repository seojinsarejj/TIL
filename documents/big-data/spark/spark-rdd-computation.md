# RDD 연산

## 주요 RDD 개념

- 변환 : RDD에서 작동ㅎ고 새로운 RDD를 반환하는 함수
- 액션 : RDD에 대한 연산 작업 후 값을 반환하거나 출력 연산을 수행하는 함수

## 거친 변환 VS 세분화된 변환

- 거친 변환 : RDD 연산처럼 데이터 집합의 모든 요소에 대해 함수를 적용하고, 변환이 적용된 새 데이터 집합을 반환
- 세분화된 변환 : 관계형 데이터베이스의 단일 행 업데이트 또는 NoSQL put연산과 같이 단일 레코드나 데이터 셀을 조작

## 변환, 액션 및 지연 평가

### 변환
일반적인 변환에는 맵과 필터 함수가 포함된다.

```python
originalrdd = sc.parallelize([0,1,2,3,4,5,6,7,8])
newrdd = origianlrdd.filter(lambda x: x % 2)
```
위 예제는 filter() 변환을 origianlrdd의 각 요소에 적용해 컬렉션의 짝수를 건너뛴다.

### 액션
액션은 값 또는 데이터를 드라이버 프로그램에 반환한다.

```python
newrdd.collect() # will return [1,3,5,7]
```

