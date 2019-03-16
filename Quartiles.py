from statistics import median
import math

length = input()
x = [int(i) for i in input().split()]

x.sort()

median2 = median(x)

if int(length) % 2 ==0:
	left_array = x[0:int(len(x)/2)]
	median1 = median(left_array)
	print(int(median1))
	print(int(median2))
	right_array = x[int(len(x)/2):len(x)]
	median3 = median(right_array)
	print(int(median3))
else:
	middle_index = math.floor(len(x)/2)
	left_array = x[0:middle_index]
	median1 = median(left_array)
	print(int(median1))
	print(int(median2))
	right_array = x[middle_index+1:len(x)]
	median3 = median(right_array)
	print(int(median3))
