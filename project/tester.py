import cv2 as cv

# Step 4: Test the classifier
test_image = "testpics/test1.jpg"
classifier = "data/cascade.xml"

img = cv.imread(test_image)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
classifier = cv.CascadeClassifier(classifier)
cars = classifier.detectMultiScale(gray, 2.9, 1)

for (x, y, w, h) in cars:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


cv.imshow("Car Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()