import math 
import random 

# check for unsupported characters in the given text
# return True if text is OK
#        False otherwise
def validateText(plainText, table):
    isValid = False

    while(isValid == False):
        
        # TODO fix user input / when invalid input it is still saved
        for c in plainText.upper():
            if (c in table) == False:
                print("Unsupported character '" + c + "'")
                plainText = input("Plain Text: ")
                break

            isValid = True

    return isValid

# convert plain text to bits according to the table
def convertToBits(plainText, table):
    bitStream = 0b0
    n = 1
    for c in plainText.upper():
        n = n + 1

        bitStream = (bitStream | map[c])

        if (n != len(plainText)):
            bitStream = bitStream << 5
        
    return bitStream

# generate random binary number of plain text bit length
def otpKey(plainText):

    length = len(plainText) * 5

    otp = random.getrandbits(length)
    
    return otp 


def xor(text, key):
    return bin(text ^ key)

# def binaryToStringList(binary):
#     decimal = 0
#     i = 1
#     binaryStringList = []

#     while(binary != 0): 
#         dec = binary % 10
#         decimal += dec * pow(10 , i - 1) 
#         binary = binary//10

#         stringData = chr(decimal)

#         if(i % 5 == 0):
#             binaryStringList.append(stringData)    
        
#         i += 1
        
        
#     print("binary to String" , binaryStringList )
#     return binaryStringList    

#set with table values for each ASCII character
table = {'A' :0b00000, 'B' :0b00001, 'C' :0b00010, 'D' :0b00011, 'E' :0b00100, 'F' :0b00101, 'G' :0b00110, 'H' :0b00111,
       'I' :0b01000, 'J' :0b01001, 'K' :0b01010, 'L' :0b01011, 'M' :0b01100, 'N' :0b01101, 'O' :0b01110, 'P' :0b01111,
       'Q' :0b10000, 'R' :0b10001, 'S' :0b10010, 'T' :0b10011, 'U' :0b10100, 'V' :0b10101, 'W' :0b10110, 'X' :0b10111,
       'Y' :0b11000, 'Z' :0b11001, '.' :0b11010, '!' :0b11011, '?' :0b11100, '(' :0b11101, ')' :0b11110, '-' :0b11111}

plainText = input("Plain Text: ")

if(validateText(plainText, table)):
    bitStream = convertToBits(plainText, table)
    print("bitstream", bin(bitStream))
    
    otpKey = otpKey(plainText)
    print("otp key  ", bin(otpKey))

    xored = xor(bitStream, otpKey)
    print("xored    ", xored)



