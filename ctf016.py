#coding=utf8
# 好多数值

from __future__ import print_function, unicode_literals
from __future__ import  unicode_literals
import requests
import re
import sys
import codecs
from PIL import Image

def chomp(x):
  if x.endswith("\r\n"): return x[:-2]
  if x.endswith("\n"): return x[:-1]
  return x

file = 'temp/haoduoshuzhi.txt'
a = []
img=Image.new('RGB',(503,122),(0,0,0))
p = img.load()

with open(file) as f:
    for line in f:
        (r,g,b) = map(lambda i:int(i),chomp(line).split(','))
        #print((r,g,b))
        a.append((r,g,b))


print(len(a))         # 61336 = 2x61x503 = 122 x 503

for i in range(503):
    for j in range(122):
        p[i,j] = a[i * 122 + j]

img.show()   
# flag{youc@n'tseeme}    


