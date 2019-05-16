t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = [int(x) for x in input().split()]
        sum += a-b
    print(sum)
