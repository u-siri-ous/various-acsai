**Given we don't have an explicit loss of knn, how do we calculate the training error?**

![](pictures/Pasted%20image%2020250203094004.png)

![](pictures/Pasted%20image%2020250203094055.png)
# Impurity 

The concept of impurity is similar to loss, in the sense that they both quantify how well the model or split is performing in terms of classification or prediction accuracy

Impurity metrics are specific to decision trees

![](pictures/Pasted%20image%2020250203094413.png)

![](pictures/Pasted%20image%2020250203095014.png)
# Entropy

Entropy is a way to quantify the impurity or disorder in a dataset

- **High Entropy**: Indicates high randomness or impurity
	- The data points are distributed across different classes.

- **Low Entropy**: Indicates low randomness or high purity
	- The data points are concentrated in a few classes.

![](pictures/Pasted%20image%2020250203095407.png)
![](pictures/Pasted%20image%2020250203095933.png)
![](pictures/Pasted%20image%2020250203095659.png)

(we use -log to make sum positive)
# Cross-Entropy

**Cross-entropy** is a measure from information theory that quantifies the difference between two probability distributions, to evaluate **how well the predicted probability distribution matches the true probability distribution**

![](pictures/Pasted%20image%2020250203105037.png)
![](pictures/Pasted%20image%2020250203105148.png)![](pictures/Pasted%20image%2020250203105103.png)

- **Cross-Entropy**: Measures the total entropy (or uncertainty) when using the predicted distribution instead of the true distribution.
    
- **KL Divergence**: Measures the difference between the true distribution and the predicted distribution, indicating the "extra" information needed due to the approximation.

---------
# Learning Decision Trees to reduce impurity - Classification

**In order to find a good tree, we should minimize the entropy**
We do a greedy approach as the problem is NP-hard

But what is a decision tree? 

![](pictures/Pasted%20image%2020250203110321.png)

![](pictures/Pasted%20image%2020250203110446.png)
# Greedy approach to decision tree

- Resort to a **greedy heuristic**:
	1. Start from an empty decision tree
	2. **[Greedy Step]** Choose:
		1. _A) a dimension among axes 
		2. B) **BEST** splitting value that minimizes the Impurity function on the chosen axes
			- When Impurity is Entropy we **minimize the entropy** also known as **maximizing the Information Gain**
			- if we want a random decision, use inverse transform sampling
	3. Once A) and B) are chosen save them as "parameters" of the model
	4. Apply **recursion to the sub-problem**.

- **Termination**:
    1. if no examples – return the **majority** from the parent (Voting such as in k-NN).
    2. else if all examples are in the same class – return the class **(pure node)**.
    3. else we are not in a termination node (keep recursing)
    4. **[Optional]** we could also terminate for some **regularization** parameters
## Information gain

**Information gain** is a measure used in decision trees to evaluate the effectiveness of a split

It quantifies the reduction in entropy (uncertainty or impurity) after the dataset is split based on a certain feature

**The goal is to maximize it**$$IG(Y|X) = \underbrace{H(Y)}_{\text{prior entropy in the node}} - \underbrace{H(Y|X)}_{\text{new, conditioned on the split}} \qquad \forall~X~~\text{splitting attribute}$$H(Y∣X) represents the **conditional entropy** of Y given X

**This measures the amount of uncertainty or entropy remaining about Y after knowing the value of X** (the entropy calculation is based on the distribution of Y after the dataset has been divided according to the attribute X)

![](pictures/Pasted%20image%2020250203112540.png)

The second term is H(Y|X)

-------------
# Summary

![](pictures/Pasted%20image%2020250203124139.png)
![](pictures/Pasted%20image%2020250203124740.png)

------------
# Decision Trees for Regression

![](pictures/Pasted%20image%2020250203124259.png)
Approximate the underlying function as a **piecewise constant function with discontinuities (non-smooth)**

![](pictures/Pasted%20image%2020250203125828.png)

We can also prune the tree to avoid overfitting

--------
# Pros and Cons of Decision trees

![](pictures/Pasted%20image%2020250203113753.png)