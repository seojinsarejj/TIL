# 1차 --- 성공
def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    result = 0
    
    for i,j in zip(A,B):
        result += i * j
        
    return result