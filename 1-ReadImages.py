# Reading images with OpenCV

from cv2 import cv2
import numpy as np

img = cv2.imread('lena.png', 0) # so here our image will be in grayscale

# display image

# cv2.imshow('image', img)

# so that image waits

cv2.waitKey(5000)

# destroy the window

cv2.destroyAllWindows()

# cv2.imwrite('lenaCopy.png', img) #we're creating a copy of the image here