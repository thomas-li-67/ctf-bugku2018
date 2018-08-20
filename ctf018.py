# !/usr/bin/python
# coding=utf-8

# 一个普通的压缩包(xp0intCTF)

# dump rar 文件

from __future__ import print_function, unicode_literals
import struct

from struct import pack, unpack, Struct

S_LONG = Struct('<L')
S_SHORT = Struct('<H')
S_BYTE = Struct('<B')

S_BLK_HDR = Struct('<HBHH')
S_FILE_HDR = Struct('<LLBLLBBHL')
S_COMMENT_HDR = Struct('<HBBH')

# block types
RAR_BLOCK_MARK          = 0x72  # r
RAR_BLOCK_MAIN          = 0x73  # s
RAR_BLOCK_FILE          = 0x74  # t
RAR_BLOCK_OLD_COMMENT   = 0x75  # u
RAR_BLOCK_OLD_EXTRA     = 0x76  # v
RAR_BLOCK_OLD_SUB       = 0x77  # w
RAR_BLOCK_OLD_RECOVERY  = 0x78  # x
RAR_BLOCK_OLD_AUTH      = 0x79  # y
RAR_BLOCK_SUB           = 0x7a  # z
RAR_BLOCK_ENDARC        = 0x7b  # {

currentOffset = 0

def dumpdata(hdata):
    print([hex(ord(i)) for i in hdata])


def parse_block_header(fd):
    currentOffset = fd.tell()
    print(hex(currentOffset),S_BLK_HDR.size)
    # read and parse base header
    buf = fd.read(S_BLK_HDR.size)
    if not buf:
        return None
    t = S_BLK_HDR.unpack_from(buf)
    header_crc, header_type, header_flags, header_size = t
    # read full header
    if header_size > S_BLK_HDR.size:
        hdata = buf + fd.read(header_size - S_BLK_HDR.size)
    else:
        hdata = buf
    currentOffset = fd.tell()

    return header_crc, header_type, header_flags, header_size,hdata

def parse_file_header(hdata, pos,fd):
    fld = S_FILE_HDR.unpack_from(hdata, pos)
    compress_size = fld[0]
    file_size = fld[1]
    host_os = fld[2]
    CRC = fld[3]
    date_time = fld[4]
    extract_version = fld[5]
    compress_type = fld[6]
    name_size = fld[7]
    mode = fld[8]
    filename = hdata[S_FILE_HDR.size + S_BLK_HDR.size:S_FILE_HDR.size+S_BLK_HDR.size+name_size]
    print('name size=',name_size, ' file size = ',compress_size,' filename=',filename)
    filebuf = fd.read(compress_size)
    currentOffset = fd.tell()
    return filename,filebuf

fn = 'temp/zip/flag.rar'
with open(fn, 'rb') as f:
    for i in range(5):
        header_crc, header_type, header_flags, header_size,hdata = parse_block_header(f)
        print(hex(header_type),hex(header_size))
        #dumpdata(hdata)
        if header_type == RAR_BLOCK_FILE or header_type == 0x7a:
            print('===========================')
            filename,filebuf = parse_file_header(hdata,S_BLK_HDR.size,f)
            print(filebuf)
        




