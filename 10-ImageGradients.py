"""
Image Gradient is directional change in intensity or color in the image
so that edges are detected

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
# CV_64F is just a datatype which is 64 bit float supporting -ve numbers

# SobelX: change in direction of intensity in Y direction
# Sobel=Y: change in direction of intensity in X direction

titles = ['image', 'Laplacian']
images = [img, lap]

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
