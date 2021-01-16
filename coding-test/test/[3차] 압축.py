# 1차 --- 성공!
def solution(msg):
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = 1
    dic = dict()
    answer = []
    
    for i in alpha:
        dic[i] = num
        num += 1
        
    index = 0
    
    while True:
        temp = msg[index] 
        while True :
            if temp in dic.keys():
                index += 1
                if index == len(msg):
                    answer.append(dic[temp])
                    break
                temp += msg[index]
            else :
                dic[temp] = num
                num += 1
                answer.append(dic[temp[:-1]]) 
                break
        if index == len(msg):
            break
        
                
    return answer


print(solution("KAKAO"))


# 다른 사람의 풀이

def other_solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer