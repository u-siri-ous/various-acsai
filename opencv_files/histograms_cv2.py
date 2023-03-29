import cv2
import numpy as np
import matplotlib.pyplot as plt

#plot the histogram of a grayscale image
img_g = cv2.imread("opencv_files/niente.png", cv2.IMREAD_GRAYSCALE)

hist_g = cv2.calcHist([img_g], [0], None, [256], [0, 255])   #none is passed to calculate histogram of the whole image, works for multiple images at a time

#plot histogram for each color channel
img_c = cv2.imread("opencv_files/niente.png", cv2.IMREAD_UNCHANGED)

color = ('b','g','r')
for i, col in enumerate(color):
    #plotting different channels in different colors
    hist_c = cv2.calcHist([img_c], [i], None, [256], [0, 255]) #putting i to differentiate between channels, takes color by itself using i as channel
    #plt.plot(hist_c, color=col)

    #other method
    channel = img_c[:,:,i]
    plt.hist(channel.ravel(), 256, [0,255], color=col)  #ravel() converts the channels into a monodimensional array
                                                        #hist fills the area underneath peaks

#show histogram (using matplotlib) / decomment lines
plt.plot(hist_g)
plt.xlim([0, 255])
plt.show()

