from random import randint

for _ in range(int(input())):
    #l = randint(1,100000)
    #r = randint(l+1,100000)
    
    l,r = map(int,input().split())
    ans1 = 0
    
    if len(bin(r))-len(bin(l))>=1:
        ans1 = (2**(len(bin(r))-2))-1
    else:
        var = list(bin(r)[2:])
        bar = list(bin(l)[2:])
        for i in range(0,len(var)):
            if var[i]!=bar[i]:
                break
        i += 1
        while(i<len(var)):
            var[i] = '1'
            i += 1
        ans = ''.join(var)
        ans1 = int(ans,2)
    print(ans1)

    
