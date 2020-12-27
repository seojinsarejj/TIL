# 프로그래머스 구명보트

# 1차 --- 정확성 75.0 효율성 0.0 --- 75.0 / 100
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