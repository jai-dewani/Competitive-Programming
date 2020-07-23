for _ in range(int(input())):
    n  = int(input())
    ar = list(map(int,input().split()))
    ar.sort()
    mid = n//2 
    ans = []
    for i in range(n):
        if i%2==0:
            mid += i
        else:
            mid -= i 
        
        ans.append(ar[mid])
    print(*ans)