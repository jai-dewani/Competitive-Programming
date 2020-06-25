for _ in range(int(input())):
    n,p = map(int,input().split())
    ar = list(map(int,input().split()))
    ans = 0
    for i in ar:
        if i>p:
            ans += i-p 
    print(ans)