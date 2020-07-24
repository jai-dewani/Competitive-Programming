for _ in range(int(input())):
    n = int(input())
    # s = input()
    # n,m = map(int,input().split())
    ar = list(map(int,input().split()))
    ans = []
    ans.append(''.join(x for x in ['a']*100))
    c = 1
    for i in range(n):
        m = ar[i]
        t = ans[-1][:m]
        t += ''.join([chr(97+c)]*50)
        c = (c+1)%26
        ans.append(t)
    for i in ans:
        print(i)