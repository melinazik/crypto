''' 
    Textbook RSA
    FInd Private Key
    Exercise 11
    
    Melina Zikou (2021)
'''

import math


# Find prime factors of a number
def primeFactors(number):
    factors = []

    # get the number of 2's that divide the number
    while number % 2 == 0:
        factors.append(2)
        number = number / 2

    # number is odd at this point
    # skip 2 for each increment
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(int(i))
            number = number / i

    if number > 2:
        factors.append(int(number))

    return factors


print(primeFactors(11413))

