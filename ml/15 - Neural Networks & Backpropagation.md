# SGD over mini-batches

![](pictures/Pasted%20image%2020250206132507.png)

This is a mid-ground because the whole batch gets updated, but is taken from shuffled input data

![](pictures/Pasted%20image%2020250206132929.png)
![](pictures/Pasted%20image%2020250206132950.png)

![](pictures/Pasted%20image%2020250206133135.png)
# Momentum

Momentum is a technique used to accelerate the convergence of gradient descent optimization algorithms

The idea behind momentum is to use a **moving average** of the gradients to update the model's parameters, rather than relying solely on the current gradient, smoothing gradient updates

![](pictures/Pasted%20image%2020250206134009.png)
where alpha is the weight given to data points compared to previous average (a common value for it is 0.9)

![](pictures/Pasted%20image%2020250206134509.png)

[Difference in optimizers - grafici belli](https://www.denizyuret.com/2015/03/alec-radfords-animations-for.html)

![](pictures/Pasted%20image%2020250206134705.png)

---------
# Multi-Layer Perceptron (MLP)

![](pictures/Pasted%20image%2020250206135238.png)
where:
* W is the weight matrix (w11,...,w1d is the wight vector of class 1 and so on)
* x is the data point vector
* b is the bias

![](pictures/Pasted%20image%2020250206135548.png)
![](pictures/Pasted%20image%2020250206135523.png)
(b is omitted)

![](pictures/Pasted%20image%2020250206140134.png)
W^1 is a **hidden layer**

Because it maps the original attribute in $d$ from another dimensionality $p$ and then $k$ is used for classifying.

- The input vector x starts with dimensionality d.
- The hidden layer maps this input to a new representation with dimensionality p.
- The output layer maps the hidden layer's output to the final dimensionality k.

A priori you do not know what $\mathbf{W}^1$ may learn

![](pictures/Pasted%20image%2020250206140824.png)
# Some non-linear activation functions

## All of them are computed element-wise
## Sigmoid 
$$ \sigma(z)= \frac{1}{1+\exp^{-z}} \quad \text{sigmoid or logistic function}$$
<center>Smooth and Differentiable alternative to sign</center>

![](pictures/Pasted%20image%2020250206170908.png)

- Used to model output probability
- Nowadays not used in middle layers
- Have to compute $\exp()$
- **Vanishing gradients** for large input magnitude
## Rectified Linear Unit - ReLU
$$ \sigma(z)= \max(0,z) \quad \text{ReLu}$$<center>ReLu is piece-wise linear function</center>

![](pictures/Pasted%20image%2020250206171126.png)

- Computationally efficient (no exp!)
- No vanishing gradients but do not let pass gradients for negative values
- Converges much faster than sigmoid (6x)
- Not differentiable in zero (subgradients)

![](pictures/Pasted%20image%2020250206171432.png)

![](pictures/Pasted%20image%2020250206171336.png)

---------------
# Neural Network Initialization

![](pictures/Pasted%20image%2020250206173814.png)

**NO, it won't!**

Each element of the activation vector will be a scaled version of the input. This behavior will occur at all layers of the neural network. As a result, when we compute the gradient, all neurons in a layer will be equally responsible for anything contributed to the final loss. **We call this property symmetry.**

This means each neuron (within a layer) will receive the **exact same gradient update value (i.e., all neurons will learn the same thing).**

![](pictures/Pasted%20image%2020250206173952.png)
![](pictures/Pasted%20image%2020250206174104.png)

------------
# Backpropagation

#### Three ways of computing the gradients $\nabla_{{w}}\mathcal{L}(x,y;{w})$

1. **Manually** (if we change the network, we have to adjust it for a 100 layer neural net) → maybe not a good idea, does not scale

2. **Finite Difference** → good to check the gradients once you have an automatic way of computing it; **very slow, unfeasible in training!** 
	![](pictures/Pasted%20image%2020250206174603.png)

3. **Backpropagation** → application of chain rule of calculus to tensors with a computational graph with caching **(differential programming with automatic differentiation)** 
## Focus on backpropagation

![](pictures/Pasted%20image%2020250206174939.png)

- **Forward Pass:**
    - The input data is passed through the network (layer by layer) to generate an output.
    - The network’s prediction is then compared with the actual target using a loss (or cost) function, which quantifies the error.
    
- **Computing the Error:**
    - The loss function measures how far the network’s prediction is from the actual target.
    - This error is the starting point for backpropagation.
    
- **Backward Pass (Backpropagation):**
    - The algorithm propagates the error backward through the network.
    - Using the chain rule from calculus, it computes the gradient of the loss function with respect to each weight. This tells us how much each weight contributed to the overall error.
    - These gradients indicate the direction and rate at which each weight should change to reduce the error.
    
- **Weight Update:**
    - Once the gradients are calculated, an optimization method (typically gradient descent or one of its variants) is used to update the weights.
    - The weights are adjusted by moving them in the direction opposite to the gradient (since we want to minimize the loss).
    
- **Iteration:**
    - This process (forward pass, error calculation, backward pass, and weight update) is repeated over many iterations (epochs) using batches of training data.
    - Over time, the network’s predictions become more accurate as the weights converge to values that minimize the loss.

![](pictures/Pasted%20image%2020250206180111.png)
![](pictures/Pasted%20image%2020250206180154.png)
![](pictures/Pasted%20image%2020250206180324.png)
# Forward pass

Basically follow the signs in the circles (random values were assigned to x and y)

![](pictures/Pasted%20image%2020250206180416.png)

# Backward pass (lotssss of pictures)

Basically, see the partial derivative wrt the previous variable for all variables

1. ![](pictures/Pasted%20image%2020250206180626.png)
2. ![](pictures/Pasted%20image%2020250206180732.png)
3. ![](pictures/Pasted%20image%2020250206180748.png)
4. (this is the same for the gradient of L on x)![](pictures/Pasted%20image%2020250206180904.png)

![](pictures/Pasted%20image%2020250206180946.png)

![](pictures/Pasted%20image%2020250206181212.png)
![](pictures/Pasted%20image%2020250206181223.png)

--------

![](pictures/Pasted%20image%2020250206181301.png)

![](pictures/Pasted%20image%2020250206181338.png)

-------

![](pictures/Pasted%20image%2020250206181448.png)








