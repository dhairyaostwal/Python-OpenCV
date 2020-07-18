import cv2
import numpy as np

img = cv2.imread('sudoku.png', 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# In upper inside threshhold function parameter thresh means min value/min cutoff
# So what th1 does is it shows the binary format either black or white
# cv2.ADAPTIVE_THRESH_MEAN_C -- Here threshold value depends on mean that is neighbourhood area
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C -- weighted sum (cross-correlation with a Gaussian window) of the 𝚋𝚕𝚘𝚌𝚔𝚂𝚒𝚣𝚎×𝚋𝚕𝚘𝚌𝚔𝚂𝚒𝚣𝚎 neighborhood of (x,y) minus C

cv2.imshow('Frame-Output', img)
cv2.imshow('New-O/p', th2)
cv2.imshow('New-O/p-2', th3)
cv2.waitKey(0)
cv2.destroyAllWindows