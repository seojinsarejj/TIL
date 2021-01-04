# 1차 --- 정답
import math
def solution(progresses, speeds):
    
    remain = [100-i for i in progresses]
    days = [math.ceil(i/j) for i,j in zip(remain,speeds)]
    
    result = []
    max_num = days[0]
    count = 1
    for i in days[1:]:
        if i > max_num:
            result.append(count)
            count = 0
            max_num = i
        count += 1
            
    result.append(count)
    
    return result