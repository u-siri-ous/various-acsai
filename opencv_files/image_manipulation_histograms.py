import cv2
import numpy as np

img_c = cv2.imread("opencv_files/niente.png")

#we can adjust our image using histograms (example on grayscale image)
gray_img = cv2.cvtColor(img_c, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray_img)  #by doing this we COULD get some more information

#same thing but on color image
channels = cv2.split(img_c)
eq_channels = []

for ch in channels:
    eq_channels.append(cv2.equalizeHist(ch))    #insomma fa cagare

eq_img = cv2.merge(eq_channels)

#what if we just want to change one thing of the image (e.g., contrast)?
#we use other colorspaces, in this example, HSV (Hue Saturation Value)
hsv_img = cv2.cvtColor(img_c, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_img)

#equalize across one of the channels: value - brightness
eq_v = cv2.equalizeHist(v)
eq_img = cv2.merge([h,s,eq_v])

eq_img = cv2.cvtColor(eq_img, cv2.COLOR_HSV2BGR)    #we obtain a "sharper image" in this case

#beware, sometimes the hist does not add to the image, it rather takes off info
#look up clahe
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))  #2 is clip limit, limits the way in which you spread the values
equalized = clahe.apply(gray_img)

cv2.imshow("original", gray_img)
cv2.imshow("equalized", equalized)
cv2.waitKey(0)