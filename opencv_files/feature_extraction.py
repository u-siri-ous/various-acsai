import cv2
import numpy as np

#features have, as a tuple:
#    - keypoint
#    - descriptor

#the below method is not used anymore (cornerHarris)
img = cv2.imread("opencv_files/niente.png")   #we don't need the colors to extract features
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#extract corners from images
corners = cv2.cornerHarris(gray_img, 2, 5, 0.04)    #harris uses sobel to find corners

#thresholding the corners for getting the better ones
img[corners > 0.01 * corners.max()] = [0,0,255] #just to see them better

cv2.imshow("corners!", img)
cv2.waitKey(0)