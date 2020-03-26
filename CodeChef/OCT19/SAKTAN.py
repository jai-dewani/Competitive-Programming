t = int(input())
for _ in range(t):
    n,m,q = map(int,input().strip().split())
    row = [0 for i in range(n+1)]
    col = [0 for i in range(m+1)]
    
    for z in range(q):
        i,j = map(int,input().strip().split())
        row[i] ^= 1
        col[j] ^= 1
    row_count = row.count(1)
    col_count = col.count(1)
    ans = row_count*n + col_count*m - 2*row_count*col_count
    print(ans)
