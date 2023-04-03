import cv2
import numpy as np

img = cv2.imread("opencv_files/mario.png")

akaze = cv2.AKAZE_create()
keypoints, descriptors = akaze.detectAndCompute(img, None)

cv2.drawKeypoints(img, keypoints, img, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#line is gradient of keypoint, when there are two it means there are two keypoints in that point
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS : For each keypoint the circle around keypoint with keypoint size and orientation will be drawn, 
#                                             size corresponds to the strength of keypoint
cv2.imshow("aaaa", img)
cv2.waitKey(0)