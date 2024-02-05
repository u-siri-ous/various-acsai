## PCA - basics and interpreting graphs

PCA is one way to reduce dimensionality on high-dimensional datasets using a transformation that preserves the most variance in the data using **the least amount of dimensions** (namely, 2 for a standard plane)

The aim is to follow these steps:
1. Construct the **covariance matrix**
2. Compute its eigenvalues
3. Use the eigenvectors to reconstruct data

To find a transformation that compresses the data (may be more than one), we aim to find the one that maximizes length variance of projection along every point in the point cloud aka a k-dimensional subspace that maximizes data variance
## Remark: Computing the covariance matrix

The covariance matrix is a square matrix in the form
![](pictures/Pasted%20image%2020240202155036.png)
![](pictures/Pasted%20image%2020240202155116.png)
![](pictures/Pasted%20image%2020240202155139.png)

------------
# Detailed steps
## First and second step - Standardize and center point cloud

We center the point cloud X, sampled from a multivariate Gaussian Distribution, to the origin (0,0) by:
1. Computing the **mean** and subtracting it from each $x \in X$
2. Computing the **standard deviation** and divide
3. Use z-score to normalize$$X' \leftarrow \frac{X-\mu}{\sigma} \text{  so that  } X' \sim N(0,1)$$This does not change the relative data position, it just physically shifts the point cloud to approximate a Normal Gaussian Distribution
## Third step - Build the covariance matrix and calculate eigendecomposition
$$Cov\_mat = \frac{1}{N}X^T \cdot X$$with N being the number of samples

Reverse sort eigenvalues and eigenvectors:

* The eigenvector with the highest eigenvalue is the first principal component
* Higher eigenvalues correspond to greater amounts of shared variance explained

In this way we form the matrix U, which has eigenvectors as columns from biggest to smallest
## Fourth step - Projection on lines made by eigenvectors

We can project any data point in the D-dimensional subspace onto the principal subspace (2, more often than not)
We need to standardize x using mean and std dev of every dimension in D

![](pictures/Pasted%20image%2020240205115020.png)

![](pictures/Pasted%20image%2020240205103549.png)

