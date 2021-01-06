# 1차 --- 67.9 / 100.0
import itertools
def solution(clothes):
    
    clothes = [count for cloth,count in clothes]
    count = len(clothes)
    
    for i in range(2,len(clothes)+1):
        comb = list(itertools.combinations(clothes,i))
        for j in range(len(comb)):
            if i == len(set(comb[j])) :
                count += 1
    
    return count

# 2차 --- 
import itertools
import collections
def solution2(clothes):

    clothes = [kind for cloth,kind in clothes]
    count = collections.Counter(clothes)
    arr = []
    result = len(clothes)

    for i in range(2,len(count)+1):
        comb = list(itertools.combinations(count.values(),i))
        arr += comb

    print(result)
    print(arr)
    for i in arr :
        multiple = 1
        for k in list(i):
            multiple *= k
        result+=multiple
    return sum(result)

print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    

# 다른 사람의 풀이
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer