""" import cv2
import numpy as np

img = cv2.imread("doggo.png")

#convert image to grayscale
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#how about videos?
cap = cv2.VideoCapture(0) #to capture from pc webcam

#extract and capture frames
while True:
    img = cap.read()[1]

    #denoise image - tab for video, detab and decomment img_gray
    img_gray = cv2.medianBlur(img_gray, 5)#img_gray = cv2.medianBlur(img_gray, 5)

    #extract edges (laplacian operator)
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5) #output is 8-bit unsigned

    #thresholding - set threshold for binary mask basically
    _, threshold = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV) #inverse threshold

    #get the color with bilateral filter - performs a gaussian blur on an image, preserving the edges "inside" the image
    color_img = cv2.bilateralFilter(img, 10, 250, 250)

    #merge color and edges - convert to trichannel image
    skt = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)

    sketch_img = cv2.bitwise_and(color_img, skt)

    cv2.imshow("cartoon!", sketch_img)
    k = cv2.waitKey(4)  #get pressed key and check to quit

    if k == ord('q'):
        break """

import cv2
import numpy as np



#load the image to cartonize
#img = cv2.imread("meme.png")
cap = cv2.VideoCapture(0)

while(True):

	#read the current frame
	img = cap.read()[1]

	#convert image to grayscale
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#apply median blur to remove noise
	img_gray = cv2.medianBlur(img_gray,5)

	#extract the edges with Laplacian Operator
	edges = cv2.Laplacian(img_gray, cv2.CV_8U,ksize=5)

	#threshholding the edges
	_, thresholded = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)

	#get the colors with the bilateral filter
	color_img = cv2.bilateralFilter(img,10,250,250)

	#merge color and edges
	skt = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)
	sketch_img = cv2.bitwise_and(color_img,skt)

	cv2.imshow("cartoon!", sketch_img)
	k = cv2.waitKey(4)
	if k == ord("q"):
		break