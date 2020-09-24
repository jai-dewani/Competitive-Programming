for _ in range(int(input())):
    n = int(input())
    s = input()
    # n,m = map(int,input().split())
    # ar = list(map(int,input().split()))
    ans1 = ""
    for i in range(len(s)):
        if s[i]=="0":
            ans1 += s[i]
        else:
            break
    # print('ans1',ans1)
    for i in range(len(s)-1):
        if s[i]=="1" and s[i+1]=="0":
            ans1 += "0"
            break
    ans2 = ""
    for i in range(len(s)-1,-1,-1):
        if s[i]=="1":
            ans2 = s[i]+ans2 
        else:
            break 
    print(ans1+ans2)