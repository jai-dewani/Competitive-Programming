def find_left(ar,x,l,r):
    mid = (l+r)//2
    if l>r:
        return l
    if ar[mid]==x:
        return mid 
    elif ar[mid]>x:
        return find_left(ar,x,l,mid-1)
    else:
        return find_left(ar,x,mid+1,r)
MOD = 10**9+7
G = [1,2,2]
right = [1,3,5]
sq_sum = [1,9,27]
next = 3 
count = G[next-1]
num = 4
while right[-1]<10**10:
    while count>0:
        G.append(next)
        count -= 1
        right.append(right[-1] + G[-1])
        # right[-1] %= MOD
        sq_sum.append(sq_sum[-1] + (num)**2*G[-1])
        sq_sum[-1] %= MOD
        num += 1
    next += 1
    count = G[next-1]
# print(num/10**9)
# print(right[-1])
# print(G)
# print(right)
# print(sq_sum)
for _ in range(int(input())):
    l,r = map(int,input().split())
    a,b = find_left(right,l,0,len(right)),find_left(right,r,0,len(right))
    ans = 0
    if a==b:
        ans += ((a+1)**2)*(r-l+1)
        ans = ans%MOD
    elif a+1==b:
        ans += ((a+1)**2)*(right[a]-l+1)
        ans = ans%MOD
        ans += ((b+1)**2)*(r-right[a])
        ans = ans%MOD
    else:
        ans += ((a+1)**2)*(right[a]-l+1)
        ans = ans%MOD
        # print(ans)
        ans += ((b+1)**2)*(r-right[b-1])
        ans = ans%MOD
        # print(ans)
        ans += sq_sum[b-1] - sq_sum[a]
        ans = ans%MOD
        # for i in range(a+1,b):
        #     ans += ((i+1)**2)*(G[i])        
            # print(ans)
    print(ans)