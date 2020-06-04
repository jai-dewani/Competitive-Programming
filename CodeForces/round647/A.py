def count(a,b):
    ans = 0
    while a>b:
        if a%2==0:
            a = a//2 
            ans += 1
        else:
            return -1
    if a==b:
        return ans
    return -1

import math
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    if a==b:
        print(0)
    elif a>b:
        if a%b==0:
            ans = count(a,b)
            if ans==-1:
                print(ans)
            else:
                ans = math.ceil(ans/3)
                print(ans)
        else:
            print(-1)
    else:
        if b%a==0:
            ans = count(b,a)
            if ans==-1:
                print(ans)
            else:
                ans = math.ceil(ans/3)
                print(ans)
        else:
            print(-1)