#coding=utf8
# 解决 bugku 王晓明的日记

from __future__ import print_function, unicode_literals
from __future__ import  unicode_literals
import requests
import re
import sys
import codecs


passwdfile = 'temp/password.txt'

with open(passwdfile) as f:
    for line in f:
        print(line)
