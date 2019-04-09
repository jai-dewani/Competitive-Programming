t = int(input())
for z in range(t):
    n,x = list(map(int,input().split()))
    st = list(input())
    ans = {n}
    for i in range(len(st)):
        if st[i]=='R':
            n+=1
            ans.add(n)
        else:
            n-=1
            ans.add(n)
    print(len(ans))
