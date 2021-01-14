def solution(land):
    
    stack = [(0,-1)]
    
    for i in land:
        m = max(i) 
        idx = i.index(m)
        if i.index(m) == stack[-1][1] :
            m = max(i[:idx] + i[idx+1:])
            idx = i.index(m)
        stack.append((m,idx))
        
    return sum(map(lambda x:x[0],stack))



# 2차 --- 풀이 참조 해결
def solution2(land):
    
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            
    return max(land[-1])


land = [1,2,3,4,4]
print(land[5])
print(solution2([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))