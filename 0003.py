def gpf(x):
    for n in xrange(2,x):
        if x % n == 0:
            x = x / n
        elif x / n == 1:
            break
    return x

print gpf(600851475143)
