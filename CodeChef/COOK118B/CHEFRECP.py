for i in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    has = {}
    freq = {}
    count = 0
    previous = None
    flag = True
    for i in ar:
        # print(has)
        if i==previous:
            count += 1
        else:
            if has.get(i)==1:
                flag = False
                break
            else:
                has[i]=1
                if freq.get(count)==1:
                    flag = False
                    break
                freq[count] = 1
                count = 1
                previous = i 
    if freq.get(count)==1:
        flag = False    
    if flag:
        print("YES")
    else:
        print("NO")