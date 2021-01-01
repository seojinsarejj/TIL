def solution(s):
    
    alpha = []
    result = 0

    for i in s:
        if i.isalpha():
            alpha.append(i)
        else : result += int(i)

    alpha.sort()

    return "".join(alpha) + str(result)





print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))