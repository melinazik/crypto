''' 
    Fast Modular Exponentiation
    Exercise 9 (iv)
    
    Melina Zikou (2021)
'''

# def fast(b, e, m):
#     g = []
#     for i in range(e):
#         g.append(i)

#     x = b
#     result = 1

#     for i in range(e-1, 0, -1):
#         if (g[i] == 1):
#             result = (result * x) % m
        
#         x = (x * x) % m

#     return result



# b = base number
# e = exponential
# m = modulo 
#     
# calculate b^e mod m

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

print(fast(2, 1234567, 12345))
print(fast(130, 7654321, 567))

#TODO check algorithm with lecture slides
