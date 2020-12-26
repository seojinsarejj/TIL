def solution(data):

    data.sort()
    #1,2,2,2,3
    result = 0
    count = 0

    for i in data:
        count += 1
        if i <= count:
            result += 1
            count = 0
    
    return result

print(solution([2,3,1,2,2]))
print(solution([1,3,3,4,1,5,2,1,5]))
1 1 1 2 3 3 4 5 5