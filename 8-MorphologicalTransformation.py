import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('j.png', 0)
ret, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Using dilation with iterations to remove small black dots 
kernal = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

titles = ['images', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'm-gradient']
images = [img, mask, dilation, erosion, opening, closing, mg]

for i in range(7):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# cv2.imshow('Frame Output', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows