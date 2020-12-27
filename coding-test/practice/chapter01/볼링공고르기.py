# 1차
def solution(ball):

    n = len(ball)
    cnt = 0
    for i in range(n):
        if ball[i] in ball[i+1:]:
            cnt += 1

    return n * (n-1) // 2 - cnt


print(solution([1,5,4,3,2,4,5,2]))


# 2차