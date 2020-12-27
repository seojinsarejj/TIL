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


# 2차 --- 정답
'''
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
'''

# 3차 --- 수정

def solution(n,lost,reserve):

    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)


    return n-len(_lost)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(5,[1,3,5],[1,2,6]))
print(solution(5,[1,5,6],[2,6,7]))