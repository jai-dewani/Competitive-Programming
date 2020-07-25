from random import randint
from math import ceil
def bin_add(a,b):
    x,y = bin(a)[2:],bin(b)[2:]
    t1,t2 = x+y,y+x
    return abs(int(t1,2)-int(t2,2))

def a():
    binary = []
    l = 0
    s = 10**10
    x,y = -1,-1
    for i in range(n):
        b = bin(ar[i])[2:]
        le = len(b)
        m = ceil(20/le)
        temp = b*3
        num = int(temp[:20],2)
        if num>l:
            l = num 
            x = i 
        if num<s:
            s = num 
            y = i 
        # print(l,s,x,y)
    bin_a = bin(ar[x])[2:]
    bin_b = bin(ar[y])[2:]
    print(ar[x],ar[y],bin_a,bin_b)
    # print(x,y)
    ans = int(bin_a+bin_b,2) - int(bin_b+bin_a,2)
    print(ans)
    return ans

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    # ar = [randint(1,10**5) for i in range(n)]
    ans = 0 
    help = []
    for i in range(n):
        for j in range(i+1,n):
            if bin_add(ar[i],ar[j])>ans:
                ans = bin_add(ar[i],ar[j])
                help = [ar[i],ar[j]]
    print(ans)
    check = a()
    if ans!=check:
        print("PROBLEM")
        print(n,ar)
        print(ans,check)
        print(help)

