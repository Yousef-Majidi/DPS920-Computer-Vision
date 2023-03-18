import cv2
import os

# set the directory path
directory1 = 'positive/'
directory2 = 'negative/'
destination1 = 'data/positive/'
destination2 = 'data/negative/'

# loop through all files in the directory
for filename in os.listdir(directory1):
    if filename.endswith('.jpg'):
        
        # read the image
        img = cv2.imread(os.path.join(directory1, filename))
        
        # resize the image to 500x500
        img_resized = cv2.resize(img, (500, 200))
        #make the resized image grayscale
        img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        
        # save img_resized in the destination folder
        cv2.imwrite(os.path.join(destination1, filename), img_resized)

        cv2.waitKey(0)

for filename in os.listdir(directory2):
    if filename.endswith('.jpg'):
        
        # read the image
        img = cv2.imread(os.path.join(directory2, filename))
        print(filename)
        
        # resize the image to 500x500
        img_resized = cv2.resize(img, (400, 400))
        # make the resized image grayscale
        img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        
        # save img_resized in the destination folder
        cv2.imwrite(os.path.join(destination2, filename), img_resized)

        cv2.waitKey(0)
        
cv2.destroyAllWindows()
