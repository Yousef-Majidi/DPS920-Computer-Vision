import cv2 as cv
import numpy as np

# open cute.jpg
img = cv.imread('cute.jpg')
#resize the image to be 10 times smaller
img = cv.resize(img, (0,0), fx=0.1, fy=0.1)
# show img
cv.imshow('cute', img)
cv.waitKey(500)

##b.	Ask for a probability value between 0 and 1 and implement the salt and pepper noise with the given probability. 
p = float(input('Enter a probability value between 0 and 1: '))
# create a copy of img
noisy_img = img.copy()
# create a noisy image using the given probability
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = np.random.rand()
        if r < p/2:
            noisy_img[i][j] = 0
        elif r < p:
            noisy_img[i][j] = 255


cv.imshow('noisy_img', noisy_img)
cv.waitKey(500)

#Smooth the above noisy image using a 3 x 3 box kernel
# create a 3x3 box kernel
kernel = np.ones((3,3), np.float32)/9
# apply the kernel to the noisy image
smoothed_img = cv.filter2D(noisy_img, -1, kernel)
# show the smoothed image
cv.imshow('smoothed_img', smoothed_img)
cv.waitKey(500)

#Filter the  noisy image using a 3 x 3 bilinear filter
# create a 3x3 bilinear kernel
bilinear_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], np.float32)/16
# apply the kernel to the noisy image
filtered_img = cv.filter2D(noisy_img, -1, bilinear_filter)
# show the filtered image
cv.imshow('filtered_img', filtered_img)
cv.waitKey(500)
# De-noise the noisy image using a 3 x 3 median filteR
# apply the median filter to the noisy image
median_filteR = cv.medianBlur(noisy_img, 3)
# show the denoised image
cv.imshow('denoised_img', median_filteR)
cv.waitKey(500)
#De-noise the noisy image using a 3x3 Gaussian filter with sigma = 1.5
# apply the Gaussian filter to the noisy image
Gaussian_filter = cv.GaussianBlur(noisy_img, (3,3), 0.5)
# show the denoised image
cv.imshow('Gaussian_filter', Gaussian_filter)
cv.imwrite('Gaussian_filter.jpg', Gaussian_filter)
cv.imwrite('denoised_img.jpg', median_filteR)
cv.imwrite('filtered_img.jpg', filtered_img)
cv.imwrite('smoothed_img.jpg', smoothed_img)
cv.imwrite('noisy_img.jpg', noisy_img)

cv.waitKey(500)

cv.destroyAllWindows()