x, y = map(float, input().split()) 

size = input()

n = int(size)

pd = x/y
result = 0.0

for k in range(0,n):
	result += (1-pd)**k * pd

print("{:.3f}".format(result))
