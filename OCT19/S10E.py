t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int,input().strip().split()))
    count = 0
    for i in range(1,n):
        if i<5:
            if min(ar[:i])>ar[i]:
                 count += 1
        else:
            if min(ar[i-5:i])>ar[i]:
                count += 1
    print(count+1)
