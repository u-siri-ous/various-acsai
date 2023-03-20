import cv2
import numpy as np

# the usage of convolutions! 
my_kernel = np.array([
    [1,0,1],
    [1,0,1],
    [1,0,1]
])

img = cv2.imread('mario.png')

filtered = cv2.filter2D(img, -1, my_kernel)    # -1 is the number of channels of image (-1 means the same number of channels as input image)
#filtered = cv2.blur(img, (10,10))     # image mat, kernel size, will blur image

cv2.imshow("mario", filtered)
cv2.waitKey(0)