# Project Euler
# Problem 24

import sys

count = 0

factorial_results = {1: 1}

def factorial(number):

    # Memoize
    if number in factorial_results:
        return factorial_results[number]

    result = number * factorial(number - 1)

    factorial_results[number] = result

    return result

def permute(selected, number, desired_perm):
    global count 

    if len(selected) == number:
        count += 1
        if count == desired_perm:
            print ''.join([str(n) for n in selected])
            sys.exit(1)

    # Optimization - check if you really want to go into the stack, or just calculate count and continue
    possible_count = count + factorial(number - len(selected))
    if possible_count >= desired_perm:
        for i in xrange(number):
            if i in selected:
                continue
            else:
                permute(selected + [i], number, desired_perm)
    else:
        count = possible_count # Assume that you actually did all the inner permutations

permute([], 10, 1000000)
