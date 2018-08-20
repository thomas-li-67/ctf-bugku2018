from PIL import Image
import numpy as np
 
ori = np.asarray(Image.open('Steganography_original.png'))
ori=ori>>2
ori=ori<<2
print("ori:")
print(ori)
 
to_add = np.asarray(Image.open('Steganography_recovered.png').convert('RGB'))
print("to add:")
print(to_add)
to_add=to_add/85
print("to add /85:")
print(to_add)
result=np.bitwise_or(ori.astype(int), to_add.astype(int))
print("result:")
print(result)
im = Image.fromarray(np.uint8(result))
im.show()
im.save('Steganography_added.png')
