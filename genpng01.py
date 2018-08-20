import png
s = ['011001110001',
     '011001110001',
     '011001110001',
     '011001110001',
     '011001110001',
     '011001110001']
s=[i for i in map(lambda x:[i for i in map(int,x)],s)]
 
f = open('c:\\1.png', 'wb')
w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
#palette=[(0x55,0x55,0x55), (0xff,0x99,0x99)]
#w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
w.write(f, s)
f.close()
