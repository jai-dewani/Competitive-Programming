from math import sqrt
def binary(ar,x,low,high):
	if low>high:
		return -1
	else:
		mid = (low+high)//2
		# print("MID",mid)
		if ar[mid]==x:
			return mid 
		elif ar[mid]>x:
			return binary(ar,x,low,mid-1)
		else:
			return binary(ar,x,mid+1,high)

def brute(n,m,x,y):
	pos_x = []
	neg_x = []
	zero_x = 0
	zero_y = 0
	pos_y = []
	neg_y = []
	for i in range(n):
		if x[i] < 0:
			neg_x.append(abs(x[i]))
		elif x[i] == 0:
			zero_x += 1
		else:
			pos_x.append(x[i])
	for i in range(m):
		if y[i] < 0:
			neg_y.append(abs(y[i]))
		elif y[i] == 0:
			zero_y += 1
		else:
			pos_y.append(y[i])
	count = 0
	pos_x.sort()
	pos_y.sort() 
	neg_x.sort() 
	neg_y.sort()
	for i in pos_y:
		h = i**2
		for j in pos_x:
			if h%j==0:
				find = h//j
				result = binary(neg_x,find,0,len(neg_x)-1)
				if result != -1:
					count += 1
	for i in neg_y:
		h = i**2
		for j in pos_x:
			if h%j==0:
				find = h//j
				result = binary(neg_x,find,0,len(neg_x)-1)
				if result != -1:
					count += 1
	for i in pos_x:
		h = i**2
		for j in pos_y:
			if h%j==0:
				find = h//j
				result = binary(neg_y,find,0,len(neg_y)-1)
				if result != -1:
					count += 1
	for i in neg_x:
		h = i**2
		for j in pos_y:
			if h%j==0:
				find = h//j
				result = binary(neg_y,find,0,len(neg_y)-1)
				if result != -1:
					count += 1
	if zero_x != 0:
		count += (n-1)*m 
	if zero_y != 0:
		count += n*(m-1)

def SieveOfEratosthenes(n):
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	return prime

def factors(x):
	factors = []
	i = 2
	while x>1:
		if prime[i] and x%i==0:
			count = 0
			while x%i==0:
				x = x//i 
				count += 1
			if count%2==1:
				factors.append(i)
		i += 1
	return tuple(factors)

def buildfact(fact):
	fact.append([])
	fact.append([])
	for i in range(2,10**5+1):
		# if i%10**3==0:
		# 	print(i//1000)
		# print(i,fact)
		if prime[i]:
			# print(i,'prime')
			fact.append([i])
			continue
		j = 2
		while True:
			if j%10**3==0:
				print(j,i)
			if prime[j] and i%j==0:
				temp = fact[i//j]
				temp1 = temp.copy()
				if j in temp1:
					temp1.remove(j)
				else:
					temp1.append(j)
				fact.append(temp1)
				break 
			j += 1
		

prime = SieveOfEratosthenes(10**5+1)
# print(prime[:10])
fact = []
buildfact(fact)
# print(fact[:100])

for _ in range(int(input())):
	n,m = map(int,input().strip().split())
	x = list(map(int,input().strip().split()))
	y = list(map(int,input().strip().split()))
	hx = {}
	hy = {}
	pos_x = []
	neg_x = []
	zero_x = 0
	zero_y = 0
	pos_y = []
	neg_y = []
	for i in x:
		hx[i] = 1
		if i==0:
			zero_x += 1
		elif i>0:
			pos_x.append(i)
		else:
			neg_x.append(abs(i))
	for i in y:
		hy[i] = 1
		if i==0:
			zero_y += 1
		elif i>0:
			pos_y.append(i)
		else:
			neg_y.append(abs(i))
	# print(pos_x,neg_x)
	# print(pos_y,neg_y)
	count = 0
	hash_x = {}
	hash_y = {}
	for i in range(len(neg_x)):
		res = tuple(fact[abs(neg_x[i])])
		if hash_x.get(res)==None:
			hash_x[res] = [i]
		else:
			hash_x[res].append(i)

	for i in range(len(neg_y)):
		res = tuple(fact[abs(neg_y[i])])
		if hash_y.get(res)==None:
			hash_y[res] = [i]
		else:
			hash_y[res].append(i)
	# print(hash_x)
	# print(hash_y)
	for i in range(len(pos_x)):
		res = tuple(fact[pos_x[i]])
		# print('res_x',res)
		arr = hash_x.get(res)
		# print('arr_x',arr)
		if arr !=None:
			for j in arr:
				prod = pos_x[i]*neg_x[j]
				find = int(sqrt(prod))
				if hy.get(find)!=None:
					# print(count)
					count += 1
				if hy.get(-find)!=None:
					# print(count)
					count += 1
				
	for i in range(len(pos_y)):
		res = tuple(fact[(pos_y[i])])
		# print('res',res,pos_y[i])
		arr = hash_y.get(res)
		# print('arr',arr)
		if arr !=None:
			for j in arr:
				prod = pos_y[i]*neg_y[j]
				find = int(sqrt(prod))
				# print('find',find)
				if hx.get(find)!=None:
					# print(count)
					count += 1
				if hx.get(-find)!=None:
					# print(count)
					count += 1
	if zero_x != 0:
		count += (n-1)*m 
	if zero_y != 0:
		count += n*(m-1)
	print(count)