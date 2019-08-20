t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int,input().strip().split()))
    h = list(map(int,input().strip().split()))
    diff = [0 for i in range(n+1)]
    power = [0 for i in range(n)]
    for i in range(n):
        diff[max(0,i-c[i])] += 1
        diff[min(n,i+c[i]+1)] -= 1
    power[0] = diff[0]
    for i in range(1,n):
        power[i] = power[i-1]+diff[i]
    power.sort()
    h.sort()
    flag = True
    for i in range(n):
        if power[i]!=h[i]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
