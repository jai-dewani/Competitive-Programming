for z in range(int(input())):
    s = input()
    a = ""
    b = ""
    a_end = -1
    ans = 0
    for i in range(1,len(s)//2):
        if s[:i] == s[i:2*i]:
            a = s[:i]
            a_end = 2*i
            mid = (len(s)-2*i)//2
            # print('a_end',a_end)
            # print('mid',mid)
            if s[a_end:a_end+mid] == s[a_end+mid:]:
                ans += 1
    print(ans)