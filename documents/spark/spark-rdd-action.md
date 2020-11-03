# 기본 RDD 액션

## count()

구문:
`RDD.count()`

- count() 액션은 인수를 취하지 않고, RDD에 있는 요소의 수를 나타내는 long 값을 반환한다.

## collect()

구문:
`RDD.collect()`

- RDD의 모든 요소를 포함하는 목록을 스파크 드라이버에 반환한다.
- 일반적으로 작은 규모의 RDD나 개발에만 유용하다.

## take()

구문:
`RDD.take(n)`

- RDD의 첫 번쨰 n개 요소를 반환한다.

## top()

구문:
`RDD.top(n, key=None)`

- 상위 n개 요소를 반환한다.
- take() 와는 달리 요소가 내렴차순으로 반환된다.
