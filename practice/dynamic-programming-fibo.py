def fibo(n):
    if n <= 2 : 
        return 1
    else:
        return (fibo(n-2) + fibo(n-1))

def bottom_up_fibo(n):
    memo = []
    for i in range(0,n):
        if i < 2:
            memo.append(1)
        else:
            memo.append(memo[i-2] + memo[i-1])

    return memo[n-1]

def memoization_fibo(n):
    if n < 2:
        return 1
    if (memo(n)):
        return memo[n]
    memo[n] = memoization_fibo(n-1) + memoization_fibo(n-2)
    return memo[n]

#print(fibo(50))
print(memoization_fibo(50))

