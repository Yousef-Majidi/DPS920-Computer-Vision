import cv2 as cv
import numpy as np

# Read image
im_s = cv.imread("Trillium_s.jpg")
im_t = cv.imread("Trillium_t.jpg")

#rotate im_t by 30 degrees counter-clockwise 
rows,cols = im_t.shape[:2]
M = cv.getRotationMatrix2D((cols/2,rows/2),30,1)
im_t = cv.warpAffine(im_t,M,(cols,rows))


# detect orb features using BFMatcher
orb = cv.ORB_create()
kp_s, des_s = orb.detectAndCompute(im_s, None)
kp_t, des_t = orb.detectAndCompute(im_t, None)
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des_s, des_t)
matches = sorted(matches, key = lambda x:x.distance)

#show top 10 matches
im_matches = cv.drawMatches(im_s, kp_s, im_t, kp_t, matches[:10], None, flags=2)
cv.imshow("matches", im_matches)
cv.waitKey(0)

# detect orb features using FLANN without crossCheck
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,table_number = 6,key_size = 12,multi_probe_level = 1)
search_params = dict(checks=50)
flann = cv.FlannBasedMatcher(index_params,search_params)
matches2 = flann.knnMatch(des_s,des_t,k=2)

#show top 10 matches
im_matches2 = cv.drawMatchesKnn(im_s, kp_s, im_t, kp_t, matches2[:10], None, flags=2)
cv.imshow("matchesFLANN", im_matches2)
cv.waitKey(0)



