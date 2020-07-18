import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# OpenCV reads image in BGR format hence convert it into RGB

cv2.imshow('Frame o/p', img)
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows