import math
t = int(input())
while t:
    n = int(input())
    array = list(input())
    at = 0
    req = math.ceil(0.75*n)
    for i in array:
        if i=='P':
            at += 1
    if at>=req:
        print(0)
    else:
        counter = 0
        flag = 0
        for i in range(2,n-2):
            if array[i]=='A' and (array[i-1]=='P' or array[i-2]=='P') and (array[i+1]=='P' or array[i+2]=='P'):
                counter += 1
                at += 1
            #print(i,array[i-2:i+3],counter)
            if at>=req:
                flag = 1
                break
        if flag==0:
            print(-1)
        else:
            print(counter)
    #print(counter,at,req)
    t = t - 1

    
