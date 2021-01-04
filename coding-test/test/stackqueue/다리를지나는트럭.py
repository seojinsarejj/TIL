# 1차 --- 성공

from collections import deque

def solution1(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    queue = deque()
    time = 1
    count = deque()

    while queue or truck_weights:
        
        if truck_weights and sum(queue) + truck_weights[0] <= weight:
            queue.append((truck_weights.popleft()))
            count.append(time)
        
        time += 1
        if time - count[0] == bridge_length :
            queue.popleft()
            count.popleft()
        
    return time


print(solution1(2,10,[7,4,5,6]))
print(solution1(100,100,[10]))
print(solution1(100,100,[10,10,10,10,10,10,10,10,10,10]))


