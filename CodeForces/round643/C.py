a,b,c,d = list(map(int,input().split()))
low = max(a+b,c)
high = min(b + c-1,d)
b_c = b+c
a_b = a+b
dic = {}
for i in range(a_b,b_c+1):
    dic[i-1] = min(b_c-i+1,i-a_b+1)
# print(dic)

ans = 0 
mul = 0
for i in range(d,c-1,-1):
    if dic.get(i)!=None:
        mul += dic[i]
        print(dic[i])
    # print(i,mul,ans)
    if i<=high:
        ans += mul
print(ans)