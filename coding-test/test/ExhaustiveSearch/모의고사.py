# 1차 --- 성공
import math
def solution(answers):
    
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c  = [3,3,1,1,2,2,4,4,5,5]
    count = [[0,1],[0,2],[0,3]]
    
    a = a * math.ceil(len(answers)/len(a))
    b = b * math.ceil(len(answers)/len(b))
    c = c * math.ceil(len(answers)/len(c))

    
    for i in range(len(answers)):
        if answers[i] == a[i] : count[0][0] += 1
        if answers[i] == b[i] : count[1][0] += 1
        if answers[i] == c[i] : count[2][0] += 1
    
    high = max(count)[0]
    
    count = [j for i,j in count if i == high]
    
    return count


# 2차 --- 수정
import math
def solution2(answers):
    
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c  = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    
    a = a * math.ceil(len(answers)/len(a))
    b = b * math.ceil(len(answers)/len(b))
    c = c * math.ceil(len(answers)/len(c))

    
    for i in range(len(answers)):
        if answers[i] == a[i] : count[0] += 1
        if answers[i] == b[i] : count[1] += 1
        if answers[i] == c[i] : count[2] += 1
    
    high = max(count)
    
    count = [i+1 for i,j in enumerate(count) if j == high]
    
    return count

# 다른 사람의 풀이
def solution3(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]