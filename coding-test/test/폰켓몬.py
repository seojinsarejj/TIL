# 1차 --- 30.0 / 100.0
import itertools
def solution1(nums):
    n = len(nums)//2    
    comb = list(itertools.combinations(nums,n))
    comb = list(map(len,list(map(set,comb))))
    return max(comb)




# 2차 --- 성공
def solution2(nums):
    n = len(nums)//2

    set_nums = set(nums)

    if len(set_nums) > n:
        return n

    return len(set_nums)

print(solution2([3,3,3,2,2,4]))