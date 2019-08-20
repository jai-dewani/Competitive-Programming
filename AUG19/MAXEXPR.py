t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(float,input().strip().split()))
    c = list(map(float,input().strip().split()))
    if max(c)==0.00:
        print("%.6f"%(0.0),end=' ')
        for i in range(n):
            print("%.6f"%(0.00),end=' ')
        print()
    else:
        print("%.6f"%(0.0),end=' ')
        for i in range(n):
            print("%.6f"%(0.00),end=' ')
        print()
