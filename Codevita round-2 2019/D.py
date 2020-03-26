def vowel(a):
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        return True
    return False

def count(st,n,totalCount):
    if n==1 and len(st)!=0:
        return totalCount+1
    # print(len(st)-4*n+4)
    for i in range(4,len(st)-n*4+5):
        # print(st[i-1],st[i])
        if vowel(st[i]) or vowel(st[i-1]):
            continue
        totalCount = count(st[i:],n-1,totalCount)
        # print(st,i,totalCount)
    return totalCount

n = int(input())
st = input()
totalCount = 0

print(count(st,n,totalCount),end='')