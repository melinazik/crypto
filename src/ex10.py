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
print("extra:", shank(3,3,8911))


# https://gist.github.com/LaurentMazare/6745649

# long pow_mod(long x, long n, long p) {
#   if (n == 0) return 1;
#   if (n & 1)
#     return (pow_mod(x, n-1, p) * x) % p;
#   x = pow_mod(x, n/2, p);
#   return (x * x) % p;
# }

# /* Takes as input an odd prime p and n < p and returns r
#  * such that r * r = n [mod p]. */
# long tonelli_shanks(long n, long p) {
#   long s = 0;
#   long q = p - 1;
#   while ((q & 1) == 0) { q /= 2; ++s; }
#   if (s == 1) {
#     long r = pow_mod(n, (p+1)/4, p);
#     if ((r * r) % p == n) return r;
#     return 0;
#   }
#   // Find the first quadratic non-residue z by brute-force search
#   long z = 1;
#   while (pow_mod(++z, (p-1)/2, p) != p - 1);
#   long c = pow_mod(z, q, p);
#   long r = pow_mod(n, (q+1)/2, p);
#   long t = pow_mod(n, q, p);
#   long m = s;
#   while (t != 1) {
#     long tt = t;
#     long i = 0;
#     while (tt != 1) {
#       tt = (tt * tt) % p;
#       ++i;
#       if (i == m) return 0;
#     }
#     long b = pow_mod(c, pow_mod(2, m-i-1, p-1), p);
#     long b2 = (b * b) % p;
#     r = (r * b) % p;
#     t = (t * b2) % p;
#     c = b2;
#     m = i;
#   }
#   if ((r * r) % p == n) return r;
#   return 0;
# }