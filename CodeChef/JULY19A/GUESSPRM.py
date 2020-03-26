def primefac(a,g):
    ans = []
    div = 2
    while a>1:
        if a%div==0:
            while a%div==0:
                a = a/div
            if div>g:
                ans.append(div)
        else:
            div += 1
    return ans


t = int(input())
for _ in range(t):
    mod = None
    n = 10
    end = False
    ans = None
    answer = False
    possible = None
    while answer == False:
        while end==False:
            print(1,n)
            mod = int(input())
            if mod!=0:
                if mod==n*n:
                    n = n*n
                else:
                    print(possible)
                    if possible is None:
                        possible = set(primefac(n*n-mod,mod))
                    else:
                        possible = possible.intersection(set(primefac(n*n-mod,mod)))
                    print(possible)
                    if len(possible)==1:
                        end = True
                        ans = list(possible)[0]
                    else:
                        n = list(possible)[-1]
        print(2,ans)
        result = input()
        if result == "Yes":
            answer = True
