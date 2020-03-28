from math import gcd
for i in range(int(input())):
    n,m = list(map(int,input().strip().split()))
    ar = list(map(int,input().strip().split()))
    lcm = 1
    hashmap = [1]*(m+1)
    for i in range(n):
        temp = gcd(lcm,ar[i])
        lcm = (lcm*ar[i])//temp
    for i in range(1,m+1):
        if lcm%i==0:
            hashmap[i] = 0
    maxlcm = 0
    ans = None
    for i in range(1,m+1):
        if hashmap[i]==1:
            temp = gcd(lcm,i)
            t = (lcm*i)//temp
            if t>maxlcm:
                ans = i
            maxlcm = max(maxlcm,t)
    if ans==None:
        print(1)
    else:
        print(ans)
