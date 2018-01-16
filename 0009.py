def is_py(a, b, c):
    return (a**2 + b**2) == c**2

product = 1
# a = 1
# b = 1
# c = 1
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if (((a + b + c) == 1000) and is_py(a, b, c)):
                product = a * b * c

print(product)