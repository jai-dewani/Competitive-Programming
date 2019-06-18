t = int(input())
while t:
    n = int(input())
    for i in range(n*10,(n+1)*10):
        st = str(i)
        st = list(map(int,list(st)))
        #print(st)
        s = sum(st)
        if s%10==0:
            print(i)
            break
    t -= 1
