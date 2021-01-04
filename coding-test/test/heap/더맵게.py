# 1차 --- 정답
import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    count = 0
    
    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second*2
        heapq.heappush(scoville,new)
        count += 1
        if scoville[0] >= K or len(scoville) <= 2:
            break
        
    if scoville[0] < K:
        return -1
    
    return count