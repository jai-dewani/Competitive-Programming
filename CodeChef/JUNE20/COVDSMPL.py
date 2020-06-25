'''
def work(n,p,mat,odd):
    for i in range(n):
        for j in range(0,n-1,2):
            print(1,i+1,j+1,i+1,j+2)
            ans = int(input())
            if ans==-1:
                print(1/0)
            if ans==0:
                continue 
            elif ans==1:
                print(1,i+1,j+1,i+1,j+1)
                ans2 = int(input())
                if ans2==0:
                    mat[i][j+1]=1
                else:
                    mat[i][j]=1
            else:
                mat[i][j] = 1
                mat[i][j+1] = 1
        if odd:
            print(1,i+1,n,i+1,n)
            re = int(input())
            if re==1:
                mat[i][n-1] = 1
'''
'''
def solve(mat, nlow, nhigh, mlow, mhigh):
    area = (nhigh-nlow+1)*(mhigh-mlow+1)
    print(1, nlow+1, mlow+1, nhigh+1, mhigh+1)
    count = int(input())
    if count==0:
        pass
    elif area==1:
        mat[nlow][mlow] = 1
    elif count==area:
        for i in range(nlow, nhigh+1):
            for j in range(mlow, mhigh+1):
                mat[i][j]=1
    else:
        n_mid = (nlow+nhigh)//2
        m_mid = (mlow+mhigh)//2
        if nlow==nhigh:
            coun = 0
            if coun!=count:
                coun += solve(mat, nlow, n_mid, mlow, m_mid)
            if coun!=count:
                mat[nlow][m_mid+1] = 1
                # coun += solve(mat, nlow, n_mid, m_mid+1, mhigh)
        elif mlow==mhigh:
            coun = 0
            if coun!=count:
                coun += solve(mat, nlow, n_mid, mlow, mhigh)
            if coun!=count:
                mat[n_mid+1][mlow] = 1
                # coun += solve(mat, n_mid+1, nhigh, mlow, mhigh)
        else:
            coun = 0
            if coun!=count:
                coun += solve(mat, nlow, m_mid, mlow, m_mid)
            if coun!=count:
                coun += solve(mat, nlow, m_mid, m_mid+1, mhigh)
            if coun!=count:
                coun += solve(mat, n_mid+1, nhigh, mlow, m_mid)
            if coun!=count:
                coun += solve(mat, n_mid+1, nhigh, m_mid+1, mhigh)

    return count
'''

def solve(mat, nlow, nhigh, mlow, mhigh):
    row = nhigh - nlow 
    col = mhigh - mlow 
    if row>col:
        
    

for _ in range(int(input())):
    n,p = map(int,input().split())
    mat = [[0 for i in range(n)] for j in range(n)]
    # solve(mat, 0, n-1, 0, n-1)
    solve(mat,0,n-1,0,n-1)
    for i in mat:
        print(*i)
    ans = int(input())
    if ans==1:
        continue
    else:
        break
'''
0 1 0
1 0 1
1 0 0
'''