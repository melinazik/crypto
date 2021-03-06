import numpy as np

# key scheduling algorithm (KSA)
def KSA(key):
    keyLen = len(key)
    
    S = list(range(256))

    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % keyLen]) % 256

        # swap values
        S[i], S[j] = S[j], S[i]
    
    # array "S" is initialized to the identity permutation
    return S

# Pseudo-random generation algorithm (PRGA)

# S : permuation array
# n : length of plain text
def PRGA(S, n):
    i = 0
    j = 0

    # key array 
    key = []

    while n > 0:
        n = n - 1
        i = (i + 1) % 256  
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        key.append(K)
        

    return key

def getKeyStream(key, n):
    S = KSA(key)
    return PRGA(S, n)
    
def encrypt(key, plainText):
    key = [ord(c) for c in key]

    keyStream = np.array(getKeyStream(key, len(plainText)))
    plainText = np.array([ord(i) for i in plainText])
    cipher = keyStream ^ plainText
    return cipher.astype(np.uint8).data.hex()

    # result = []
    # i = 0
    # # xor and hex values
    # for c in plainText:
    #     value = ("%02X" % (ord(c) ^ keyStream[i]))  # XOR and taking hex
    #     result.append(value.upper())
    #     i = i + 1


    # return ''.join(result)

def decrypt(key, cipherText):
    # convert ciphertext from hex to plain ASCII
    

    result = encrypt(key, cipherText)

    return result


key = 'HOUSE'
plainText = 'MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE'

encrypted = encrypt(key, plainText)

print('plaintext: ' + plainText)

print('ciphertext: ' + encrypted.upper())

cipherText = '15dda667fe6add1a49167a12a40cf54b42d4cd7014e2ef5c0a87a3010b47eb7919777ddb578614557294aeafd9621c8b19'.upper()
decrypted = decrypt(key, cipherText)
print ('\ndecrypted:', decrypted.upper())