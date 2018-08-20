#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("temp/paintpaintpaint.jpg", "r")

# 重新设置文件读取指针到jpg尾
fo.seek(0x52f6, 0)
#print(fo.read())
print(fo.read().decode('hex'))
fo.close()