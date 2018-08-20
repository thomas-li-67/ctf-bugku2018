# coding=utf8

import base64
import re

enstr = '''gndk€rlqhmtkwwp}z'''



for p in range(len(enstr)):
    c=enstr[p]
    print(ord(c))
      
print("===") 
flag = 'flag{'
for p in range(len(flag)):
    c=flag[p]
    print(ord(c))

str=''
rot = 1
for p in range(len(enstr)):
    c=enstr[p]
    print(ord(c))
    if ord(c) >= 128:
        str += chr(128 - rot)  
    else:
        str += chr((ord(c) - rot) % 128)
    print(rot)    
    print((ord(c) - rot))    
    rot += 1
    if rot >= 19:
        rot = 1
    
print(str)    