# 1차 --- 50.0 / 100/0
import math
def solution(w,h):
    return w*h - math.ceil(h/w) * w


# 2차
import math
def solution2(w,h):
    
    return math.ceil(h/w) + h

print(solution2(4,11))