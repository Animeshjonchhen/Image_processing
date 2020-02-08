#Discrete Fourier Transform
import cv2
import numpy as np
from PIL import Image

img1 = cv2.imread("Images/images.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img1)

# shifting result by N/2 to bring in center
fshift = np.fft.fftshift(f)

# The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks.

mag_spec = 20 * np.log(np.abs(fshift))
mag_spec = np.asarray(mag_spec, dtype=np.uint8)

cv2.imshow(" Original Image Animesh", img1)

cv2.imshow("After log transform Dft", mag_spec)

# rotation
img_rtr = Image.open("Images/images.jpg")
rotate = img_rtr.rotate(45)

rotate.show()

f2 = np.fft.fft2(rotate)
# shifting result by N/2 to bring in center
fshift2 = np.fft.fftshift(f2)

# The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks.
mag_spec2 = 20 * np.log(np.abs(fshift2))
mag_spec2 = np.asarray(mag_spec2, dtype=np.uint8)
cv2.imshow(' Animesh Rotation', mag_spec2)

# image translation
num_rows, num_cols = img1.shape[:2]

translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
img_translation = cv2.warpAffine(img1, translation_matrix, (num_cols + 70, num_rows + 110))
cv2.imshow('Animesh Translation', img_translation)

f1 = np.fft.fft2(img_translation)

# shifting result by N/2 to bring in center
fshift1 = np.fft.fftshift(f1)

# The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks.
mag_spec1 = 20 * np.log(np.abs(fshift1))
mag_spec1 = np.asarray(mag_spec1, dtype=np.uint8)

cv2.imshow('Animesh Translation', mag_spec1)

cv2.waitKey(0)