''' 
    Plots of Arithmetic Sequences
    Exercise 25
    
    Melina Zikou (2021)
'''

import matplotlib.pyplot as plt
import numpy as np
import math 

# count divisors of an integer
def t(n) :
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
             
            # if divisors are equal,
            # count only one
            if (n / i == i) :
                count = count + 1
            else : # otherwise count both
                count = count + 2
            
    return count
    
# Set Euler-Mascheroni constant g = 0.577
g = 0.577

# define linear space for the plot
n = np.linspace(1, 10000000, 100000)

# sequence a_n
a = np.log(n) + 2*g - 1

# sequence b_n
def b(n):
    sum = 0
    sumArray = []
    for r in range(int(n)):
        sum = sum + (1/n) * t(r)
        sumArray.append(sum)
    return sumArray
  
fig = plt.figure(figsize = (10, 5))

# Create 1st plot
plt.plot(n, a)
# Show 1st plot
plt.show()

# Create 2nd plot
plt.plot(n, b(100000))
# Show 2nd plot
plt.show()
