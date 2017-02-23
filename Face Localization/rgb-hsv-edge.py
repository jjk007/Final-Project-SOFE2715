import numpy as np
import cv2

# load image and save it as a BGR array
img_file = 'exercise-3.jpg'
img = cv2.imread(img_file, cv2.IMREAD_COLOR) # array of pixels represented by BGR values
print(img)

# convert BGR to HSV color space
# step 1 of algorithm
img_1 = cv2.imread('exercise-3.jpg')
hsv = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV) # array of pixels represented by HSV values

# convert to edge map using Sobel operator
# step 2 of algorithm
sobel_edge = cv2.Sobel(img_1, cv2.CV_64, 1, 0, ksize = 5)
