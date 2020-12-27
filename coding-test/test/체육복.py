# 1차
'''
def solution(n, lost, reserve):
    
    lost_lst = lost[:]


    for i in lost:
        if (i-1) in reserve:
            lost_lst.remove(i)
            reserve.remove(i-1)
            
        elif (i+1) in reserve:
            lost_lst.remove(i)
            reserve.remove(i+1)

    return n-len(lost_lst)


print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
'''
# 2차

def solution(n, lost, reserve):
    
    lost_lst = lost[:]

    for i in lost:
        if i in reserve:
            lost_lst.remove(i)
            reserve.remove(i)
    
    lost = lost_lst[:]
    
    for i in lost
        if (i-1) in reserve:
            lost_lst.remove(i)
            reserve.remove(i-1)
        elif (i+1) in reserve:
            lost_lst.remove(i)
            reserve.remove(i+1)

    return n-len(lost_lst)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(5,[1,3,5],[1,2,6]))
print(solution(5,[1,5,6],[2,6,7]))