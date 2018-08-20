from PIL import Image
import numpy as np
 
I=Image.open('Steganography_added.png')
stego = np.asarray(I)
extracted = stego & 0b00000011
extracted *= int(255 / 3)
print("what we get:")
print(extracted)
im = Image.fromarray(np.uint8(extracted))
im.show()
im.save('Steganography_get.png')
 
