def change(n) :
    cnt = 0
    coin = [500,100,50,10]

    for i in coin:
        cnt += n//i
        n %= i

    print(cnt)

change(1260)