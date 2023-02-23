import cv2 as cv
import numpy as np

#open a color image and display it
img = cv.imread('nail_polish.jpg', cv.IMREAD_COLOR)
img2 = cv.imread('batman.jpg', cv.IMREAD_COLOR)

#increase brightness
#Bright = cv.add(img, 100)

#increase contrast
#Contrast = cv.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, 0)

img2 = cv.resize(img2, (img.shape[1], img.shape[0]))

#while True:
#    alpha = float(input("Enter alpha value (0-1): "))
#    if alpha >= 0 and alpha <= 1:
#        break
#    else:
#        print("Error, alpha must be between 0 and 1")

#blend = (1 - alpha) * img + alpha * img2

#convert img to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Apply histogram equalization to saturation channel
hsv[:,:,2] = cv.equalizeHist(hsv[:,:,2])

cv.imshow('image',img)
cv.imshow('hsv',hsv)
#cv.imshow('blend', blend)
#cv.imshow('Bright',Bright)
#cv.imshow('Contrast',Contrast)

cv.waitKey(0)
