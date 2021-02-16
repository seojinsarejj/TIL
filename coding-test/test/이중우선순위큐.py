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

# 2차 --- 성공
import heapq

def sort_heap(heap):
    sort_heap = []

    for i in range(len(heap)):
        sort_heap.append(heapq.heappop(heap))
    
    heap = sort_heap

    return heap

def solution2(operations):
    
    heap = []
    
    for o in operations:

        operation = o.split(" ")
        
        heap = sort_heap(heap)

        if operation[0] == "I":
            heapq.heappush(heap,int(operation[1]))
        else :
            if heap:
                if operation[1] == "1":
                    heap = heap[:-1]
                else :
                    heapq.heappop(heap)
                    
    if heap:
        heap = sort_heap(heap)
        return [heap[-1],heap[0]]
    
    return [0,0]
