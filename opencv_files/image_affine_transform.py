import cv2
import numpy as np

#geometrical transformation of images (https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html)
img = cv2.imread('opencv_files/mario.png')

''' 
a b c       same as a b c       (affine transformation)
d e f               d e f
0 0 1   

0 0 1 is a throwaway line to square the matrix (based on identity matrix)
submatrix abde is for rotaion and scaling
cf is for translating 

perspective vs affine tranformations (https://towardsdatascience.com/perspective-versus-affine-transformation-25033cef5766)
about the *matrix* (https://vovkos.github.io/doxyrest-showcase/opencv/sphinx_rtd_theme/page_tutorial_warp_affine.html)
'''
#scaling
h = img.shape[0]
w = img.shape[1]
img_res = cv2.resize(img, (h//2, w//2), interpolation=cv2.INTER_CUBIC)   #resizes image to (h,w) and interpolates (optional) to make it sharper
#interpolation is a type of estimation, a method of constructing (finding) new data points based on the range of a discrete set of known data points

#img_res = cv2.resize(img, None, fx=0.5, fy=0.5)     #to scale image as well

#translation (projective/affine)
x = 200     #left is negative
y = 30      #up is negative

mat1 = np.float32([[1,0,x],[0,1,y]])     #2x3 matrix, x,y translate image
img_affine = cv2.warpAffine(img_res, mat1, dsize=(750,500))    #apply translation to the image and modify size according to (W,H), pay attention

#rotation
mat2 = cv2.getRotationMatrix2D((h//2, w//2), 180, 1)    #create rotation matrix (start point, angle, scale)
img_rotat = cv2.warpAffine(img, mat2, dsize=(w,h))      #rotate by 180 degrees and plot it on a (w,h) image

#computing the matrix
pts1 = np.float32([[125,45],[200,80],[150,90]])   #we need at least three points to be 'matched' meaning these will be moved to the second set of points
pts2 = np.float32([[90,10],[500,700],[80,5]])   
#matrici sono 3x3 intrinsicamente, ma siccome l'ultima riga è canonica, e le 2 3x2 sono assimilate a una 2x3 con riga canonica aggiunta
#poi moltiplico la nuova matrice per l'immagine (in una versione di sottospazio dove il colore non viene toccato)

mat3 = cv2.getAffineTransform(pts1, pts2)         #we compute the (translation) matrix to move these points 

#cv2.imshow('res', img_rotat)     
print(mat3)
cv2.waitKey(0)