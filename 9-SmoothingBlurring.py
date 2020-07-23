import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# creating a kernel of 5x5 ones
# 25 = 5x5
kernel1 = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel1)
blur = cv2.blur(img, (5,5));

# Using Gausian Blur filter
"""
G.Blur works on the principle of in any image higher weights are in middle of image than
as the distance increases from mid
"""

gBlur = cv2.GaussianBlur(img, (5,5), 0);


# Median Filter
"""
It replace each pixel's value with the median of its neighbouring pixel.
Suitable for micro particle like salt and pepper noise grains in the image
Kernel size must be odd here
"""

mBlur = cv2.medianBlur(img, 5);

# Bilateral Filter highly suitable for noise reduction while keeping image edges sharp

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75);

titles = ['images', '2D Convolution', 'Blur', 'Gausian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gBlur, mBlur, bilateralFilter]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()