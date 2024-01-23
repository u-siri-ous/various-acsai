**This is a recap + tantecose di linear algebra, some things are considered known**
### Vector to Vector operations
#### Dot product - standard inner product

$$x, y \in \mathbb{R}^D \rightarrow x^Ty = \langle x,y \rangle = \sum^D_i x_i \cdot y_i$$
The result is a scalar. Geometrically, it's interpreted as $$v \cdot w = |v||w| cos (\theta)$$where $\theta$ is the angle between v and w
#### Cosine similarity
![[../pictures/Pasted image 20240123112141.png]]
#### Outer product
![[../pictures/Pasted image 20240123112330.png]]
#### Hadamard product - component-wise product (also in matrices)
![[../pictures/Pasted image 20240123112821.png]]

-----------
### Matrix operations

#### Standard product
![[../pictures/Pasted image 20240123112634.png]]

--------------
### **Norms**

The norm of a vector is its length, with the most common norm being the l2 norm (or **Euclidean norm**):
![[../pictures/Pasted image 20240123104220.png|]]

A norm is a function f : R n → R must satisfy:
1. Non-negativity            for all x, f(x) >= 0
2. Definiteness                f(x) = 0 iff x = 0
3. Closure wrt to product by a scalar i.e. **f(tx) = |t| f(x), t** **∈** **R**
4. Closure wrt sum i.e. **f(x+y) = f(x) + f(y)**
5. The triangle inequality ||x+y|| <= ||x|| + ||y||

![[../pictures/Pasted image 20240123104252.png]]
### **Orthogonal Matrices**

The orthogonality of vectors is defined by their dot product:

                                               <v,w> = 0 iff they are orthogonal

**A matrix is orthogonal if all of its columns are pairwise orthogonal and normalized** (orthonormal)
  
It follows that:

![[../pictures/Pasted image 20240123104851.png]]

And that the transpose is equal to the inverse
### **Affine spaces and sets**

The affine space exists independently of the chosen basis, as it lacks the usual coordinate system (i.e., the origin)

There is instead the notion of **translation vectors** between points in the space

A set is affine **iff** it contains all lines through any two points in the set (the set contains the linear combination of any two points in it, provided that all the coefficients sum to 1)

Formally:

![[../pictures/Pasted image 20240123105027.png]]

Each vector space can be regarded as an affine space A(V, V, α) where α(x, v) is the sum of x and v in V

The affine subspaces of A(V) are the sets x+W={x+w∣w∈W} where:
* x∈V 
* W is linear subspace of V
### **Hyperplanes**

A hyperplane is an affine set (called space by prof) of dimension n-1, it generalizes the notion of common plane to higher dimensions 

It divides the space into two half-spaces (in the example below it divides a common 2dimensional plane with a 1dimensional line)

![[../pictures/Pasted image 20240123105401.png]]

**Projection onto a Subspace**

![[../pictures/Pasted image 20240123105432.png]]

![[../pictures/Pasted image 20240123105505.png]]
### Dimensionality reduction operations on matrices

![[../pictures/Pasted image 20240123110520.png]]![[../pictures/Pasted image 20240123110533.png]]
### Geometry of linear maps and bases

We usually work wrt of the standard or **canonical basis**, which is a set of vectors, each of whose components are zero, exception made for one that is equal to one. This lets us **write any vector in our space as a weighted sum of these basis vectors.** This can lead to severe distortion of our working space, as seen in this example:
![[../pictures/Pasted image 20240123115657.png]]

Suppose V and V' to be vector spaces. $F: V \rightarrow V'$ is linear iff:
* It is closed wrt sum $\rightarrow F(v_1+v_2)= F(v_1)+F(v_2)$
* It is closed wrt scalar product $\rightarrow F(\alpha v) = \alpha F(v), \forall \alpha \in \mathbb{R}$ 
### Linear dependence 

A set of vectors $v_1, v_2, ..., v_k \in V$ is said to be **linearly dependent** if there exist $a_1, a_2, ..., a_k \in \mathbb{R}$, **with at least one non-zero scalar**, such that $$a_1v_1+a_2v_2+...+a_kv_k = 0$$ (i.e. a set of vectors is linearly dependent if and only if one of them is zero or a linear combination of the others.)

**If the equation is satisfied only if all a's are = 0, the set is linearly independent**

In the above example, the space is compressed due to a linear dependence of the chosen basis vectors
### Rank

The concept of rank is closely related to linear independence, **it is the maximum number of linearly independent columns amongst all subsets of columns** 
![[../pictures/Pasted image 20240123121222.png]]
### Determinant and invertibility

The determinant of a matrix is a scalar value that is a function of its entries. **It's defined only for square matrices**.

![[../pictures/Pasted image 20240123121524.png]]

To find a determinant we can use the Laplace expansion. In general:

![[../pictures/Pasted image 20240123121834.png]]

A matrix is **invertible** iff its determinant is nonzero. The inverse matrix is defined (example with 2x2 matrix and 3x3 matrix below) as:
$$A^{-1} = \frac{1}{det(A)}C^T$$where $C^T$ is the **transposed cofactor matrix** (aka adjoint or adjugate) defined (for a 3x3 matrix) as:
![[../pictures/Pasted image 20240123122619.png|350]]
![[../pictures/Pasted image 20240123122116.png|400]]

