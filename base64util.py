import base64

base64str = 'a2V5cy50eHQ='

destr = base64.b64decode(base64str)

print(destr)

str1 = b'index.php'

print(base64.b64encode(str1))