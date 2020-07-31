for _ in range(int(input())):
    n = int(input())
    # s = input()
    # n,m = map(int,input().split())
    # ar = list(map(int,input().split()))
    if n<=30:
        print("NO")
    else:
        print("YES")
        if n-30 in [14,6,10]:
            print(15,10,6,n-31)
        else:
            print(14,6,10,n-30)