for _ in range(int(input())):
    s = input()
    i = 0
    count = 0
    while i<len(s)-1:
        if s[i:i+2]=='xy' or s[i:i+2]=='yx':
            count += 1
            i += 2
        else:
            i += 1
    print(count)