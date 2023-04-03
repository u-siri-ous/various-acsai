import cv2
import numpy as np

img1 = cv2.imread("panorama/left.png")
img2 = cv2.imread("panorama/right.png")

#1 - extract the features from both images (we use orb as the images are not that different in terms of rotation)
orb = cv2.ORB_create()

#2 - we compute keypoints, feature match and filter the images
kpts1, des1 = orb.detectAndCompute(img1, None)
kpts2, des2 = orb.detectAndCompute(img2, None)

# we use knn (not done yet in ml)
# we pick the k nearest points and see their class to classify the keypoint
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)   #bruteforce matcher using hamming distance
matches = matcher.knnMatch(des1, des2, k=2) #match the points through knn, k is arbitrary

# ratio test: the prob that a match is correct is determined by computing the ratio of the distance from the closest neighborhood 
#             with the distance of the second closest neighborhood
good_matches = []
for n,m in matches:
    if m.distance < 0.03*n.distance:
        good_matches.append(m)

# we need to check if we have 4 points for homography
if len(good_matches) >= 4:

#3 - convert and compute homography
    src_points = np.float32([kpts1[m.queryIdx].pt for m in good_matches])
    dst_points = np.float32([kpts2[m.trainIdx].pt for m in good_matches])

    M, mask = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)    #fct used for more than 4 points, ransac removes the unmatched points

#4 - put images together
    dst_img = cv2.warpPerspective(img1, M, (img1.shape[1]+img2.shape[1], img1.shape[0]+img2.shape[0]))
    dst_img[0:img2.shape[0], 0:img2.shape[1]] = img2.copy()

    cv2.namedWindow("panorama", cv2.WINDOW_KEEPRATIO)
    cv2.imshow("panorama", dst_img)
    cv2.waitKey(0)

#non funziona mannaggina mannaggetta