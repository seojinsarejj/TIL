# 코딩테스트에서 유용한 함수

## 내장 함수 (Built-in Function)

### zip
- 두 iterable한 인자를 묶어 튜플 배열로 반환한다.

```python
a = [1,2,3,4]
b = ['a','b','c','d']

for i,j in zip(a,b) :
    print(i,j)
```

```bash
1 a
2 b
3 c
4 d
```

### enumerate
- 인덱스를 값과 함께 반환한다.

```python
a = ['a','b','c','d']

for i,j in enumerate(a):
    print(i,j)
```

```bash
0 a
1 b
2 c
3 d
```

### set
- 집합 자료형 생성
- 중복을 허용하지 않으며, 순서가 없다.

```python
s1 = set([1,2,3])
s1
```

```bash
{1,2,3}
```

#### union, intersection, difference
- 각각 합집합, 교집합, 차집합을 구하는 함수

```python
a = set([1,2,3])
b = set([2,3,4])

a | b  # {1, 2, 3, 4}
a & b  # { 2, 3 }
a - b  # {1}
```

### sorted with key
- 정렬 시 정렬 기준을 설정 가능하다.

```python
a = [['b',1],['a',0],['d',3],['c',4]]

a = sorted(a, key=lambda x : x[1]) # key로 람다함수를 사용
print(a)
```

```bash
[['a', 0], ['b', 1], ['d', 3], ['c', 4]]
```

## itertools

### permutations
- r개의 데이터를 뽑아 나열하는 모든 경우(순열)

```python
from itertools import permutations

data = ['A','B','C']

result = list(permutations(data,3))

print(result)
```
```bash
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

### combinations
- r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합, 중복을 허용하지 않음)

```python
from itertools import combinations

data = ["A", "B", "C"] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)
```

```bash
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

## collections

### Counter
- 횟수를 세는 함수

```python
from collections import Counter

data = ['A','B','C','A','C','C']

result = Counter(data)

print(dict(result))
```

```bash
{'C': 3, 'A': 2, 'B': 1}
```

### deque
- 큐를 쉽게 구현할 수 있는 라이브러리

#### 함수
- popleft() : 첫 번째 원소 제거
- appendleft() : 첫 번째 원소 삽입
- pop() : 마지막 원소 제거
- append() : 마지막 원소 삽입

```
from collections import deque

data = deque([2, 3, 4])
data.append(5)

print(data) # deque([2, 3, 4, 5])
print(data.popleft()) # 2
print(list(data)) # [3, 4, 5]
```