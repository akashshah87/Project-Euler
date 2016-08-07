# Project Euler
# Problem 4 - Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    if int((str(number)[::-1])) == number:
        return True
    else:
        return False

def has_3_digit_factors(number):

    if number<100:
        return False

    for i in xrange(100, 1000):
        if number%i == 0:
            if 100 <= number/i <= 999:
                return True

    return False

largest_palindrome = -1
for i in xrange(100*100, 999*999 + 1):
    if is_palindrome(i) and has_3_digit_factors(i):
        largest_palindrome = max(i, largest_palindrome)

print largest_palindrome
