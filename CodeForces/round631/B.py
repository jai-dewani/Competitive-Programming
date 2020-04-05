def check(ar,n):
    global hashmap
    hashmap = [0]*200000
    count1 = None
    count2 = None
    ans = []
    for i in range(n):
        t = ar[i]
        if hashmap[t]==1:
            flag = True
            if count1!=None:
                flag = False
                #print('a')
            for i in range(1,i+1):
                if hashmap[i]==0:
                    flag = False
                    #print('b')
                if not flag:
                    break
            if flag:
                count1 = i
                for i in range(count1+1):
                    hashmap[i]=0
            else:
                #print('c')
                break
                    
        hashmap[t] = 1
    if count1==None:
        #print(0)
        return 0
    else:
        flag = True
        #print(n-count1+1)
        for i in range(1,n-count1+1):
            if hashmap[i]==0:
                flag = False
            if not flag:
                break
        if flag:
            return [count1,n-count1]
        else:
            #print('d')
            return 0
for _ in range(int(input())):
    ans = []
    n = int(input())
    ar = list(map(int,input().split()))
    t = check(ar,n)
    #print('t',t)
    if t!=0:
        ans.append(t)
    ar = ar[::-1]
    t = check(ar,n)
    #print('t',t)
    if t!=0:
        t = t[::-1]
        ans.append(t)
    print(len(ans))
    for i in ans:
        print(*i)
    
    
