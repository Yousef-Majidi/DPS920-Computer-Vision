import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
sx,sy = -1,-1
color = (0,255,255)

 
# mouse callback function
def draw_circle(event,x,y,flags,param):
    
    
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
            else:
                cv.circle(img,(x,y),5,(0,0,255),2)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        else:
            cv.circle(img,(x,y),5,(0,0,255),2)
            
def polyLine(event, x, y, flags, param):
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


img = np.zeros((512,512,3), np.uint8)

cv.namedWindow('image')
cv.setMouseCallback('image',polyLine)
while(1):
    cv.imshow('image',img)        
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