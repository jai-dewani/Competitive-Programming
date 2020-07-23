for _ in range(int(input())):
    # n = int(input())
    # s = input()
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    hashmap = [0]*1001
    for i in range(n):
        hashmap[a[i]] += 1
    ans = -1 
    for i in range(m):
        if hashmap[b[i]]>0:
            ans = b[i]
            break
    if ans!=-1:
        print("YES")
        print(1,ans)
    else:
        print("NO")