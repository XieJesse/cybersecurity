#Jesse Xie
#Cybersecurity
#Lab02 - Vigenere Encoder/Decoder
#2021-10-04

import sys

with open(sys.argv[2], 'r') as f:
    textfile = f.read() #put contents of textfile into string
with open(sys.argv[3], 'r') as f:
    keyfile = f.read() #put contents of keyfile into string

def shiftLetter(letter, number):
    value = ord(letter)
    value = value + number
    if (letter.islower()):
        if (value > 122):
            value -= 26
    if (letter.isupper()):
        if (value > 90):
            value -= 26
    return chr(value)

keyfile = keyfile.lower()

finalString = ""
keyIndex = 0 ;
for i in range(len(textfile)-1):
    if (textfile[i].isalpha()):
        shift = 0
        if (sys.argv[1] == "encode"):
            shift = ord(keyfile[keyIndex]) - 97
        if (sys.argv[1] == "decode"):
            shift = 26 - (ord(keyfile[keyIndex]) - 97)
        newLet = shiftLetter(textfile[i],shift)
        finalString += newLet
        keyIndex += 1
        if (keyIndex > len(keyfile)-1):
            keyIndex = 0
    else:
        finalString += textfile[i]
print(finalString)

