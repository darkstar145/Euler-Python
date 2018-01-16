# Find the sum of all the primes below two million.
# 142913828922

import math

def isPrime(x):
    if (x == 1):
        return False
    elif (x == 2 or x == 3):
        return True
    for i in range(2, int(math.ceil(math.sqrt(x)))):
        if (x % i == 0):
            return False
    return False;

sum = 2
for i in range(3, 2000000, 2):
    if (isPrime(i)):
        sum += i
print sum

