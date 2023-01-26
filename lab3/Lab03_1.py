# open nail_polish.jpg and display it

import cv2 as cv
import numpy as np

# read image
img = cv.imread('nail_polish.jpg')

# display image
cv.imshow('image', img)