from math import floor, log2
def log(a):
    if a<=1:
        return 0
    else:
        return log(floor(a/2)) + 1

def F(a,b):
    n = len(a)
    posA = [-1]*(n+1)
    posB = [-1]*(n+1)
    ret = 0
    for i in range(n):
        posA[a[i]] = i
        posB[b[i]] = i
    for i in range(1,n+1):
        ret += log(abs(posA[i]-posB[i]))
    return ret

def main(p,q,v):
    result = 1
    n = len(q)
    for i in range(v):
        r = q[n-i:]+ q [:n-i]
        #print('r',r)
        result *= F(p,r)
    return result%998244353

for _ in range(int(input())):
    n,v = map(int,input().split())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    print(main(p,q,v))
