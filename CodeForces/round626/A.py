for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    found = False
    for i in range(n-1):
        if ar[i]%2==0:
            found = True 
            ans = [i+1] 
            break 
        elif (ar[i]+ar[i+1])%2==0:
            found = True
            ans = [i+1,i+2]
            break 
    if ar[-1]%2==0:
        found = True

    if found:
        print(len(ans))
        print(*ans)
    else:
        print(-1)