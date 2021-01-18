# 1차 --- 성공
def solution(n):
    
    answer = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
            
    return answer    
            
# 다른 사람의 풀이
def other_solution(n):
    return bin(n).count('1')
