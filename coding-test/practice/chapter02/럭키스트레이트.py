def solution(n):
    s = str(n)
    middle = len(s)//2

    first = s[:middle]
    second = s[middle:]

    first = list(map(int,first))
    second = list(map(int,second))

    if sum(first) == sum(second) :
        return "LUCKY"
    
    return "READY"


print(solution("123402"))
print(solution("7755"))
