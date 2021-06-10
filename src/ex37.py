''' 
    Complexities of factorization algorithms
    Exercise 37
    
    Melina Zikou (2021)
'''
import math

def coppersmith(n):
    return math.log10(n)

def quadraticSieve(n):
    return math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))

def gnfs(n):
    return math.exp(math.pow(math.log(n), 1/3) * math.pow(math.pow(math.log(math.log(n)), 2), 1/3))


bits = [100, 200, 1024, 2048, 4096]

print("COPPERSMITH")
for i in bits:
    print(coppersmith(i))

print()
print("QUADRATIC SIEVE")
for i in bits:
    print(quadraticSieve(i))

print()
print("GNFS")
for i in bits:
    print(gnfs(i))