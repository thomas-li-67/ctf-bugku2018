#!/usr/bin/env python


from __future__ import print_function, unicode_literals
import base64
import re


def encryt(key, plain):
    cipher = ''
    for i in range(len(plain)):
        cipher += chr(ord(key[i % len(key)]) ^ ord(plain[i]))
    
    return cipher


def getPlainText():
    plain = ''
    with open('plain.txt') as f:
        while True:
            line = f.readline()
            if line:
                plain += line
                continue
            break
    return plain


def main():
    key = 'LordCasser'
    plain = getPlainText()
    cipher = encryt(key, plain)
    with open('cipher.txt', 'w') as f:
        f.write(cipher.encode('base_64'))

#==============================

def getCipherText():
    cipher = ''
    
    with open('cipher.txt') as f:
       # while True:
            line = f.readline()
        #    if line:
              #  line = re.sub(r'\n','',line)
        #    line = f.readline()  
            cipher += line
         #       continue
         #   break         
    return base64.b64decode(cipher)        

def decryt(key, cipher):
    plain = ''
    for i in range(len(cipher)):
        plain += chr(ord(key[i % len(key)]) ^ ord(cipher[i]))
    
    return plain

def mymain():
    key = 'LordCasser'
    cipher = getCipherText()
    plain = decryt(key, cipher)
    print(plain)

if __name__ == '__main__':
    mymain()

#====================



