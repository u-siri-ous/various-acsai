# The Basis function

![[../pictures/Pasted image 20250205213525.png]]

This means that the basis function does NOT change the feature space → **the dimensionality does NOT increase**

![[../pictures/Pasted image 20250205213635.png]]

This can be thought as a **feature map** → **A basis function is a function used to map input data into a new space where it is easier to model the underlying patterns and relationships**

Let's consider the one dimensional case

We have already seen that we could change the feature $x$ to add the bias term ${x}\doteq [x,1]$$$\begin{align}

{x} &= \begin{bmatrix}

       x \\

       1

     \end{bmatrix}

     \rightarrow \quad

   {\phi}({x}) = \begin{bmatrix}

       x^2\\

       x \\

       1

     \end{bmatrix}

\end{align}$$So input dimension is $d=2$ then output dimension after ${\phi}(\cdot)$ is $m=3$.

**In this case, we used a second order polynomial to lift up the features**$${\phi}_m({x}) = x^m$$![[../pictures/Pasted image 20250205212252.png]]

This is the basis for 
# Polynomial Regression

![[../pictures/Pasted image 20250205212855.png]]
![[../pictures/Pasted image 20250205213736.png]]

m>d means the dimensionality **increases**

Note that applying linear regression to non-linear data is indeed possible, but it also ensures you get a massive training error (imagine fitting a line to a parabola)

Also, increasing m *too* much can let us incur in the curse of dimensionality!!!

![[../pictures/Pasted image 20250205215010.png|500]]

**We need to find the sweet spot for m which fits the data good but avoids overfitting**![](pictures/Pasted%20image%2020250205215050.png)
## Problems of PR

![[../pictures/Pasted image 20250205214750.png]]

The concept of a basis function is simple and scales well to higher dimensions

However, the risk of losing control of dimensionality is real, and it goes hand-in-hand with overfitting

A solution to this is:
# Weight Decay - $l_2$ regularization

Weight decay **penalizes** large weights in the model, by adding a **regularization term** $\lambda$ to the loss function or to GD

This prevents overfitting and improves generalization

![](pictures/Pasted%20image%2020250205215336.png)

![](pictures/Pasted%20image%2020250205220204.png)







