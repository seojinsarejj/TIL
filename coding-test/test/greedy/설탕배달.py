# 백준 2839번

# 1차 --- 정답
def solution(n):

    cnt = 0

    while n > 0:
        if n % 5 == 0 :
            cnt += n//5
            break
        n -= 3
        cnt += 1

    if n < 0 :
        return -1

    return cnt

print(solution(18)) #4
print(solution(4)) # -1
print(solution(6)) # 2
print(solution(9)) # 3
print(solution(11)) # 3