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

    # key array 
    cipherText = []

    for c in plainText:
        i = (i + 1) % 256  
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]

        hexed = ("%02X" % ord(chr(S[(S[i] + S[j]) % 256] ^ ord(c))))

        cipherText.append(hexed)

    return cipherText

#prga for encryption
def PRGADecrypt(S, cipherText):
    i = 0
    j = 0

    # key array 
    plainText = ''

    for c in cipherText:
        i = (i + 1) % 256  
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]
        
        char = chr(int(c,16) ^ S[(S[i] + S[j]) % 256])

        plainText += char

    return plainText


#     return cipher
def listToString(list):  
    
    # initialize an empty string 
    str = ""  
    
    # traverse in the string   
    for element in list:  
        str += element 
    
    # return string   
    return str


def encrypt(key, plainText):
    S = KSA(key)
    cipherText = PRGAEncrypt(S, plainText)


    return listToString(cipherText)

def decrypt(key, cipherText):
    S = KSA(key)
    cipherList=cipherText.split(' ')
    
    plainText = PRGADecrypt(S, cipherList)

    return plainText

key = 'HOUSE'
plainText = 'MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE'
print('PLAIN TEXT:' , plainText)
print('KEY:' , key)

encrypted = encrypt(key, plainText)
print('\nENCRYPTED:', encrypted)


# cipherText = '15DDA667FE6ADD1A49167A12A40CF54B42D4CD7014E2EF5C0A87A3010B47EB7919777DDB578614557294AEAFD9621C8B19'
cipherText = " ".join(encrypted[i:i+2] for i in range(0, len(encrypted), 2))
decrypted = decrypt(key, cipherText)
print('\nDECREPTED:' , decrypted)
