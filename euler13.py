# Project Euler
# Problem 13 - first ten digits of sum of 100 50-digit numbers

numbers = []
with open('euler13.txt') as number_file:
    for line in number_file:
        numbers.append(line.strip())

result = ""
carry = 0
for i in xrange(49, -1, -1):
    r = sum([int(n[i]) for n in numbers]) + carry
    bit, carry = r%10, r/10
    result = str(bit) + result

if carry > 0:
    result = str(carry) + result

print result[:10]
