# 1차 --- 시간 초과

import itertools

def solution1(numbers):
    
    numbers = list(map(str,numbers))
    comb = list(itertools.permutations(numbers,len(numbers)))

    num = list(map(lambda x : int("".join(list(x))),list(comb)))
    num.sort()

    return str(num[-1])

# 2차 --- 36.4/100

def solution2(numbers) :
        # 6 10 2
        #[3, 30, 34, 5, 9]
        result = []

        for i in range(len(numbers)):
            num_len = len(str(numbers[i]))
            if num_len != 1 :
                value = numbers[i] / (10**(num_len-1))
            else :
                value = numbers[i] * 1.1
            result.append((numbers[i],value))

        result.sort(key=lambda x : x[1],reverse=True)
        print(result)

        answer = "".join(list(map(lambda x : str(x[0]), result)))

        return answer
            

# 3차 --- 45.5

def solution3(numbers) :
        # 6 10 2
        #[3, 30, 34, 5, 9]
        result = []

        if max(numbers) == 0 : 
            return "0"

        for i in range(len(numbers)):
            num_len = len(str(numbers[i]))
            if num_len != 1 :
                value = numbers[i] / (10**(num_len-1))
                value += value/ 10**num_len
                value += value/ 10**num_len**2
            else :
                value = numbers[i] * 1.1
            result.append((numbers[i],value))

        result.sort(key=lambda x : x[1],reverse=True)

        answer = "".join(list(map(lambda x : str(x[0]), result)))

        return answer

# 다른 사람의 풀이 --- 정답

def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)
    return str(int(''.join(numbers)))


print(solution3([6,10,2]))
print(solution3([3, 30, 34, 5, 9]))
print(solution3([40, 403]))
print(solution3([10, 101]))
print(solution3([1,11,111,1111]))
print(solution3([0,0,0,0,0,0]))

# [(403, 4.03), (40, 4.0)]

