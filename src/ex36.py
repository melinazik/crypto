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

def probability(L, n):

    for i in L:
        if (len(bin(i)) - 2 >= math.floor(n/2) and (len(bin(i)) - 2 <= math.floor(n/2) + 1 or len(bin(i)) - 2 <= math.floor(n/2) - 1)):
            return 1

        return -1

count = 0
K = 1000
for i in range(0,K):
    n = 10
    m = random.getrandbits(n)
    L = divisors(m)

    if(probability(L, n) == 1):
        count = count + 1


print(count/ K)