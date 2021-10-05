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

if (sys.argv[1] == "encode"): #encode part
    encodedString = ""
    keyIndex = 0 ;
    for i in range(len(textfile)-1):
        if (textfile[i].isalpha()):
            shift = ord(keyfile[keyIndex]) - 97
            newLet = shiftLetter(textfile[i],shift)
            encodedString += newLet
            keyIndex += 1
            if (keyIndex > len(keyfile)-1):
                keyIndex = 0
        else:
            encodedString += textfile[i]
    print(encodedString)
        
if (sys.argv[1] == "decode"): #decode part
    decodedString = ""
    keyIndex = 0 ;
    for i in range(len(textfile)-1):
        if (textfile[i].isalpha()):
            shift = 26 - (ord(keyfile[keyIndex]) - 97)
            newLet = shiftLetter(textfile[i],shift)
            decodedString += newLet
            keyIndex += 1
            if (keyIndex > len(keyfile)-1):
                keyIndex = 0
        else:
            decodedString += textfile[i]
    print(decodedString)
        
    
