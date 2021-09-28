#Jesse Xie
#Lab 01 - Monocypher
#Cybersecurity
#2021-09-27

#1.1

import sys

with open(sys.argv[1], 'r') as f:
    text = f.read()      

text = text.lower()
letterFrequencyList = []
for i in range(26):
    letterFrequencyList.append(0.0)
letterCount = 0

for char in text:
    if (char.isalpha()):
        added = False
        i = 0
        while added is False:
            if (ord(char)-97 == i):
                letterFrequencyList[i] = letterFrequencyList[i] + 1
                added = True
            else:
                i = i + 1
        letterCount = letterCount + 1

for i in range(26):
   letterFrequencyList[i] = letterFrequencyList[i] / letterCount
   if (sys.argv[2] == "frequency"):
       print(str(chr(i+97)) + ":" + str(letterFrequencyList[i]))
 

    
