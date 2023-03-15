import numpy as np
import cv2 as cv
import csv

def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou


def get_iou(alg_file, gt_file):
    try:
        with open(alg_file, 'r') as file:
            reader = csv.reader(file)
            alg = list(reader)
        with open(gt_file, 'r') as file:
            reader = csv.reader(file)
            gt = list(reader)
        if len(alg) != len(gt):
            print(len(alg), len(gt))
            return "Error: Number of rows in both files must be equal."
        iou = 0
        for i in range(len(alg)):
            alg_bb = [int(alg[i][1]), int(alg[i][2]), int(alg[i][1]) + int(alg[i][3]), int(alg[i][2]) + int(alg[i][4])]
            gt_bb = [int(gt[i][1]), int(gt[i][2]), int(gt[i][1]) + int(gt[i][3]), int(gt[i][2]) + int(gt[i][4])]
            iou += bb_intersection_over_union(alg_bb, gt_bb)
        return iou / len(alg)
    except:
        return "Error!"
    
print(get_iou('detections.csv', 'gt.csv'))