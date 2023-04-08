import cv2 as cv
import numpy as np
import os

# Step 1: Generate positive and negative sample lists
pos_images_dir = "positive"
neg_images_dir = "negative"
pos_list_file = "pos_list.txt"
neg_list_file = "neg_list.txt"

#display position of pos_list_file

with open(pos_list_file, "w") as f:
    for img_file in os.listdir(pos_images_dir):
        f.write(os.path.join(pos_images_dir, img_file) + " 1 " + "5 " + "5 " + "480 " + "190" "\n")

with open(neg_list_file, "w") as f:
    for img_file in os.listdir(neg_images_dir):
        f.write(os.path.join(neg_images_dir, img_file) + "\n")



# Step 2: Create a vector file
vec_file = "pos_vec.vec"
pos_samples = len(os.listdir(pos_images_dir))
width, height = 64, 64

cmd = f"opencv_createsamples -info {pos_list_file} -num {pos_samples} -w {width} -h {height} -vec {vec_file}"
os.system(cmd)

# Step 3: Train the classifier
data_dir = "data"
bg_file = "neg_list.txt"
num_pos = 56
num_neg = 340
num_stages = 9
vec_file = "pos_vec.vec"

cmd = f"opencv_traincascade -data {data_dir} -vec {vec_file} -bg {bg_file} -numPos {num_pos} -numNeg {num_neg} -numStages {num_stages}  -minHitRate {0.998} -maxFalseAlarmRate {0.3} -w {width} -h {height}  -featureType LBP"
os.system(cmd)