# 파이썬 큐 구현

## list
> list로 구현하는 방식. 성능 면에서 좋지 않음

```python
queue = [4, 5, 6]
# 삽입
queue.append(7)
queue.append(8)

# 삭제
queue.pop(0)
>> 4
queue.pop(0)
>> 5
```

## deque
> collections 모듈의 deque로 구현. 양방향 삽입, 삭제를 지원

```python
from collections import deque

queue = deque([4,5,6])

# 삽입
queue.append(7)
queue.append(8)

# 삭제
queue.popleft()
>> 4
queue.popleft()
>> 5
```

## Queue
> queue 모듈의 Queue 클래스를 사용하여 구현

```python
from queue import Queue

queue = Queue()

# 삽입
que.put(4)
que.put(5)
que.put(6)

# 삭제
queue.get()
>> 4
queue.get()
>> 5
queue.get()
>> 6