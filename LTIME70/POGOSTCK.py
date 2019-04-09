t = int(input())
for z in range(t):
    n,k = list(map(int,input().split()))
    ar = list(map(int,input().split()))
    #print(ar)
    ans = -10000000000
    for j in range(k):
        temp = 0
        for i in range(n-1-j,-1,-k):
            temp += ar[i]
            if temp>ans:
                ans = temp
        
    print(ans)
