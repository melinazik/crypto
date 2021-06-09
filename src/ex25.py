''' 
    Plots of Arithmetic Sequences
    Exercise 25
    
    Melina Zikou (2021)
'''

import matplotlib.pyplot as plt
import numpy as np
import math 


# function to count divisors of an integer
def t(n) :
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
             
            # If divisors are equal,
            # count only one
            if (n / i == i) :
                count = count + 1
            else : # Otherwise count both
                count = count + 2
            
    return count
    

# Set Euler-Mascheroni constant g = 0.577
g = 0.577

# Creating vectors X and Y
n = np.linspace(1, 10000000, 100000)
a = np.log(n) + 2*g - 1

def b(n):
    sum = 0
    sumArray = []
    for r in range(int(n)):
        sum = sum + (1/n) * t(r)
        sumArray.append(sum)
    return sumArray
  
fig = plt.figure(figsize = (10, 5))

# Create the plot
plt.plot(n, a)
# Show the plot
plt.show()

plt.plot(n, b(100000))
plt.show()
