t = int(input())
for _ in range(t):
    l,nl = input().strip().split()
    r,nr = input().strip().split()
    nl = int(nl)
    nr = int(nr)
    ans = 0
    mod = 10**9+7
    for i in range(nl,nr+1):
        n1 = list(str(i))
        le = len(n1)
        last = n1[0]
        #print(i,n1,last)
        for i in range(1,le):
            if n1[i]==last:
                n1[i]='0'
                #print("POINT")
            else:
                last = n1[i]
        ans += int(''.join(n1))
        ans %= mod
        
    print(ans%mod)
        
