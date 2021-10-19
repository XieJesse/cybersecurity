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

def xor(key,inp): #xor method that accepts key and inp string
    output = []
    keyIndex = 0
    for char in inp: #add xor'ed character to array
        output.append(char ^ key[keyIndex])
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
    for i in xorOutput:
        out += chr(i)
        outfile = open("output","wb")
        outfile.write(chr(i).to_bytes(1,byteorder="little"))
    print(out)
