#Jesse Xie
#Lab 01 - Monocypher
#Cybersecurity
#2021-09-27

f = open("alice.txt", "r")
alice = f.read()
alice = alice.lower()
letterFrequencyList = []
for i in range(26):
    letterFrequencyList.append(0)
print(len(alice))
letterCount = 0 


    
