# 1차 --- 5.9 / 100.0
def solution(n,a,b):
    
    lst = [i for i in range(1, n+1)]
    meet = set([a,b])
    count = 1
    
    while len(lst) > 2:
        winner = []
        count += 1
        for i in range(1,len(lst)+1,2):
            match = lst[i:i+2]
            
            if set(match) == meet: 
                return count 
            
            if a in match : winner.append(a)
            elif b in match : winner.append(b)
            else: winner.append(i)
        lst = winner
        
    return 0

# 2차 --- 29.4 / 100.0
def solution2(n,a,b):
    
    lst = [i for i in range(1, n+1)]
    meet = set([a,b])
    count = 0
    
    while len(lst) > 2:
        winner = []
        count += 1
        for i in range(0,len(lst),2):
            match = lst[i:i+2]
            if set(match) == meet: 
                return count 
            
            if a in match : winner.append(a)
            elif b in match : winner.append(b)
            else: winner.append(lst[i])
        lst = winner
        
    return count

# 3차 --- 성공
def solution3(n,a,b):
    
    lst = [i for i in range(1, n+1)]
    meet = set([a,b])
    count = 0
    
    while len(lst) >= 2:
        winner = []
        count += 1
        for i in range(0,len(lst),2):
            match = lst[i:i+2]
            if set(match) == meet: 
                return count 
            
            if a in match : winner.append(a)
            elif b in match : winner.append(b)
            else: winner.append(lst[i])
        lst = winner
        
    return count

print(solution3(8, 1, 2))
print(solution3(8, 2, 3))
print(solution3(8, 4, 7))
