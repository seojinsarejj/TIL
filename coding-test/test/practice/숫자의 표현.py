# 1차 --- 성공
def solution(n):
    
    count = 0
    
    for i in range(1,n+1):
        if i % 2 != 0 and n % i == 0 or i % 2 == 0 and n % i == n * 0.5:
            count += 1
    return count