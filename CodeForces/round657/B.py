from random import randint
def valid(l,r,i,mod):
    if mod<0:
        b = abs(mod)
        if b<=r-l:
            x,y,z = i, l, l+b
            return [True,x,y,z]
        return [False]*4 
    else: 
        if mod<=r-l:
            x,y,z = i, l+mod, l
            return [True, x, y, z]
        return [False]*4 

for _ in range(int(input())):
    l,r,m = map(int,input().split())
    # l,r,m = randint(1,500000),randint(1,500000),randint(1,10**10)
    a,b,c = None, None, None
    for i in [l,l+1,r-1,r]:
        if m<i:
            neg = m%i-i 
            ans1,x,y,z = valid(l,r,i,neg)
            if ans1==True:
                print(x,y,z)    
                a,b,c = x,y,z
                break
        else:
            pos = m%i 
            neg = m%i-i 
            ans1,x,y,z = valid(l,r,i,pos)    
            if ans1==True:
                print(x,y,z)
                a,b,c = x,y,z
                break 
            else:
                ans1,x,y,z = valid(l,r,i,neg)
                if ans1==True:
                    print(x,y,z)    
                    a,b,c = x,y,z
                    break
