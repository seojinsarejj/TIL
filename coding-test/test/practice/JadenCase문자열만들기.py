# 1차 --- 43.8 / 100.0
def solution(s):
    change = list(map(lambda x : x[0].upper() + x[1:].lower(),s.split()))
    return " ".join(change)


print(solution("3people unFollowed me"))
