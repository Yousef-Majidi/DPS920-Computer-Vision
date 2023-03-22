import cv2 as cv
import time


# initialize variables
background = None
motion_detected = False
frame_count = 0
start_time = None
motion_sensitivity = 0.01

# capture video from camera
cap = cv.VideoCapture(0)

while True:
    # capture a frame from the camera
    ret, frame = cap.read()
    if ret == False:
        break

    # convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # save the first frame as background
    if background is None:
        background = gray
        continue

    # displaye te background image
    cv.imshow('Background Image', background)

    # calculate the absolute difference between the current frame and the background
    diff = cv.absdiff(background, gray)

    # show the difference image
    cv.imshow('Current Frame', diff)

    # threshold the difference image
    thresh = cv.threshold(diff, 128, 255, cv.THRESH_BINARY)[1]

    # count the number of pixels changed by at least 128 gray levels
    num_pixels_changed = cv.countNonZero(thresh)

    # if the count is larger than the motion sensitivity, then motion is detected
    if num_pixels_changed > motion_sensitivity * gray.size:
        motion_detected = True
        if start_time is None:
            start_time = time.time()

        # output the time the activity was detected
        print('Motion detected at {}'.format(
            time.strftime('%H:%M:%S', time.localtime(start_time))))
        # save the current color frame in a file (with a timestamp)
        cv.imwrite('motion_{}.jpg'.format(time.strftime(
            '%H_%M_%S', time.localtime(start_time))), frame)

    # if motion is detected, save the current frame and display the difference image
    if motion_detected:
        # display the difference image
        cv.imshow('Difference Image', thresh)

        # update the background image
        background = gray.copy()
        motion_detected = False
        frame_count = 0
        start_time = None

    # increment the frame count and wait for 5 seconds before capturing the next frame
    frame_count += 1
    if frame_count > 100:
        background = gray.copy()
        frame_count = 0
    key = cv.waitKey(5000)
    if key == 27 or key == ord('q'):
        break

# release the capture and close all windows
cap.release()
cv.destroyAllWindows()
