ar = []
for i in range(10):
    a = []
    for j in range(10):
        a.append(i*10+j+1)
    ar.append(a)
for i in ar:
    print(*i)
n = int(input())
k = int(input())
for i in range(10):
    for j in range(10):
        if ar[i][j]%k==0:
            ar[i][j]=-1
for i in range(k+1,k+n):
    for j in range(100):
        if ar[j//10][j%10]%i==0:
            ar[j//10][j%10]=-1
        if ar[j//10][j%10]==-1:
            k = j+i
            if k<100:
                ar[k//10][k%10]=-1
for i in ar:
    print(*i)
