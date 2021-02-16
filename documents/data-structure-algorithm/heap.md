# 힙 ( Heap )

> 우선 순위 큐를 위하여 만들어진 자료구조

![heap](../../images/heap.gif "heap")

## 우선 순위 큐 ( Priority Queue )

> 우선순위의 개념을 큐에 도입한 자료 구조

- 데이터들이 우선순위를 가지고 있고 우선순위가 높은 데이터가 먼저 나간다.

## 힙(heap)이란

- **완전 이진 트리의 일종**으로 우선순위 큐를 위하여 만들어진 자료구조이다.
- 여러 개의 값들 중 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조
- **반정렬 상태**를 유지한다.
  - 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있다는 정도
  - 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰(작은) 이진트리
- 힙 트리는 중복된 값을 허용한다. ( 이진 탐색 트리는 허용하지 않는다. )

## 구현

### 모듈 임포트

```python
import heapq
```

### 최소 힙 생성

- `heapq` 모듈은 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와준다.

```python
heap = []
```

### 힙에 원소 추가

```python
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)
```

```python
[1,3,7,4]
```

### 힘에서 원소 삭제

```python
print(heapq.heappop(heap))
print(heap)
```

```python
1
[3,4,7]
```

### 기존 리스트를 힙으로 변환

```python
heap = [4,1,7,3,8,5]
heapq.heapify(heap)
print(heap)
```

```python
[1,3,4,5,7,8]
```
