# 1차 --- 70.0 / 100.0
def solution(n):    
    
    num = "124"
    index = 3
    answer = ""
    
    while n > 0:
        
        index = len(num)
        r = n % index
        answer += num[r-1]
        n = n - index
        num = "1" * index + "2" * index + "4" * index
        
        
    return answer[::-1]



# 2차 --- 성공
import math
def solution2(n):    
    
    num = "124"
    index = 3
    answer = ""
    
    while n > 0:
        
        answer += num[math.ceil(n % index / (index // 3))- 1]
        n -= index
        index *= 3
            
    return answer[::-1] 

print(solution2(4))

# 다른 사람의 풀이
def change124(n):
    num = ['1','2','4']
    answer = ""
    
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

print(change124(10))