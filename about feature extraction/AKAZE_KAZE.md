## [AKAZE and KAZE](https://docs.opencv.org/3.4/db/d70/tutorial_akaze_matching.html) 

AKAZE and KAZE features come from the necessity of a new scale-space, different from the Gaussian scale space, as it does not respect the natural boundaries of objects and smoothes to the same degree both details and noise at all scale levels

## KAZE

KAZE features are oriented (in contrast to SIFT and SURF) and describe edges in *frequency space*, hence they are robust to noise and blur

The aim is to detect and descrice features in nonlinear scale spaces, blurring small details adaptively to preserve boundaries

### Nonlinear Diffusion Filtering

Nonlinear diffusion approaches describe the evolution of the *luminance* ( perceived brightness in a specific region of an image) of an image through increasing scale levels as the **divergence of a function that controls the adaptive diffusion process**

A classic nonlinear diffusion equation uses *nonlinear partial differential equations*, the solutions of which are approximated via the *linear-implicit and semi-implicit schemes* &rarr; **AOS schemes**

This is applied to enhance keypoint stability, after they are detected at multiple scales

#### The how-to:

* Given an input image, we build the nonlinear scale space up to
a maximum evolution time using AOS techniques and variable conductance diffusion:
    * The image is first convolved with a Gaussian kernel
    * The image gradient histogram is then used to obtain *k*, the contrast parameter &rarr; **Perona and Malik Diffusion**
    * The nonlinear scale space is then built iteratively given the evolution times 
>**REM:** This is done similarly to SIFT, discretizing the scale space in logarithmic steps with octaves and sublevels

* Then, we detect 2D features of interest that exhibit a maxima of the scale-normalized
determinant of the Hessian response through the nonlinear scale space

* Finally, we compute the main orientation of the keypoint and obtain a scale and rotation invariant descriptor considering first order image derivatives:
    * **Orientation** 
        * Similar to SURF, we find the dominant orientation in a circular area of radius 6σi with a sampling step of size σi
        * For each of the samples in the circular area, first order derivatives are weighted with a Gaussian centered at the interest point
        * Then, the derivative responses are represented as points in vector space and the dominant orientation is found by summing the responses within a sliding circle segment covering an angle of π/3
        * **The longest vector is the dominant orientation**
    * **Descriptor**
        * Same as M-SURF descriptor, adapted to nonlinear scale space,  the descriptor vector of length 64 is normalized into a unit vector to achieve invariance to contrast

## AKAZE - Accelerated KAZE

- The scale space

The nonlinear scale space is discretized in a series of *octaves* and *sub-levels*, and each one is mapped to a corresponding scale $\sigma$, and converted to time units

### Fast Explicit Diffusion
