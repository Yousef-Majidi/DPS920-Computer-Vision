import cv2 as cv
import time
import numpy as np

# initialize variables
background = None
motion_detected = False
frame_count = 0
start_time = None
motion_sensitivity = 0.01

# capture video from camera
cap = cv.VideoCapture(0)

# set parameters for Farneback optical flow algorithm
pyr_scale = 0.5
levels = 3
winsize = 15
iterations = 3
poly_n = 5
poly_sigma = 1.1
flags = cv.OPTFLOW_FARNEBACK_GAUSSIAN

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

    # calculate dense optical flow
    flow = cv.calcOpticalFlowFarneback(
        background, gray, None, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags)

    # calculate the magnitude of the flow vectors
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])

    # threshold the magnitude to count significant flow vectors
    mag_threshold = (mag > 20)

    # calculate the percentage of significant flow vectors
    percent = mag_threshold.sum() / (gray.shape[0] * gray.shape[1])

    # display the motion vectors
    hsv = np.zeros_like(frame)
    hsv[..., 1] = 255
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
    rgb = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    cv.imshow('Motion Vectors', rgb)

    if percent > motion_sensitivity:
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
        motion_detected = False
        frame_count = 0
        start_time = None

    # increment the frame count and wait for 5 seconds before capturing the next frame
    frame_count += 1
    if frame_count > 100:
        background = gray.copy()
        frame_count = 0

    # update the background image
    background = gray.copy()

    key = cv.waitKey(1)
    if key == 27 or key == ord('q'):
        break

# release the capture and close all windows
cap.release()
cv.destroyAllWindows()
