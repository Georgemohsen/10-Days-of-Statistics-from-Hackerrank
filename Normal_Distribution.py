import math

mean, sd = map(int,input().split())

greaterThan = input()

failed = input()

def normalDistribution(std, mean, x):
	dummy = 1 + math.erf((x-mean) / (std*math.sqrt(2)))
	return 0.5*dummy

result1 = 1- normalDistribution(sd, mean, float(greaterThan))
result2 = 1- normalDistribution(sd, mean, float(failed))
result3 = normalDistribution(sd, mean, float(failed))

print("{:.2f}".format(result1))
print("{:.2f}".format(result2))
print("{:.2f}".format(result3))