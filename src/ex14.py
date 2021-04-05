''' 
    Tonelli - shanks Algorithm
    (Modular Arithmetic)
    Exercise 14
    
    Melina Zikou (2021)
'''
# x ^ 2 = a mod p
# x ^ 2 = 17592194433025 mod 309485009821345068724781063

# Legendre symbol

# The Legendre symbol ( a | p) denotes the value of a ^ ((p-1)/2) (mod p)
# (a | p) ≡  1     if a is a square (mod p)
# (a | p) ≡ -1     if a is not a square (mod p)
# (a | p) ≡  0     if a ≡ 0

# Algorithm pseudo-code
# (copied from Wikipedia):
# All   ≡   are taken to mean   (mod p)   unless stated otherwise.

# Input : p an odd prime, and an integer n .
# Step 0. Check that n is indeed a square  : (n | p) must be ≡ 1

# Step 1. [Factors out powers of 2 from p-1] Define q -odd- and s such as p-1 = q * 2^s
# if s = 1 , i.e p ≡ 3 (mod 4) , output the two solutions r ≡ +/- n^((p+1)/4) .

# Step 2. Select a non-square z such as (z | p) = -1 , and set c ≡ z^q .

# Step 3. Set r ≡ n ^((q+1)/2) , t ≡ n^q, m = s .

# Step 4. Loop.
# if t ≡ 1 output r, p-r .

# Otherwise find, by repeated squaring, the lowest i , 0 < i< m , such as t^(2^i) ≡ 1
# Let b ≡ c^(2^(m-i-1)), and set r ≡ r*b, t ≡ t*b^2 , c ≡ b^2 and m = i.

#from https://rosettacode.org/wiki/Tonelli-Shanks_algorithm

def legendreSymbol(a, p):
    return pow(a, (p - 1) // 2, p)
    

def tonelliShanks (a, p):
    if (legendreSymbol(a,p) == 1):

        q = p - 1
        s = 0
        while q % 2 == 0:
            q = q // 2
            s += 1

        if s == 1:
            return pow(a, (p + 1) // 4, p)
        
        # find n so that n|p = -1
        z = 2
        while (p - 1 != legendreSymbol(z, p)):
            z += 1

        c = pow(z, q, p)
        r = pow(a, (q + 1) // 2, p)
        t = pow(a, q, p)
        m = s

        v = 0

        while (t - 1) % p != 0:
            v = (t * t) % p

            for i in range(1, m):
                if (v - 1) % p == 0:
                    break

                v = (v * v) % p

            b = pow(c, pow(2, m - i - 1), p)
            r = (r * b) % p
            c = (b * b) % p
            t = (t * c) % p
            m = i
        
        return r

a = 17592194433025
p = 309485009821345068724781063

print(tonelliShanks(a,p))