import random
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    #n = random.randint(2,20)
    #m = random.randint(2,100)
    #ar = [0 for i in range(m)]
    fmax = 0
    smax = 0
    findex = 0
    sindex = 0
    for z in range(n):
        d,v = list(map(int,input().split()))
        #d = random.randint(1,m)
        #v = random.randint(1,100)
        if v>fmax:
            if d==findex:
                fmax = v
            else:
                smax = fmax
                fmax = v
                sindex = findex
                findex = d
        elif v>smax and d!=findex:
            if d==sindex:
                smax = v
            else:
                smax = v
                sindex = d
        #ar[d-1] = max(ar[d-1],v)
    #ar.sort()
    #ans = ar[-1]+ar[-2]
    ans1 = fmax+smax
    '''
    if ans1!=ans:
        print("ERROR",ans,ans1)
        print(n,m,d,v)
        print(fmax,smax,findex,sindex)
        print(ar)
        break
    '''
    print(ans1)
        
