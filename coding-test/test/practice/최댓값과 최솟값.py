def solution(s):
    num = list(map(int,s.split()))
    print(num)
    return str(min(num)) + " " + str(max(num))


print(solution("1 2 3 4"))