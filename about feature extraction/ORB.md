## ORB (Oriented FAST and Rotated BRIEF)

[ORB](https://docs.opencv.org/3.4/d1/d89/tutorial_py_orb.html) comes to our help when we need real-time and cost effective replacement to SIFT

It builds on [FAST](https://docs.opencv.org/3.4/df/d0c/tutorial_py_fast.html) and [BRIEF](https://medium.com/@deepanshut041/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6)

It adds to them:

* The addition of a fast and accurate orientation component to FAST

* The efficient computation of oriented BRIEF features

* Analysis of variance and correlation of oriented
BRIEF features

* A learning method for de-correlating BRIEF features under rotational invariance, leading to better performance in *nearest-neighbor* applications

ORB is a fusion of FAST keypoint detector and BRIEF descriptors, applying Harris corner measure to fine the top *n* points among them

### Adding rotation invariance to keypoints and descriptors

**oFAST**

To add rotation invariance, we compute the *intensity-weighted centroid* of the patch with located corner at center

**The direction of this vector from this corner point to centroid gives the orientation by applying atan**

**rBRIEF**

For descriptors, ORB uses BRIEF descriptors, steering it according to the just-computed orientation of keypoints

For any feature set of n binary tests at location (x<sub>i</sub>,y<sub>i</sub>), define a 2×n matrix, S which contains the coordinates of these pixels

Then, using the orientation of patch, $\theta$, its rotation matrix is found and rotates the S to get steered/rotated version, S $\theta$

ORB constructs a lookup table for precomputed BRIEF patterns, so as long as the keypoint orientation si consistent across *views*, the correct set of points S $\theta$ will be used for the descriptors