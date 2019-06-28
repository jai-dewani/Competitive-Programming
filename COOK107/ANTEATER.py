from collections import Counter
t = int(input())
for _ in range(t):
    r,c = list(map(int,input().split()))
    matrix = []
    for i in range(r):
        matrix.append(list(input()))
    sim = [[[]for i in range(c)]for j in range(r)]
    ants = []
    eaters = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j]=='U' or matrix[i][j]=='D' or matrix[i][j]=='L' or matrix[i][j]=='R':
                ants.append([i,j,matrix[i][j]])
            elif matrix[i][j]=='#':
                eaters.append([i,j])

    
    for i in range(len(ants)):
        row,col,d = ants[i]
        ver = 0
        hor = 0
        #print(ants[i])
        if d=="U":
            ver = -1
        elif d=="D":
            ver = 1
        elif d=="L":
            hor = -1
        else:
            hor = 1
        time = 0
        #print("RC",r,c)
        while row<r and row>=0 and col>=0 and col<c and matrix[row][col]!='#':
            if time!=0:
                sim[row][col].append(time)
            row += ver
            col += hor
            time += 1
            #print(time,row,col)
    ''' 
    print(ants)
    print(eaters)
    for i in sim:
        print(i)
    '''
    
    ans = 0
    for i in range(r):
        for j in range(c):
            temp = Counter(sim[i][j])
            for k in temp:
                var = temp[k]
                ans += (var*(var-1))//2
    print(ans)
