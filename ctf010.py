# coding=utf8

from __future__ import unicode_literals
import base64
import re
from pprint import pprint
from functools import reduce

def dump(obj):
  '''return a printable representation of an object for debugging'''
  newobj=obj
  if '__dict__' in dir(obj):
    newobj=obj.__dict__
    if ' object at ' in str(obj) and not newobj.has_key('__type__'):
      newobj['__type__']=str(obj)
    for attr in newobj:
      newobj[attr]=dump(newobj[attr])
  return newobj

enstr = '''公正公正公正诚信文明公正民主公正法治法治友善平等和谐敬业和谐富强和谐富强和谐文明和谐平等公正公正和谐法治公正公正公正文明和谐民主和谐敬业和谐平等和谐敬业和谐敬业和谐和谐和谐公正法治友善法治'''

values = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'

index = [i for i in range(len(enstr)) if i % 2 == 0]

#print(index)
h2v = lambda a: int(ord(a) - ord('A') + 10) if (a >= 'A' and a <= 'F') else int(ord(a) - ord('0'))

values2duo = lambda v: values.find(v) // 2
enstr2duos = lambda s: list(map(values2duo,list(map(lambda i: s[i:i+2],index))))
duos2hex = lambda d: reduce(lambda i,x: [i]+[x] if type(i) is int and i<10  else i+[x] if i[-1] >= 0 and i[-1] < 16 else i+ [x + 10] if  i[-1] == 88 else i+ [x+6] ,d)


duos = enstr2duos(enstr)

print(duos)
duos2 = list(map(lambda i: 88 if i==10 else 99 if i==11 else i,duos))
#print(duos2)
#print(duos2hex(duos2))
hexstr = duos2hex(duos2)
hexstr = list(filter(lambda i: i<16,duos2hex(duos2)))
hexstr2 = reduce(lambda i,x: [i*16 + x] if type(i) is int else i+[x] if i[-1] >= 16 else i[0:-1] + [i[-1]*16 + x]  ,hexstr)
print(hexstr)
print(hexstr[0:-1])
print(hexstr2)
print(map(lambda i:hex(i),hexstr2))
#print(type([1,1]))
print(''.join(map(lambda i:chr(i),hexstr2)))


