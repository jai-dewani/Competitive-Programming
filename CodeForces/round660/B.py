from math import ceil 
for _ in range(int(input())):
    n = int(input())
    # s = input()
    # n,m = map(int,input().split())
    # ar = list(map(int,input().split()))
    s = ''
    k = ceil(n/4)
    for i in range(n-k):
        s += '9'
    if n%4!=0:
        s += '8'
    s += '8'*(n//4)
    print(s)