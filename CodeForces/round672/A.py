for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))

    count = 0
    for i in range(1,n):
        if ar[i]<ar[i-1]:
            count += 1
    if count==n-1:
        print("NO")
    else:
        print("YES")