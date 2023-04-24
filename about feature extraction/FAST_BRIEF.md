## [FAST](https://medium.com/data-breach/introduction-to-fast-features-from-accelerated-segment-test-4ed33dde6d65) (Features from Accelerated Segments Test)

Given a pixel *p* in an array fast compares the brightness of *p* to surrounding 16 pixels that are in a small circle around *p*

Pixels in the circle is then sorted into three classes:

* lighter than *p*

* darker than *p*

* similar to *p*

If more than 8 pixels are darker or brighter than *p* than it is selected as a **keypoint**

Keypoints found by FAST gives us information of the location of determining edges in an image, lacking, however the orientation and scale component

## BRIEF (Binary Robust Independent Elementary Features)

>The defined neighborhood around pixel(keypoint) is known as a patch, which is a square of some pixel width and height

BRIEF deals with noise-sensitivity by pre-smoothing the patch via a Gaussian kernel, increasing stability and repeatability of the descriptors

It then creates a binary feature vector out of the patch via the binary test $\tau$
![image](https://user-images.githubusercontent.com/45935623/234045549-ae2e94c9-7502-462e-9f89-cbccf1ae04c3.png)

*n* (x,y) pairs have to be selected from one of the sampling geometries found at this [link](https://medium.com/data-breach/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6)

The descriptor looks like this:

![image](https://user-images.githubusercontent.com/45935623/234047460-9e475e13-08d7-4b5e-8407-3fdf3e277410.png)
