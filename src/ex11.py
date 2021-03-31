''' 
    Textbook RSA
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

# Find gcd (greatest common divisor) of two numbers
def gcd(a, b):
  
    if (a == 0):
        return b
    return gcd(b % a, a)

# Find Euler's Totient Function (φ)
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

# Find modular inverse of a mod m
def modularInverse(a, m):
     
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

print(primeFactors(11413))
print(phi(11413))
print(modularInverse(809,1001))


