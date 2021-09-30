#Jesse Xie
#Lab 01 - Monocypher
#Cybersecurity
#2021-09-27

#1.1

import sys
import math

with open(sys.argv[1], 'r') as f:
    text = f.read() #put contents of file into string   

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
   if (sys.argv[2] == "frequency"): #prints relative frequencies accordingly
       print(str(chr(i+97)) + ":" + str(letterFrequencyList[i]))

#1.2

relativeFrequency = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
    0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
    0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
    0.00074
    ] #relative frequencys for letters in english from cs.wellesley.edu
       
if (sys.argv[2] == "decode"):
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
    
