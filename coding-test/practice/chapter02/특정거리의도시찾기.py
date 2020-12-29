# [[1,2],[1,3],[2,3],[2,4]]
# 1차 
'''
from collections import deque

def solution(n,m,road,k,start):
    
    distance = [-1 for _ in range(n+1)]
    print(distance)
    distance[0] = 0
    distance[start] = 0
    # 0 0 1 1 -1
    queue = deque()
    while -1 in distance :
        linked_road = []
        for i in range(m):
            if start in road[i]:
                linked_road += road[i]
        
        linked_road = [i for i in linked_road if i != start]
        for i in linked_road:
            if distance[i] == -1 :

                distance[i] = distance[start] + 1
                queue.append(i)
        start = queue.popleft()


    if k not in distance :
        return -1
    
    result = [i for i in distance if i == k]

    return result
    

print(solution(4,4,[[1,2],[1,3],[2,3],[2,4]],2,1))
print(solution(4,3,[[1,2],[1,3],[1,4]],2,1))
print(solution(4,4,[[1,2],[1,3],[2,3],[2,4]],1,1))
'''
