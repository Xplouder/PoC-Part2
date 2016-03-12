import math


def multiply_up(n):
    if n == 0:
        return 1
    else:
        return n * multiply_up(n - 1)


for x in range(100):
    print multiply_up(x)
    print math.factorial(x)
    print 
