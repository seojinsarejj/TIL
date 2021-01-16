# 1차 --- 43.8 / 100.0
def solution1(s):
    change = list(map(lambda x : x[0].upper() + x[1:].lower(),s.split()))
    return " ".join(change)

# 2차 --- 성공
def solution2(s):
    answer = s[0].upper()
    
    for i in range(1,len(s)):
        if s[i] != " " and s[i-1] == " " :
            answer += s[i].upper()
        else :
            answer += s[i].lower()
    
    return answer

print(solution2("3people     u me"))

# 다른 사람의 풀이 --- ........하
def solution(s):
    return s.title()
