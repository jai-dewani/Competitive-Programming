for _ in range(int(input())):
    n= int(input())
    ar = list(map(int,input().split()))
    xor = []
    hashmap = {}
    flag = True 
    # for i in range(n):
    #     if hashmap.get(ar[i])==None:
    #         hashmap[ar[i]] = 1
    #     else:
    #         hashmap[ar[i]] += 1
    #         flag = False
    #         break 
    # if not flag:
    #     print("NO")
    # else:
    for i in range(n):
        orr = 0
        for j in range(i,n):
            orr = orr | ar[j]
            if hashmap.get(orr)!=None:
                flag = False
                break 
            else:
                hashmap[orr] = 1
        if not flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")