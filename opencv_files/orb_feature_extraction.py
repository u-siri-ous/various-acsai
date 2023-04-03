import cv2
import numpy as np

#orb feature extraction

img = cv2.imread("opencv_files/mario.png")

orb = cv2.ORB_create(nfeatures=100)
#a lot of keypoints will be drawn if we don't limit them
#we can notice that ORB takes more values but in a smaller part of the image

keypoints, descriptors = orb.detectAndCompute(img, None)

cv2.drawKeypoints(img, keypoints, img, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#line is gradient of keypoint, when there are two it means there are two keypoints in that point
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS : For each keypoint the circle around keypoint with keypoint size and orientation will be drawn, 
                                            #size corresponds to the strength of keypoint
cv2.imshow("aaaa", img)
cv2.waitKey(0)