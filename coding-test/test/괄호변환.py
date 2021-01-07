# 1차 --- 정답
def test_right(p):
    stack = []
    
    for i in p:
        if i == "(" :
            stack.append(i)
        else :
            try:
                stack.pop()
            except:
                return False
    if stack == []:
        return True
    
    return False


def reverse(p):
    
    result =""

    for i in p:
        if i == "(" :
            result+= ")"
        else :
            result+="("
            
    return result

def divide(p):
    
    if p == "":
        return ""
    
    stack =[]
    
    stack.append(p[0])
    index = 0
    while True:
        index += 1
        
        if stack == []:
            break
        elif stack[-1] != p[index] :
            stack.pop()
        else :
            stack.append(p[index])
        
    u = p[:index]
    v = p[index:]
    
    if test_right(u) :
        return u + divide(v)
    else:
        return "(" + divide(v) + ")" + reverse(u[1:-1])
    

def solution(p):
    
    if test_right(p) == True or p == "":
        return p
    
    else : return divide(p)
        
        
        
# 다른 사람의 풀이 
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


print(solution("(()())()")) # "(()())()"   
print(solution(")(")) # "()"
print(solution("()))((()")) #()(())()""         