# coding=utf8

import base64
import re

enstr = '''e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA'''

#enstr = '''@iH<,{bdR2H;i6*Tm,Wx2izpx2!'''

for p in range(127):
    destr=''
    for i in enstr:
        temp = chr((ord(i) + p) % 128)
        if 32<ord(temp)<127:
            destr += temp
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(destr)  
        e = re.compile(".+=$")
        if e.match(destr):
            flag = base64.b64decode(destr)
            print(flag)          
 

