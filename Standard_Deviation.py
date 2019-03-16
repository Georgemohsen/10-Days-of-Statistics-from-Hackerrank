import math

length = input()
x = [int(i) for i in input().split()]

u = sum(x)/int(length)

x_u = []

for i in range(0,int(length)):
	x_u.append(int((x[i]-u)**2))

standard_deviation = math.sqrt(sum(x_u)/int(length))

print("{:.1f}".format(standard_deviation))
	
