#coding=utf8
# 解决 convert

from __future__ import print_function, unicode_literals
from __future__ import  unicode_literals
import requests
import re
import sys
import codecs


fn = 'temp/convert.txt'

buf=''
with open(fn) as f:
    for line in f:
       buf = buf + line

#print(len(buf))       

def genbin(buf):
    for i in range(len(buf) // 8):
        yield buf[8 * i:8 * i + 8]

def bin2hex(b):
    return reduce(lambda c,x: c * 2 + (ord(x) - ord('0'))  , [i for i in b],0)

hexbuf = []
for b in genbin(buf):
    hexbuf.append(bin2hex(b))

#print(bin2hex('11111111'))

'''
print(hexbuf)
print([(hex(i),chr(i)) for i in hexbuf])
print(len(hexbuf))

'''
for i in hexbuf:
    print(chr(i),end='')

#print(hex(bin2hex('01010010')))