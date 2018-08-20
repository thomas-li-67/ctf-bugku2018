import base64
import re

with open('temp/1.txt', 'r') as myfile:
  data=myfile.read().replace('\n', '')
#print(data)  
strbytes = base64.b64decode(data)
#print(strbytes)

#str = 'abcde'
stresc = strbytes.decode(encoding='UTF-8',errors='strict')

# decode \000 - \777 oct escape str
outstr = ''
offset = 0
octbyte = 0
while True:
    if offset >= len(strbytes):
        outstr += chr(octbyte)
        break   
    if strbytes[offset] == ord('\\') :
        if octbyte > 0:
            outstr += chr(octbyte)
            octbyte = 0
    else:
        o = int(strbytes[offset] - ord('0'))
        octbyte = ((octbyte * 8) + o)       
    offset += 1     
hexstr = outstr
#print(hexstr)

# decode \x00 - \xff hex escape str

outstr = ''
offset = 0
hexbyte = 0
while True:
    if offset >= len(hexstr):
        outstr += chr(hexbyte)
        break   
    if hexstr[offset] == '\\' :
        if hexbyte > 0:
            outstr += chr(hexbyte)
            hexbyte = 0
        offset += 1    
    else:
        if hexstr[offset] >= 'a' and hexstr[offset] <= 'f':
            o = int(ord(hexstr[offset]) - ord('a') + 10)
        else:    
            o = int(ord(hexstr[offset]) - ord('0'))
        hexbyte = ((hexbyte * 16) + o)       
    offset += 1     

#print(outstr)  
unicodestr = outstr

# decode \u0000 - \uffff unicode str

outstr = ''
offset = 0
hexword = 0
while True:
    if offset >= len(unicodestr):
        outstr += chr(hexword)
        break   
    if unicodestr[offset] == '\\' :
        if hexword > 0:
            outstr += chr(hexword)
            hexword = 0
        offset += 1    
    else:
        if unicodestr[offset] >= 'a' and unicodestr[offset] <= 'f':
            o = int(ord(unicodestr[offset]) - ord('a') + 10)
        else:    
            o = int(ord(unicodestr[offset]) - ord('0'))
        hexword = ((hexword * 16) + o)       
    offset += 1           

#print(outstr)

# String.fromCharCode(38,35

charcodestr = re.sub(r"String\.fromCharCode\(", "", outstr)
charcodestr = re.sub(r"\)", "", charcodestr)
#print(charcodestr)
charcodes = charcodestr.split(',')
outstr = ''
for i in range(len(charcodes)):
    outstr += chr(int(charcodes[i]))

print(outstr)    

#
#  &#x26;&#x23;

htmlencodes = outstr.split(';')
outstr = ''
byte=0
for code in htmlencodes:
    s = re.sub(r"^&#x","",code)
    byte=0
    if len(s) < 2 :
        break
    for j in [0,1]:
        if s[j] >= 'a' and s[j] <= 'f':
            o = int(ord(s[j]) - ord('a') + 10)
        else:    
            o = int(ord(s[j]) - ord('0'))
        byte = ((byte * 16) + o)    
    print(byte)       
    outstr += chr(byte)
print(outstr)    


##  url 编码
##  &#102;&#108;&#97;&#103;&#37;&#55;&#66;&#99;&#116;&#102;&#95;&#116;&#102;&#99;&#50;&#48;&#49;&#55;&#49;&#55;&#113;&#119;&#101;&#37;&#55;&#68;

htmlencodes = outstr.split(';')
outstr = ''
byte=0
for code in htmlencodes:
    s = re.sub(r"^&#","",code)
    byte=0
    if len(s) < 2 :
        break
    for j in range(len(s)):
        if s[j] >= 'a' and s[j] <= 'f':
            o = int(ord(s[j]) - ord('a') + 10)
        else:    
            o = int(ord(s[j]) - ord('0'))
        byte = ((byte * 10) + o)    
    print(byte)       
    outstr += chr(byte)
print(outstr)   

# flag%7Bctf_tfc201717qwe%7D 
