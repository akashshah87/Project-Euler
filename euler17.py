# Project Euler
# Problem 17 - how many letters will be used while listing out 1 - 1000

database = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        }

def letters(number, standalone=False):
    if number in database:
        if number == 100 or number == 1000:
            if standalone:
                return 'one'+database[number]

        return database[number]

    highest_place_value = 10 ** (len(str(number)) - 1)

    if highest_place_value == 100:
        if number % highest_place_value == 0:
            count = letters(number / highest_place_value) + letters(highest_place_value) 
        else:
            count = letters(number / highest_place_value) + letters(highest_place_value) + 'and' + letters(number % highest_place_value)
    elif highest_place_value == 10:
        count =  letters(number/highest_place_value * highest_place_value) + letters(number % highest_place_value)
    else:
        count = letters(number / highest_place_value) + letters(highest_place_value) + letters(number % highest_place_value)

    database[number] = count
    return count

count = sum(len(letters(n, standalone=True)) for n in range(1, 1001))

print count
