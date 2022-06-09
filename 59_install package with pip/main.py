import numpy as np
from PIL import  Image

img = Image.open("logo.jpg")

print("format file : "+ img.format)
print("format file : "+ str(img.size))
print("format file : "+ img.mode)

img.show()