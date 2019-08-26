t = int(input())
for i in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        a = list(input())
        matrix.append(list(map(int,a)))
    pep = [[0,0] for i in range(n)]
    left, right = 0,0
    for i in range(n):
        for j in range(n//2):
            #print(i,j)
            pep[i][0] += matrix[i][j]
        for j in range(n//2,n):
            pep[i][1] += matrix[i][j]
        left += pep[i][0]
        right += pep[i][1]
    diff = abs(left-right)
    #print(diff,left,right)
    for i in range(n):
        z = abs((left-pep[i][0]+pep[i][1])-(right-pep[i][1]+pep[i][0]))
        #print(z,i)
        diff = min(z,diff)
        if diff==0:
            break
    print(diff)
