import cv2

img = cv2.imread('opencv_files/img.jpg')    #reads image

width = img.shape[1]    #.shape returns a tuple
height = img.shape[0]
channels = img.shape[2]

print(width, height, channels)

cv2.imshow('maggggica', img)    #shows image. syntax .imread(title, image)
cv2.waitKey()   #keeps image until time (if specified, in milliseconds) expires

#cv2.destroyAllWindows() #useful in jupyterlab

#cv2.imwrite('terribile.jpg', img)    #first argument is title (with extension that can be different from imread), second is the image