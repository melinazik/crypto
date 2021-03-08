''' 
    One Time Pad (OTP) algorithm
    Exercise 1 (ii)
    author : Melina Zikou 
'''
import random 

# check for unsupported characters in the given text
# return True if text is OK
#        False otherwise
def validateText(plainText, table):
    isValid = False

    while(isValid == False):
        
        # TODO fix user input / when invalid input it is still saved
        # TODO fix space
        for c in plainText.upper():
            if(c == ' '):
                continue
            elif (c in table) == False:
                print("Unsupported character '" + c + "'")
                plainText = input("PLAIN TEXT: ")
                break

            isValid = True

    return isValid

# convert plain text to bits according to the table
# parameters: plainText -> text given 
#             table  -> table given with characters - bin values
# return      plain text converted to binary 
def convertToBits(plainText, table):
    bitStream = 0b0
    n = 1
    for c in plainText.upper():
        n = n + 1

        bitStream = bitStream << 5
        bitStream = (bitStream | table[c])
        
    return bitStream

# generate random binary number of plain text bit length
# parameters: plainText -> text given 
# return      one time pad key
def otpKey(plainText):

    length = len(plainText) * 5

    otp = random.getrandbits(length)
    
    return otp

# xoring function
def xor(text, key):
    return text ^ key

# convert binary number to characters according to table values
# parameters: binary -> binary number to convert
#             length -> length of plainText
#             table  -> table given with characters - bin values
# return      list with characters
def binaryToString(binary, length, table):
    mask = 0b11111

    charList = []

    for i in range(length):
        # isolate last 5 bits of the bit stream
        last = binary & mask
        binary = binary >> 5

        # find the element on the table that matches the isolated bits
        for element in table:
            if (table[element] == last):
                charList.append(element)
    
    # reverse the charList / characters are encoded from end to start
    result = charList[::-1]
    return result

def printText(charList):
    for c in charList:
        print(c, end="")


#set with table values for each ASCII character
table = {'A' :0b00000, 'B' :0b00001, 'C' :0b00010, 'D' :0b00011, 'E' :0b00100, 'F' :0b00101, 'G' :0b00110, 'H' :0b00111,
       'I' :0b01000, 'J' :0b01001, 'K' :0b01010, 'L' :0b01011, 'M' :0b01100, 'N' :0b01101, 'O' :0b01110, 'P' :0b01111,
       'Q' :0b10000, 'R' :0b10001, 'S' :0b10010, 'T' :0b10011, 'U' :0b10100, 'V' :0b10101, 'W' :0b10110, 'X' :0b10111,
       'Y' :0b11000, 'Z' :0b11001, '.' :0b11010, '!' :0b11011, '?' :0b11100, '(' :0b11101, ')' :0b11110, '-' :0b11111}

plainText = input("PLAIN TEXT: ")

if(validateText(plainText, table)):
    # encryption
    bitStream = convertToBits(plainText, table)
    # testing
    # print("bitstream", bin(bitStream))
    
    otpKey = otpKey(plainText)
    # testing
    # print("otp key  ", bin(otpKey))

    xored1 = xor(bitStream, otpKey)
    # testing
    # print("xored    ", bin(xored1))

    cipherText = binaryToString(xored1, len(plainText), table)
    print("ENCRYPTED:   ", end='')
    printText(cipherText)

    print()
    # decryption
    xored2 = xor(xored1, otpKey)
    # testing
    # print("xored    ", bin(xored2))

    decrypted = binaryToString(xored2, len(plainText), table)
    print("DECRYPTED:   ", end='')
    printText(decrypted)


