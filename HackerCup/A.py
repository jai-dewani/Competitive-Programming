output = open('output.txt','w+')
for _ in range(int(input())):
    n = int(input())
    i = input()
    o = input()
    p = [["N" for i in range(n)] for j in range(n)]
    # print(i[0]=="Y",o[0]=="Y")
    # print(i,o)
    for j in range(n):
        p[j][j] ="Y"
    for diff in range(1,n):
        for j in range(n-diff):
            if p[j][j+diff-1]=="Y":
                # print(o[j],i[j+diff])
                if o[j+diff-1]=="Y" and i[j+diff]=="Y":
                    p[j][j+diff] = "Y"
        for j in range(diff,n):
            if p[j][j-diff+1]=="Y":
                if o[j-diff+1]=="Y" and i[j-diff]=="Y":
                    p[j][j-diff]="Y"
                    # print(p)
    
    output.write(f"Case #{_+1}:\n")
    for j in p:
        output.write(''.join(j)+"\n")
    