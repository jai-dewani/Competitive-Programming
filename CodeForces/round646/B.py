for _ in range(int(input())):
    s = input()
    n = len(s)
    ones = [0 for i in range(n)]
    zeros = [0 for i in range(n)]
    one = s.count('1')
    zero = s.count('0')
    for i in range(n):
        if s[i]=='0':
            zeros[i] = zeros[i-1] + 1
            ones[i] = ones[i-1]
        else:
            zeros[i] = zeros[i-1] 
            ones[i] = ones[i-1] + 1
    cost = 10**9

    for i in range(n):
        cost = min(cost, zeros[i]+one-ones[i], zero-zeros[i]+ones[i])
    print(cost)

