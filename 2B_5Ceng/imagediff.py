# coding = utf-8
from __future__ import print_function, unicode_literals
from PIL import Image

img1 = Image.open('2bs.png')
im1 = img1.load()
img2 = Image.open('b2.png')
im2 = img2.load()

w,h = img1.size
max = 0
min = 0
count = 0
jc = 0
mc =0
ff =0

binary = []

for y in range(h):
    for x in range(w):
        if(im1[x,y] != im2[x,y]):
            diff = im1[x,y][2]-im2[x,y][2]
            xor = (im1[x,y][2]^im2[x,y][2]) & 0xff
            if im2[x,y][2] == 0xff:
                ff = ff + 1
            if diff > max :
                max = diff
            else:
                if diff < min:
                    min = diff    
            #if diff == -211:      
            #if  im2[x,y][2] == 0xfe: 
            print((x,y),hex(im1[x,y][2]),hex(im2[x,y][2]),im1[x,y][2]-im2[x,y][2],im1[x,y][2]^im2[x,y][2])
            #print(chr(diff & 0xff),end=)
            if diff > 0:
                jc += 1
                binary.append(1)
            else:
                mc += 1
                binary.append(0)
          #  print(diff,xor)
            count += 1
print(count,count - ff)  
print(max,min,jc,mc,ff)      
'''   
def p9(a):
   print(a)

for i in range(len(binary) / 9):
    p9(binary[i * 9:i * 9 + 9])
'''

def bin2hex(b):
    return reduce(lambda c,i: c*2 + i,b[0:8])

def p8(a):
   print(a,hex(bin2hex(a)))
'''
for i in range(len(binary) // 9):
    p8(binary[i * 9:i * 9 + 9])
'''    