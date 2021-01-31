# 1차 --- 33.3 / 100.0
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
        
        for j in range(i,n-i):
            arr[j][i] = index
            index += 1
            if index > m :
                return sum_arr(arr)
                
        for j in range(i+1,n-i*2):
            arr[n-1-i][j] = index
            index += 1
            if index > m :
                return sum_arr(arr)

        for j in range(i+1,n-2-i):
            arr[n-1-j][-1*(i+1)] = index
            index += 1
            if index > m :
                return sum_arr(arr)



            
            