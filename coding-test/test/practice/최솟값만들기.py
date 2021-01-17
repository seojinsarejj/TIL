# 1차 --- 성공
def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    result = 0
    
    for i,j in zip(A,B):
        result += i * j
        
    return result


# 다른 사람의 풀이
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))