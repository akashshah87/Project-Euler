# Project Euler
# Problem 9 - Find the product abc for the only Pythagorean triplet (a**2 + b**2 = c**2) where a + b + c = 1000

squares = {}
reverse_squares = {}

def square(number):
    if number in squares:
        return squares[number]
    else:
        sq = number**2
        squares[number] = sq

# Calculate all potential c squares (i.e. a**2 + b**2 is capped at 2000000)

c = 1
while c**2 < 2000000:
    sq = c**2
    squares[c] = sq
    reverse_squares[sq] = c
    c += 1

for a in xrange(1, 999):
    for b in xrange(a+1, 999):
        if a + b > 1000:
            continue

        pot_c_sq = square(a) + square(b)

        if pot_c_sq in reverse_squares:
            pot_c = reverse_squares[pot_c_sq]

            if a + b + pot_c == 1000:
                print a*b*pot_c
