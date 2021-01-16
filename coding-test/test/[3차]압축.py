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