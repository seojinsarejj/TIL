def solution(s):
    lst0to1 = [z for z in s.split("1") if z != ""]
    lst1to0 = [z for z in s.split("0") if z != ""]
    return min(len(lst0to1),len(lst1to0))


print(solution("0001100"))
