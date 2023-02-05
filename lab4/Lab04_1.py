# open image nail_polish.jpg

import cv2 as cv
import numpy as np

img = cv.imread('nail_polish.jpg')
if (img is None):
    print('Error: Cannot open image')
    exit(1)

cv.imshow('Original', img)
cv.waitKey(500)

# in a loop ask user if they want to rotate, resize, or apply perspective transformation, or exit

while True:
    print('press 1 to rotate')
    print('press 2 to resize')
    print('press 3 to apply perspective transformation')
    print('press 4 to exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        # ask for an angle in degrees
        angle = int(input('Enter an angle in degrees: ')) * -1

        # rotate around th center of the image with the given angle and display the rotated image
        rows, cols, _ = img.shape
        matrix = cv.getRotationMatrix2D((cols/2, rows/2), angle, 1)
        rotated = cv.warpAffine(img, matrix, (cols, rows))
        cv.imshow('Rotated', rotated)
        cv.waitKey(1000)
        cv.destroyWindow('Rotated')

    elif choice == '2':
        # ask for a resizing factor along each axis and resize the image
        factor = float(input('Enter a resizing factor: '))
        resized = cv.resize(img, None, fx=factor, fy=factor,
                            interpolation=cv.INTER_AREA)
        cv.imshow('Resized', resized)
        cv.waitKey(1000)
        cv.destroyWindow('Resized')

    elif choice == '3':
        # apply transform with the following homography matrix and display the transformed image
        H = np.array([[0.4, -0.4, 190], [0.15, 0.4, 100], [0, 0, 1]])
        transformed = cv.warpPerspective(img, H, (img.shape[1], img.shape[0]))
        cv.imshow('Transformed', transformed)
        cv.waitKey(1000)
        cv.destroyWindow('Transformed')

    elif choice == '4':
        # exit
        break
