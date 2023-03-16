import dlib
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import imutils

import csv
path = 'faces/'
list_file = 'list.csv'
alg_file = 'detections.csv'

frontalface_detector = dlib.get_frontal_face_detector()

def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def detect_face(image_path):
    try:
        image = cv.imread(image_path)
        image = imutils.resize(image, width=600)
        rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        rects = frontalface_detector(rgb, 1)

        if len(rects) < 1:
            return "No Face Detected."

        with open(alg_file, 'a', newline='') as file:
            writer = csv.writer(file)
            for (i, rect) in enumerate(rects):
                (x, y, w, h) = rect_to_bb(rect)
                cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)          
                writer.writerow([image_path, x, y, w, h])

        plt.imshow(image, interpolation='nearest')
        plt.axis('off')
        plt.show()
    except:
        return "Error!"


with open(list_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(path + '/' + row[0])
        detect_face(path + '/'+ row[0])


