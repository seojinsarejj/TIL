# 1차 --- 83.3 / 100.0
import heapq
def solution(operations):
    
    heap = []
    
    for o in operations:
        print(heap)
        operation = o.split(" ")
        
        if operation[0] == "I":
            heapq.heappush(heap,int(operation[1]))
        else :
            if heap:
                if operation[1] == "1":
                    heap = heap[:-1]
                else :
                    heapq.heappop(heap)
                    
    if heap:
        return [heap[-1],heap[0]]
    
    return [0,0]



