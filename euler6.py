# Project Euler
# Problem 6 - Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# (a+b)**2 - (a**2 + b**2) = a**2 + b**2 - 2ab - a**2 - b**2 = 2ab

def diff(numbers):
    sum = 0

    for i in xrange(0, len(numbers)):
        for j in xrange(i+1, len(numbers)):
            sum += 2 * numbers[i] * numbers[j]
    
    return sum

print diff(range(1, 100))
