We represent images as 3 matrices for r, g, b in this kind of architecture
For FF NN, images are monodimensional arrays which cause loss of informations

Let's reuse alien planets:
* Alphabet = {\\, /}
* Computer = 2x2 pixels
* Filled squares are seen as 1
* Empty squares are seen as -1
Build an image recognizer 

We can use a signed sum 

![[Pasted image 20231116151915.png]]
## Image classifier 

If sign(sum) is + output /
else output \

There are 16 sign patterns (2 signs for each entry of the 2x2 matrix), but they grow exponentially and we can't check them all

Taking another example:
* Alphabet = {/, \\, X, O}
* 3x3 matrix

We can see this creates ambiguity (consider / and X)

![[Pasted image 20231116153524.png]]

![[Pasted image 20231116153538.png]]

----------------

CNN's take their name from the convolution operation, in which a smaller matrix (called *kernel* or *filter*) is slid through the whole image and put in hadamard product with that part of the bigger matrix in order to reduce its dimensionality 

![[Pasted image 20231107145639.png]]
![[Pasted image 20231107150229.png]]

We also define a threshold for classification. This may be updated and/or tuned.
## Convolution, formally, Stride and Pooling

Given a matrix M, which is an image, and K, which is the kernel and has a dimension smaller than the image (typically 3x3), we define the convolution of M by K as the matrix obtained by taking the Hadamard product of K with every K-sized submatrices of M

We define the **stride** of a convolution based on the steps we move the kernel over the image, and it's typically less than the size of the kernel
Imagine a convolutional neural network is taking an image and analyzing the content,
If the filter size is 3x3 pixels, the contained nine pixels will be converted down to 1 pixel in the output layer
**Naturally, as the stride, or movement, is increased, the resulting output will be smaller**

![[Pasted image 20231107160439.png]]

**Pooling layers provide an approach to down sampling feature maps by summarizing the presence of features in patches of the feature map**, in a more robust way wrt stride as it is less lossy

Two common pooling methods are:
- **Average Pooling**: Calculate the average value for each patch on the feature map (namely, looking at the picture above, the max between a, b, e, f)
- **Maximum Pooling (or Max Pooling)**: Calculate the maximum value for each patch of the feature map (namely, looking at the picture above, the avg between a, b, e, f)

Pooling layers are typically added after a convolutional layer, and it can be considered as a non-weighted convolution

![[Pasted image 20231107161126.png]]

The convolution is a linear map given by a matrix multiplication $$M \in M_{mxn} \mapsto M_{m'xn'}$$ and $$\mathbb{R}^{mn} \mapsto \mathbb{R}^{m'n'}$$so a convolution is a FFNN with shared parameters, some weights are the same and some are always 0

Convolution (*) is a linear operation, so:
**Given a constant** $c$ :
$$ c(M)*K = c(M*K) $$$$(M_1+M_2)*K=M_1*K + M_2*K$$ 