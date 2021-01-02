# 1차 --- 정답
def solution(citations):
    
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= n-i :
            return len(citations[i:])
    
    return 0



# 다른 사람의 풀이
def solution(citations):
    # 3,0,6,1,5
    citations.sort(reverse=True)
    # 6 5 3 1 0
    answer = max(map(min, enumerate(citations, start=1)))
    # 6,1 5,2 3,3 1,4 0,5
    # 1 2 3 1 0
    # 3
    return answer

    