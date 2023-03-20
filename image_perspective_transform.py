import cv2
import numpy as np
'''
notes, right code is in image_perspective_transform
in the case of a perspective transformation, we have a 3x3 matrix
referred to as homography matrix

a1 a2 tx
a3 a4 ty
w1 w2 1

why should we use it? we have two more "degrees of freedom" to modify the image (as opposed to affine : rotate, scale, shear)

we have two sets of point and we should match the start and destination point and estimate the translation matrix
affine: 6 deg - 3 pairs of points (no more than)
perspective: 8 deg - 4 pairs of points (at least)
'''
img = cv2.imread('scan_input/gerry.png')

# taking corners set as start (sheet corners)
# the format is column, row
""" src_points = np.array([ #counterclockwise corners in float32
    [28,227],
    [131,987],
    [730,860],
    [572,149]
], dtype=np.float32) """

# what if i don't know the corners i want? we get the corners by clicking on the image (molto più figo)

# callback = function called each time the mouse is pressed on the image
src_points = []
img_copy = img.copy()

def onClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # check if i have the 4 corners already, if not i add it on the array
        if len(src_points) < 4:
            src_points.append([x, y])
            cv2.circle(img_copy, (x,y), 10, (0,0,255), -1) # printing a filled circle where we clicked
            cv2.imshow("sei stato scottato", img_copy)

# destination points (should match the order of start points), need same aspect ratio tho
dst_points = np.array([
    [0,0],
    [0,800],
    [600,800],
    [600, 0]
], dtype=np.float32)

cv2.namedWindow("sei stato scottato", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("sei stato scottato", onClick)   # handle mouse event

cv2.imshow("sei stato scottato", img_copy)
cv2.waitKey(0)

# compute homography matrix
src_float = np.array(src_points, dtype=np.float32)
H = cv2.getPerspectiveTransform(src_float, dst_points)

# apply to image
out_img = cv2.warpPerspective(img, H, (600,800))

# create a window to display the 4 corners, and one for output
cv2.namedWindow("sei stato scottato, ma meglio", cv2.WINDOW_KEEPRATIO)

cv2.imshow('sei stato scottato', img)
cv2.imshow('sei stato scottato, ma meglio', out_img) 

cv2.waitKey(0)