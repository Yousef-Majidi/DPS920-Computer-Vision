import cv2
import numpy as np

# Load the pre-trained Haar Cascade classifier for car detection
car_cascade = cv2.CascadeClassifier('data/cascade.xml')

for var in range(1, 30):
    # Load the image
    image = cv2.imread('testpics/test' + str(var) + '.jpg')

    if image is None:
        continue

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect the car in the image using the Haar Cascade classifier
    cars = car_cascade.detectMultiScale(gray, 1.001, 5, 0, (50, 50))

    # print the number of cars detected
    print('Number of cars detected: ' + str(len(cars)))

   # apply non-maximum suppression to remove overlapping bounding boxes
    indices = cv2.dnn.NMSBoxes(cars, [1.0]*len(cars), 0.9, 0.01)

    # sort the indices in descending order based on the confidence scores
    indices_sorted = sorted(
        range(len(cars)), key=lambda i: cars[i][2], reverse=True)

    # draw a rectangle around the most confident car
    if len(indices_sorted) > 0:
        i = indices_sorted[0]
        (x, y, w, h) = cars[i]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with the rectangles around the cars detected
    cv2.imshow('Car Detection', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
