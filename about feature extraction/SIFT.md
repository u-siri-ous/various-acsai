## SIFT (Scale-Invariant Feature Transform)

[SIFT](https://aishack.in/tutorials/sift-scale-invariant-feature-transform-introduction/) adds the scale invariant property to cornerHarris (as a corner might change when the image is scaled)

To create a scale space, you take the original image and generate progressively blurred out images

Then, you resize the original image to half size, you generate blurred out images again and again
> [Visualizing octaves](https://aishack.in/static/img/tut/sift-octaves.jpg)

It performs these 5 steps: 
### 1) Scale-space extrema detection 

Uses a [Laplacian of Gaussian](https://automaticaddison.com/how-the-laplacian-of-gaussian-filter-works/#:~:text=Laplacian%20of%20Gaussian%20is%20a,locate%20boundaries%2C%20and%20extract%20features.) as a blob and edge detector  

We introduce the $\sigma$, which is the scaling parameter, and identifies points which are invariant to scale and rotation

The scale space of an image is defined ad a function L(x, y, $\sigma$) from a **convolution** of a Gaussian kernel G(x, y, $\sigma$) and an input image I(x, y)

In practice, it will use a Difference of Gaussians between octaves as an approximation of the much more expensive Laplacian of Gaussians

![Difference of Gaussians](https://user-images.githubusercontent.com/45935623/233586232-e475b637-6295-4bc1-9e01-765d7fcab163.png)

Therefore, we can find the local maxima across the scale and space as a list (x, y, $\sigma$) 
> there will be a maxima at (x,y) with $\sigma$ scaling

Once this DoG are found, images are searched for local extrema over scale and space 

For example, one pixel in an image is compared with its 8 neighbours as well as 9 pixels in next scale and 9 pixels in previous scales 

If it is a local extrema, it is a potential keypoint, meaning that *that* keypoint is best represented in that scale

### 2) Keypoint Localization

Once candidates are found, we need to filter them based on:
* Subsceptibility to noise
* Contrast, i.e. intensity of extrema
* Location, as the DoG is reactive to edges

**Noise and Contrast**

The approach uses the Taylor Expansion of D(x, y, $\sigma$) up to quadratic terms, shifted to the origin as **sample point**

D(x, y, $\sigma$) and its derivatives are evaluated at the sample point, with *x* being the offset from it; the location of the point is determiden by the derivative with respect to *x* and setting it to 0
>The Hessian and derivative of D are approximated by using differences of neighboring sample point

If the offset calculated is larger than 0.5 in any dimension, then it means that the extremum lies closer to a different sample point, in this case, the sample point is changed

**Eliminating edge responses**

A 2x2 Hessian is used to compute principal curvature, as a poorly defined peak in the DoG function will have a large principal curvature across the edge but a small one in the perpendicular direction

In the event that the determinant is negative, the point is discarded as the curvatures have different signs
>this also takes the approach of cornerHarris, removing edges using eigenvalues and their ratios

### 3) Orientation Assignment

By assigning a consistent orientation to each keypoint based on local image properties, the keypoint descriptor can be represented relative to this orientation and therefore achieve invariance to image rotation

An orientation histogram is formed from the gradient orientations of sample points within a region around the keypoint, with 36 bins covering the 360 degree range of orientations
 
Each sample added to the histogram is weighted by its gradient magnitude and by a Gaussian-weighted circular window with a σ that is 1.5 times that of the scale of the keypoint; the highest peak and any other peak above its 80% are used to create a keypoint in that orientation

### 4) Keypoint Descriptor Generation

The descriptor is a vector achieved from the aforementioned histogram


