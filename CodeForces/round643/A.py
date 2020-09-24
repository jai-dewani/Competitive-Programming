for i in range(int(input())):
    a,k = map(int,input().split())
    ans = a
    stop = 0
    for i in range(k-1):
        temp = str(ans)
        maxi = max(temp)
        mini = min(temp)
        if mini=='0':
            stop = i
            break
        else:
            ans += int(mini)*int(maxi)
    print(ans)
