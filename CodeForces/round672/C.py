for _ in range(int(input())):
    n,q = map(int,input().split())
    ar = list(map(int,input().split()))
    t = [ar[0]]
    up = True 
    for i in range(1,n):
        if up:
            if ar[i]>t[-1]:
                t[-1] = ar[i] 
            elif ar[i]<t[-1]:
                t.append(ar[i])
                up = False 
        else:
            if ar[i]<t[-1]:
                t[-1] = ar[i] 
            elif ar[i]>t[-1]:
                t.append(ar[i])
                up = True 
    if up==False:
        t.pop()
    ans = 0
    # print(t)
    if len(t)%2:
        ans += t[-1]
        for i in range(0,len(t)-1,2):
            ans += t[i]-t[i+1]
    else:
        for i in range(0,len(t),2):
            ans += t[i]-t[i+1]
    print(max(max(ar),ans))
