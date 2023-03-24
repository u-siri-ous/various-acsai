import cv2
import numpy as np
#import os
'''
In this exercise, you will have to use both the homography matrix and some bitwise operators
in order to place an image of your choice over a billboard image. The latter is provided by
me, and you can find it in the same folder of this document.

You have to perform two main steps:
1 - Use the homography to match the image of your choice with the billboard (we have seen
this in class);

2 - Create a binary mask. In a binary mask, white pixels are the ones that we want in the final
image, black pixels are the ones that we do not want in the final image (think about the
example seen in class with white circle and t-rex);

3 - Use the binary mask to place the image you choose on the billboard.

Advice: you can use the function fillConvexPoly to create the white pixels in the mask.
'''
#the idea is to pinpoint the corners in which the image "mandorlo" should be in the billboard
#i can open the billboard and save those points in a numpy array (taking the snippet did in class)

#assert os.path.exists('Exercise_1/billboard.jpg')  #was given a check path integrity error
img = cv2.imread('Exercise_1/mandorlo.jpg')
bg = cv2.imread('Exercise_1/billboard.jpg')

# mandorlo 479x600
src_points = np.array([[0,0],
                       [0,479],
                       [600,479],
                       [600,0]], 
                       dtype=np.float32)

#destination points
bg_copy = bg.copy()
dst_points = []

def onClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(dst_points) < 4:
            dst_points.append([x, y])
            cv2.circle(bg_copy, (x,y), 20, (0,0,255), -1) # printing a filled circle where we clicked
            cv2.imshow("coord", bg_copy)

cv2.namedWindow("coord", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("coord", onClick)   # handle mouse event

cv2.imshow("coord", bg_copy)
cv2.waitKey(0) 

#destination points_array
#dst_points = [[308, 451], [332, 2383], [2642, 2057], [2658, 755]]

shape = (bg.shape[1], bg.shape[0])

# compute homography matrix
dst_float = np.array(dst_points, dtype=np.float32)

homography = cv2.getPerspectiveTransform(src_points, dst_float)
out = cv2.warpPerspective(img, homography, dsize=shape)     #slanted image 

#resize image to dimensions of billboard screen
mandorlo = cv2.resize(out, dsize=shape)

#create black mask on billboard for bitwise xor
masked = cv2.fillConvexPoly(bg, np.int32([dst_float]), (0,0,0)) 
      
final = cv2.bitwise_xor(masked, mandorlo)

cv2.namedWindow("final", cv2.WINDOW_KEEPRATIO)
#cv2.namedWindow("masked", cv2.WINDOW_KEEPRATIO)
cv2.imshow("final", final)
#cv2.imshow("masked", masked)
cv2.waitKey(0)