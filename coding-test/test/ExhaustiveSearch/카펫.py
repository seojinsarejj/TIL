# 완전탐색
# 1차 --- 성공

def solution(brown, yellow):
    
    total = brown + yellow
    
    num = [i for i in range(1,yellow+1) if yellow%i==0]
    
    for i in num:
        if (i+2) * (yellow//i + 2) == total:
            return [yellow//i + 2,i+2]
        
    
# 다른 사람의 풀이
def solution2(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow% i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]
    