def solution(n,coins):
    coins.sort()
    # 1 1 2 3 9

    target = 1
    for coin in coins:
        if coin > target:
            break
        target += coin

    return target

print(solution(5,[3,2,1,1,9]))     
