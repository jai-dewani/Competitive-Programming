mod = 1000000007
n = int(input())
ar = [0 for i in range(n+1)] 
ar[0] = 1
ar[1] = 1
for i in range(2, n + 1) : 
    ar[i] = (ar[i - 1] + ar[i - 2])%mod
ans1 = ar[n]%mod
ans2 = 0
for i in range(n-2):
    ans2 += ar[i]*ar[n-3-i]
    ans2 = ans2%mod
ans = (ans1+ans2)%mod
print(ans)
