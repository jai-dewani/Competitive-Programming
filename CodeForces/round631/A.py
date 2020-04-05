for i in range(int(input())):
    n, x = list(map(int,input().split()))
    ar = list(map(int,input().split()))
    limit = 2*(n+x)
    hashmap = [0]*(2*(n+x))
    for i in ar:
        if i<limit:
            hashmap[i] = 1
    for i in range(1,len(hashmap)):
        if hashmap[i]==1:
            continue
        else:
            if x==0:
                break
            x = x-1
        #print(i,x)
    print(i+x-1)
