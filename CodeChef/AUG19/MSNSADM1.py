t = int(input())
for _ in range(t):
    n = int(input())
    ar1 = list(map(int,input().strip().split()))
    ar2 = list(map(int,input().strip().split()))
    maxi = (ar1[0]*20)-(ar2[0]*10)
    for i in range(n):
        maxi = max(maxi,max((ar1[i]*20)-(ar2[i]*10),0))
        #print('debug',maxi)
    print(maxi)
