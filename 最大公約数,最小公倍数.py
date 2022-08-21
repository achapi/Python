from functools import reduce
import math

def gcd(*numbers):return reduce(math.gcd, numbers)

def _lcm(x,y):return (x * y) // math.gcd(x, y)

def lcm(*numbers):return reduce(_lcm, numbers, 1)
