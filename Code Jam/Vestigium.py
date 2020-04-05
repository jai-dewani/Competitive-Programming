for q in range(int(input())):
    n = int(input())
    mat = []
    for i in range(n):
        temp = list(map(int,input().split()))        
        mat.append(temp)
    col = 0
    row = 0
    for i in range(n):
        c = [0]*(n+1)
        for j in range(n):
            t = mat[i][j]
            if c[t]==1:
                col += 1
                break
            c[t] += 1
    for i in range(n):
        r = [0]*(n+1)
        for j in range(n):
            t = mat[j][i]
            if r[t]==1:
                row += 1
                break
            r[t] += 1
    k = 0
    for i in range(n):
        k += mat[i][i]
    print("Case #"+ str(q+1) + ":",k,col,row)
