t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int,input().strip().split()))
    c = ar[0]
    ar = ar[1:]
    i = 0
    j = c-1
    ans = 0
    while i<=j:
        ans += ar[i]
        i += 1
        j -= 1
    print(ans)