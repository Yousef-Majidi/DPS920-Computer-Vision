import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('nail_polish.jpg')

cv.imshow('image', img)

cv.waitKey(2000)

# break the image into its color channels
b, g, r = cv.split(img)

# add 100 to all channels
b = cv.add(b, 100)
g = cv.add(g, 100)
r = cv.add(r, 100)

# merge the channels back into an image
img_bright = cv.merge((b, g, r))

cv.imshow('img_bright', img_bright)
cv.imwrite('img_bright.jpg', img_bright)
cv.waitKey(200)


# multiply all channels by 1.5
b = cv.multiply(b, 1.5)
g = cv.multiply(g, 1.5)
r = cv.multiply(r, 1.5)

img_contrast = cv.merge((b, g, r))

# display in a separate window
cv.imshow('img_contrast', img_contrast)
cv.imwrite('img_contrast.jpg', img_contrast)

cv.waitKey(200)

img2 = cv.imread('cute.jpg')

# resize the image to match img
img2 = cv.resize(img2, (img.shape[1], img.shape[0]))

cv.imshow('image4', img2)

cv.waitKey(200)
# ask the user for a number between 0 and 1
alpha = float(input('Enter a number between 0 and 1: '))

# blend the two images
blend = (1 - alpha) * img + alpha * img2

# display the blended image
cv.imshow('blend', blend)
cv.imwrite('blend.jpg', blend)
cv.waitKey(200)

# convert img to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# histogram before equalization
plt.hist(hsv[:, :, 1].ravel(), 256, [0, 256])
plt.show()
cv.waitKey(200)

# apply histogram equalization to the saturation channel
hsv[:, :, 1] = cv.equalizeHist(hsv[:, :, 1])

# convert back to BGR color space
hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# show the equalized image
cv.imshow('equalized', hsv)

# histogram of the equalized image
plt.hist(hsv[:, :, 1].ravel(), 256, [0, 256])
plt.show()
cv.waitKey(200)

cv.imwrite('equalized.jpg', hsv)

cv.closeAllWindows()

