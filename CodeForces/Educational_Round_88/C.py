# from random import randint
# from check import check

result = ""
for _ in range(int(input())):
    # h = randint(1,10**6)
    # c = randint(1,h-1)
    # t = randint(c+1,h-1)
    h,c,t = map(int,input().split())
    min_diff = h-t
    ans = 0
    temp = h
    cups = 1
    mid = (h+c)/2 

    if t<=mid:
        ans = 1
    elif t>=h:
        ans = 0
    else:
        i = 1
        while True:
            if i%2:
                temp = temp + cups + c
            else:
                temp = temp*cups + h
            cups += 1
            temp = temp/cups
            # print('temp',temp,abs(t-temp),min_diff)
            if abs(t-temp)<min_diff:
                # print('change',min_diff,abs(t-temp))
                min_diff = abs(t-temp)
                ans = i 
            elif i%2==0 and (t-temp)>min_diff:
                # print('break',i,t,temp,min_diff)
                break
            # print('logs',i,temp,t)
            if temp==t:
                ans = i 
                # print('break',i,t,temp,min_diff)
                break
            i += 1
    # ans1 = check(h,c,t)
    # if ans+1!=ans1:
    #     print('ERROR')
    #     print(h,c,t,ans+1,ans1)
    #     break
    # print(ans+1)
    result += str(ans+1)+'\n'
print(result)

