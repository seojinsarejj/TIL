
from collections import deque

def solution(n,m,graph):


    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    x =0
    y = 0

    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]
            
    
    

graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

graph2 = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]

print(solution(5,6,graph))
print(solution(3,3,graph2))