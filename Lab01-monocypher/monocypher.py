#Jesse Xie
#Lab 01 - Monocypher
#Cybersecurity
#2021-09-27

#1.1

f = open("alice.txt", "r")
alice = f.read()
alice = alice.lower()
letterFrequencyList = []
for i in range(26):
    letterFrequencyList.append(0)
print(len(alice))
letterCount = 0 

for char in alice:
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

print(letterCount)

for i in range(26):
   letterFrequencyList[i] = letterFrequencyList[i] / letterCount
   print(str(chr(i+97)) + ":" + str(letterFrequencyList[i]))
 

    
