import cv2
import numpy as np

img = cv2.imread("mario.png", cv2.IMREAD_GRAYSCALE)

'''sobel operator'''
# the sobel operator needs the first partial derivatives, requires a grayscale image
# sobel uses two kernels, one for x one for y
der_x = cv2.Sobel(img, -1, 1, 0)    #1 is for axis (in order x, y), -1 maintains the same number of channels as input
der_y = cv2.Sobel(img, -1, 0, 1)    #assumes a positive derivative (pretty strong assumption, as pixels in an image are only positive)

#derivative as absolute values, scaling in the range [0,255] 
abs_x = cv2.convertScaleAbs(der_x)
abs_y = cv2.convertScaleAbs(der_y)

#get an image with both derivatives (addWeighted with same weights)
total = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

'''laplacian operator'''
# the laplacian operator needs the second partial derivatives (un sacco meglio)
# laplacian usa sobel, crea un gradiente con le derivate seconde NON miste
der = cv2.Laplacian(img, -1, ksize=3)    #ksize is kernel size, needed as laplacian is a filter
abs_der = cv2.convertScaleAbs(der)

cv2.imshow("mario", abs_der)
cv2.waitKey(0)