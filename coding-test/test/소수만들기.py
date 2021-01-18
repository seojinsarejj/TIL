# 1차 --- 성공
import itertools
def solution(nums):
    
    comb = list(itertools.combinations(nums,3))
    count = 0
    
    for num in comb:
        s = sum(num)
        for i in range(2, s // 2 +1):
             if s % i == 0 :
                    break
        else : count += 1
    
    return count
    