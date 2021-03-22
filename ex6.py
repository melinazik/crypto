from collections import deque  

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


# the function sumxor
# accepts a binary list of the form [1,0,1,...]
# and returns the xor-sum of the bits
def sumxor(list):
    r = 0
    for v in list: 
        r = r^v
    return r

def lfsr(seed, feedback, bits):
    
    newFeedback = []

    for i in range(len(feedback)):
        if 1 in feedback:
            newFeedback.append(feedback.index(1))
            feedback[feedback.index(1)] = 0

    seed = deque(seed) # make a new deque 
    output = []
    
    for i in range(bits):
        xor = sumxor([seed[j] for j in newFeedback])
        output.append(seed.pop()) #extract to output the right-most bit of current seed
        seed.appendleft(xor)      #insert from left the result of the previous xor 

    return output

def listToBits(l):
    
    binary = 0b0

    for i in range(len(l)):
        n = l[i]
        binary = binary ^ n
        binary = binary << 1
    
    binary = binary >> 1
    return binary

def bitsToList(bits):
    mask = 0b1

    bitList = []

    for i in range(bits.bit_length()):
        last = bits & mask
        bits = bits >> 1

        bitList.append(last)

    result = bitList[::-1]
    return result


def xor(text, key):
    return text ^ key

def printText(charList):
    for c in charList:
        print(c, end="")


#set with table values for each ASCII character
table = {'A' :0b00000, 'B' :0b00001, 'C' :0b00010, 'D' :0b00011, 'E' :0b00100, 'F' :0b00101, 'G' :0b00110, 'H' :0b00111,
       'I' :0b01000, 'J' :0b01001, 'K' :0b01010, 'L' :0b01011, 'M' :0b01100, 'N' :0b01101, 'O' :0b01110, 'P' :0b01111,
       'Q' :0b10000, 'R' :0b10001, 'S' :0b10010, 'T' :0b10011, 'U' :0b10100, 'V' :0b10101, 'W' :0b10110, 'X' :0b10111,
       'Y' :0b11000, 'Z' :0b11001, '.' :0b11010, '!' :0b11011, '?' :0b11100, '(' :0b11101, ')' :0b11110, '-' :0b11111}

plainText = 'AB'
length = len(plainText)*5
plain = convertToBits('AB', table)
cipher =  convertToBits('.S', table)

seed = xor(plain, cipher)
seed = bitsToList(seed)
seed = seed[::-1]

# cipherText = 'i!))aiszwykqnfcyc!?secnncvch'.upper()

# plainTextBits = (xor(convertToBits(cipherText, table), keyStream))

# plainText = binaryToString(plainTextBits, len(cipherText), table)

# seed = bitsToList(seed)

# 'i!))aiszwykqnfcyc!?secnncvch'

feedback = [0,0,0,0,0,1,1,0,1,1]

plainText = 'i!))aiszwykqnfcyc!?secnncvch'.upper()
length = len(plainText)*5

output = lfsr(seed, feedback, length)


output = listToBits(output)
# print(bin(output))
cipherText = binaryToString(xor(convertToBits(plainText, table), output), length//5, table)

printText(cipherText)

# printText(plainText)