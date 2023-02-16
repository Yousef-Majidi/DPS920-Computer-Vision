import cv2 as cv

img = cv.imread("cute.jpg")
img = cv.resize(img, (0,0), fx=0.1, fy=0.1)
cv.imshow("cute",img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#3x3 Sobel filter
sobelx = cv.Sobel(gray,cv.CV_64F,1,1,ksize=3)
cv.imshow("sobelx",sobelx)

# applying a Canny edge detector.
canny = cv.Canny(gray, 100, 200)
cv.imshow("canny",canny)

cv.closeAllWindows()
