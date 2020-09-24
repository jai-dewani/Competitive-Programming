for _ in range(int(input())):
    n = int(input())
    # s = input()
    # n,m = map(int,input().split())
    ar = list(map(int,input().split()))
    allOnes = True
    for i in range(n):
        if ar[i]!=1:
            allOnes = False
            break 
    if allOnes:
        if n%2==0:
            print("Second")
        else:
            print("First")
    else:
        ones = 0 
        for i in range(n):
            if ar[i]==1:
                ones += 1
            else:
                break 
        if ones%2==0:
            print("First")
        else:
            print("Second")
        
