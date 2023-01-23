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

counter = 0
# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
   
    # Display the frame
    cv.imshow('frame',frame)
    key = cv.waitKey(25)
    

    # Press Q or ESC on keyboard to exit
    if key%256 == ord('q') or key%256 == 27:
        break
    
   
    
    # press x on keyboard to take a screenshot. crops and adds border to the screenshot and saves it.
    if key & 0xFF == ord('x'):
        
        img = f'image{counter}.png'
        modified_img = frame[30 : 360, 30 : 640 ]
        modified_img= cv.copyMakeBorder(modified_img,50,50,50,50,cv.BORDER_CONSTANT,value=PINK)
        cv.imwrite(img, modified_img) 

        read_img = cv.imread(img)
        cv.namedWindow(img)
        cv.imshow(img, read_img)
        time.sleep(1)
        cv.destroyWindow(img)
        counter += 1

          
        


# Release the video capture 
cap.release()
