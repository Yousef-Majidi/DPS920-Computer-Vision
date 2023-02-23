import cv2 as cv
import numpy as np

cv.ocl.setUseOpenCL(False)
img1 = cv.imread('Trillium_s.jpg',0) # query
img2 = cv.imread('Trillium_t.jpg',0) # template

w, h = img2.shape[::-1]

copy1 = img1.copy()
copy2 = img1.copy()
copy3 = img1.copy()

res = cv.matchTemplate(copy1,img2, cv.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(copy1,top_left, bottom_right, 255, 2)
cv.imshow('Trillium template',img2)
cv.imshow('Trillium',copy1)
cv.waitKey(10000)


res = cv.matchTemplate(copy2,img2, cv.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(copy2,top_left, bottom_right, 255, 2)
cv.imshow('Trillium template 2',img2)
cv.imshow('Trillium2',copy2)
cv.waitKey(10000)


copy3 = cv.resize(copy3, (0,0), fx=2, fy=2)
rows,cols = copy3.shape
M = cv.getRotationMatrix2D((cols/2,rows/2),30,1)
copy3 = cv.warpAffine(copy3,M,(cols,rows))
res = cv.matchTemplate(copy3,img2, cv.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(copy3,top_left, bottom_right, 255, 2)
cv.imshow('Trillium template 3',img2)
cv.imshow('Trillium3',copy3)
cv.waitKey(10000)

cv.destroyAllWindows()
