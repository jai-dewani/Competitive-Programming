
for _ in range(int(input())):
    n = int(input())
    t = bin(n)[2:]
    values = [2**i for i in range(70,-1,-1)]
    # print(values)
    last = None
    ans = 0
    i = 0
    while values[i]>n:
        i += 1
    while n>0:
        if bin(n)[2:].count('1')==1:
            ans += 2*n-1
            n = 0
        else:
            temp = 0
            while n&values[i]!=values[i]:
                # print(i,values[i])
                i += 1
            temp += values[i]
            n -= values[i]
            i += 1
            while n&values[i]!=values[i]:
                # print(i,values[i])
                i += 1
            temp += values[i]
            n -= values[i]
            i += 1
            ans += (temp-1)*2
    print(ans)
            

    # for i in range(100):
    #     val = i ^ (i+1)
    #     ans += bin(val)[2:].count('1')
    #     if i*2==ans:
    #         print(i+1,bin(val)[2:].count('1'), ans, "YES", bin(i+1)[2:])
    #     else:
    #         print(i+1,bin(val)[2:].count('1'), ans)
    #     # print(str(i^(i+1)).count('1'),end=' ')
