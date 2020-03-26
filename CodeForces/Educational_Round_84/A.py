for _ in range(int(input())):
    n, k = map(int,input().split())
    flag = False
    if (k%2==0 and n%2==0) or (k%2==1 and n%2==1):
        if n>=k**2:
            flag = True
    if flag:
        print("YES")
    else:
        print("NO")
