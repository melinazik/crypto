import math 
import random 

# check for unsupported characters in the given text
# return True if text is OK
#        False otherwise
def validateText(plainText, map):
    isValid = False

    while(isValid == False):

        for c in plainText.upper():
            if (c in map) == False:
                print("Unsupported character '" + c + "'")
                plainText = input("Plain Text: ")
                break

            isValid = True

    return isValid

# convert plain text to bits according to the map
def convertToBits(plainText, map):
    bitStream = ''
    for c in plainText.upper():
        bitStream += map[c]
    
    return bitStream

# create random key of plain text length 
def otpKey(plainText):
    otp = ""
    digits = "01"

    for i in range(len(plainText)):
        otp += digits[math.floor(random.random() * 10)]
    
    return otp 

def xor(text, key):
    return bin(int(text) ^ int(key))



map = {'A' :'00000', 'B' :'00001', 'C' :'00010', 'D' :'00011', 'E' :'00100', 'F' :'00101', 'G' :'00110', 'H' :'00111',
       'I' :'01000', 'J' :'01001', 'K' :'01010', 'L' :'01011', 'M' :'01100', 'N' :'01101', 'O' :'01110', 'P' :'01111',
       'Q' :'10000', 'R' :'10001', 'S' :'10010', 'T' :'10011', 'U' :'10100', 'V' :'10101', 'W' :'10110', 'X' :'10111',
       'Y' :'11000', 'Z' :'11001', '.' :'11010', '!' :'11011', '?' :'11100', '(' :'11101', ')' :'11110', '-' :'11111'}

plainText = input("Plain Text: ")

if(validateText(plainText, map)):
    bitStream = convertToBits(plainText, map)
    otpKey = otpKey(plainText)



