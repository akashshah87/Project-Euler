# Project Euler
# Problem 2 - By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

prev = 1
fib = 2
sum = 0

while True:

    if fib > 4000000:
        break

    if fib%2 == 0:
        sum += fib

    fib, prev = fib + prev, fib

print sum
