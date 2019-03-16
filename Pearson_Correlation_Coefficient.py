import statistics
import math

length = input()
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

ux = statistics.mean(x)
uy = statistics.mean(y)


stdx = statistics.pstdev(x) 
stdy = statistics.pstdev(y)

den = stdx*stdy*int(length)
num = 0

for k in range(0,int(length)):
	num += (x[k]-ux)*(y[k]-uy)

pearson = num/den
print("{:.3f}".format(pearson))	