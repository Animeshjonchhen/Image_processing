from PIL import Image as im
import numpy as np

#converts rbg image into greyscale


image = im.open('Images/index.png')
image.show('index.png')
image_array = np.array(image)
print(image_array)
# image = im.open('images.png').convert('LA')
# image.save('grey_image.png')
image = im.open('greyscale.png')
image.show('greyscale.png')
image_array = np.array(image)
print(image_array)