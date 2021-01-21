# 1차 --- 성공
def solution(cacheSize, cities):
    
    lst = []
    count = 0
    
    for i in cities:
        i = i.lower()
        if i not in lst:
            lst.append(i)
            if len(lst) > cacheSize:
                lst = lst[1:]
            count += 5
        else:
            lst.remove(i)
            lst.append(i)
            count += 1
            
    return count
    
    