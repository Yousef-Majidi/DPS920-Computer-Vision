import cv2 as cv
import time 
PINK = [174,55,255]

# Start a video capture, using device's camera
cap = cv.VideoCapture(0)

# Check if video file opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print("Frame width: " , frame_width)
print("Frame height: " , frame_height)

snapshotCount = 0
# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
   
    # Display the frame
    cv.imshow('frame',frame)
    key = cv.waitKey(25)

    # calculate frames per second
    fps = cap.get(cv.CAP_PROP_FPS)
    print("Frames per second: {0}".format(fps))

    # Press Q or ESC on keyboard to exit
    if key%256 == ord('q') or key%256 == 27:
        break
    
   
    
    # press x on keyboard to take a screenshot. crops and adds border to the screenshot and saves it.
    elif key & 0xFF == ord('x'):
        
        snapshotName = "image{}.jpeg".format(snapshotCount)
        croppedFrame = frame[30:690, 30:1250]
        color = [54, 54, 171]
        paddedFrame = cv.copyMakeBorder(croppedFrame, 50,50, 50, 50, cv.BORDER_CONSTANT,value=color)
        cv.imwrite(snapshotName, paddedFrame)
        print(snapshotName+" created!")
        img = cv.imread(snapshotName, 1)
        cv.imshow('image', img)
        cv.waitKey(3000)
        cv.destroyWindow('image')
        print('window destroyed')
        snapshotCount+=1

          
        


# Release the video capture 
cap.release()

# close all window frames
cv.destroyAllWindows()
