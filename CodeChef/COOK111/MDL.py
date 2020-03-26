for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().strip().split()))
    for i in range(n-2):
        a,b,c = ar[i],ar[i+1],ar[i+2]
        mini = min(a,b,c)
        maxi = max(a,b,c)
        if a!=mini and a!=maxi:
            pass
        elif b!=mini and b!=maxi:
            ar[i+1] = a
        else:
            ar[i+1] = a
            ar[i+2] = b
        #print(ar)
    print(ar[-2],ar[-1])
