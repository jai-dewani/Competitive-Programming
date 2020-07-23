for _ in range(int(input())):
    n = int(input())
    # s = input()
    # n,m = map(int,input().split())
    ar = list(map(int,input().split()))
    subset = []
    high = -1
    count = 0
    for i in range(2*n):
        if high == -1:
            high = ar[i]
            count = 1
        else:
            if ar[i]<high:
                count += 1
            else:
                # print(i,count)
                subset.append(count)
                high = ar[i]
                count = 1
    subset.append(count)
    subset.sort()
    dp = [[0 for i in range(2*n+1)] for j in range(len(subset))]
    for i in range(len(subset)):
        dp[i][0] = 1
        dp[i][subset[i]] = 1
    for i in range(1,len(subset)):
        for j in range(n+1):
            if dp[i-1][j]==1:
                dp[i][j] = 1
            if j>=subset[i-1] and dp[i-1][j-subset[i]]==1:
                dp[i][j] = 1
    # print(subset)
    # print(dp)
    if dp[-1][n]==1:
        print("YES")
    else:
        print("NO")            