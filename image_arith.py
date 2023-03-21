import cv2
import numpy as np

#the image is a matrix, so it only makes sense if we define an arithmeyic to operate with them
img = cv2.imread('mario.png')
#img2 = cv2.imread('doggo.png')     #for blending
img2 = np.zeros(img.shape, dtype=np.uint8)   #for bitwise operators

resized = cv2.resize(img2, (img.shape[1], img.shape[0]))    #to blend images we need them to be of the same dimension, also for bitwise operators

masked = cv2.circle(img2, (200,100), 50, (255,255,255), -1)

x = np.uint8([250])
y = np.uint8([50])

res_cv2 = cv2.add(x,y)  #will clip value at 255 as it's the maximum
res_np = x + y  #or np.add(x,y), once we've reached 255, it overflows starting back from 0

#create a new matrix of same dimension, and sum the two matrices or use a scalar notation
M = np.full(img.shape, 50, dtype=np.uint8)  #each value in M is 50
#instead of creating the whole matrix, we are able to obtain the same result with a single pixel (1,3) (broadcasting) 
#one dimension must be concorde (in this, the depth), and the pixel will behave as a scalar

added = cv2.add(img, M)     #makes brighter image, use cv2.subtract(img, M) to make it darker

#blend images (commented sennò rompe)
#blend = cv2.addWeighted(img, 0.5, resized, 0.5, 0)

#bitwise operators (logic gates)
and_img = cv2.bitwise_and(img, masked)      #displays what's inside the circle (white=1, black=0)
or_img = cv2.bitwise_or(img, masked)        #displays both
xor_img = cv2.bitwise_xor(img, masked)      #displays the circle in negative
not_img = cv2.bitwise_not(img, masked)      #displays negative image (will invert both is second argument is given)

cv2.imshow("diff", xor_img)
cv2.waitKey(0)