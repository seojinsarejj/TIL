# 프로그래머스 큰수만들기

# 1차 --- 83.3/100
'''
def solution(number, k):
    
    
    number_lst = [int(num) for num in number]
    answer = []
    
    total_num = len(number_lst) - k
    
    for i in range(total_num):
        
        if i == 0:
            start = 0
            end = -1 * (total_num - 1)
            temp = number_lst[:end]
        elif i == total_num-1 :
            start = start + temp.index(answer[i-1]) + 1 
            temp = number_lst[start:]
        else :
            start = start + temp.index(answer[i-1]) + 1
            end = (i - (total_num - 1))
            temp = number_lst[start:end]
        
        answer.append(max(temp))
        
    return "".join([str(num) for num in answer]) 
    
        
    
# print(solution("1924",2))
# print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("35",1))

'''
# 2차 --- 91.7/100
'''
def solution(number, k):
    
    
    number_lst = [int(num) for num in number]
    answer = []
    
    total_num = len(number_lst) - k

    if total_num == 1:
        return str(max(number_lst))
    

    start = 0
    end = -1 * (total_num - 1)
    temp = number_lst[:end]

    answer.append(max(temp))

    for i in range(1,total_num-1):
    
        start = start + temp.index(answer[-1]) + 1
        end = (i - (total_num - 1))
        temp = number_lst[start:end]
        
        answer.append(max(temp))


    start = start + temp.index(answer[-1]) + 1 
    temp = number_lst[start:]
    answer.append(max(temp))
    
        
    return "".join([str(num) for num in answer]) 
    
        
    
print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("35",1))
'''

# 3차 --- 해설 확인


def solution(number, k):
    # stack에 입력값을 순서대로 삽입 
    stack = [number[0]]
    for num in number[1:]:
        # 231234
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
        # 참고 : len(stack) > 0 == stack
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거 
            k -= 1
            # 내부의 값을 제거 
            stack.pop()
        # 새로운 값을 삽입 
        stack.append(num)
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문 
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
    
print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
#775841
print(solution("35",1))