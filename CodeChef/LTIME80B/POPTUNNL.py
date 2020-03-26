for _ in range(int(input())):
    n,k = map(int,input().strip().split())
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    visited = [False]*n
    visited[0] = True
    found = False
    current = [0,None]
    pointer = 0
    step = 0
    while len(current)>0:
        node = current[pointer]
        if node == None:
            if pointer == len(current):
                break
            current.append(None)
            step += 1
            pointer += 1
            print(current)
            # continue
        elif node == n-1:
            found = True
            break
        else:
            ar = matrix[node]
            visited[node] = True
            for i in range(len(ar)):
                print(ar[i],visited[i])
                if ar[i]=='1' and visited[i]==False:
                    print("Its happening")
                    current.append(i)
            pointer += 1
            print(node,ar,current)
    if found:
        print(step)
    else:
        print(-1)
