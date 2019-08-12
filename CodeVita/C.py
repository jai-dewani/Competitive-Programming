def sieve(n, prime, a): 
    for i in range(2,n+1): 
        prime[i] = True
       
    prime[1] = False
  
    p = 2
    while(p * p <= n): 
        if (prime[p] == True): 
            i = p * 2 
            while(i <= n): 
                prime[i] = False
                i += p 
        p+=1
      
    j = 0
    for p in range(2,n+1):  
        if (prime[p]==True):  
            a[j] = p
            
            j+=1


t = int(input())
for _ in range(t):
    n = int(input())
    maxprime = 10**6
    prime = [False](maxprime+1)
    a = [0]*maxprime
    sieve(maxprime,prime,a)
    ar = []
    while(1):
        if(a[i] * a[i] * a[i] > n): 
            break
        while (n % a[i] == 0): # if a[i] is a factor of n 
            n = n / a[i] 
            ar.append(a[i]) 
        i+=1
    ans = set([])
    lar = len(ar)
    for i in range(lar):
        for j in range(i+i,lar):
            ans.add(ar[i]*ar[j])
    ans = list(ans).sort()
    print(1,*ans)
'''

t = int(input())
for _ in range(t):
    n = int(input())
    ar1 = []
    ar2 = []
    for i in range(1,int(pow(n,0.5))):
        if n%i==0:
            ar1.append(i)
            ar2.append(n//i)
    l = len(ar1)
    for i in range(l):
        print(ar1[i],end=' ')
    for i in range(l):
        print(ar2[l-i-1],end=' ')
    print()
'''
