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
            

print(solution2([6,10,2]))
print(solution2([3, 30, 34, 5, 9]))
print(solution2([40, 403]))

