from math import factorial as f 
from math import exp

u = input()
x = input()

U = float(u)
X = int(x)

prob = ( exp(-U) *  U**X ) / f(X)
print("{:.3f}".format(prob))