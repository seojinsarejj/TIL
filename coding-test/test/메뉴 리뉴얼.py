# 1차 --- 15.0 / 100.0
import itertools
def solution(orders, course):
    
    result = []
    
    for order in range(len(orders)):
        for i in orders[order+1:]:
            inter = set(orders[order]) & set(i)
            if len(inter) in course:
                inter = sorted(list(inter))
                result.append("".join(inter))
    
    result = sorted(list(set(result)))
    return result

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))