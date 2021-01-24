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