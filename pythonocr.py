import pyocr

toola=pyocr.get_available_tools()[:]

n=toola[0].get_name()

from PIL import Image

#ii=Image.open('d:\\ctf\\temp\\flag.jpeg')
ii=Image.open('d:\\ctf\\temp\\2.png')
print toola[0].image_to_string(ii,lang='eng')