# 1차 --- 33.3 / 100.0
# def sum_arr(arr):
#     result = []
    
#     for i in arr:
#         result += i
    
#     return result

# def solution(n):
    
#     index = 1
#     arr = [[1 for _ in range(i)] for i in range(1,n+1)]
#     m = sum([i for i in range(1,n+1)])
    
#     for i in range(n):
        
#         for j in range(i,n-i):
#             arr[j][i] = index
#             index += 1
#             if index > m :
#                 return sum_arr(arr)
                
#         for j in range(i+1,n-i*2):
#             arr[n-1-i][j] = index
#             index += 1
#             if index > m :
#                 return sum_arr(arr)

#         for j in range(i+1,n-2-i):
#             arr[n-1-j][-1*(i+1)] = index
#             index += 1
#             if index > m :
#                 return sum_arr(arr)


# 2차 --- 성공
def sum_arr(arr):
    result = []
    
    for i in arr:
        result += i

    return result

def solution(n):
    
    index = 1
    arr = [[1 for _ in range(i)] for i in range(1,n+1)]
    m = sum([i for i in range(1,n+1)])
    
    for i in range(n):
        
        for j in range(i*2,n-i):
            arr[j][i] = index
            index += 1
            if index > m :
                return sum_arr(arr)
                
        for j in range(i+1,n-i*2):
            arr[n-1-i][j] = index
            index += 1
            if index > m :
                return sum_arr(arr)  


        for j in range(i+1,n-1-i*2):
            arr[n-1-j][-1*(i+1)] = index
            index += 1
            
            if index > m :
                return sum_arr(arr)

# 다른 사람의 풀이
def other_solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0;num=1;d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d];num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])

            
            