for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    impossible = False 
    charaters = {}
    count = {}
    indexOfChar = {}
    for i in range(26):
        charaters[chr(97+i)] = 0 
    for i in range(n):
        charaters[a[i]] += 1
    for i in range(n):
        if b[i]>a[i]:
            impossible = True
            break 
        if charaters[b[i]]==0:
            impossible = True
            break 
        if a[i]!=b[i]:
            if count.get(b[i])==None:
                count[b[i]] = [i]
            else:
                count[b[i]].append(i)
        else:
            if indexOfChar.get(a[i])==None:
                indexOfChar[a[i]] = i
    steps = 0
    answer = []
    alpha = [chr(97+i) for i in range(26)]
    rev_alpha = alpha[::-1]
    for i in rev_alpha:
        if count.get(i)!=None:
            # print(count[(i,j)])
            steps += 1
            if indexOfChar.get(i)!=None:
                index = indexOfChar[i]
                answer.append(sorted( [index] + count[i] ))
            else:
                index = -1 
                for k in range(n):
                    if a[k]==i:
                        index = k
                        break
                answer.append(sorted( [index] + count[i] ))
    if impossible:
        print(-1)
    else:
        print(steps)
        for i in answer:
            print(len(i),*i)
    
    