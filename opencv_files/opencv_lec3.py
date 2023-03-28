import cv2
import numpy as np

#lecture 3 on opencv
#canvas = np.zeors((500,500,3), dtype='uint8')       #blank image in bgr format
                                                    #if channels are omitted, just the first value of the color tuple 

#alternative to imshow is matplotlib, which will show images in rgb, so convert to bgr with .cvtColor(image, cv2.COLOR_BGR2RGB)

img = cv2.imread('opencv_files/doggo.png', cv2.IMREAD_UNCHANGED)     #second argument will not drop the fourth channel in case of transparency if <0
                                                        #analogous to cv2.IMREAD_UNCHANGED 
                                                        #(https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html)

#adding transparency/transparency elements
t_img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)           #creates fourth channel if it doesn't exist

cv2.imshow("doggo", t_img)
cv2.waitKey(0)
'''
alternative method: create the channel manually and stack it (iff the channels aren't already 4)

alpha = np.full((img.shape[0],img.shape[1]), fill_value=255, dtype='uint8') the channel needs to have the same dimension as the starting picture
255 means no transparency

t_img = np.dstack([img,alpha])

if the layer is created with np.zeros(), the image will be all transparent, so pay attention
'''