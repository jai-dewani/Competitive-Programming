for z in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    ar.sort()
    current = 1
    i = 0
    # print(ar)
    while i<n:
        call = 0
        found = 0
        while i<n:
            if ar[i]>current+call:
                call += 1
            elif ar[i]>=current+call:
                found = 1
                call += 1
                break 
            # print('c',i,call)
            i += 1
        i += 1
        # print('b',i,call)
        if found:
            current += call
            call = 0
            while i<n and current+call>=ar[i]:
                i +=1
                call += 1
            current += call
    print(current)