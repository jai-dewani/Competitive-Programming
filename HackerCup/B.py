output = open('output2.txt','w+')
inputt = open('input2.txt','r')
for _ in range(int(inputt.readline())):
    print(_+1)
    n = int(inputt.readline())
    s = inputt.readline()
    dic = {}
    dic['A'] = 0
    dic['B'] = 0 
    for i in range(n):
        dic[s[i]] += 1

    output.write(f"Case #{_+1}: ")
    if abs(dic['A']-dic['B'])>=3:
        output.write("N\n")
    else:
        output.write("Y\n")
output.close()
inputt.close()