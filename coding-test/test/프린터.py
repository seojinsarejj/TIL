# 1차 --- 85.0/100.0
from collections import deque

def solution1(priorities, location):
    
    count = 0
    priorities = list(enumerate(priorities, start=0))
    queue = deque()
    
    for i,j in priorities:
        queue.append((j,i))

    if queue != []:
        return queue[0][0]

    n = queue.popleft()

    while len(queue) != 0:

        n = queue.popleft()

        if max(queue)[0] > n[0] :
            queue.append(n)
        else :
            count += 1
            if n[1] == location:
                return count

    return 0

print(solution1([2,1,3,2],2))
print(solution1([4,6],0))


# 2차 --- 성공
from collections import deque

def solution2(priorities, location):
    
    count = 0
    priorities = list(enumerate(priorities, start=0))
    queue = deque()
    
    for i,j in priorities:
        queue.append((j,i))

    if len(queue) == 1:
        return queue[0][0]

    n = queue.popleft()

    while len(queue) != 0:

        if max(queue)[0] > n[0] :
            queue.append(n)
        else :
            count += 1
            if n[1] == location:
                return count
        
        n = queue.popleft()

    return count + 1

print(solution2([2,1,3,2],2))
print(solution2([4,6],0))