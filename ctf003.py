# ctf.bugku.com
# 速度要快

import requests
import re
import time
import base64


url = 'http://120.24.86.145:8002/web6/'


r = requests.get(url)
sessid = r.cookies['PHPSESSID']
r.encoding = "utf-8"  
flagbase64 = r.headers['flag']
flag = base64.b64decode(flagbase64)
print(sessid)
print(flag.decode())
p = re.compile('.+:\s+(.+)$')
m = p.match(flag.decode())
print(m)
v = m.group(1)
print(v)
vv = base64.b64decode(v)
print(vv)
vvv = vv.decode()
print(vvv)
#e = eval('str=' + eval(flag))
#str = b'\xe8\xb7\x91\xe7\x9a\x84\xe8\xbf\x98\xe4\xb8\x8d\xe9\x94\x99\xef\xbc\x8c\xe7\xbb\x99\xe4\xbd\xa0flag\xe5\x90\xa7: NTI4OTY0'
print(r.headers)
print("====================\n")
#time.sleep( 1 )


header = {'Cookie':'Timeout=alive;PHPSESSID=' + sessid}
r = requests.post(url, data = {'margin':vvv},headers = header)
print(r.headers)
r.encoding = "utf-8" 
print(r.encoding)
#print(r.cookies['PHPSESSID'])
print(r.text)

print("+++++++++++++++++++")


    