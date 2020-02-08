import numpy as np
from PIL import Image as im,ImageDraw as ig_draw

o_image = im.open('Images/images.jpg').convert("LA")
row = o_image.size[0]
col = o_image.size[1]
gamma1 = 1.2

result_img1 = im.new("L", (row, col))

for x in range(1 , row):
    for y in range(1, col):
        value = pow(o_image.getpixel((x,y))[0]/255,(1/gamma1))*255
        if value >= 255 :
            value = 255
        result_img1.putpixel((x,y), int(value))
img_draw = ig_draw.Draw(o_image)
img_draw.text((10,20),"Original Image",fill='Black') 
o_image.show()

img_draw = ig_draw.Draw(result_img1)
img_draw.text((10,20),"Animesh Lal Jonchhen",fill='Black') 

result_img1.show()
result_img1.save('gamma_correction.png')
