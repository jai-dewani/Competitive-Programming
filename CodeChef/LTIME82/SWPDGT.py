for i in range(int(input())):
    a,b = input().strip().split()
    ans = int(a)+int(b)
    for i in range(len(a)):
        for j in range(len(b)):
            ai = a[0:i] + b[j] + a[i+1:]
            bi = b[0:j] + a[i] + b[j+1:]
            ans = max(ans,int(ai)+int(bi))
    print(ans)
