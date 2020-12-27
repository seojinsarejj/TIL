# 1차 
def solution(food_times,k):
    # 3,1,2
    # 3
    n = len(food_times)
    index = 0
    for i in range(k):
        while food_times[index%n] < 1:
            index+=1
        food_times[index%n] -= 1
        index+=1


    return index%n + 1


print(solution([3,1,2],3))