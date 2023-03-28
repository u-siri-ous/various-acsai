import cv2
import numpy as np

def OnClick(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		if len(dst_points) < 4:
			dst_points.append([x,y])
			cv2.circle(img_copy, (x,y), 50, (0,0,255),-1)
			cv2.imshow("Base Img", img_copy)

#load the two images
base_img = cv2.imread("Exercise_1/billboard.jpg")
img_copy = base_img.copy()
img2 = cv2.imread("Exercise_1/mandorlo.jpg")

#get images data
base_h,base_w = base_img.shape[:2]
img2_h,img2_w = img2.shape[:2]

#create source and destination points sets
src_points = np.array([
						[0,0],
						[0,img2_h],
						[img2_w,img2_h],
						[img2_w,0],
], dtype=np.float32)
dst_points = []

cv2.namedWindow("Base Img", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("Base Img", OnClick)
#cv2.namedWindow("Img 2", cv2.WINDOW_KEEPRATIO)

cv2.imshow("Base Img", base_img)
#cv2.imshow("Img 2", img2)
cv2.waitKey(0)

#computing the homography matrix
dst_float = np.array(dst_points,dtype=np.float32)
H = cv2.getPerspectiveTransform(src_points,dst_float)

#apply H to the image to be warped
warped = cv2.warpPerspective(img2, H, (base_w,base_h))

#create the mask
mask = np.zeros(base_img.shape,dtype=np.uint8)

#set to white the pixels that we want to copy in the billboard
cv2.fillConvexPoly(mask,np.int32(dst_points),(255,255,255))

#invert the mask
mask = cv2.bitwise_not(mask)

#apply the mask to the billboard image
masked_bill = cv2.bitwise_and(base_img,mask)

#apply the mask to the warped image
final_img = cv2.bitwise_or(masked_bill,warped)

cv2.namedWindow("Final Image", cv2.WINDOW_KEEPRATIO)
cv2.imshow("Final Image", final_img)
cv2.waitKey(0)