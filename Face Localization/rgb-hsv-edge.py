import numpy as np
import cv2

# load image and save it as a BGR array
img_file = 'exercise-3.jpg'
img = cv2.imread(img_file, cv2.IMREAD_COLOR) # array of pixels by BGR values
# print(img)

# convert BGR to HSV color space
# step 1 of algorithm
img_1 = cv2.imread('exercise-3.jpg')
hsv = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV) # array of pixels by HSV values
# print hsv

# convert to edge map using Sobel operator
# step 2 of algorithm
sobel_edge = cv2.Sobel(img_1, cv2.CV_64F, 1, 0, ksize = 5)

cv2.imshow("image", hsv)
cv2.waitKey(0)
# cv2.destroyAllWindows("image")
