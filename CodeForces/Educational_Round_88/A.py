from math import ceil 
for i in range(int(input())):
    n,m,k = map(int,input().split())
    if m==0:
        ans = 0
    else:
        each = n//k 
        if each>=m:
            ans = m 
        else:
            ans = each - ceil((m-each)/(k-1))
            # print(each, (m-each)/(each-1), ceil((m-each)/(n-1)))
    print(ans)