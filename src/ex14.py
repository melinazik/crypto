''' 
    Tonelli - shanks Algorithm
    (Modular Arithmetic)
    Exercise 14
    
    Melina Zikou (2021)
'''

# Legendre symbol
# The Legendre symbol (a | p) => a ^ ((p-1)/2) (mod p)
# (a | p) =  1     if a is a square (mod p)
# (a | p) = -1     if a is not a square (mod p)
# (a | p) =  0     if a ≡ 0
def legendreSymbol(a, p):
    return pow(a, (p - 1) // 2, p)

# calculates x so that x ^ 2 = a mod p
# with Tonelli Shanks Algorithm
# parameters: p prime
#             a integer
# return : x
def tonelliShanks (a, p):
    # check that a is a square: (n | p) = 1
    if (legendreSymbol(a,p) == 1):
        

        # Partition p-1 to q * 2^e for an odd q 
        # (reduce all the powers of 2 from p - 1)
        q = p - 1
        e = 0
        while q % 2 == 0:
            q = q // 2
            e += 1

        # find z so that z|p = -1
        z = 2
        while (p - 1 != legendreSymbol(z, p)):
            z += 1

        # set c = z^q (mod p)          => successive powers of z to update a and t
        # set r = a ^((q+1)/2) (mod p) => a guess of the square root
        # set t = a^q (mod p)          => how much guess is off
        # set m = e : e is the exponent - decreases with each update
        c = pow(z, q, p)
        r = pow(a, (q + 1) // 2, p)
        t = pow(a, q, p)
        m = e
        v = 0

        # loop until t = 1
        while (t - 1) % p != 0:
            v = (t * t) % p

            # if t != 1 : find the lowest i (0 < i < m) so that t^(2^i) = 1
            for i in range(1, m):
                if (v - 1) % p == 0:
                    break

                v = (v * v) % p

            # set b = c^(2^(m-i-1)) (mod p)
            # set r = r * b (mod p)
            # set t = t * b^2 (mod p)
            # set c = b^2 (mod p)
            # set m = i.
            b = pow(c, pow(2, m - i - 1), p)
            r = (r * b) % p
            c = (b * b) % p
            t = (t * c) % p
            m = i
        
        return r

a = 17592194433025
p = 309485009821345068724781063

print(tonelliShanks(a,p))