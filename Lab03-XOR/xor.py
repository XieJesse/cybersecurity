#Jesse Xie
#Cybersecurity
#Lab03 - XOR Cipher
#2021-10-18


import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
  print("mode:"+mode)
  print("key: "+key)
  print("inp: "+inp)

def xor(key,inp):
    output = []
    keyIndex = 0
    for char in inp:
        output.append(str((ord(char) ^ ord(key[keyIndex]))))
        keyIndex += 1
        if keyIndex == len(key):
            keyIndex = 0
    return output

if mode == "numOut":
    output = ""
    xorOutput = xor(key,inp)
    for i in xorOutput:
        output += str(hex(int(i)))[2:4] + ' '
    print(output)
