n = input()
x = [int(i) for i in input().split()]
w = [int(j) for j in input().split()]

num_sum = 0

for inc in range(0,int(n)):
	num_sum+=(x[inc]*w[inc])

deno_sum = sum(w)
result = num_sum/deno_sum

print("{:.1f}".format(result)) 	
