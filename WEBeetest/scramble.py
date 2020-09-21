# -*- coding: utf8 -*-
sourceFile = open("./WEBeeBits0.txt", "r")
SourceBits = []
for line in sourceFile.readlines():
	strline = line.split(',')
	for i in range(len(strline)):
		SourceBits.append(int(strline[i]))
sourceFile.close()

PADBITS = 8*1
for i in range(PADBITS):
	SourceBits.insert(0, 0)
M = len(SourceBits)
out_bits = [0 for i in range(M)]
state = [1,0,0,1,0,0,0]
for i in range(7, M):
	feedback = state[3] ^ state[6]
	out_bits[i] = SourceBits[i] ^ feedback
	state[1:7] = state[0:6]
	state[0] = feedback

outputfile1 = open("./descrambleBits0.txt", "w")
for b in range(len(out_bits)):
	outputfile1.write(str(out_bits[b]))
	if b < len(out_bits) - 1:
		outputfile1.write(",")
outputfile1.write("\n")
outputfile1.close()

out = []
for i in range(0, M):
    out.append(0)
state2 = 9

for i in range(7, M):
    feedback = int(bool(state2 & 64))^(int(bool(state2 & 8)))
    out[i] = feedback ^ out_bits[i]
    state2 = ((state2 << 1) & 0x7e) | feedback

outputfile2 = open("./scrambleBits0.txt", "w")
for b in range(len(out)):
	outputfile2.write(str(out[b]))
	if b < len(out) - 1:
		outputfile2.write(",")
outputfile2.write("\n")
outputfile2.close()

