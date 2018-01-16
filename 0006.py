def sum_of_squares(x):
    sum = 0
    for num in range(1, x+1):
        sum += num**2
    return sum

def square_of_sum(x):
    sum = 0
    for num in range(1, x+1):
        sum += num
    return sum**2

print square_of_sum(100) - sum_of_squares(100)
