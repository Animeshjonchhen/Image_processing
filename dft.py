import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im,ImageDraw as ig_draw

o_image = im.open('Images/fourier_bw.png')
#row = o_image.size[0]
# col = o_image.size[1]
# result = im.new("L", (row, col))
# zero = np.zeros(row,col)

#for i in range(row):
 #   for j in range(col):
 #       value = np.fft.fft2(o_image)
       # result.putpixel((i,j), int(value))
# plt.plot(result)
# plt.show()
img_1 = np.fft.fft2(o_image)
plt.plot(img_1)
plt.show()