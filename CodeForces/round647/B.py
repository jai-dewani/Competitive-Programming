for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    if n%2:
        print(-1)
    else:
        xor = {}
        hashmap = [0] * 1025 
        for i in range(n):
            for j in range(i+1,n):
                x = ar[i]^ar[j]
                if xor.get(x)==None:
                    xor[x] = [[i,j]]
                else:
                    xor[x].append([i,j])
        # print(xor)
        for key in sorted(xor.keys()):
            value = xor[key]
            if len(value)>=n//2:
                print(key)
                break
        else:
            print(-1)
