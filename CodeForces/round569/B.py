n = int(input())
ar = list(map(int,input().split()))
mod = [abs(i) for i in ar]

if n%2==0:
    for i in range(n):
        if ar[i]>=0:
            ar[i]=-ar[i]-1
else:    
    maxi = mod[0]
    index = 0
    for i in range(n):
        if mod[i]>maxi:
            maxi = mod[i]
            index = i
    for i in range(n):
        if i==index:
            if ar[i]<0:
                ar[i] = -ar[i]-1
        else:
            if ar[i]>=0:
                ar[i] = -ar[i]-1


print(*ar)
