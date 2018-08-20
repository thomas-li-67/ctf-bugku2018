#coding=utf8

from __future__ import  print_function, unicode_literals
import zipfile
import binascii
import string

dictab = string.ascii_letters + string.digits + '+/=_'
#dictab = '_CR32i5n0ts4f3'
def strgen(l):
    if l == 1 :
        for i in dictab:
            yield i
    else:    
        for j in strgen( l - 1 ):
            for i in dictab:
                yield i + j


def newStrGen():
    return strgen

def CrackCrc(crc,l):
   # g = newStrGen()
    for s in strgen(l):
       # print(s)
        if crc == (binascii.crc32(s) & 0xffffffff):
         #   print(s)
            return s       

def CrackCrc6(crc):
    return CrackCrc(crc,6)

def CrackFile(file):
    crc = zipfile.ZipFile(file,'r').getinfo('data.txt').CRC
    print(hex(crc),crc)
    print(file)
    return CrackCrc(crc)            

crc = [0x7c2df918,0xa58a1926,0x4dad5967]

#print(CrackCrc(0x7c2df918,6))
print(''.join(map(CrackCrc6,crc)))

'''
for s in strgen(6):
    print(s)                    
   # print(binascii.crc32(s))
'''
'''
text = ''.join([CrackFile('temp/123/out'+str(f)+'.zip') for f in range(68) ])
print(text)
'''
'''
print(binascii.crc32('AAAA'),hex(binascii.crc32('AAAA')),hex(binascii.crc32('AAAA') &  0xffffffff))
t = CrackFile('temp/123/out2.zip')
print(t)

t = CrackFile('temp/123/out3.zip')
print(t)
'''
'''
for s in strgen():
    print(s)                    
    print(binascii.crc32(s))
'''
'''
Offset      0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F

00000000   50 4B 03 04 14 00 01 00  08 00 EB 00 1D 49 F1 08   PK        ? I?
00000010   0D 9B 12 00 00 00 04 00  00 00 08 00 00 00 64 61    ?           da
00000020   74 61 2E 74 78 74 E6 16  68 87 E9 1E 7F 8A F8 C0   ta.txt?h囬  婙?
00000030   91 1F 41 2A 98 B5 C3 FB  50 4B 01 02 00 00 14 00   ?A*樀名PK      
00000040   01 00 08 00 EB 00 1D 49  F1 08 0D 9B 12 00 00 00       ? I? ?   
00000050   04 00 00 00 08 00 00 00  00 00 00 00 01 00 00 00                   
00000060   00 00 00 00 00 00 64 61  74 61 2E 74 78 74 50 4B         data.txtPK
00000070   05 06 00 00 00 00 01 00  01 00 36 00 00 00 38 00             6   8 
00000080   00 00 00 00                                            

F1 08 0D 9B 是CRC
'''
'''
python 2.7 下 binascii.crc32() - document signed vs unsigned results
Python 2.6:

>>> binascii.crc32('Hello')
-137262718

Python 3.0:

>>> binascii.crc32(b'Hello')
4157704578

要用 binascii.crc32('AAAA') &  0xffffffff

Placing a note in the standard library documentation would be a start.   
Just say in Python 3.0 it always returns the result as an unsigned 
integer whereas in Python 2.6 a 32-bit signed integer is returned. 
Although the numerical value may differ between versions, the underlying 
bits are the same.  Use crc32() & 0xffffffff to get a consistent value 
(already noted).

Note: Not everyone uses checksums in only a packed-binary format.  
Having the integer value just change across Python  versions like that 
is a real subtle compatibility problem to point out.
'''