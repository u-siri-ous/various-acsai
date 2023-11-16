Given a NN *N* with *L* layers, we define some cost functions
### Quadratic cost fcn

$$
C = \frac{1}{2n}\sum_x||y(x)-a^L(x)||^2
$$Where:
* y is the label
* training sample has size n

Key property is

$$
C=\frac{1}{n}\sum_xC_x
$$where:
* $C_x=\frac{1}{2}||y-a^L||^2$
		so cost is avg or sum of costs at each point 
* $a^L$ is the output vector of the last layer, see lec.7

The **error** in neuron $j$ in layer $l$ is defined to be $$\delta_j^l = \frac{\partial C}{\partial z^l_j}$$$\delta^l$ is the <u>vector</u> with coordinates $\delta_j^l$
There is a simple formula to compute the error at the last layer
## BP1 - error at last layer

We define this to be $$\delta^L_j = \frac{\partial C}{\partial a^L_j}~\sigma'(z^L_j)$$where $$\frac{\partial C}{\partial a_j^L} = \biggl(\frac{1}{2}\biggr)~2~(y_j-a_j^L)~(-1) = a_j^L-y_j$$remembering that $C$ is the quadratic cost function

Now we can properly define $$\delta^L= \nabla_aC~\odot~\sigma'(z^L)$$Trivially, $\nabla_aC$ is the vector whose components are $\frac{\partial C}{\partial a^L_j}$ 
## BP2 - error at preceding layers 
$$\delta^l=((w^{l+1})^T~\delta^{l+1})\odot\sigma'(z^l)$$where:
* w is the matrix of weights from layer $l$ to layer $l+1$, transposed to get the opposite (namely, backpropagate error)
## BP3 - partial derivatives wrt biases

$$\frac{\partial C}{\partial b_j^l} = \delta_j^l$$and $$\frac{\partial C}{\partial b}=\delta$$with a **big** abuse of notation, this says that $\delta$ is being evaluated at the same neuron as $b$
## BP4 - partial derivatives wrt weights
$$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k~\delta^l_j$$To remember this better, we can write this as $$\frac{\partial C}{\partial w} = a_{in}~\delta_{out}$$where:
* $a_{in}$ : activation fcn of neuron at the <u>tail</u> of the arc
* $\delta_{out}$ : error of the neuron at the <u>head</u> of the arc

Now, $$
\begin{aligned}
&\delta^L= \nabla_aC~\odot~\sigma'(z^L)~(BP1)\\
&\delta^l=((w^{l+1})^T~\delta^{l+1})\odot\sigma'(z^l)~(BP2)\\
&\frac{\partial C}{\partial b_j^l} = \delta_j^l~(BP3)\\
&\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k~\delta^l_j~(BP4)\\
\end{aligned}
$$
### Proof of BP1

![[Pasted image 20231116150509.png]]

------
## The algorithm

1. Compute $a^1$ - act fcn of input layer
2. <u>Feedforward pass</u> 
	for $l=2,3,...,L$ 
		Compute $z^l=w^l~a^{l-1}~+~b^l$
		and $a^l=\sigma(z^l)$
1. <u>Output layer error</u> $\delta^L$ 
	Compute $\delta^L= \nabla_aC~\odot~\sigma'(z^L)$ 
4. <u>Backpropagation using BP2</u> 
	for $l = L-1, L-2,...,2$, in this order
		Compute $\delta^l=((w^{l+1})^T~\delta^{l+1})\odot\sigma'(z^l)$ 
5. <u>Output</u>: Gradient of the cost function C is given by
	$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k~\delta^l_j~(BP4)\text{ and }\frac{\partial C}{\partial b_j^l} = \delta_j^l$
	Namely, BP3 and BP4

If $r$ is the learning rate, update all weights and biases by moving in the direction of $-r\nabla C$ to old weights and biases

A rough complexity analysis says that it requires only two passes of N

