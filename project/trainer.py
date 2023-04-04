import cv2 as cv
import numpy as np
import os

# Step 1: Generate positive and negative sample lists
pos_images_dir = "./positive"
neg_images_dir = "./negative"
pos_list_file = "./pos_list.txt"
neg_list_file = "./neg_list.txt"

with open(pos_list_file, "w") as f:
    for img_file in os.listdir(pos_images_dir):
        f.write(os.path.join(pos_images_dir, img_file) + "\n")

with open(neg_list_file, "w") as f:
    for img_file in os.listdir(neg_images_dir):
        f.write(os.path.join(neg_images_dir, img_file) + "\n")

# Step 2: Create a vector file
vec_file = "./pos_vec.vec"
pos_samples = len(os.listdir(pos_images_dir))
width, height = 64, 64

cmd = f"opencv_createsamples -info {pos_list_file} -num {pos_samples} -w {width} -h {height} -vec {vec_file}"
os.system(cmd)