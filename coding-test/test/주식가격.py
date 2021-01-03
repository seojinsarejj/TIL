# 1차 --- 정답
def solution(prices):
    
    result = []
    
    for i in range(len(prices)):
        for j in range(i+1,len(prices)) :
            if prices[j] < prices[i] :
                result.append(j - i) 
                break
        else : result.append(len(prices)-1-i)
            
            
    return result


# 다른 사람의 풀이 --- 큐 사용
from collections import deque
def solution2(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
    