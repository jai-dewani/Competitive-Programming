def cal(n):
    ans = 1
    base = 2
    counter = 0
    while n:
        counter+=1
        if n%2==0:
            n = n>>1
            base = base*base
        else:
            n -= 1
            ans = ans*base
            n = n>>1
            base = base*base
        base = base%(10**9+7)
        ans = ans%(10**9+7)
    #print(counter)
    return ans

def calc(n):
    ans = 1
    while n:
        ans = ans*2
        #ans = ans%(10**9+7)
        n-= 1
    return ans%(10**9+7)


t = int(input())
while t:
    #n = 10**9
    n = int(input())
    '''
    counter1 = 0
    for i in range(10**n):
        ar = list(map(int,list(str(i))))
        ar += list(map(int,list(str(10**n-i-1))))
        ar = list(set(ar))
        if len(ar)==2:
            #print(i)
            counter1+=1
    print(counter1)
    ar = []
    '''
    counter2 = (cal(n)*5)%(10**9+7)
    print(counter2)
    t -= 1
