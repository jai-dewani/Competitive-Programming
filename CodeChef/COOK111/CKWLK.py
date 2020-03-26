for _ in range(int(input())):
    n = input()
    flag = len(n)-1
    count1 = 0
    while n[flag]=='0':
        flag -= 1
        count1 += 1
    num = n[:flag+1]
    num = int(num)
    count2 = 0
    while num%2==0:
        num  = num//2
        count2 += 1
    
    if num==1 and count2<=count1:
        print("Yes")
    else:
        print("No")
