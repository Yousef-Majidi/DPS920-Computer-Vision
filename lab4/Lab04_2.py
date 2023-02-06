import cv2 as cv
import numpy as np

img = cv.imread('batman.jpg')

cv.imshow('image', img)
print("provide a probability between 0 and 1")
prob = float(input())
while prob < 0 or prob > 1:
    print("provide a probability between 0 and 1")
    prob = float(input())
# add salt and pepper noise
noise = np.random.rand(img.shape[0], img.shape[1], img.shape[2])
img[noise < prob/2] = 0
img[noise > 1 - prob/2] = 255

cv.imshow('noisy', img)

# smooth the image using 3x3 box kernel
box = np.ones((3, 3), np.float32) / 9
smoothed = cv.filter2D(img, -1, box)
cv.imshow('smoothed', smoothed)

#filter the noisy image using a 3x3 bilinear filter
bilinear = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], np.float32) / 16
filtered = cv.filter2D(img, -1, bilinear)
cv.imshow('filtered', filtered)

#De-noise the noisy image using a 3x3 median filter
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#De-noise the noisy image using a 3x3 Gaussian filter 0.1
gaussian = cv.GaussianBlur(img, (3, 3), 1.5)
cv.imshow('gaussian', gaussian)


cv.waitKey(20000)