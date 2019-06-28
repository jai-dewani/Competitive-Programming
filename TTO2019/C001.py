t = int(input())
current = ""
previous = []
for _ in range(t):
    x = input()
    n = 0
    k = 0
    if x[0]=='4':
        n = int(x)
        current = previous.pop()
    elif x[0]=='3' or x[0]=='2':
        n,k  = list(map(int,x.split()))
        if n==2:
            previous.append(current)
            current = current[0:len(current)-k]
        else:
            print(current[k-1])
    else:
        n,k = x.split()
        n = int(n)
        previous.append(current)
        current += k
    
        
