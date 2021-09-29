#Jesse Xie
#Lab 01 - Monocypher
#Cybersecurity
#2021-09-27

#1.1

import sys
import math

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

relativeFrequency = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
                     0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                     0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
                     0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                     0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
                     0.00074
                     ]
       
if (sys.argv[2] == "decode"):
     closest = sys.maxsize
     shift = 0
     for i in range(26):
         current = 0 
         for j in range(26):
             curIndex = j+i
             if (curIndex >= 26):
                 curIndex -= 26
             current += math.pow((letterFrequencyList[curIndex] - relativeFrequency[j]),2)
         current = math.sqrt(current)
         if (current < closest):
             closest = current
             shift = i
     print(shift)

    
