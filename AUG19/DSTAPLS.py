t = int(input())
for _ in range(t):
    n,k = list(map(int,input().strip().split()))
    temp = n//k
    if temp%k==0:
        print("NO")
    else:
        print("YES")
