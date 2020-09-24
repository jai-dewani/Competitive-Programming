for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    ar.sort()
    count = 0
    i = 0
    last = 0
    while i<n:
        t = ar[i]
        if t-1>last:
            i += 1
            last += 1
        else:
            i += t 
            last -= t - 1
            count += 1
            # print(i)
    print(count)
