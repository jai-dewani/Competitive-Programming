n, m, k = map(int,input().split())
chips = []
for i in range(k):
    a = list(map(int,input().split()))
    chips.append(a)
targets = []
for i in range(k):
    a = list(map(int,input().split()))
    targets.append(a)

ans = ""
for i in range(n):
    for j in range(m-1):
        ans += "D"
    ans += "R"

for i in range(n):
    for j in range(m-1):
        ans += "U"
    ans += "L"
print(len(ans))
print(ans)
