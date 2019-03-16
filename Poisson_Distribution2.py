x, y = map(float, input().split()) 

expected_A = 160 + 40 * ( x + x**2 )
expected_B = 128 + 40 * ( y + y**2 )

print("{:.3f}".format(expected_A))
print("{:.3f}".format(expected_B))