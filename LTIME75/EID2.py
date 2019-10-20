t = int(input())
for _ in range(t):
    a1,a2,a3,c1,c2,c3 = list(map(int,input().strip().split()))
    ar = [[a1,c1],[a2,c2],[a3,c3]]
    ar.sort()
    flag = True
    for i in range(2):
        if ar[i][0]<ar[i+1][0] and ar[i][1]>=ar[i+1][1]:
            flag = False
        if ar[i][0]==ar[i+1][0] and ar[i][1]!=ar[i+1][1]:
            flag = False
    if flag:
        print("FAIR")
    else:
        print("NOT FAIR")