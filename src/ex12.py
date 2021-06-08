''' 
    Textbook RSA
    Exercise 12
    
    Melina Zikou (2021)
'''

import math
import base64

# Converts a rational x/y fraction into
# a list of partial quotients [a0, ..., an]
def rationalToContFrac(x,y):
    a = x // y
    q = []
    q.append(a)

    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        q.append(a)
    return q

# Converts a finite continued fraction [a0, ..., an]
# to an x/y rational.
def contFracToRational (frac):
    if len(frac) == 0:
        return (0, 1)

    num = frac[-1]
    denom = 1

    for i in range(-2, -len(frac) - 1, -1):
        num, denom = frac[i]*num+denom, num
    return (num, denom)

# computes the list of convergents
# using the list of partial quotients
def convergentsFromContFrac(frac):
    c = []
    for i in range(len(frac)):
        c.append(contFracToRational(frac[0:i]))
    return c

def fast(b,e,m):
    x = b
    g = e
    d = 1

    while g > 0:
        if g % 2 == 0:
            x = (x * x) % m
            g = g / 2
        else:
            d = (x * d) % m
            g = g - 1
    return d

def isPerfectSquare(n):
    t = math.sqrt(n)
    if t * t == n:
        return t
    else:
        return -1
   
# Finds d knowing (e,n)
# applying the Wiener continued fraction attack
def findD(e,N):
    frac = rationalToContFrac(e, N)
    convergents = convergentsFromContFrac(frac)
    
    for (k, d) in convergents:
        
        #check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            b = N - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots

            D = (b * b) - (4 * N)

            if(D >= 0):
                t = isPerfectSquare(D)
                if t != -1 and (b + t) % 2 == 0:
                    return d

# print char objects of a list as a string
def printText(text):
    for i in range(len(text)):
        print(text[i], end="")


N = 194749497518847283
e = 50736902528669041

f = open("..\\files\\textbookRSA.txt", "r")
cipher= f.read()


d = findD(e, N)
privateKey = [N, d]
# print(d)


C = []
M = []
asciiM = []

# convert from base64 to utf - 8
cipher = base64.b64decode(cipher).decode('utf-8')

print(cipher)

cipher = cipher.replace('\r\n', ',')
cipher = cipher.replace('C=[', '')
cipher = cipher.replace(']', '')
cipher = cipher.split(',')

for c in cipher:
    C.append(c)

for c in C:
    M.append(fast(int(c),d,N))


for m in M:
    asciiM.append(chr(m))

print("Private Key:", privateKey)
printText(asciiM)
