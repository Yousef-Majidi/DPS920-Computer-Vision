import cv2 as cv
import numpy as np

ix, iy = -1, -1
ix,iy,sx,sy = -1,-1,-1,-1
color = (0, 0, 255)

def draw_circle(event, x, y, flags, param):
    global ix, iy, sx, sy, color
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, color, -1)
        if ix != -1:
            cv.line(img, (ix, iy), (x, y), color, 2, cv.LINE_AA)
        else:
            sx, sy = x, y
        ix, iy = x, y
    elif event == cv.EVENT_RBUTTONDOWN:
        print('Right button')
        ix, iy = -1 , -1
        cv.line(img, (x, y), (sx, sy), color, 2, cv.LINE_AA)




img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
    
while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if  k == 27:
       break
    elif k == ord('r'):
        color = (0, 0, 255)
    elif k == ord('w'):
        color = (255, 255, 255)
    elif k == ord('g'):
        color = (0, 255, 0)
    elif k == ord('y'):
        color = (0, 255, 255)
    elif k == ord('x'):
        cv.imwrite('image.jpg', img)
        print('Image saved')



cv.destroyAllWindows()
