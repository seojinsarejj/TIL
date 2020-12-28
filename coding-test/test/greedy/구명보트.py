# 프로그래머스 구명보트

# 1차 --- 정확성 75.0 효율성 0.0 --- 75.0 / 100
'''
def solution(people,limit):

    people.sort()
    count = 0

    while people != [] :
        
        people_lst = [p for p in people[:-1] if p <= (limit - people[-1])]

        if people_lst  != []:
            people.remove(max(people_lst))

        people.pop()

        count += 1


    return count


print(solution([70,50,80,50],100))
print(solution([70,80,50],100))
'''

# 2차 
'''
def solution(people,limit):
    
    count = 0

    while people != [] :
        
        people_lst = [p for p in people[:-1] if p <= (limit - people[-1])]

        if people_lst  != []:
            people.remove(max(people_lst))

        people.pop()

        count += 1


    return count
'''

# 3차 --- 95.0/100
'''
def solution(people,limit):
    
    people.sort()
    count = 0

    while len(people) > 1 :
        
        if people[-1] + people[0] <= limit:
            del people[0]

        people.pop()

        count += 1

    if len(people) == 1:
        count += 1
    
    return count

print(solution([70,50,80,50],100))
print(solution([70,80,50],100))
'''

# 해설 확인

def solution(people,limit):

    people.sort()
    count = 0
    i = 0
    j = len(people) -1

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        count += 1

    
    return count

print(solution([70,50,80,50],100))
print(solution([70,80,50],100))
