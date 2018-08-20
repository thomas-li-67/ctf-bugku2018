import base64
import re

enstr = '''636A56355279427363446C4A49454A7154534230526D684356445A31614342354E326C4B4946467A5769426961453067'''

enstr2 = ""

h2v = lambda a: int(ord(a) - ord('A') + 10) if (a >= 'A' and a <= 'F') else int(ord(a) - ord('0'))

for p in range(int(len(enstr)/2)):

    c1=enstr[2*p]
    c2=enstr[2*p+1]
   
    byte = ((h2v(c1) * 16) + h2v(c2))    
    print(byte)
    print(chr(byte))
    enstr2 += chr(byte)  

print(enstr2)   
print(len(enstr2)) 
print(base64.b64decode(enstr2))