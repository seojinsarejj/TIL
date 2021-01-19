# 1차 --- 성공
import math
def solution(n, words):
    
    stack = [words[0]]
    
    for i in words[1:]:
        if i not in stack and i[0] == stack[-1][-1]:
            stack.append(i)
        else :
            turn = math.ceil((len(stack)+1) / n)
            num = (len(stack)+1) % n
            if num == 0:
                num = n
            return [num,turn]
        
    return [0,0]

print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))

# 다른 사람의 풀이
def other_solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]