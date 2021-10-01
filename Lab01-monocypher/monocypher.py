#Jesse Xie
#Lab 01 - Monocypher
#Cybersecurity
#2021-09-27

#1.1

import sys
import math

def frequency(text):
    letterFrequencyList = []
    for i in range(26):
        letterFrequencyList.append(0.0) #create blank list for letter frequencies
    letterCount = 0
    for char in text.lower():
        if (char.isalpha()): #counts only letters
            added = False
            i = 0
            while added is False: #add one to the frequency list when the letter shows up
                if (ord(char)-97 == i):
                    letterFrequencyList[i] += 1
                    added = True
                else:
                    i = i + 1 
            letterCount = letterCount + 1

    for i in range(26): #convert frequency to relative frequency
       letterFrequencyList[i] = letterFrequencyList[i] / letterCount
    return letterFrequencyList

if (sys.argv[1] == "frequency"): #prints relative frequencies accordingly
    with open(sys.argv[2], 'r') as f:
        textfile = f.read() #put contents of file into string
    freqs = frequency(textfile)
    for i in range(26):
        print(str(chr(i+97)) + ":" + str(freqs[i]))

#1.2

if (sys.argv[1] == "decode"):
     with open(sys.argv[2], 'r') as f:
         text = f.read()
     with open(sys.argv[3], 'r') as f:
         reference = f.read()
     relativeFrequency = frequency(reference)
     letterFrequencyList = frequency(text)
     closest = sys.maxsize
     shift = 0
     for i in range(26): #loop for shifts 0-25
         current = 0 
         for j in range(26): #loop for letters a-z
             curIndex = j+i 
             if (curIndex >= 26): #shifted index adjusted for index in list
                 curIndex -= 26
             current += math.pow((letterFrequencyList[curIndex] - relativeFrequency[j]),2)
         current = math.sqrt(current) #distance formula to find distance in current shift
         if (current < closest):
             closest = current
             shift = i #keeps track of closest shift
     newText = ""
     for char in text: #shifts letters in the text accordingly, adds to a new text
         if (char.isalpha()):
             newOrd = ord(char)-shift
             if ((newOrd < 97) and (char.islower())): #shift for lowercase letters
                 newOrd += 26
             if ((newOrd < 65) and (char.isupper())): #shift for uppercase letters
                 newOrd += 26
             newText += str(chr(newOrd))
         else: newText += char
     print(newText) #outputs new text
