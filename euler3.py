# Project Euler
# Problem 3 - largest prime factor of the number 600851475143

def prime_factors(number):
    prime_factors_found = []

    if number > 1:
        i = 2 
        while True:
            if number%i == 0:
                prime_factors_found.append(i)
                prime_factors_found.extend(prime_factors(number/i))
                break

            i += 1

    return prime_factors_found

print max(prime_factors(600851475143))
