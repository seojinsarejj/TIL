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