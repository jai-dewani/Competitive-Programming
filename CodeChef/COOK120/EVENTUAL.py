for _ in range(int(input())):
    n = int(input())
    s = input()
    count = [0]*26
    for i in range(n):
        count[ord(s[i])-97] += 1 
    flag = True 
    for i in count:
        if i%2:
            flag=False 
    if flag:
        print("YES")
    else:
        print("NO")