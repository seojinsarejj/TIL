# 1차 --- 성공
NOTATION = "0123456789ABCDEF"
def change(total,n):
    q,r = divmod(total,n)
    m = NOTATION[r]
    return change(q,n) + m if q else m
    

def solution(n, t, m, p):
    
    answer = ""
    total = t * m
    
    result = ""
    i = 0
    while len(result) < total:
        result += change(i,n)
        i += 1

    result = result[:total]
    for i in range(1,len(result)+1):
        if (i % m == 0 and p == m) or i % m == p :
            answer += result[i-1]
        
    return answer


