ans = [1, 2, 1, 3, 1, 4, 2, 3, 2, 1, 5, 1, 6, 4, 2, 2, 1, 7, 3, 1, 8, 2, 5, 1, 9, 2, 2, 3, 3, 1, 10, 4, 4, 4, 1, 11, 5, 5, 6, 6, 1, 12, 5, 1, 13, 6, 1, 14, 7, 8, 3, 1, 15, 7, 2, 1, 16, 3, 1, 17, 9, 2, 1, 18, 4, 1, 19, 10, 2, 11, 7, 1, 20, 6, 2, 12, 7, 13, 8, 2, 1, 21, 3, 1, 22, 14, 3, 3, 1, 23, 8, 1, 24, 15, 4, 5, 4, 1, 25, 8, 1, 26, 16, 4, 1, 27, 5, 2, 2, 1, 28, 9, 2, 6, 2, 1, 29, 9, 3, 6, 1, 30, 10, 3, 1, 31, 7, 4]
t = int(input())
for _ in range(t):
    n = int(input())
    print(ans[n-1])


# ar = [0]
# ans = [1]
# for i in range(1,128):
#     x = ar[i-1]
#     x_lasttime = -1
#     for j in range(i-2,-1,-1):
#         if ar[j]==x:
#             x_lasttime = j
#             break
#     if x_lasttime==-1:
#         ar.append(0)
#     else:
#         ar.append(i-1-j)
#     count = 0
#     for j in range(len(ar)):
#         if ar[j]==ar[i]:
#             count += 1
#     ans.append(count)
# print(ar)
# print(ans)