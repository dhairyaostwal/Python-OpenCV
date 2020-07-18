# HSV (HUE SATURATION & VALUE)

import cv2
import numpy as np



while(True):
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerBlue = np.array([82, 51, 51])
    upperBlue = np.array([133, 255, 255])

    mask = cv2.inRange(hsv, lowerBlue, upperBlue)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # cv2.imshow('Frame-Output', mask)
    cv2.imshow('Frame-Output', res)
    # cv2.imshow('Frame-Output', hsv)
    key = cv2.waitKey(1)