''' 
    RC4 algorithm
    Exercise 1 (i)
    author : Melina Zikou 
'''

import numpy as np

# key scheduling algorithm (KSA)
def KSA(key):
    keyLen = len(key)
    key = [ord(x) for x in key]
    
    S = [x for x in range(256)]

    j = 0

    for i in range(256):
        j = (j + S[i] + int(key[i % keyLen])) % 256

        # swap values
        S[i], S[j] = S[j], S[i]
    
    # array "S" is initialized to the identity permutation
    return S

# Pseudo-random generation algorithm (PRGA)
# S : permuation array

#prga for encryption
def PRGAEncrypt(S, plainText):
    i = 0
    j = 0

    cipherText = []

    for c in plainText:
        i = (i + 1) % 256  
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]

        # xor and convert from ASCII to hex 
        hexed = ("%02X" % ord(chr(S[(S[i] + S[j]) % 256] ^ ord(c))))

        cipherText.append(hexed)

    return cipherText

#prga for encryption
def PRGADecrypt(S, cipherText):
    i = 0
    j = 0

    plainText = ''

    for c in cipherText:
        i = (i + 1) % 256  
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]
        
        # xor and convert from hex to plain ASCII
        char = chr(int(c,16) ^ S[(S[i] + S[j]) % 256])

        plainText += char

    return plainText

# convert a list to string
def listToString(list):  
    
    # initialize an empty string 
    str = ""  
    
    # traverse in the string   
    for element in list:  
        str += element 
    
    # return string   
    return str

# encryption
def encrypt(key, plainText):
    S = KSA(key)
    cipherText = PRGAEncrypt(S, plainText)


    return listToString(cipherText)

# decryption
def decrypt(key, cipherText):
    S = KSA(key)
    cipherList=cipherText.split(' ')
    
    plainText = PRGADecrypt(S, cipherList)

    return plainText

# set key and plain text
key = 'HOUSE'
plainText = 'MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE'
print('PLAIN TEXT:' , plainText)
print('KEY:' , key)

# encrypt the plain text
encrypted = encrypt(key, plainText)
print('\nENCRYPTED:', encrypted)

# split the cipher text into chunks of two characters each first
# and then join these chunks with spaces
cipherText = " ".join(encrypted[i:i+2] for i in range(0, len(encrypted), 2))

# decrypt the cipher text
decrypted = decrypt(key, cipherText)
print('\nDECRYPTED:' , decrypted)
