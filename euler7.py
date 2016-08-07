# Project Euler
# Problem 7 - find the 10001st prime number

primes = []

number = 2
while True:
    for i in primes:
        if number%i == 0:
            break
    else:
        primes.append(number)
        if len(primes) == 10001:
            print number
            break

    number += 1
