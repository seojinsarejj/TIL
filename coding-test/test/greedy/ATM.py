# 백준 11399

# 1차 --- 정답
def solution(n, time):
    # 3 1 4 3 2
    time.sort()
    # 1 2 3 3 4
    time_total = []

    for i in range(n):
        if i == 0:
            time_total.append(time[i])
        else :
            time_total.append(time_total[i-1] + time[i])
        
    return sum(time_total)


print(solution(5,[3,1,4,3,2]))
        