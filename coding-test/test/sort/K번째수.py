# 1차 --- 정답
def solution(array, commands):
    
    result = []
    
    for command in commands:
        new_array = array[command[0]-1:command[1]]
        new_array.sort()
        result.append(new_array[command[2]-1])
        
    return result


# 다른 사람의 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

    