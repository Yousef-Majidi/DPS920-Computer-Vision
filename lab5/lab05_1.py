import cv2 as cv
import numpy as np

#open the image
img = cv.imread('batman.jpg', cv.IMREAD_GRAYSCALE)

#find edges using sobel 3x3
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobelx2 = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobelx3 = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=3)

#fins edges using canny edge detection  
canny = cv.Canny(img, 100, 200)


#close the image
cv.imshow('image', img)
cv.imshow('sobelx', sobelx)
cv.imshow('sobelx2', sobelx2)
cv.imshow('sobelx3', sobelx3)
cv.imshow('canny', canny)
cv.waitKey(0)
cv.destroyAllWindows()
