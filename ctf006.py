import base64
import re

enstr = '''KYsd3js2E{a2jda}'''
col = 2

print(enstr)
steps = int(len(enstr)/col)
print(steps)


destr=''
for i in range(steps):
    print(i)
    for j in range(col):
      destr += enstr[j*steps + i]
print(destr)    