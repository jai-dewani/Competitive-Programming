for _ in range(int(input())):
    # n = int(input())
    x,y,z = map(int,input().split())
    # ar = list(map(int(input().split())))
    found = True 
    if x==y and x>=z:
        a,b,c = x,z,z
    elif x==z and x>=y: 
        a,b,c = y,x,y
    elif y==z and y>=x:
        a,b,c = x,x,y
    else:
        found = False
    if found:
        print("YES")
        print(a,b,c)
    else:
        print("NO")