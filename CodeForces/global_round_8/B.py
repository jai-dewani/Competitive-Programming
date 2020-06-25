n = int(input())
str = 'codeforces'
ans = ''
freq = [1,1,1,1,1,1,1,1,1,1]
count = 1
i = 0
while count<n: 
	count = count//freq[i]
	freq[i] += 1 
	count *= freq[i]
	i = (i+1)%10
for i in range(10):
	ans += str[i]*freq[i]
print(ans)