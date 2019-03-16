# input() --> in python3.x
# raw_input() --> in python2.x
length = input()
data = [int(x) for x in input().split()]

mean = sum(data)/len(data)
print("{:.1f}".format(mean)) 


# sort the list
data.sort()
# calculating the median
if len(data) % 2 == 0:
	index2 = int(len(data)/2)
	index1 = int ( index2 - 1)
	print(index1)
	print(index2)
	median =int(( data[index1] + data[index2] )/2)
	print("{:.1f}".format(median))
elif len(data) %2 !=0:
	middle_index = ((len(data)+1 )/ 2) -1
	print("{:.1f}".format(data[middle_index])
		