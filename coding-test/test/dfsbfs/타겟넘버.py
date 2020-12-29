# 1차 
'''
def solution(numbers, target):
    
    start = 0
    len_numbers = len(numbers) # 5
    stack = []
    count = 0
    
    def dfs(a,start):
        
        
        if start >= len_numbers:
            if sum(stack) == target:
                count += 1
            stack.pop()
            return True

        if start < len(stack):
            stack.pop()
            
        stack.append(a * numbers[start])
        dfs(-1, start+1)
        dfs(1, start+1)
        
    dfs(1,start)
    print(count)
    
    return count
        
 '''   

# 2차 --- 100.0
count = 0
def solution(numbers, target):
     
    global count
    
    def dfs(a,index,sum):
        
        global count
        if index == len_numbers:
            if sum == target:
                count += 1
            return

        sum += (a * numbers[index])

        dfs(-1, index+1,sum)
        dfs(1, index+1,sum)
        

    index = 0
    len_numbers = len(numbers) # 5
   
    dfs(1,index,0)
    dfs(-1,index,0)
    return count//2

print(solution([1,1,1],1)) # 2

        
#                           0
#                -1                         1
#           -1       1                -1        1
#         -1  1    -1  1            -1   1    -1  1


# 다른 사람의 풀이 --- 이렇게 간단한 거라니...현타온다...


def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])