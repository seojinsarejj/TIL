# itertools를 이용하여 순열,조합 구현하기

## 순열 (permutations)

- 반복 가능한 객체에 대하여 중복을 허용하지 않고 r개를 뽑아 나열한다.
- 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 취급
- permutations(반복 가능한 객체, r)

```python
from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=" ")
```

```bash
(1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)
```

## 조합 (combinations)

- 반복 가능한 객체에 대하여 중복을 허용하지 않고 r개를 뽑는다.
- 뽑은 순서는 고려하지 않기 때문에 순서가 다르더라도 중복된다면 무시한다.
- combination(반복 가능한 객체, r)

```python
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")
```

```bash
(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
```
