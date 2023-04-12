import cv2
import numpy as np



#scale invariant feature transform (SIFT)
#the surf operator is better but has been removed from opencv-contrib-python, piammale

#a feature is a relevant point in the image (corner, edge, point of color change)

img = cv2.imread("opencv_files/mario.png")

sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(img, None)

#what is none?

cv2.drawKeypoints(img, keypoints, img, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#line is gradient of keypoint, when there are two it means there are two keypoints in that point
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS : For each keypoint the circle around keypoint with keypoint size and orientation will be drawn, 
#                                             size corresponds to the strength of keypoint

cv2.imshow("aaaa", img)
cv2.waitKey(0)