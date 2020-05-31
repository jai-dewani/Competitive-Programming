for _ in range(int(input())):
    ar = list(map(int,input().strip().split()))
    s = sum(ar[:-1])
    # print(s)
    p = ar[-1]
    s *= p
    if s>24*5:
        print("Yes")
    else:
        print("No")