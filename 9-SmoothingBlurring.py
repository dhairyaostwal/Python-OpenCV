import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('OpenCV_Logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# creating a kernel of 5x5 ones
# 25 = 5x5
kernel1 = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel1)

titles = ['images', '2D Convolution']
images = [img, dst]

for i in range(2):
    plt.subplot(1,2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()