# -*- coding: utf8 -*-

def getSym(x):
	t={'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':10,'1011':11,'1100':12,'1101':13,'1110':14,'1111':15}
	return t[x]

wifiFiles = open("./webeepayload.txt", "w")
sourceFile = open("./descrambleBits0.txt", "r")
SourceBits = []
for line in sourceFile.readlines():
	strline = line.split(',')
	for i in range(len(strline)):
		SourceBits.append(int(strline[i]))
sourceFile.close()

M = len(SourceBits)

ST = M // 8
for i in range(2,ST):
	bits = [0 for j in range(8)]
	for j in range(8):
		bits[7-j] = SourceBits[i*8 + j]
	strbit = ""
	for k in range(4):
		strbit =  strbit + str(bits[k])
	high = getSym(strbit)
	strbit = ""
	for k in range(4,8):
		strbit =  strbit + str(bits[k])
	low = getSym(strbit)
	strn = str(high * 16 + low)
	wifiFiles.write(strn+',')
wifiFiles.write("\r\n")
wifiFiles.close()

sourceFile2 = open("./webeepayload.txt","r")
line = sourceFile2.readlines()[0]
strline = line.split(',')
laststrline = strline[-1]
sourceBytes = []
for n in range(len(strline)):
    if(strline[n] != '\n'):
        sourceBytes.append(int(strline[n]))

payload = bytes(sourceBytes)
data_bits = []
msg_len = len(payload)
for i in range(msg_len):
    for n in range(8):
        data_bits.append(int(bool(payload[i] & (1<<n))))

generatebitsfile = open("./generatebitsfile.txt", "w")
for b in range(len(data_bits)):
	generatebitsfile.write(str(data_bits[b]))
	if b < len(data_bits) - 1:
		generatebitsfile.write(",")
generatebitsfile.write("\n")
generatebitsfile.close()
