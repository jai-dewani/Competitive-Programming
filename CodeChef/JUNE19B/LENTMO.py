t = int(input())
while t:
    n = int(input())
    ar = list(map(int,input().split()))
    k = int(input())
    x = int(input())
    #change = list(map(int,input().split()))
    change = []
    
    for i in range(n):
        temp = (ar[i]^x)-ar[i]
        change.append(temp)
    
    change.sort(reverse=True)
    summ = 0
    i = 0
    if k==n:
        summ = max(0,sum(change))
    else:
        if k%2==0:
            step = 2
            while i<=n-step:
                if sum(change[i:i+step])>0:
                    summ += sum(change[i:i+step])
                    for z in range(i,i+step):
                        change[z] = -1*change[z]
                i += step
            change.sort(reverse=True)
            while i<=n-step:
                if sum(change[i:i+step])>0:
                    summ += sum(change[i:i+step])
                    for z in range(i,i+step):
                        change[z] = -1*change[z]
                i += step
        else:
            step = 1
            while i<=n-step:
                if sum(change[i:i+step])>0:
                    summ += sum(change[i:i+step])
                else:
                    break
                i += step
    print(sum(ar)+summ)
    #print(change)
    t -= 1
