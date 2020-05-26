for i in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    if x1==x2 or y1==y2:
        ans = 1
    else:
        ans = (x2-x1)*(y2-y1) + 1
    print(ans)