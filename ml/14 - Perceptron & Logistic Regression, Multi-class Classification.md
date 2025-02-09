# Perceptron 

The perceptron is a simple type of NN, consisting on the following components:

![[../pictures/Pasted image 20250205221625.png]]

![[../pictures/Pasted image 20250205221120.png]]In this case, the activation fcn is the **step** function

![[../pictures/Pasted image 20250205221250.png]]
![[../pictures/Pasted image 20250205221449.png]]
## Learning a perceptron

![[../pictures/Pasted image 20250205221958.png]]

**The perceptron will converge to a non-optimal solution** (or separation of the (hyper)plane)

But if the data is not **linearly separable**, it does not work

To say that data is **linearly separable** means that you can draw a single straight line (in two dimensions), or a hyperplane (in higher dimensions), to separate the data points into distinct classes without any errors

---------
# Logistic Regression - Logit

Logistic regression is a statistical method used for binary classification tasks

Despite its name, it's actually a type of linear model for classification 

**The goal of logistic regression is to predict the probability that a given input belongs to a particular class**:

![[../pictures/Pasted image 20250205225210.png]]

![[../pictures/Pasted image 20250205225844.png]]

In general, the threshold is **0.5** to map it to a predicted class.$$\frac{1}{1+\exp^{-{\theta}^T{x}}} > 0.5$$The logit model does **not** have a closed form solution as best weights and biases are found through iterative methods

![[../pictures/Pasted image 20250205230330.png]]
# Generalized linear model

The GLM is a generalization of linear regression that allows for the dependent variable to be not normally distributed → **choice of distribution based on y**

![[../pictures/Pasted image 20250206092943.png]]

![[../pictures/Pasted image 20250206093325.png]]

![[../pictures/Pasted image 20250206093425.png]]

We **maximize log-likelihood** to find the best fit parameters
# MLE for LR - Update rule for LR

![[../pictures/Pasted image 20250206093844.png]]
![[../pictures/Pasted image 20250206093919.png]]
![[../pictures/Pasted image 20250206094045.png]]
Calculating the gradient of log-likelihood and derivative of sigmoid, we get:

![[../pictures/Pasted image 20250206094213.png]]

Finally:

![[../pictures/Pasted image 20250206094514.png]]

We need to simplify and expand products, getting:

![[../pictures/Pasted image 20250206094902.png]]
![[../pictures/Pasted image 20250206095021.png]]

GD gives you a global minimum/maximum on convex functions → **optimization is easy**

-------------------
# Information theory on Log Loss

A slight modification to the binary classification problem:

* The problem at hand is binary classification, where the target variable y can take one of two values: 0 or 1

* Instead of representing the target y as a single value (0 or 1), we can represent it as a vector $\vec{y}$ (of dim=2 for binary classification and dim=n for multi-class)

- ${y} \in \{0,1\}^K$ with ${y}$ being a **Categorical distribution** where the mass is all concentrated in the index of the ground-truth label ⇾ **the probability is assigned entirely to the correct class and zero to the other class**
	- Only `[1,0]` and `[0,1]` are possible for 2 classes since it has to be a prob. distribution
	- `[1,1]` is not a prob. distribution (because both classes **cannot** be assigned 1)

#### The concept above is known as One-Hot Encoding

# Comparing One-Hot encoding and LR

![[../pictures/Pasted image 20250206100755.png]]

It's all a matter of **comparing the prob. distributions!!** (you see where I'm going with this...) 

![[../pictures/Pasted image 20250206100950.png]]

>Note that KL reverts to Cross-Entropy for One-Hot Encoding → **there is no uncertainty in the data!! A label is either 1 or 0**

![[../pictures/Pasted image 20250206101436.png]]
(If the true label for a data point is class 0, the one-hot encoded vector for this label is P(y = 0 | x) = [1,0])
### Maximizing Log-Likelihood and minimizing Cross-Entropy are the same

![[../pictures/Pasted image 20250206101841.png]]

>Note: use full KL for soft labels (like in LR)!!! Not just Cross-Entropy

# One-Hot Encoding in multi-class classification

One-Hot Encoding is just a selector of probability of the model

It will return the probability for which the ground truth is 1

**Used in NN for multi-class classification**

![[../pictures/Pasted image 20250206102559.png]]

--------------
# Multi-class Classification

We need a bridge from binary to multi-class

![[../pictures/Pasted image 20250206103608.png]]
![[../pictures/Pasted image 20250206103633.png]]
Aggregating 3 One vs Rest into one single classifier
### Rules in One vs Rest

![[../pictures/Pasted image 20250206103918.png]]
![[../pictures/Pasted image 20250206103934.png]]
#### Ok, now, how do we do this?

![[../pictures/Pasted image 20250206104008.png]]
# From binary to multi-class, formally

This is all a matter of changing the **decision boundary** from a vector to a matrix where each row manages a class!

![[../pictures/Pasted image 20250206110650.png]]
![[../pictures/Pasted image 20250206110719.png]]
![[../pictures/Pasted image 20250206110805.png]]
![[../pictures/Pasted image 20250206111024.png]]
![[../pictures/Pasted image 20250206111035.png]]

# From vector to matrix

**Decision boundary $\{{w}_k,b_k\}_{k=1}^K$ per class** given K classes.

We can model directly everything with a matrix:$$ \underbrace{{y}}_{\mathbb{R}^{Kx1}} = \underbrace{{W}}_{\mathbb{R}^{K\times d}}\underbrace{{x}}_{\mathbb{R}^{d\times1}} + \underbrace{{b}}_{\mathbb{R}^K}$$or$$ \underbrace{{Y}}_{\mathbb{R}^{Kxn}} = \underbrace{{W}}_{\mathbb{R}^{K\times d}}\underbrace{{X}}_{\mathbb{R}^{d\times n}} + \underbrace{{b}}_{\mathbb{R}^K}$$for multiple points instead of just one → **broadcasting on b for as X is n-dimensional** (b is not a scalar anymore but expanded to match WX)
![[../pictures/Pasted image 20250206112741.png]]
Because argmax jumps between discrete values without smooth transitions and has discontinuities, it's not possible to compute gradients, **making it non-differentiable**

![[../pictures/Pasted image 20250206113724.png|250]]

So we need something that outputs more informative data, given that using argmax may remove classes close to the top, making a point misclassified (there can even be ties!!)
# SoftMax

![[../pictures/Pasted image 20250206113654.png|250]]

SoftMax is a soft selector, using a smooth and differentiable function

It outputs a vector of probabilities, with one value for each class, such that the sum of all values is equal to 1

![](pictures/Pasted%20image%2020250206114006.png)

![](pictures/Pasted%20image%2020250206114017.png)
## Cross-entropy in function of p

![](pictures/Pasted%20image%2020250206114546.png)(the scores are raw and output of the model before softmax)

--------------------
![](pictures/Pasted%20image%2020250206114843.png)

![](pictures/Pasted%20image%2020250206115048.png)
![](pictures/Pasted%20image%2020250206115217.png)

![](pictures/Pasted%20image%2020250206115840.png)



















































