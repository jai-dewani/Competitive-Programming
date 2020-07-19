for _ in range(int(input())):
    n = int(input())
    s = list(input())

    i = 0
    st = "abacaba"
    found = False 
    while i<n-6:
        if not found:
            flag = True 
            for j in range(7):
                if s[i+j]=="?":
                    continue
                elif s[i+j]!=st[j]:
                    flag = False 
                    break 
            if flag:
                ans = [x for x in s]
                for j in range(7):
                    ans[i+j]=st[j]
                check = 0 
                for j in range(n-6):
                    if ans[j:j+7]==list(st):
                        # print("NO")
                        check += 1
                if check==1:
                    found = True 
                    for i in range(n):
                        if ans[i]=="?":
                            ans[i] = "d"
                    print("Yes")
                    print("".join(x for x in ans))
                    break 
        i += 1
    if not found:
        print("No")
    

def a():
    found = False 
    two = False
    for i in range(n-6):
        if s[i:i+7]==list("abacaba"):
            if found:
                two = True 
            else:
                found = True 
    if two:
        print("No")
    else:
        if found:
            print("Yes")
            ans = ""
            for i in s:
                if i=="?":
                    ans += "d"
                else:
                    ans += i
            print(ans)
        else:
            for i in range(n-6):
                st = "abacaba"
                found = False
                flag = True  
                for j in range(7):
                    if s[i+j]=="?":
                        continue
                    elif s[i+j]!=st[j]:
                        flag = False 
                        break 
                # print(flag,found,i)
                if flag:
                    found = True 
                    ans = []
                    for j in s:
                        if j=="?":
                            ans.append("d")
                        else:
                            ans.append(j)
                    for j in range(7):
                        ans[i+j] = st[j]
                    break 
            if found:
                print("Yes")
                print("".join(x for x in ans))
            else:
                print("No")