x, y = map(float, input().split()) 

size = input()

n = int(size)

pd = x/y 
prob_1st_defective = (1-pd)**4 * pd

print("{:.3f}".format(prob_1st_defective))
