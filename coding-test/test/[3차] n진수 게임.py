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


# 다른 사람의 풀이
big = ["A","B","C","D","E","F"]
def other_solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer