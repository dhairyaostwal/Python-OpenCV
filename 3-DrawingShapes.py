from cv2 import cv2
import numpy as np

# img = cv2.imread('lena.png',-1)
# using numpy for importing dark background image
img = np.zeros([512, 512, 3], np.uint8)

# img = cv2.line(img, (0,50), (50,500), (150,0,255), 5) #pink colored line
# img = cv2.arrowedLine(img, (0,0), (500,500), (255,150,0), 2) #light blue colored arrow

# Drawing a Rectangle

img = cv2.rectangle(img, (5,5), (45,45), (0,255,0), -5, )
# if thickness is negative then shape will be filled in here - rectangle

img = cv2.circle(img, (447,63), 63, (150,255,200), -1)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Hey", (10,500), font, 2, (255, 120, 102), 3)


cv2.imshow('image', img)

cv2.waitKey(5000)

cv2.destroyAllWindows