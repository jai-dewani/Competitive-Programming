t = int(input())
for z in range(t):
	n,k = list(map(int,input().split()))
	ar = list(map(int,input().split()))
	ar.sort()
	sum1 = 0
	sum2 = 0
	summ = sum(ar)
	for i in range(k):
		sum1 += ar[i]
		sum2 += ar[n-1-i]
	diff1 = abs(summ-2*sum1)
	diff2 = abs(summ-2*sum2)
	print(max(diff1,diff2))