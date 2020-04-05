for q in range(int(input())):
    n = input()
    ans = ""
    depth = 0
    for i in range(len(n)):
        t = int(n[i])
        if t==depth:
            ans += n[i]
        elif t>depth:
            ans += "("*(t-depth)
            ans += n[i]
            depth = t
        else:
            ans += ")"*(depth-t)
            ans += n[i]
            depth = t
    ans += ")"*depth
    print("Case #"+str(q+1)+":",ans)
