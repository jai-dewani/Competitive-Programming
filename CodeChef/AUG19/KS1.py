t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int,input().strip().split()))
    xor = [0 for i in range(n)]
    xor[0] = ar[0]
    for i in range(1,n):
        xor[i] = xor[i-1]^ar[i]
    count = [0 for i in range(10**6+1)]
    bad = [0 for i in range(10**6+1)]
    ans = 0
    for i in range(n):
        ans += count[xor[i]]*(i+1)-bad[i]
        count[xor[i]] += 1
        bad[xor[i]] += (i)
    ans += bad[0]
    #print(xor)
    #print(has)
    print(ans)
