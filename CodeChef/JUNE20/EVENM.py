for _ in range(int(input())):
    n = int(input())
    if n%2:
        matrix = [[0 for i in range(n)] for j in range(n) ]
        for i in range(n):
            for j in range(n):
                val = i*n + j
                matrix[i][j] = val+1 
    else:
        num = [i+1 for i in range(n*n)]
        matrix = [0]*n
        for i in range(n):
            if i%2:
                ar = num[i*n:(i+1)*n]
                matrix[i] = ar[::-1]
            else:
                ar = num[i*n:(i+1)*n]
                matrix[i] = ar 
    for i in matrix:
        print(*i)