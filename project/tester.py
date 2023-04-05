import cv2 as cv

# Step 4: Test the classifier
test_image = "testpics/test1.jpg"
classifier = "data/cascade.xml"

img = cv.imread(test_image)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
classifier = cv.CascadeClassifier(classifier)
faces = classifier.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()