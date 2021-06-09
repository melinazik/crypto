''' 
    Textbook RSA
    Exercise 11
    
    Melina Zikou (2021)
'''

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

# print char objects of a list as a string
def printText(text):
    for i in range(len(text)):
        print(text[i], end="")

C = [3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,909,9958,792,909,4132,3143,9958,3203,5343,792,3143,4443]

N = 11413
e = 19 

phi = phi(N)
d = modularInverse(e,phi)
privateKey = [N, d]

M = []
asciiM = []

for c in C:
    M.append(fast(c,d,N))

for m in M:
    asciiM.append(chr(m))

print("Private Key:", privateKey)
printText(asciiM)
