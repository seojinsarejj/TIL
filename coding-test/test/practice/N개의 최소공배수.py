# 1차 --- 성공
def solution(arr):
    
    sum = 1
    for i in arr:
        sum *= i
    
    for i in range(1,sum):
        for j in arr:
            if i % j != 0:
                break
        else :
            return i
    
    return sum