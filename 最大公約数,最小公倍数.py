from functools import reduce
import math

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)