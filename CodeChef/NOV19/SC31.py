for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n):
        x = input()
        x = int(x,2)
        ans = ans^x
    ones = bin(ans)[2:]
    ans = ones.count('1')
    print(ans)