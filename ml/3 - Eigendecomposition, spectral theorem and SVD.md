Continuing on the path of basics of linear algebra, we talk about **eigendecomposition (aka diagonalization) of a matrix**

## Remark: how to find eigenvalues of a matrix

The eigenvalues of a matrix can be found by **det(A - Iλ) = 0**, where I is the n x n identity matrix

The eigenvectors of a matrix can be found by substituting for each eigenvalue in the spectrum and computing **Ker(A-Iλ)**, or, equivalently,**(A−λI) x = 0**—and solve for x; the resulting nonzero solutions form the set of eigenvectors of A corresponding to the selected eigenvalue.

The determinant of a matrix is the product of its eigenvalues

-------------

The Eigendecomposition of a square matrix is a factorization s.t the matrix is represented by its **eigenvalues and eigenvectors** (this concept is often called diagonalization of a matrix)

Let **A** be a square _n_ × _n_ matrix with _n_ linearly independent eigenvectors _qi_ (where _i_ = 1, ..., _n_). Then **A** can be [factorized](https://en.wikipedia.org/wiki/Matrix_decomposition "Matrix decomposition") as: $$A = Q \land Q^{-1}$$
where:
* **Q** is the square _n_ × _n_ matrix whose _i-th column is the **eigenvector** q-i_ of **A**, 
* **Λ** is the [diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix "Diagonal matrix") whose diagonal elements are the corresponding **eigenvalues**, i.e. _Λii_ = _λi_ (also called Σ)

**only diagonalizable matrices can be factorized this way**

![[../pictures/Pasted image 20240202094847.png|700]]
![[../pictures/Pasted image 20240202142659.png]]
## Geometric interpretation of eigenvectors

Eigenvectors only change direction under the linear transformation represented by the matrix, and they are scaled with corresponding eigenvalues

Taking as example a parametric unit sphere $$\{t \in [0, 2\pi] |x=cos(t), y=sin(t)\}$$A applies a linear transformation to each point p = (x, y) and stacks all points in a matrix, such that the result is A @ P (i.e. A matrix mult P)

This is useful to compute the determinant; take the pic below:
![[../pictures/Pasted image 20240202145821.png|400]]
The determinant is the ratio between $$\frac{\text{area or volume of destination shape}}{\text{area or volume of source shape}}$$in this case, a **circle** (from which we take the matrix P) got transformed in an **ellipse** by means of a linear map A

**Eigenvectors** direction is scale independent (see red vectors wrt pink vectors), the scaling is determined by their **eigenvalues**

This tells us that if the determinant is close to 1 the area of the transformed ellipse can approximate the input

Grey vectors are the ones that changes after the linear map

-------
# Singular Value Decomposition

Singular Value Decomposition (SVD) is a factorization or decomposition of a matrix into three simpler matrices, which can provide insights into the properties of the original matrix. Given a matrix A, its singular value decomposition is expressed as:
$$A=UΣV^T$$
Here:

- A is an m×n matrix.
- U is an m×m orthogonal matrix with the eigenvectors of $AA^T$ as columns (meaning $U^TU=UU^T=I$).
- Σ is an m×n diagonal matrix with eigenvalues of $AA^T \text{ or } A^TA$ on the diagonal or any positive real value, known as the singular values.
- $V^T$ is the transpose of an n×n orthogonal matrix V with the eigenvectors of $A^TA$ as columns (meaning $V^TV=VV^T=I$)

SVD, differently from eigendecomposition, works for non-square matrices as well (we don't need to invert anything) 

![](pictures/Pasted%20image%2020240202151946.png)
![](pictures/Pasted%20image%2020240202152133.png)
![](pictures/Pasted%20image%2020240202152120.png)

Both eigendecomposition and SVD apply 3 steps:
1. Rotation of vectors
	1. $V^T$ in SVD
	2. $U^{-1}$ in eigendecomposition (matrix with eigenvector columns)
2. Scaling / reflection
	1. Σ in both methods (diagonal eigenvector matrix)
3. Rotation / reflection of space
	1. U in both methods (matrix with eigenvector columns)

![](pictures/Pasted%20image%2020240202154819.png)