#Jesse Xie
#Cybersecurity
#Lab03 - XOR Cipher
#2021-10-18


import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()[:-1]
inp = open(inpfile,"rb").read()[:-1]
debug = False

if(debug):
  print("mode:"+mode)
  print("key: "+key)
  print("inp: "+inp)

def xor(key,inp): #xor method that accepts key and inp string
    output = []
    keyIndex = 0
    for char in inp: #add xor'ed character to array
        output.append((char) ^ (key[keyIndex]))
        keyIndex += 1 #keep track of index
        if keyIndex == len(key):
            keyIndex = 0
    return output

if mode == "numOut":
    out = ""
    xorOutput = xor(key,inp)
    for i in xorOutput:
        out += hex(i)[2:4] + ' '
    print(out)

if mode == "human":
    out = ""
    xorOutput = xor(key,inp)
    outfile = open("output","wb")
    for i in xorOutput:
        outfile.write((i).to_bytes(1,byteorder="little"))
