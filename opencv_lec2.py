import cv2
import numpy as np

img = cv2.imread('img.jpg')
#cv2.imshow('title', img)
cv2.waitKey(1000)                       #milliseconds to close image, 0 means keep open until kbhit
print(img.shape[2])                     #shape[0] rows, shape[1] columns
#cv2.imwrite('facaldo.png', img)        #cose dell'altra volta

(b,g,r) = img[0,0]                      #inside each i store the value of each channel of pixel at (0,0)
print(b,g,r)                            #opencv uses BGR, not RGB

""" a = img[0,0]
cv2.imshow('pixelino', a)
cv2.waitKey() """

#changing the color of a portion of the image
#corner = img[0:100,0:100]  doesn't work as lists are passed by reference
img[0:100,0:100] = (0,0,255)            #what if i want to change the image permanently?
#cv2.imshow("title", img)
#cv2.waitKey(0)

#how to: create a black picture
canvas = np.zeros((500,500,3), dtype='uint8')       #an rgb (3 channel) 500x500 image, unsigned int, to create grayscale, remove the number of channels
                                                    #in a grayscale image, color are just ann int from 0 to 255 (as opposed to a triple (b,g,r)) 

#how to: draw a line in the picture
green = (0,255,0)
cv2.line(canvas, (0,0), (500,500), green)

#how to: draw a rectangle/square in the picture
red = (0,0,255)
cv2.rectangle(canvas, (50,50), (200,200), red)          #create unfilled square
cv2.rectangle(canvas, (200,200), (300,300), red, -1)    #create filled square (with negative thickness)
                                                        #positive thickness changes lines individually

#how to: draw a circle in the picture
blue = (255,0,0)
cv2.circle(canvas, (350,350), 50, blue)                 #create unfilled circle with center (350,350) and radius 50
cv2.circle(canvas, (30,30), 20, blue, -1)               #create filled circle with center (30,30) and radius 20

cv2.imshow("title", canvas)
cv2.waitKey(0)

