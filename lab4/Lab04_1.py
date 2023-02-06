import cv2 as cv
import numpy as np

#open image
img = cv.imread('batman.jpg')

cv.imshow('image', img)

#ask user for input
print('Do you want to resize the image (s), rotate (r), apply perspective transformation (p), or exit? (x)')
key = cv.waitKey(0)
while key != ord('x'):
    if key == ord('s'):
        #resize image
        print('Enter the x scale factor (0.5, 1, 2, etc.)')
        Xscale = float(input())
        print('Enter the y scale factor (0.5, 1, 2, etc.)')
        Yscale = float(input())
        resized = cv.resize(img, None, fx=Xscale, fy=Yscale, interpolation=cv.INTER_LINEAR)
        cv.imshow('resized', resized)
        ## destroy the window after 20 seconds
        cv.waitKey(20000)
        cv.destroyWindow('resized')
        print('Do you want to resize the image (s), rotate (r), apply perspective transformation (p), or exit? (x)')
    elif key == ord('r'):
        #rotate image
        print('Enter the angle of rotation (0, 90, 180, 270, etc.)')
        angle = int(input())
        rows, cols, ch = img.shape
        M = cv.getRotationMatrix2D((cols/2, rows/2), angle, 1)
        rotated = cv.warpAffine(img, M, (cols, rows))
        cv.imshow('rotated', rotated)
        cv.waitKey(20000)
        cv.destroyWindow('rotated')
        print('Do you want to resize the image (s), rotate (r), apply perspective transformation (p), or exit? (x)')
    elif key == ord('p'):
        #apply perspective transformation
        H = np.array([[0.4, -0.4, 190], [0.15, 0.4, 100], [0, 0, 1]])
        transformed = cv.warpPerspective(img, H, (img.shape[1], img.shape[0]))
        cv.imshow('transformed', transformed)
        cv.waitKey(20000)
        cv.destroyWindow('transformed')
        print('Do you want to resize the image (s), rotate (r), apply perspective transformation (p), or exit? (x)')
    else:
        print('Invalid input')
    print('Do you want to resize the image (s), rotate (r), apply perspective transformation (p), or exit? (x)')
    key = cv.waitKey(0)


