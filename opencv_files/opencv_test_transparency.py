import cv2
import numpy as np

img = cv2.imread('opencv_files/img.jpg', cv2.IMREAD_UNCHANGED)     #second argument will not drop the fourth channel in case of transparency if <0
                                                        #analogous to cv2.IMREAD_UNCHANGED 
                                                        #(https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html)

#adding transparency/transparency elements
#t_img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)           #creates fourth channel if it doesn't exist

alpha = np.full((img.shape[0],img.shape[1]), fill_value=150, dtype='uint8')       #or np.zeros
t_img = np.dstack([img,alpha])

cv2.imwrite("opencv_files/niente.png", t_img)        #this is fully transparent with fill_value=0 and opaque with fill_value=255