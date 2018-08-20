#!/usr/bin/python
# coding=utf-8


chars = ",.0123456789?abcdefghijklmnopqrstuvwxyz"
codes = """--..-- .-.-.- ----- .---- ..--- ...-- ....- ..... -.... --... ---..
      ----. ..--.. .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. --
      -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."""
c2mkeys = dict(zip(chars,codes.split()))
m2ckeys = dict(zip(codes.split(),chars))

def char2morse(char):
  return c2mkeys.get(char.lower(),char)

def morse2char(mstr):
    return m2ckeys.get(mstr) if m2ckeys.get(mstr)  else '*'

#print ' '.join(char2morse(c) for c in 'SOS')
#morsestr = '-.-.  -..- -..'
morsestr = '..... -... -.-. ----.  ..--- ..... -....  ....- ----. -.-. -... ----- .---- ---.. ---.. ..-. ..... ..---  . -.... .---- --... -.. --... ----- ----. ..--- ----. .---- ----. .---- -.-.'
print morsestr
print ''.join(morse2char(m) for m in morsestr.split())
print (''.join(morse2char(m) for m in morsestr.split())).upper()
print map(lambda m:(m,morse2char(m)),morsestr.split())