# 1차 --- 성공
def solution(s):
    
    stack = []
    
    for num in s:
        if stack == []:
            stack.append(num)
        elif num == stack[-1]:
            stack.pop()
        else:
            stack.append(num)
        
            
    if stack == []:
        return 1
    
    return 0
        