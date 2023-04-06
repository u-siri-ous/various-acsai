import cv2
import numpy as np

#features have, as a tuple:
#    - keypoint
#    - descriptor

#the below method is not used anymore (cornerHarris)
img = cv2.imread("opencv_files/mario.png")   #we don't need the colors to extract features
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create a downscale image
resized = cv2.resize(img, None, fx=0.5, fy=0.5)
gray_img = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)


#extract corners and edges from images
corners = cv2.cornerHarris(gray_img, 2, 11, 0.04)    #harris uses sobel (gradient) to find corners and edges
#why odd value - we need center

#thresholding the corners for getting the better ones
resized[corners > 0.001 * corners.max()] = [0,255,0] #just to see them better

cv2.imshow("corners!", resized)
cv2.waitKey(0)