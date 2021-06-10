''' 
    Probability of number to have a factor of
    binary length of {[n/2], [n/2] +- 1}
    Exercise 36
    
    Melina Zikou (2021)
'''

import math
import random

# find all divisors of integer number
def divisors(n):
    i = 1
    factors = []
    while i <= n :
        if (n % i==0) :
            factors.append(i)
        i = i + 1

    return factors

# calculate probability
def probability(L, n):

    for i in L:
        # print(len(bin(i)))
        if (len(bin(i)) - 2 >= math.floor(n/2) and (len(bin(i)) - 2 <= math.floor(n/2) + 1 or len(bin(i)) - 2 <= math.floor(n/2) - 1)):
            
            return 1

count = 0
K = 1000

for i in range(0,K):
    n = 64
    m = random.getrandbits(n)
    L = divisors(m)
    # print(len(bin(m)) - 2)

    if(probability(L, n) == 1):
        count = count + 1

print(count/ K)