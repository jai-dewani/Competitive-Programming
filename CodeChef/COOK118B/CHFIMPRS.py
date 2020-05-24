from collections import Counter 
for _ in range(int(input())):
    n,m = map(int,input().split())
    matrix = []
    for i in range(n):
            matrix.append(list(map(int,input().split())))
    count = Counter()
    for i in range(n):
        for j in range(m):
            count[matrix[i][j]] += 1
    # print(matrix,count)
    odd_possible = 0
    if m%2==1:
        odd_possible = n 
    freq = list(count.values())
    odd_values = 0
    for i in freq:
        if i%2==1:
            odd_values += 1
    if odd_values>odd_possible:
        print(-1)
    else:
        odd_list = []
        even_list = []
        for i in count:
            if count[i]%2==1:
                odd_list.append(i)
                even_list += [i]*((count[i]-1)//2)
            else:
                even_list += [i]*(count[i]//2)
        # print('even',even_list)
        # print('odd',odd_list)
        answer = []
        if odd_possible==0:
            i = 0
            step = m//2 
            for j in range(n):
                half = even_list[i:i+step]
                o_half = half[::-1]
                answer.append(half + o_half)
                # print(even_list[i:i+step])
                i += step
                # print(i)
        else:
            i = 0
            step = m//2
            for j in range(n):
                half = even_list[i:i+step]
                o_half = half[::-1]
                if odd_list==[]:
                    odd_list += [even_list[i+step]]*2
                    i += 1
                middle = odd_list.pop()
                answer.append(half + [middle] + o_half)
                i += step
                # print(i)
        # print('answer')
        for i in answer:
            print(*i)

