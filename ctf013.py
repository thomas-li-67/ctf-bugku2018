# coding=utf8

import base64
import re

enstr = '''666c61677b616537333538376261353662616566357d'''

enstr2 = ""

h2v = lambda a: int(ord(a) - ord('a') + 10) if (a >= 'a' and a <= 'f') else int(ord(a) - ord('0'))

for p in range(int(len(enstr)/2)):

    c1=enstr[2*p]
    c2=enstr[2*p+1]
   
    byte = ((h2v(c1) * 16) + h2v(c2))    
    print(byte)
    print(chr(byte))
    enstr2 += chr(byte)  

print(enstr2)   
print(len(enstr2)) 
print(base64.b64decode(enstr))