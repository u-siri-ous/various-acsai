import cv2
import numpy as np

""" 
the usage of convolutions! 
convolutions is a technique that involves: 
* an image 
* and a kernel (namely, 2 matrices), with weights of the convolution as the proper filter that we are applying by sliding the kernel over the image
the kernel is often odd dimensioned to find the center better

it doesn't make sense to apply a filter to an image with a transparency channel
filtering is non reversible (meaning that i cannot recover details that are simply not there)
i.e. if i have a "convoluted image" as input, there's no way to recover the original (yet)
"""
my_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

my_kernel = my_kernel / 9   # blurs image my averaging out the matrix

img = cv2.imread('opencv_files/mario.png')

filtered = cv2.filter2D(img, -1, my_kernel)    # -1 is the number of channels of image (-1 means the same number of channels as input image)
#filtered = cv2.blur(img, (10,10))     # image mat, kernel size, will blur image according to the tuple (can also be done manually with the kernel)
#filtered = cv2.GaussianBlur(img, (3,3), 10)      # 1 is std deviation, for denoising
#filtered = cv2.medianBlur()     # to reduce salt and pepper grain

#increasing image sharpness / unsharped mask technique
unsharped = cv2.addWeighted(img, 1.5, filtered, -0.5, 0)    # does an algebric sum between the two images, with defined weights (in this,
                                                            # the first image is more important, to preserve details, 0 is a "safe" gamma value

cv2.imshow("mario", filtered)
cv2.waitKey(0)