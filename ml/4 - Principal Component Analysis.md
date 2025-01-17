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
![](pictures/Pasted%20image%2020250114150651.png)
![](pictures/Pasted%20image%2020250114150701.png)

------------
# Detailed steps
## First and second step - Standardize and center point cloud

We center the point cloud X, sampled from a multivariate Gaussian Distribution, to the origin (0,0) by:
1. Computing the **mean** and subtracting it from each $x \in X$
2. Computing the **standard deviation** and divide
3. Use z-score to normalize$$X' \leftarrow \frac{X-\mu}{\sigma} \text{  so that  } X' \sim N(0,1)$$This does not change the relative data position, it just physically shifts the point cloud to approximate a Normal Gaussian Distribution

------------------
## Third step - Build the covariance matrix and calculate eigendecomposition
$$C = \frac{1}{N}X^T \cdot X$$with N being the number of samples

![](pictures/Pasted%20image%2020250115122037.png)

Perform eigendecomposition or SVD and reverse sort eigenvalues and reorder eigenvectors accordingly:

* The eigenvector with the highest eigenvalue is the first principal component

* Higher eigenvalues correspond to greater amounts of shared variance explained
	* If λ=0, the associated principal component captures **no variance**, meaning it does not contribute any meaningful information about the data's spread or structure.

* Eigenvectors show the direction where data spreads out the most (principal components -- new axes for data projection)

**In this way we form the matrix U, which contains the eigenvectors of the covariance matrix as columns, ordered from the one associated with the largest eigenvalue to the smallest eigenvalue

---------------------
## Fourth step - Projection on lines made by eigenvectors and reconstruction

We can project any data point in the D-dimensional subspace onto the principal subspace (2, more often than not)
We need to standardize x using mean and std dev of every dimension in D

![](pictures/Pasted%20image%2020240205115020.png)

![](pictures/Pasted%20image%2020250115170934.png)

----------------------------
## Fifth step - Undo initial standardization

Perform: $$x_i \leftarrow x_i^T \text{ } \sigma + \mu$$
![](pictures/Pasted%20image%2020240205103549.png)


![](pictures/Pasted%20image%2020240205140727.png)
This image shows all the steps in detail
## Choosing principal components

**Select the Top k Principal Components**: Choose the top k eigenvectors (principal components) based on the largest eigenvalues

**The value of k typically depends on how much variance you want to retain in the data**

For example, if you want to capture 95% of the variance, choose the smallest k such that the sum of the first k eigenvalues divided by the total sum of all eigenvalues is greater than or equal to 0.95

![](pictures/Pasted%20image%2020250115173238.png)
![](pictures/Pasted%20image%2020250115173446.png)

or use this notation![](pictures/Pasted%20image%2020250115175011.png)

![](pictures/Pasted%20image%2020250117100327.png)

----------------
# Exercise Cheatsheet

## Scaling 

A matrix (usually Delta) appears, it's a diagonal square matrix that has **scaling coefficients** on the diagonal

For example, if we wanted to scale the matrix X by 5%, we would use $$U\Delta U^T X^T$$where Delta is the scaling matrix in this form (proportional to the other dimensions) $$\Delta = \begin{bmatrix}
1.05 & 0 \\
0 & 1.05 
\end{bmatrix}  $$This would be an **enlarging** of the starting matrix 
After a scaling, the determinant is scaled by the scaling coefficient
To apply scaling n times, use Delta^n

## Flipping the principal components

Flipping the principal components means swapping them by swapping the two columns of U $$U(\Gamma U)^TX^T$$where Gamma is the **mirror matrix** $$\Gamma = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}  $$
## Rotating

To rotate X, we need to multiply U by a **rotational matrix**

Below are some common examples![](pictures/Pasted%20image%2020250115153501.png|)
#### Rotating, shifting and stretching does not affect the determinant

If the biggest Principal component is downward, there will be negative values in the covariance matrix

It is helpful to calculate the covariance matrix to see how it is affected by affine transformations (usually this is point a of any exercise)

----------

Another type of question for exercise 1 could be related to data fitting issues that may arise when working with PCA and supervised learning
These include:

- **Loss of Interpretability**: Principal components lack real-world meaning.  
    _Solution_: Use PCA only when interpretability is less critical or combine PCA with domain knowledge.
    
- **Overfitting**: Retaining too many components captures noise.  
    _Solution_: Use cross-validation to select the optimal number of components.
    
- **Underfitting**: Retaining too few components discards important information.  
    _Solution_: Retain enough components to capture a high percentage of variance (e.g., 95%).
    
- **Covariance Structure Bias**: PCA ignores the target variable, retaining components unrelated to prediction.  
    _Solution_: Use supervised dimensionality reduction methods like Partial Least Squares (PLS) or Linear Discriminant Analysis (LDA).
    
- **Sensitivity to Scaling**: Features with larger variances dominate PCA.  
    _Solution_: Normalize or standardize data before applying PCA.
    
- **Temporal or Sequential Data Issues**: PCA disregards temporal relationships, disrupting patterns.  
    _Solution_: Use time-series-specific techniques like dynamic PCA.
    
- **Data Sparsity and Noise**: PCA amplifies sparse or noisy data.  
    _Solution_: Preprocess to remove noise or use sparse PCA for sparse datasets.
    
- **Impact on Model Regularization**: PCA alters the feature space, misaligning regularization penalties.  
    _Solution_: Re-tune regularization parameters post-PCA or use original features when regularization is critical.
    
- **Class or Target Imbalance**: PCA does not account for class imbalance or target variable distribution.  
    _Solution_: Address class imbalance (e.g., SMOTE for classification) or use supervised dimensionality reduction.
    
- **Misalignment with Supervised Goals**: PCA minimizes variance, not prediction error.  
    _Solution_: Evaluate the necessity of PCA and consider feature selection methods better aligned with predictive goals.

Using the dimension with the highest variance (which is the main goal of PCA) **isn't always the best approach for some supervised classification tasks**

**This should be considered whether the class overlap, which would lead to losing information by making them not linearly separable and when performance metrics drop after applying PCA**

Sometimes, projecting onto dimensions with lower variance can preserve class separability by not making them overlap and improve the performance of supervised classification

Principal components with high variance might merge classes together if the variance is within-class rather than between-class

------------------





