# Project Euler
# Problem 10 - Sum of all primes below 2000000

primes = []

def sieve(number):
    filtered_numbers = set()
    sum = 0

    for i in xrange(2, number):
        if i not in filtered_numbers:
            sum += i
            filtered_numbers.update(xrange(i, number, i))

    return sum

print sieve(2000000)
