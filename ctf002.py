import requests
import re
import time


url = 'http://120.24.86.145:8002/qiumingshan/'


r = requests.get(url)
sessid = r.cookies['PHPSESSID']
r.encoding = "utf-8"  
o = re.sub(r"<style[^<]+</style>", "", r.text)
o = re.sub(r"<[^>]+>", "", o,re.UNICODE)
#o = re.sub(r"\s+","",o)
a = o.split()
e = re.compile("[0123456789+*/-]+")
expr = e.match(a[2])
print(expr.group())
value = eval(expr.group())
#print(r.encoding)
print(sessid)
print(a[2])
print(value)
print(r.headers)
print("====================\n")
#time.sleep( 1 )

#cookies = dict(PHPSESSID=sessid)
#r = requests.post(url, data = {'value':value},cookies=cookies)
#print(r.headers)
##r.encoding = "utf-8" 
#print(r.encoding)
#print(r.cookies['PHPSESSID'])
#print(r.text)
#print("--------\n")

##jar = requests.cookies.RequestsCookieJar()
#jar.set('PHPSESSID', sessid, path='/cookies',timeout='alive')
header = {'Cookie':'Timeout=alive;PHPSESSID=' + sessid}
r = requests.post(url, data = {'value':value}, headers = header)
print(r.headers)
r.encoding = "utf-8" 
print(r.encoding)
#print(r.cookies['PHPSESSID'])
print(r.text)

    