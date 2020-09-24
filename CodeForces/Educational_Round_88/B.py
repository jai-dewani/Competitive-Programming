for _ in range(int(input())):
    n,m,x,y = map(int,input().split())
    v = [[0 for i in range(m)] for j in range(n)]
    mat = []
    for i in range(n):
        mat.append(input())
    if x<y/2:
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == '.':
                    count += 1
        ans = x*count
    else:
        ones = 0 
        twos = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='.':
                    ones += 1
                    if j>0 and mat[i][j-1]=='.' and v[i][j-1]==0:
                        # print(i,j)
                        ones -= 2
                        twos += 1
                        v[i][j] = 1
        # print('z',ones,twos)
        ans = x*ones + y*twos
    print(ans)
