''' 
    Avalanche Effect on Block Ciphers
    AES and Blowfish algorithms
    Exercise 2
    
    Melina Zikou (2021)
'''

from Crypto.Cipher import Blowfish
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
import random

#The byteorder argument determines the byte order used to represent the integer. 
#If byteorder is "big", the most significant byte is at the beginning of the byte array. 
#If byteorder is "little", the most significant byte is at the end of the byte array.

#convert bitstream (messages) to bytes
def bitsToBytes(x):
    # create string
    s = ''.join(str(e) for e in x)

    # return bytes
    # int(s,2) -> convert string to int base 2
    # byteorder='big' -> most significant byte 
    #                    is at the beginning of the byte array
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

# count different bits
def differentBits(x, y):
    # convert bytes to bits
    x = (bin(int.from_bytes(x, byteorder="big"))[2:])
    y = (bin(int.from_bytes(y, byteorder="big"))[2:])

    # add zeros until length = 64
    x = list((64*2 - len(x)) * str(0) + x)
    y = list((64*2 - len(y)) * str(0) + y)

    # s = ''.join(str(e) for e in x)
    # print("x:", s)
    # print()

    count = 0
    
    for i in range(0, 64*2):
        if (x[i] != y[i]):
            count += 1

    return count


def changeBit(y, i):
    if (y[i] == 1):
        y[i] = 0
    else:
        y[i] = 1

def ECBMode(key, cipher, xBytes, yBytes):
    xEnc = cipher.encrypt(xBytes)
    yEnc = cipher.encrypt(yBytes)

    return differentBits(xEnc, yEnc)

def CBCMode (key, cipher, iv, xBytes, yBytes):
    xEnc = cipher.encrypt(iv + xBytes)
    yEnc = cipher.encrypt(iv + yBytes)

    return differentBits(xEnc, yEnc)

# AES algorithm - ECB and CBC Modes
def aes(key, xBytes, yBytes):
    # ECB MODE 
    cipher = AES.new(key, AES.MODE_ECB)
    
    # different bits
    countECB = ECBMode(key, cipher, xBytes, yBytes)

    # CBC MODE
    blockSize = AES.block_size
    iv = get_random_bytes(blockSize)
    cipher = AES.new(key, Blowfish.MODE_CBC, iv)

    # different bits
    countCBC = CBCMode(key, cipher, iv, xBytes, yBytes)

    return countECB, countCBC

# Blowfish algorithm - ECB and CBC Modes
def blowfish(key, xBytes, yBytes):
    # ECB MODE 
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    # different bits
    countECB = ECBMode(key, cipher, xBytes, yBytes)

    # CBC MODE
    blockSize = Blowfish.block_size
    iv = get_random_bytes(blockSize)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    
    # different bits
    countCBC = CBCMode(key, cipher, iv, xBytes, yBytes)


    return countECB, countCBC

countAESECB = 0
countAESCBC = 0
countBlowfishECB = 0
countBlowfishCBC = 0

messages = 35

# number of messages ( > 30 )
for j in range(messages):
    x = []
    for i in range(0, 64*2):
        # random message x
        x.append(random.randint(0, 1))

    y = x.copy()

    # change 1 random bit in message y
    randIndex = random.randint(0, 64*2 - 1)
    changeBit(y, randIndex)

    xBytes = bitsToBytes(x)
    yBytes = bitsToBytes(y)
    
    key = get_random_bytes(16)

    a, b = aes(key, xBytes, yBytes)
    countAESECB += a 
    countAESCBC += b

    a, b = blowfish(key, xBytes, yBytes)
    countBlowfishECB += a 
    countBlowfishCBC += b 

print("AVERAGE DIFFERENCE IN BITS")
print("--------------------------")
print("AES - ECB MODE:", countAESECB / messages)
print("AES - CBC MODE:", countAESCBC / messages)
print("--------------------------")
print("Blowfish - ECB MODE:", countBlowfishECB / messages)
print("Blowfish - CBC MODE:", countBlowfishCBC / messages)
