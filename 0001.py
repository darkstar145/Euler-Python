# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

def sum_multiple(mult, maxi):
    return ( (maxi/mult) * (mult + (maxi/mult * mult)) ) / 2

print(sum_multiple(3,999) + sum_multiple(5,999) - sum_multiple(15,999))