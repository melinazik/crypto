''' 
    Fischer Miller Spiffy mode of operation on AES 
    Exercise 8
    
    Melina Zikou (2021)
'''

from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto import Random
import random

# print char objects of a list as a string
def printText(mBytes):
    for b in range(len(mBytes)):
        print(bin(mBytes[b]), end="")

def FSM(cipher, message, iv):
    c = []
    for i in range(0, len(message) - 2):
        if(i == 0):
            c.append(iv ^ cipher.encrypt(bytes(message[i] ^ iv[0])))
        else:
            c.append(message[i] + cipher.encrypt(message[i + 1] + c[i - 1]))

    return c

message = get_random_bytes(16)
key = get_random_bytes(16)

cipher = AES.new(key)
iv = get_random_bytes(1)

c = FSM(cipher, message, iv)
printText(c)
