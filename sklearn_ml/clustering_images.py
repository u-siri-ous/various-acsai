import cv2
from sklearn.cluster import KMeans
import numpy as np

# load an rgb image and quantize the colors, map the colors in an image to a lower dimensional colorspace
image = cv2.imread('sklearn_ml/doggino.jpg')

(h,w,c) = image.shape

# convert the image from 3d to 2d
img2D = image.reshape(h*w, c)

# instantiate kmeans with the number of colors we want
kmeans_model = KMeans(n_clusters=16)

clusters_labels = kmeans_model.fit_predict(img2D)

# post-processing information
rgb_colors = kmeans_model.cluster_centers_.round(0).astype(int)

# reshape in 3d
img_quantized = np.reshape(rgb_colors[clusters_labels], (h,w,c))
img_quantized = img_quantized.astype('uint8')

cv2.imshow("kmeaned", img_quantized)
cv2.waitKey(0)