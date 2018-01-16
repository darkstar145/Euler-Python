def is_palindrome(n):
    return str(n) == str(n)[::-1]

max_palindrome = 0
for x in range(99,999):
    for y in range (99,999):
        product = x * y
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product
print max_palindrome
