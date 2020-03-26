t = int(input())
for i in range(t):
    n,q = list(map(int,input().strip().split()))
    p = list(map(int,input().strip().split()))
    p.sort()
    for i in range(q):
        x = int(input())
        count = 0
        for i in range(n):
            if x<=p[i]:
                break
            else:
                x = 2*(x-p[i])
                count += 1
        print(count)
