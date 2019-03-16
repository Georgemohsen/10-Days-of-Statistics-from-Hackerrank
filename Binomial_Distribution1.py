from math import factorial as f

x, y = map(float, input().split()) 

p = x / (x + y)

def comb(n,r):
	return f(n)/ (f(r)*f(n-r))

n = 6
result = 0.0
for k in range(3,7):
	result += p**k * (1-p)**(n-k) * comb(n,k)

print("{:.3f}".format(result))
