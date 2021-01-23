# 1차 --- 70.0 / 100.0
def solution(n):    
    
    num = "124"
    index = 3
    answer = ""
    
    while n > 0:
        
        index = len(num)
        r = n % index
        answer += num[r-1]
        n = n - index
        num = "1" * index + "2" * index + "4" * index
        
        
    return answer[::-1]


print(solution(18234))