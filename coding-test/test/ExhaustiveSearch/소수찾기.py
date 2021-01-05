# 1차 --- 성공
import itertools
def solution(numbers):


    number = [num for num in numbers]
    result = [int(num) for num in number if num in ['2','3','5','7']]
    
    
    for i in range(2,len(numbers)+1):
        arr = itertools.permutations(number,i)
        for j in list(arr):
            num = int("".join(list(j)))
            if num == 1 or num == 0:
                break
            for n in range(2,num):
                if num % n == 0 :
                    break
            else: result.append(num)
    
    result = set(result)
    
    return len(result)

        

print(solution("17"))
print(solution("011"))
print(solution("0011"))



# 다른 사람의 풀이 

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)