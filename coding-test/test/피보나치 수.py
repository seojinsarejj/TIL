# 1차 --- 85.7 / 100.0
def solution(n):
    
    memo = [0] * (n+1)
    
    def fibo(n):
        if n <= 2:
            return 1
        if memo[n] : return memo[n]
        memo[n] = fibo(n-2) + fibo(n-1)
        return memo[n]
    
    return fibo(n)%1234567

print(solution(5))