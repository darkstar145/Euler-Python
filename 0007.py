def is_prime(n): # test if n is prime
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def prime_list(n): # create list of n prime numbers
    list = []
    counter = 0
    i = 0
    while counter <= n:
        if is_prime(i) == True:
            list.append(i)
            i += 1
            counter += 1
        else:
            i += 1
    return list

def prime(n): # return nth prime number
    list = prime_list(n)
    return list[n-1]

print prime(10001)
