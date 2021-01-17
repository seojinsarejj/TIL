# 1차 --- 82.1 / 100.0
# import itertools
# def solution(relation):
#     row = len(relation)
#     col = len(relation[0])
#     result = 0
#     remain =[]
    
    
#     for i in range(col):
#         r = [item[i] for item in relation]
#         if row == len(set(r)):
#             result += 1
#         else:
#             remain.append(i)
    
#     temp = []
    
#     for num in range(2,col+1):
#         comb = list(itertools.combinations(remain,num))
#         for item in comb:
#             r = []
#             for rw in relation:
#                 a = []
#                 for i in item:
#                     a.append(rw[i])
#                 r.append(tuple(a))
#             if row == len(set(r)):
#                 result += 1
#                 temp += list(item)
#         remain = [i for i in remain if i not in set(temp)]
#         # print(temp)
#         # print(remain)
#     return result

# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# print(solution(relation))

# relation = [["b","2","a","a","b"],["b","2","7","1","b"],["1","0","a","a","8"],["7","5","a","a","9"],["3","0","a","f","9"]]
# print(solution(relation))


# 2차 --- 성공
import itertools
def check_mini(key,item):
    item = set(item)
    
    for k in key:
        k = set(k)
        if k == k.intersection(item) :
            return False
    return True


def solution(relation):
    row = len(relation)
    col = len(relation[0])
    result = 0
    remain =[]
    
    
    for i in range(col):
        r = [item[i] for item in relation]
        if row == len(set(r)):
            result += 1
        else:
            remain.append(i)
    
    key = []
    
    for num in range(2,col+1):
        comb = list(itertools.combinations(remain,num))
        for item in comb:
            r = [tuple([row[i] for i in item]) for row in relation]
            if row == len(set(r)) and check_mini(key,item):
                result += 1
                key.append(item)
    return result

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))

relation = [["b","2","a","a","b"],["b","2","7","1","b"],["1","0","a","a","8"],["7","5","a","a","9"],["3","0","a","f","9"]]
print(solution(relation))


# 다른 사람의 풀이
from collections import deque
from itertools import combinations
def other_solution(relation):
    n_row=len(relation)
    n_col=len(relation[0])  #->runtime error 우려되는 부분

    candidates=[]
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))

    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp))==n_row:
            final.append(keys)

    answer=set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)
