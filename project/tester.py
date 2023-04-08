import cv2

# Load the pre-trained Haar Cascade classifier for car detection
car_cascade = cv2.CascadeClassifier('data/cascade.xml')

for var in range(1, 30):
    # Load the image
    image = cv2.imread('testpics/test' + str(var) + '.jpg')

    image = cv2.resize(image, (300, 170))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cars in the image using the Haar Cascade classifier
    cars = car_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    # Draw rectangles around the cars detected in the image
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with the rectangles around the cars detected
    cv2.imshow('Car Detection', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
