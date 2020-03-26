t = int(input())
for i in range(t):
    n,q = list(map(int,input().strip().split()))
    s = list(input())
    pairs = {i:[] for i in range(n)}
    for i in range(n-2):
        if s[i]==s[i+1]:
            pairs[i].append(i+1)
        elif s[i]==s[i+2]:
            pairs[i].append(i+2)
    if s[n-1]==s[n-2]:
        pairs[n-2].append(n-1)
        
    for i in range(q):
        l,r = list(map(int,input().strip().split()))
        flag = False
        l -= 1
        r -= 1
        for j in range(l,r):
            for k in range(len(pairs[j])):
                #print(pairs[j],r)
                if pairs[j][k]<=r:
                    flag = True
                    break
            if flag:
                break
        if flag:
            print("YES")
        else:
            print("NO")
