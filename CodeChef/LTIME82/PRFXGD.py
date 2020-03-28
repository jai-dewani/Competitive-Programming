for i in range(int(input())):
    s = input()
    k,x = map(int,input().split())
    ans = 0
    dic = {}
    for i in range(97,97+26):
        dic[chr(i)] = 0
    for i in range(len(s)):
        dic[s[i]] += 1
        if dic[s[i]]>x:
            if k>0:
                k -=1
                dic[s[i]] -= 1
                continue
            else:
                break
        else:
            ans += 1
    print(ans)
