# 빅오 표기법

## 빅오 표기법이란
- 알고리즘의 효율성을 표기해주는 표기법
- 알고리즘의 시간 복잡도와 공간 복잡도를 나타내는데 주로 사용된다.

## 빅오 표기법의 특징

### 1. 계수,상수항 무시
- 데이터의 입력값(n)의 크기에 따라 영향 받기 때문에 계수는 무시한다.
- ex) O(2N) -> O(N) , O(N+1) -> O(N)

### 2. 영향력 없는 항 무시
- 데이터 입력값(n)의 크기에 따라 영향을 받기 때문에 가장 영향력이 큰 항 외에 영향력이 없는 항들은 무시한다.
- ex) O(N^2+2N+1) -> O(N^2)

## 빅오 표기법 성능 비교
![bit-o-compare](../../images/big-o-compare.png "big-o-compare")

***faster - O(1) < O(logn) < O(N) < O(nlogn) < O(n^2) < O(2^n) - slower***

## 예시

### 1. O(1)
- 입력값과 상관없이 일정한 시간이 드는 알고리즘
- 스택에서 Push, Pop
```C
int func(int N) {
    return N = N + 1;
}
```



### 2. O(N)
- N의 크기가 시간에 미치는 영향이 정비례함
- for문
```C
int func(int N) {
    int value=0;
    for(int i = 0; i < N; i++) 
        value += i;
    return value
}
```

### 3. O(N^2)
- N의 크기에 비례하여 제곱으로 상승함
- 이중for문, 삽입정렬,버블정렬,선택정렬
```C
int func(int N) {
    int value = 0;
    for (int j = 0; j < N; j++) 
        for (int i = 0; i < N; i++) 
            value += i;
    return value
}
```

### 그 외
- **O(logn)** : 이진트리
- **O(nlogn)** : 퀵 정렬, 병합정렬, 힙 정렬
- **O(2^n)** : 피보나치 수열

### 연습 문제

```python
a = 5 # Constant 1
b = 6 # Constant 1
c = 10 # Constant 1
for i in range (n) :
    for j in range (n) :
        x = i * i # n^2 => for문 중첩 사용
        y = j * j # n^2
        z = i * j # n^2
    for k in range (n) :
        w = a*k + 45 # n
        v = b*b # n
    d = 33 # Constant 1
```

- 각 연산 횟수를 더하면 시간 복잡도는 아래와 같다.
- T(n) = 3 + 3n^2 + 2N + 1 = 3n^2 + 2N + 4
- 이를 Big-O로 표기하면 O(n^2) 이다.