## ORB (Oriented FAST and Rotated BRIEF)

[ORB](https://docs.opencv.org/3.4/d1/d89/tutorial_py_orb.html) comes to our help when we need real-time and cost effective replacement to SIFT

It builds on [FAST](https://docs.opencv.org/3.4/df/d0c/tutorial_py_fast.html) and [BRIEF](https://medium.com/@deepanshut041/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6)

### FAST (Features from Accelerated Segments Test)

Given a pixel *p* in an array fast compares the brightness of *p* to surrounding 16 pixels that are in a small circle around *p*

Pixels in the circle is then sorted into three classes:

* lighter than *p*

* darker than *p*

* similar to *p*

If more than 8 pixels are darker or brighter than *p* than it is selected as a **keypoint**

Keypoints found by FAST gives us information of the location of determining edges in an image, lacking, however the orientation and scale component

### BRIEF (Binary Robust Independent Elementary Features)

>The defined neighborhood around pixel(keypoint) is known as a patch, which is a square of some pixel width and height

BRIEF deals with noise-sensitivity by pre-smoothing the patch via a Gaussian kernel, increasing stability and repeatability of the descriptors

[link](https://medium.com/data-breach/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6)

It adds to them:

* The addition of a fast and accurate orientation component to FAST

* The efficient computation of oriented BRIEF features

* Analysis of variance and correlation of oriented
BRIEF features

* A learning method for de-correlating BRIEF features under rotational invariance, leading to better performance in *nearest-neighbor* applications

### Keypoint Detection

