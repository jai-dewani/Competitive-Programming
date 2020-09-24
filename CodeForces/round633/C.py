for _ in range(int(input())):
    n  = int(input())
    ar = list(map(int,input().split()))
    flag = True
    for i in range(n-1):
        if ar[i]>ar[i+1]:
            flag = False
    if flag:
        print(0)
        continue 
    time = 0
    maxSoFar = ar[0]
    diff = 0
    for i in range(n):
        if ar[i]>maxSoFar:
            maxSoFar = ar[i]
        else:
            diff=max(diff,maxSoFar-ar[i])
    while 2**time<=diff:
        time += 1
    print(time)