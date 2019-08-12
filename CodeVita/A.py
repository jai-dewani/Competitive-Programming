from collections import Counter
t = int(input())
ar = list(map(int,input().strip().split()))

result = Counter(ar)
ans = max(result[i] for i in result)

print(ans)
'''
enclose = [False for i in range(t)]
maxi = ar[0]
maxi_index = 0
for i in range(t):
    if ar[i]>maxi:
        maxi = ar[i]
        maxi_index = i
    if ar[i]<mini:
        mini = ar[i]
        mini_index = i

stop = True
big = maxi
big_index = maxi_index

while stop:
    mini = -1
    mini_index = -1
    for i in range(t):
        if ar[i]<mini and ar[i]!=-1:
            mini = ar[i]
            mini_index = i
    big = maxi
    big_index = maxi_index
    for i in range(t):
        if ar[i]
'''
