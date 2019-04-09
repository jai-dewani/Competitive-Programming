
def prime(low,high):
	# print('1',low,high)
	ar = []
	low = int(low)
	high = int(high)
	for i in range(low,high):
		# print(i,len(ar))
		flag = True
		for j in range(2,int(pow(i,0.5))+2):
			if i%j==0:
				flag=False
				break
		if flag:
			ar.append(i)
	print(len(ar))

if __name__=='__main__':
	import multiprocessing as mp
	print("Number of processors: ", mp.cpu_count())
	from multiprocessing import Pool
	pool = Pool()
	t = int(input())
	import time
	start = time.time()
	result1 = pool.apply_async(prime,args=(0,t/8))
	result2 = pool.apply_async(prime,args=(1*t/8,t/4))
	result3 = pool.apply_async(prime,args=(2*t/8,3*t/8))
	result4 = pool.apply_async(prime,args=(3*t/8,4*t/8))
	result5 = pool.apply_async(prime,args=(4*t/8,5*t/4))
	result6 = pool.apply_async(prime,args=(5*t/8,6*t/8))
	result7 = pool.apply_async(prime,args=(6*t/8,7*t/8))
	result8 = pool.apply_async(prime,args=(7*t/8,t))
	pool.close()
	pool.join()
	print('end')
	end = time.time()
	print('Time: ',(end-start))
	start = time.time()
	prime(0,t)
	end = time.time()
	print('Time: ',(end-start))
	# print(result4+result3+result2+result1)