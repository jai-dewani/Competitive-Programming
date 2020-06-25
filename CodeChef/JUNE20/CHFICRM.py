for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    flag = True
    count = [0,0]
    for i in range(n):
        m = ar[i]
        if m==5:
            count[0] += 1
            continue
        elif m==10:
            if count[0]>0:
                count[0] -= 1
                count[1] += 1
                continue
            else:
                flag = False
                break 
        else:
            if count[1]>0:
                count[1] -= 1
            elif count[0]>1:
                count[0] -= 2
            else:
                flag = False
                break 
    if flag:
        print("YES")
    else:
        print("NO")
        