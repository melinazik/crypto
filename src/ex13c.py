''' 
    Safe and Sophie Germain Primes
    Miller Rabin method
    Exercise 13 (iii)
    
    Melina Zikou (2021)
'''

import random
import math
import sys
import time
from fractions import Fraction

# b = base number
# e = exponential
# m = modulo 
#     
# calculate b^e mod m
def fast(b,e,m):
    x = b
    g = e
    d = 1

    while g > 0:
        if g % 2 == 0:
            x = (x * x) % m
            g = g // 2
        else:
            d = (x * d) % m
            g = g - 1
    return d

# Miller Rabin Primality Test 
def rabinMiller(n):
     s = n-1
     r = 0
     # s is composite
     while s & 1 == 0:
         s = s // 2
         r += 1

     k = 0
     while k < 128:
        a = random.randrange(2, n - 1)
        x = fast(a, s, n) 

        # if x composite
        if x != 1:
            i = 0

            while x != (n - 1):
                if i == r - 1:
                    return False
                else:
                    i = i + 1
                    x = fast(x, 2, n)
        k += 2
     return True
        

# decrease the number of potential primes to be tested
def isPrime(n):
    # lowPrimes => all primes under 1000
    
    lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

    # numbers greater than 3
    if (n >= 3):
        # n & 1 = 0 +> n is composite
        if (n & 1 != 0):
            for p in lowPrimes:
                if (n == p):
                    return True
                if (n % p == 0 or n % p == (n - 1) // 2):
                    return False
            return rabinMiller(n)
        
    return False

def generateLargePrime(k):
     # k is the desired bit length
     r = 100 * (math.log(k,2) + 1) # max number of attempts

     while r > 0:
         n = random.randrange(pow(2, k - 1), pow(2,k))
         r -= 1
         if isPrime(n) == True:
            return n
     return r


# rabin miller prime

start = time.time()

found = False
while(found == False):    
    p = generateLargePrime(900)
    if(isPrime(2 * p + 1) == True):
        found = True


print(int(p))
end = time.time()
print("\nSAFE PRIME - 1500 bits:", end - start)




