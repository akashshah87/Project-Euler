# Project Euler
# Problem 14 - Collatz Problem longest chain for starting number under 1000000

def function(number):
    if number%2 == 0:
        return number/2
    else:
        return 3*number + 1

sequence_results = {1:1}
def sequence(start_number):

    if start_number in sequence_results:
        return sequence_results[start_number]

    seq = 1 + sequence(function(start_number))

    sequence_results[start_number] = seq
    return seq

max_res = 0
max_start = 0

for i in xrange(1, 1000000, 2): # No need to run for even numbers, every even number can be reached from a smaller odd number by adding one step in the chain
    res = sequence(i)
    if res > max_res:
        max_res = res
        max_start = i

print max_start, max_res
