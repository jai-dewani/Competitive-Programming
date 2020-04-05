for q in range(int(input())):
    n = int(input())
    l = []
    hashmap = [0]*2400
    for i in range(n):
        a,b = map(int,input().split())
        l.append([a,b,i])
        for j in range(a,b):
            hashmap[j] += 1
    flag = True
    for i in range(2400):
        if hashmap[i]>2:
            flag = False
    ans = ""
    if not flag:
        ans = "IMPOSSIBLE"
        print("Case #" + str(q+1) + ": IMPOSSIBLE")
    else:
        ans = ["0"]*n
        j = 0
        c = 0
        l.sort()
        for i in range(n):
            t = l[i][0]
            s = l[i][1]
            index = l[i][2]
            if t>=j:
                ans[index] = "J"
                j = s
            else:
                ans[index] = "C"
                c = t
        ans = "".join(ans)
        print("Case #" + str(q+1) + ": " + ans)
