for _ in range(int(input())):
    t = int(input())
    if t%2:
        ans = t//2
    else:
        count = 0
        temp = t
        while temp%2==0:
            count += 1
            temp = temp//2
        val = 2**(count+1)
        # print(val)
        ans = t//val 
    print(ans)