''' 
    Chinese Remainder Theorem (CRT) - RSA
    Exercise 18
    
    Melina Zikou (2021)
'''
import random, sys, os


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
     
    # for x in range(1, m):
    #     if (((a % m) * (x % m)) % m == 1):
    #         return x
    # return -1
    if gcd(a, m) != 1:
      return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
   
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def rabinMiller(num):
   s = num - 1
   t = 0
   
   while s % 2 == 0:
      s = s // 2
      t += 1
   for trials in range(5):
      a = random.randrange(2, num - 1)
      v = pow(a, s, num)
      if v != 1:
         i = 0
         while v != (num - 1):
            if i == t - 1:
               return False
            else:
               i = i + 1
               v = (v ** 2) % num
      return True

def isPrime(num):
   if (num < 2):
      return False

   lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
   571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
   673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
   911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
	
   if num in lowPrimes:
      return True
   for prime in lowPrimes:
      if (num % prime == 0):
         return False
   return rabinMiller(num)

def generateLargePrime(keysize = 1024):
   while True:
      num = random.randrange(2**(keysize-1), 2**(keysize))
      if isPrime(num):
         return num   
# b = base number
# e = exponential
# m = modulo  
# calculate b^e mod m
def fast(b,e,m):
    x = b
    g = e
    d = 1

    while g > 0:
        if g % 2 == 0:
            x = (x * x) % m
            g = g/2
        else:
            d = (x * d) % m
            g = g - 1
    return d


def generateKey(keySize):
   # Step 1: Create two prime numbers, p and q. 
   #         Calculate n = p * q.
   p = generateLargePrime(keySize)
   print("p:", p)
   q = generateLargePrime(keySize)
   print("q:", q)

   n = p * q

   print("N:", n)

	
   # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if gcd(e, (p - 1) * (q - 1)) == 1:
        break

   print("e:", e)
    
   # Step 3: Calculate d, the mod inverse of e.
   d = modularInverse(e, (p - 1) * (q - 1))
   print("d:", d)
   print()

   # dp = d mod (p - 1)
   dp = d % (p - 1) 

   # dq = d mod (q - 1)
   dq = d % (q - 1)

   # qinv = modular inverse of q mod p
   qinv = modularInverse(q, p)

   print("dp:", dp)
   print("dq:", dq)
   print("qinv:", qinv)
   print()

   
   publicKey = (n, e)
   privateKey = (n, d)
   print('Public key:', publicKey)
   print('Private key:', privateKey)
   return (publicKey, privateKey)

generateKey(100)

# # print char objects of a list as a string
# def printText(text):
#     for i in range(len(text)):
#         print(text[i], end="")

# C = [3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,909,9958,792,909,4132,3143,9958,3203,5343,792,3143,4443]

# N = 11413
# e = 19 

# phi = phi(N)
# d = modularInverse(e,phi)

# privateKey = [N, d]

# M = []
# asciiM = []

# for c in C:
#     M.append(fast(c,d,N))

# for m in M:
#     asciiM.append(chr(m))

# print("Private Key:", privateKey)
# printText(asciiM)
