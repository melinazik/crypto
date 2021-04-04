''' 
    Vigenere cracking algorithm
    Exercise 3
    
    Melina Zikou (2021) 
'''

# Kasiski: https://en.wikipedia.org/wiki/Kasiski_examination
# Frequency Analysis : https://en.wikipedia.org/wiki/Frequency_analysis

import numpy as np

# Find coincidences of letters in the cipher text.
# The index of the max coincidence is the size of the key.
# param     text -> cipher text
# return    size of key 
def getKeyLength(text):
    #initialize coincidences array
    coincidences = [0]
    textLen = len(text)

    for i in range(1, textLen):
        # in each shift of the bottom message
        # the first letter has no letter to compare to
        # => coincidences array at this index is 0
        coincidences.append(0)
        
        for j in range(textLen):
            if(text[j] == text[(j + i) % textLen]):
                    coincidences[i] += 1

    return coincidences.index(max(coincidences))

def getKey(text, keyLen, frequency):
    textLen = float(len(text))
    key = ''

    for i in range(0, keyLen):
        
        textFrequency = {} # array with frequency of each letter in the cipher text
        maxVal= -1
        maxPosition = 0
        rolledArray = frequency

        # for each letter in the alphabet we have to find the 
        # max frequency of the letter in accordance to another letter 
        # [letter of key - letter of cipher text]
        for j in range(0, 26):
            if(j > 0):
                rolledArray = np.roll(rolledArray, 1)

            for k in range(0, 26):
                # set initial frequency of each letter to 0
                textFrequency[chr(k + ord('A'))] = 0

            # find the frequencies of each position of the key.
            # start at the letter position of the key to be found
            # and loop through the cipher text
            k = i
            while(k < textLen):
                letter = text[k]
                textFrequency[letter] += 1 / textLen * 100  # set frequency
                k += keyLen

            # Sum the frequency values of textFrequency * rolledArray
            # textFrequency -> frequency in cipher textFrequency
            # rolledArray   -> frequency of english alphabet
            sumVal = 0
            for k in range(0, 26):
                sumVal += textFrequency[chr(k + ord('A'))] * rolledArray[k]

            # max of sumVal's during a parse of the alphabet wins
            # maxPosition -> position of the letter found
            if(sumVal > maxVal):
                maxVal = sumVal
                maxPosition = j

        # add the letter to the key
        key += chr(maxPosition + ord('A'))
    
    return key

def textToInt (string):
    return [ord(i) for i in string]

def decipher(text, key, textLen, keyLen):
    plainText = ''
    for i in range(textLen):
        value = (text[i] - key[i % keyLen]) % 26
        plainText += chr(value + ord('A'))

    return plainText

# Letter frequencies of English language
# http://cs.wellesley.edu/~fturbak/codman/letterfreq.html
frequency = [ 8.167, 1.492, 2.782, 4.253, 12.702, 2.015, 6.094, 2.228, 6.966, 
              0.153, 0.772, 4.025, 2.406,  6.749, 7.507, 1.929, 0.095, 5.987, 
              6.327, 9.056, 2.758, 0.978,  2.360, 0.150, 1.974, 0.074]

f = open("..\\files\\vigenere.txt", "r")
cipherText = f.read()

keyLen = getKeyLength(cipherText)
key = getKey(cipherText, keyLen, frequency)

cipherTextInt = textToInt(cipherText)
keyInt = textToInt(key)

plainText = decipher(cipherTextInt, keyInt, len(cipherText), keyLen)

print('KEY:', key)
print()
print('PLAIN TEXT\n-----------')
print(plainText)
