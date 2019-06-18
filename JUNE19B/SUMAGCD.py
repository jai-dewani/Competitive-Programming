import math

def gcd(ar):
    if len(ar)==1:
        return ar[0]
    elif len(ar)==0:
        return 0
    else:
        ans = math.gcd(ar[0],ar[1])
        for i in range(2,len(ar)):
            ans = math.gcd(ans,ar[i])
        return ans

t = int(input())
while t:
    n = int(input())
    ar = list(map(int,input().split()))
    if len(set(ar))==1:
        print(2*ar[0])
    else:
        ar = list(set(ar))
        n = len(ar)
        fmax = 0
        fi = -1
        smax = 0
        si = -1
        for i in range(n):
            if ar[i]>fmax:
                smax = fmax
                fmax = ar[i]
                si = fi
                fi = i
            elif ar[i]>smax:
                smax = ar[i]
                si = i
            
        ar1 = ar[0:fi]+ar[fi+1:n]
        ar2 = ar[0:si]+ar[si+1:n]
        #print(ar1,maxi,index)
        ans1 = gcd(ar1)+fmax
        ans2 = gcd(ar2)+smax
        #print(ar1,fmax,fi)
        #print(ar2,smax,si)
        ans = max(ans2,ans1)
        print(ans)
    t -= 1
