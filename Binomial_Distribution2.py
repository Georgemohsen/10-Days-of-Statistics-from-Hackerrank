from math import factorial as f

percentage, size = map(float, input().split())

percentage /=100
n = int(size)

def comb(n,r):
	return f(n)/ (f(r)*f(n-r))

result1 = 0.0
result2 = 0.0

for k in range(0,3):
	result1 += percentage**k * (1-percentage)**(n-k) * comb(n,k)
	if k ==2:
		continue
	else:
		result2 += percentage**k * (1-percentage)**(n-k) * comb(n,k)

print("{:.3f}".format(result1))
print("{:.3f}".format(1-result2))		
			
