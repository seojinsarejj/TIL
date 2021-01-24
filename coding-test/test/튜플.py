# 1차 --- 성공
def solution(s):
    
    s = [list(map(int,i)) for i in [i.split(",") for i in s[2:-2].split("},{")]]
    s.sort(key=lambda x : len(x))
    
    answer = []
    
    for i in s:
        answer += list(i)

    result = []

    for i in answer:
        if i not in result:
            result.append(i)            
    
    
    return result
    
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# 다른 사람의 풀이
import re
from collections import Counter
def other_solution(s):
    
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))