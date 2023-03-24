import cv2 as cv
import numpy as np

# Remember that there are differents between contourns and edges

img = cv.imread('Exercise_1/billboard.jpg')
img = cv.resize(img, dsize=(500,500), fx=0.5, fy=0.5)
cv.imshow('Cars', img)

blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
canny = cv.resize(canny, dsize=(500,500), fx=0.5, fy=0.5)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
''' Treshold tries to binarize the image:
        if the pixel is below 125 it becomes 0 (or black),
        if the pixel is above 125 it becomes 255 (or white)
'''

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
''' Contours is a python list with all the contours of the img
    Contour retrieval mode:
        RETR_LIST: All the contourns in the list
        RETR_TREE: All the hierarchical contourns
        RETR_EXTERNAL: Only the external contourns
    Contourn approximation method:
        CHAIN_APPROX_NONE: Returns all the contourns
        CHAIN_APPROX_SIMPLE: Compresses all the contourns to a single one that make sense
'''
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
blank = cv.resize(blank, dsize=(500,500), fx=0.5, fy=0.5)
cv.imshow('Contourns Drawn', blank)

cv.waitKey(0)