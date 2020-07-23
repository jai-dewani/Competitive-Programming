for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    order = []
    i = 0
    current = a[0]
    while i<n:
        if a[i]!=current:
            order.append(i)
            current = a[i]
        i += 1
    if a[-1]=='1':
        order.append(n)
    # print(order)
    i = n-1 
    current = b[-1]
    if current=='1':
        order.append(n)
    while i>=0:
        if b[i]!=current:
            order.append(i+1)
            current = b[i]
        i -= 1
    print(len(order),*order)