from math import log

def prime_factors(n):
    factors = []
    f = 2
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f        
        else:
            f += 1
    if n > 1:
        factors.append(n)
    return factors

def list_factors(n):
    list = []
    for i in range(1,n):
        for f in prime_factors(i):
            if f not in list:
                list.append(f)
    return list

def smallest_multiple(n):
    product = 1
    for i in list_factors(n):
        product *= i ** int(log(n, i)) # multiply by greatest power of prime factor less than n
    return product

print smallest_multiple(20)
