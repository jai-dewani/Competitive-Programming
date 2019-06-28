import numpy as np
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    order = []
    ar = []
    profit = 0
    C = list(map(int,input().split()))
    extra = [i for i in C]
    for z in range(n):
        d,f,b = list(map(int,input().split()))
        extra[d-1] -= 1
        ar.append([d,f,b])
    #print(extra)
    tempo = np.array(extra)
    index = list(np.argsort(-tempo))
    #print(extra,index)
    extra.sort(reverse=True)
    ofset = 0
    for i in range(n):
        d,f,b = ar[i]
        if C[d-1]>0:
            #print(1,profit,f)
            profit += f
            order.append(d)
            C[d-1] -= 1
        else:
            profit += b
            order.append(index[ofset]+1)
            extra[ofset] -= 1
            if extra[ofset] <= 0:
                ofset += 1
            '''
            temp = 0
            while extra[temp]<=0:
                temp += 1
            
            order.append(index[temp]+1)
            extra[temp] -= 1
            '''
    print(profit)
    print(*order)
            
