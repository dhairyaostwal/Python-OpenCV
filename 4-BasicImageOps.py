import cv2
import numpy as np

img = cv2.imread('cr7.jpg')
img2 = cv2.imread('lena.png')
# Resizing the dimensions to 30% original size

scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# print(img.shape) # returns no. of rows, columns and channels
# print(img.size) # returns the no. of pixels
# print(img.dtype) # returns the data type of the image

"""
Result:

(2048, 3072, 3)
18874368
uint8 aka 1 byte 9 bit unsigned integers
"""

# ROI(Region of Interest)

# ball = resized[289:500, 406:591]
# resized[612:532, 727:601] = ball

img2 = cv2.resize(img2, (512, 512))
img = cv2.resize(img, (512,512))

dst = cv2.addWeighted(img, .7, img2, .5, 0)

cv2.imshow('Image Output', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()