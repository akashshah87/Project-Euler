# Project Euler
# Problem 5 - What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def random_function_name(max_number):

    number = 1
    for i in xrange(1, max_number+1):
        if number%i == 0:
            continue
        else:
            for j in xrange(i-1, 1, -1):
                if i%j == 0:
                    number *= i/j
                    break
            else:
                number *= i
    return number

print random_function_name(20)
