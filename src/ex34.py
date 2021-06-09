''' 
    Sum of primes => prime
    Exercise 34
    
    Melina Zikou (2021)
'''
import math


def calculatePrimes(lower, upper):
    primes = []
    for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def findPrimes(num, primes):
    flag = False
    first = -1
    second = -1
    third = -1

    for i in range(len(primes)):
 
        # Take the first prime number
        first = primes[i]
        for j in range(len(primes)):
 
            # Take the second prime number
            second = primes[j]
 
            # Subtract the two prime numbers
            # from the N to obtain the third number
            third = num - first - second
 
            # If the third number is prime
            if (third in primes) :
                flag = True
                break
     
        if (flag):
            break
     
    # Print the three prime numbers
    # if the solution exists
    if (flag):
        return 1
    else :
        return -1

lower = 1000
upper = 2000

primeLog = calculatePrimes(1, upper + 2)
primeArray = calculatePrimes(lower, upper)

count = 0
for i in primeArray:
    if(findPrimes(i, primeLog) == 1):
        count = count + 1
        
print(len(primeArray))
print(count)