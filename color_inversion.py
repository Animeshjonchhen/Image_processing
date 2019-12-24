from PIL import Image as im,ImageDraw as ig_draw


img = im.open('Images/images.jpg').convert("LA")


pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        x,y = pixels[i,j][0],pixels[i,j][1]
        x,y = abs(x-255), abs(y-255)
        pixels[i,j] = (x,y)
img_draw = ig_draw.Draw(img)
img_draw.text((20,20),"Animesh Lal Jonchhen",fill='Black') 
img.show()
img.save('color_inversion.png')
