import math
import random
t = int(input())
while t:
    n = random.randint(2,10**18)
    k = random.randint(1,10**18)
    #n,k = list(map(int,input().split()))
    first = k-1
    d = n-1
    m = first//d
    if first%d!=0:
        m+=1
    #m = math.ceil(first/d)
    #print(first,d,last)
    #first = first%(10**9+7)
    #last = last%(10**9+7)
    '''
    i = k-1
    ans2 = 0
    while i>0:
        ans2 += i
        i -= d
    ans2 %= (10**9+7)
    '''
    ans1 = (m*(2*first-(m-1)*d))//2
    ans1 = ans1%(10**9+7)
    #ans2 = (m1*(2*first-(m-1)*d))//2
    #ans2 %= (10**9+7)
    #ans = (m*(first+last))//2
    #ans = ans%(10**9+7)
    print(ans1)
    '''
    if ans2!=ans1:
        print("ERROR",ans1,ans2,n,k)
        break
    '''
    '''
    if ans1!=ans:
        print("ERROR",n,k)
        print(ans,ans1)
        break
    '''
    t -= 1
