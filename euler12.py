# Project Euler
# Problem 12 - Find the first triangle number to have over five hundred divisors

from math import sqrt

factors_result = {1:1}

def get_factors_length(number):

    #if number in factors_result:
    #    return factors_result[number]

    factors = 0
    for i in xrange(1, int(sqrt(number)+1)):
        if number%i == 0:
            factors += 2

    #factors_result[number] = factors
    return factors

number = 1
while True:
    triangle_number = number * (number + 1) / 2
    factors_length = get_factors_length(triangle_number)

    if factors_length > 500:
        print triangle_number
        break

    number += 1
