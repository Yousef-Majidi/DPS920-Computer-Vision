import cv2
import json
import csv


def calculate_iou(box1, box2, img, img_height, img_width, csv_file_path, append_to_file=True):
    gt_x, gt_y, gt_w, gt_h = box1
    dt_x, dt_y, dt_w, dt_h = box2

    # Calculate intersection coordinates
    x_inter = int(max(gt_x, dt_x))
    y_inter = int(max(gt_y, dt_y))
    w_inter = int(min(gt_x + gt_w, dt_x + dt_w) - x_inter)
    h_inter = int(min(gt_y + gt_h, dt_y + dt_h) - y_inter)

    # Draw blue bounding box around intersection
    if w_inter > 0 and h_inter > 0:
        overlay = img.copy()
        cv2.rectangle(img, (x_inter, y_inter), (x_inter + w_inter,
                      y_inter + h_inter), BLUE, -1)
        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

    # Calculate true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN)
    if w_inter > 0 and h_inter > 0:
        TP = w_inter * h_inter
        TN = img_width * img_height - (gt_w * gt_h + dt_w * dt_h - TP)
        FP = dt_w * dt_h - TP
        FN = gt_w * gt_h - TP
    else:
        TP = 0
        TN = img_width * img_height - (gt_w * gt_h + dt_w * dt_h)
        FP = dt_w * dt_h
        FN = gt_w * gt_h

    # Calculate recall (R), precision (P), and F1 score
    R = TP / (TP + FN) if (TP + FN) != 0 else 0
    P = TP / (TP + FP) if (TP + FP) != 0 else 0
    F1 = 2 * P * R / (P + R) if (P + R) != 0 else 0

    # Export the results to a CSV file
    fieldnames = ['TP', 'TN', 'FP', 'FN', 'R', 'P', 'F1']
    row = {'TP': TP, 'TN': TN, 'FP': FP, 'FN': FN, 'R': R, 'P': P, 'F1': F1}
    mode = 'a' if append_to_file else 'w'

    with open(csv_file_path, mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if mode == 'w':
            writer.writeheader()

        writer.writerow(row)


# Define colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
GRAY = (128, 128, 128)

# load the annotation file
with open('testpics/annotations.json', 'r') as f:
    annotations = json.load(f)

# Load the pre-trained Haar Cascade classifier for car detection
car_cascade = cv2.CascadeClassifier('data/cascade.xml')

for var in range(1, 30):
    # Load the image
    image = cv2.imread('testpics/testpic' + str(var) + '.jpg')

    if image is None:
        continue

    # get the coordinates of the ground truth
    reduced_x = int(annotations[var - 1]["label"][0]["x"])
    reduced_y = int(annotations[var - 1]["label"][0]["y"])
    reduced_w = int(annotations[var - 1]["label"][0]["width"])
    reduced_h = int(annotations[var - 1]["label"][0]["height"])
    original_h = int(annotations[var - 1]["label"][0]["original_height"])
    original_w = int(annotations[var - 1]["label"][0]["original_width"])

    x_ratio = original_w / 100
    y_ratio = original_h / 100

    x = reduced_x * x_ratio
    y = reduced_y * y_ratio
    w = reduced_w * x_ratio
    h = reduced_h * y_ratio

    # ground truth coordinates
    ground_truth = [x, y, w, h]

    # draw a transparent yellow rectangle around the ground truth
    overlay = image.copy()
    cv2.rectangle(overlay, (int(x), int(y)),
                  (int(x) + int(w), int(y) + int(h)), YELLOW, -1)
    cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect the car in the image using the Haar Cascade classifier
    cars = car_cascade.detectMultiScale(gray, 1.001, 5, 0, (50, 50))

   # apply non-maximum suppression to remove overlapping bounding boxes
    indices = cv2.dnn.NMSBoxes(cars, [1.0]*len(cars), 0.9, 0.01)

    # sort the indices in descending order based on the confidence scores
    indices_sorted = sorted(
        range(len(cars)), key=lambda i: cars[i][2], reverse=True)

    # draw a rectangle around the most confident car
    if len(indices_sorted) > 0:
        i = indices_sorted[0]
        (x, y, w, h) = cars[i]

    calculate_iou(ground_truth, [x, y, w, h], image,
                  original_h, original_w, 'results/results.csv', var > 1)

    # draw a green box around the detection
    cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 2)

    # Display the image with the rectangles around the cars detected
    cv2.imshow('Car Detection', image)

    # save the image as "result" + the number of the image
    cv2.imwrite('results/result' + str(var) + '.jpg', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
