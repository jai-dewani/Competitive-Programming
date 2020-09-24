for _ in range(int(input())):
    n = int(input())
    prince = [0]*n
    princes = [0]*n
    choice = []
    for q in range(n):
        ar = list(map(int,input().split()))
        if ar[0]==0:
            choice.append([])
        else:
            b = ar[1:]
            b.sort()
            choice.append(b)
    left = []
    for i in range(n):
        for j in choice[i]:
            if prince[j-1]==0:
                prince[j-1] = 1
                princes[i-1] = 1
                break
        if princes[i-1]==0:
            left.append(i)
    if len(left)==0:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        ans1 = left[0]+1
        ans2 = -1
        for i in range(n):
            if prince[i]==0:
                ans2 = i+1
                break
        print(ans1,ans2)
    
