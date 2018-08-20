import zlib
 
for i in xrange(100000):
    s = str(i).rjust(5,'0')
    #print s
    if zlib.crc32(s) & 0xffffffff == 0x845623bc:
        print s
 