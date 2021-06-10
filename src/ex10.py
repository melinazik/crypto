''' 
    Shank's Algorithm - Baby Step/Giant Step
    Compute Discrete Logarithm
    Exercise 10
    
    Melina Zikou (2021)
'''
import math

# find x such that
# g^x = y mod p
def shank(g, y, p):

    # ceil func: the smallest integer not less than sqrt of p
    m = math.ceil(math.sqrt(p))

    table = []

    # Baby step
    # map of g^1,...,g^m (mod p) : 1,..m . 
    table = {pow(g, i, p): i for i in range(m)}

    # Giant Step Precomputation c = g^(-m) mod p
    # Fermat's little theorem
    c = pow(g, m * (p - 1), p)

    # Giant step
    # Search equivalent value in the table   
    for j in range(m):
        x = (y * pow(c, j, p)) % p

        if x in table:
            return j * m + table[x]


print("0:", shank(2,2404,3571))
print("1:", shank(2,2912,3989))
print("2:", shank(2,9077,12161))
print("3:", shank(2,30359,53549))
print("4:", shank(2,672304,685301))