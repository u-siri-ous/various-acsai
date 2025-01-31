# Unsupervised learning

In UL we want to find hidden patterns in unlabeled data -> we need to get the **data distribution and structure** 

![](pictures/Pasted%20image%2020250130102523.png)

-----
# Normal distribution

![](pictures/Pasted%20image%2020250130095844.png)

- $\mu$ is the mean vector
- $\Sigma$ is the covariance matrix
- $k$ is the dimension of the space where $x$ takes values -> x is a k-dimensional random vector

For continuous random variables, we can't determine the probability of a single exact value because the probability is technically zero

Instead, **we look at the probability density function (PDF) to find the probability over an interval**

We need to introduce a distance metric for multivariate distributions, here we use the
# Mahalanobis Distance

This distance metric measures distance between a point P and a distribution D
It generalizes the notion of z-score for multivariate distributions:
#### How many standard deviations away P is from the mean of D

**This distance is zero for P at the mean of D, and grows as P moves away from the mean along each principal component axis**

 If each of these axes is re-scaled to have unit variance, then the Mahalanobis distance corresponds to standard Euclidean distance in the transformed space
 ![](pictures/Pasted%20image%2020250130101740.png)
 
 The Mahalanobis distance is thus unitless, scale-invariant, and takes into account the correlations of the data set 

-----

![](pictures/Pasted%20image%2020250130102050.png)
![](pictures/Pasted%20image%2020250130102106.png)

------------
# Maximum Likelihood Principle

Suppose that we have a model with parameters $\theta$ and a collection of datapoints X

If we want to find the most likely value for the parameters of our model, given the data, that means we want to find $$argmax_\theta = P(\theta|X)$$![](pictures/Pasted%20image%2020250130110044.png)

P(X|$\theta$) is called **the likelihood function** -> likelihood measures how well the chosen model with its parameters explains the observed data

# Maximum Likelihood Estimator (MLE)

The Probability Density fcn can be interpreted in 2 ways:
 1. A fcn of **datapoints**, given the **parameters** -> probability of data given params (P) 
	![](pictures/Pasted%20image%2020250130115438.png)
	![](pictures/Pasted%20image%2020250130120006.png)
 
 2. A fcn of **parameters**, given the **datapoints** -> likelihood of params given data (L)
	![](pictures/Pasted%20image%2020250130115523.png)
	![](pictures/Pasted%20image%2020250130120041.png)
	* Note that the partial derivative can be taken wrt Sigma as well

We can simplify math by using the **log-likelihood** to maximixe L (or minimize -L): 
![](pictures/Pasted%20image%2020250130120844.png)
For multiple data points:![](pictures/Pasted%20image%2020250130120520.png)

Given that we have this property, we can simplify the overall likelihood fcn:

![](pictures/Pasted%20image%2020250130120723.png)
**The const goes away in derivation as well as -1/2 ln |Sigma| as its derivative is 0 wrt mu**

![](pictures/Pasted%20image%2020250130121825.png)

Set:
* x = x - mu
* x^T = (x - mu)^T
* A = Sigma^-1

![](pictures/Pasted%20image%2020250130121839.png)

------
# Summary

![](pictures/Pasted%20image%2020250130122511.png)

By estimating the parameters of an unknown distribution given data, we get an estimate of the density of the data

We use this for:

1. Predicting the probability that a new, unseen data is coming from the same generative process. 
2. This means that by estimating the density, you can test how "anomalous" is an unseen data point (assuming your estimate is a good one). It can be used in Anomaly Detection applications. 
3. Given that you have a density, you can also use the parametric model to generate new data from the density.

!!! Given that the **sample mean** is used, the approximation will not be perfect


