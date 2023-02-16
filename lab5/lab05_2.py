import cv2 as cv
import numpy as np

#open the image



#use houghcircles to find circles in the image


def drawLines(canny, img, threshold):
    
    lines = cv.HoughLinesP(canny, 1, np.pi/180, threshold, minLineLength=10, maxLineGap=250)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)



def drawCircles(blur,img, minRadius, maxRadius):
    circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1, img.shape[0]/64, param1=200, param2=10, minRadius=minRadius, maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(img,(i[0],i[1]),2,(0,0,255),3)

#while x is not pressed keep asking for input
batman = cv.imread('batman.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('image', batman)
print("Press 'l' to find lines in the building image")
print("Press 'c' to find circles in the coin image")
print("Press 'x' to exit")
while cv.waitKey(1) != ord('x'):
    if cv.waitKey(1) == ord('l'):
        building = cv.imread('Building.jpeg', cv.IMREAD_GRAYSCALE)
        canny = cv.Canny(building, 50, 200)
        threshold = int(input("Enter threshold: "))
        drawLines(canny, building, threshold)
        cv.imshow('LineBuilding', building)
        ## destroy the window after 15 seconds
        cv.waitKey(15000)
        cv.destroyWindow('LineBuilding')
    if cv.waitKey(1) == ord('c'):
        coin = cv.imread('Coins.jpeg', cv.IMREAD_COLOR)
        gray = cv.cvtColor(coin, cv.COLOR_BGR2GRAY)
        blur = cv.medianBlur(gray, 5)
        minRadius = int(input("Enter minRadius: "))
        maxRadius = int(input("Enter maxRadius: "))
        drawCircles(blur, coin, minRadius, maxRadius)
        cv.imshow('CircleCoin', coin)
        ## destroy the window after 15 seconds
        cv.waitKey(15000)
        cv.destroyWindow('CircleCoin')

cv.destroyAllWindows()

