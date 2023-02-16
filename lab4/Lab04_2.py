import cv2 as cv
import numpy as np

img = cv.imread('cute.jpg')

img = cv.resize(img, (0,0), fx=0.1, fy=0.1)
# show img
cv.imshow('cute', img)
cv.waitKey(500)

p = float(input('Enter a probability value between 0 and 1: '))

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

i = int(input('Enter a row number: '))
j = int(input('Enter a column number: '))
print('The pixel value at ({}, {}) is {}'.format(i, j, noisy_img[i][j][0]))
print('The pixel value at ({}, {}) is {}'.format(i-1, j-1, noisy_img[i-1][j-1][0]))
print('The pixel value at ({}, {}) is {}'.format(i-1, j, noisy_img[i-1][j][0]))
print('The pixel value at ({}, {}) is {}'.format(i-1, j+1, noisy_img[i-1][j+1][0]))
print('The pixel value at ({}, {}) is {}'.format(i, j-1, noisy_img[i][j-1][0]))
print('The pixel value at ({}, {}) is {}'.format(i, j+1, noisy_img[i][j+1][0]))
print('The pixel value at ({}, {}) is {}'.format(i+1, j-1, noisy_img[i+1][j-1][0]))
print('The pixel value at ({}, {}) is {}'.format(i+1, j, noisy_img[i+1][j][0]))
print('The pixel value at ({}, {}) is {}'.format(i+1, j+1, noisy_img[i+1][j+1][0]))


# create a 3x3 box kernel
kernel = np.ones((3,3), np.float32)/9

smoothed_img = cv.filter2D(noisy_img, -1, kernel)

print('Smoothed, The pixel value at ({}, {}) is {}'.format(i, j, smoothed_img[i][j][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i-1, j-1, smoothed_img[i-1][j-1][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i-1, j, smoothed_img[i-1][j][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i-1, j+1, smoothed_img[i-1][j+1][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i, j-1, smoothed_img[i][j-1][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i, j+1, smoothed_img[i][j+1][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i+1, j-1, smoothed_img[i+1][j-1][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i+1, j,   smoothed_img[i+1][j][0]))
print('Smoothed, The pixel value at ({}, {}) is {}'.format(i+1, j+1, smoothed_img[i+1][j+1][0]))

cv.imshow('smoothed_img', smoothed_img)
cv.waitKey(500)

# create a 3x3 bilinear kernel
bilinear_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], np.float32)/16

filtered_img = cv.filter2D(noisy_img, -1, bilinear_filter)

cv.imshow('filtered_img', filtered_img)
cv.waitKey(500)

# apply the median filter to the noisy image
median_filteR = cv.medianBlur(noisy_img, 3)
# show the denoised image
cv.imshow('denoised_img', median_filteR)
cv.waitKey(500)

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
