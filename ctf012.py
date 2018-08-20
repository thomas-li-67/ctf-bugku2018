# coding=utf8

from __future__ import unicode_literals
import re
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


array = [
    'ZWAXJGDLUBVIQHKYPNTCRMOSFE',
    'KPBELNACZDTRXMJQOYHGVSFUWI',
    'BDMAIZVRNSJUWFHTEQGYXPLOCK',
    'RPLNDVHGFCUKTEBSXQYIZMJWAO',
    'IHFRLABEUOTSGJVDKCPMNZQWXY',
    'AMKGHIWPNYCJBFZDRUSLOQXVET',
    'GWTHSPYBXIZULVKMRAFDCEONJQ',
    'NOZUTWDCVRJLXKISEFAPMYGHBQ',
    'QWATDSRFHENYVUBMCOIKZGJXPL',
    'WABMCXPLTDSRJQZGOIKFHENYVU',
    'XPLTDAOIKFZGHENYSRUBMCQWVJ',
    'TDSWAYXPLVUBOIKZGJRFHENMCQ',
    'BMCSRFHLTDENQWAOXPYVUIKZGJ',
    'XPHKZGJTDSENYVUBMLAOIRFCQW'
        ]

matrix = []

enstr = '''HCBTSXWCRQGLES'''
key   = '''2,5,1,3,6,4,9,7,8,14,10,13,11,12'''

keyarray = list(map(lambda s: int(s),key.split(',')))

index = [i for i in range(len(enstr)) if i % 2 == 0]

#print(index)

def array2matrix(a):
    m = []
    for i in range(len(a)):
        m += [[c for c in a[i]]]
    return m    
 

def dumpmatrix(m):
    for l in m:
        for c in l:
            print c,
        print("\n")    

def dumpmatrixr(m):
    cn = len(m[0])
    ln = len(m)
    for j in range(cn):
        str=''
        for i in range(ln):
            str += m[i][j]
        print(str)  

def whichpos(a,c):
    for i in range(len(a)):
        if c == a[i]:
            return i
    return -1        


shiftindex = lambda index,s: list(map(lambda i: (i + s) % 26 ,index))
shiftline = lambda a,i,s: list(map(lambda p: a[p],shiftindex(i,s)))



matrix = array2matrix(array)
index = [i for i in range(len(matrix[0]))]
dumpmatrix(matrix)
#print(matrix)
#print index
#print(whichpos(matrix[0],'H'))
#print(shiftindex(index,13))
#print(keyarray)

outmatrix = [1] * 14
for i in range(len(keyarray)):
    k = enstr[i]
    ai = keyarray[i]
    p = whichpos(matrix[ai-1],k)
    outmatrix[i] = shiftline(matrix[ai-1],index,p)
    print k,ai,p
    print shiftindex(index,p)
    print matrix[ai-1]
    print outmatrix[ai-1]
    print "=============================="

#print(outmatrix)    
dumpmatrixr(outmatrix)
dumpmatrix(outmatrix)
