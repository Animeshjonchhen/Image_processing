import cv2

img = cv2.imread('Images/noise.jpg',0)
cv2.imshow('Mean Filter Animesh',img)
blur = cv2.blur(img, (5, 5))

cv2.imwrite('animesh.png',blur)
cv2.waitKey(0)