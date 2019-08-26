t = int(input())
for i in range(t):
    n,m,k,l,r = list(map(int,input().strip().split()))
    c  = [0 for i in range(n)]
    p = [0 for i in range(n)]
    for i in range(n):
        c[i],p[i] = list(map(int,input().strip().split()))
    
    for i in range(n):
        if c[i]>k:
            c[i] = max(k,c[i]-m)
        elif c[i]<k:
            c[i] = min(k,c[i]+m)
    #print(c)
    minn = 10**6
    index = -1
    for i in range(n):
        if c[i]>=l and c[i]<=r and p[i]<minn:
            minn = p[i]
            index = i
    if index==-1:
        print(-1)
    else:
        print(minn)
