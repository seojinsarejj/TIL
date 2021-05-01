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