![[Pasted image 20231024141706.png]]

The discrete perceptron assigns predictions of 0 and 1 to the points according to what side of the line they are
The continuous perceptron assigns a prediction between 0 and 1 to every point in the plane:
* the points over the line get a prediction of 0.5
* the points on one side of the line get predictions higher than 0.5
* and the points on the other side get predictions lower than 0.5

We can also see the output of an ANN similarly, the boundary of the resulting classifier is a combination of the boundaries of the input classifiers, [(check this out to visualize)](http://playground.tensorflow.org/)

![[Pasted image 20231024142808.png]]

and this scales to bigger models

----------
## Training an ANN

A feedforward NN with n inputs is just a function $$\mathbb{N}: \mathbb{R}^n \rightarrow \mathbb{R}$$ Now:
1. Choose an error function
2. Use Gradient Descent to update weights and biases
### Naive strategy

Label weights and biases , based on the arcs of the NN, suppose the error function is *C*,
$$
\frac{\partial C}{\partial w_j} \approx \frac{C(W+\epsilon e_j)-C(W)}{\epsilon} 
$$
Where:
* $\epsilon$ is a small number
* e<sub>j</sub> is the j<sup>th</sup> standard basis vector
* w<sub>j</sub> is the j<sup>th</sup> weight considered
* W is the vector of weights

It will take *s+t* forward passes of N to compute the gradient, where *s* is the number of weights and *t* is the number of biases

We now need to compute the gradient 
$$
\nabla C = \biggl(\frac{\partial C}{\partial x_1}, ...,\frac{\partial C}{\partial x_{s+t}}\biggr)
$$
But this is a huge vector

There is a way to compute the gradient with only two forward passes of N

----------
### Backpropagation algo

Let $w^l_{jk}$ be the **weight of the arc** from the $k^{th}$ neuron in layer $l-1$ to the $j^{th}$ neuron in layer $l$ and let $b^l_j$ be the **bias** of the $j^{th}$ neuron in layer $l$ (imagine this living "inside the neuron") 
![[Pasted image 20231024154224.png]]
Suppose all activation fcn are **sigmoids**, the activation of the $j^{th}$ neuron in layer $l$ is defined as 
$$
a^l_j = \sigma \biggl(\sum_k w^l_{jk}~a^{l-1}_k~+~b^l_j\biggr)
$$Define a matrix $w^l$ s.t. the entry in the $j^{th}$ row and the $k^{th}$ column is $w^l_{jk}$ and let $a^l$ be the vector output by layer $l$ such that
$$
a^l=\sigma(w^l~a^{l-1}~+~b^l)
$$where:
* $w^l$ is a matrix
* $a^{l-1}$ is a vector
* $b^l$ is a vector

-------------
## On Linear Algebra
### Exercise - Linear Algebra and NN

Show that (AB)C  = A(BC) using NN

Let N be a NN with $A = W^1$, $B= W^2$ and $C=W^3$ with the identity activation fcn (no activation fcn)

Non ho capito perchè ha fatto sta cosa però daje, basically we can collapse layers and both things are outputs of N (?)
### The Matrix Product

Let $A, B$ be two matrices nxm and mxp, they are multipiable and $C$ is:
$$
c_{ij} = \sum _{k=1}^n a_{ik}~b_{kj}
$$
### The Hadamard Product (notes because we didn't do this in LA)

![[Pasted image 20231024160914.png]]

------

Let's dfferentiate at the nodes instead of the arcs; let $$z^l\equiv w^l~a^{l-1}~+~b^l$$and $$z^l_j = \sum_k w^l_{jk}~a^{l-1}_k~+~b^l_j$$We plan to differentiate wrt $z_j^l$ instead of $w^l_{jk}$, we'll see it in lec. 8
### On notation

copia foto viola