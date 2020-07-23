import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)    
lr = cv2.pyrDown(img)
ur = cv2.pyrUp(lr) # upgrading res lr

titles = ['image', 'Lower Resolution', 'Upper Resolution']
images = [img, lr, ur]

for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
