Clustering has the objective to find a partition of the data in clusters, with each of them sharing at least one characteristic that sets it apart from the others

Further formalizing the problem:

**Inputs**:
* a set of points $\{x_1, x_2, ..., x_n\}$ in a d-dimensional space $\mathbb{R}^d$
* a number of clusters to find $k$

**Outputs**:
* a set of **centroids** $\rightarrow$ a centroid is the mean vector of a cluster of data points in a high-dimensional space $\{\mu_1, \mu_2, ...,\mu_n\} \in \mathbb{R}^d$  (vectors)
* a set of scalar **labels** mapping data points to centroids $\{y_1, y_2,...,y_n\}$ (i.e. expressing the info "data point $x$ is mapped to centroid $\mu$")

We want to find sets of points with the **least variance** $\rightarrow$ **NP hard**
# K-means algorithm (Lloyd's or Naive method)

**Given a dataset, we aim to group it into a given K clusters**
### First step - finding reference centroids

These are found from random sampling of the set of centroids $\{\mu_1, \mu_2, ...,\mu_n\} \in \mathbb{R}^d$
### Second step - assignment

Assign each datapoint to the closest cluster centroid $$y_i = argmin_k||x_i + \mu_j||^2_2$$This means finding the index k of the cluster centroid μ_j that minimizes the squared Euclidean distance to the data point x_i

Essentially, **it's assigning each data point to the closest cluster centroid**

and update centroids $$\mu_k \leftarrow \frac{\sum_{i=1}^n 1\{y_i=k\}x_i}{\sum_{i=1}^n 1\{y_i=k\}}$$where $1\{y_i = k\}$ is the **indicator function** defined as 
$$1\{y_i = k\} = \begin{cases}
1 & \text{ if } y_i = k \\
0 & \text{ if } y_i \neq k
\end{cases}$$this expresses that we have to consider the point when calculating the average iff the data point x_i is assigned to cluster k 

**By dividing the sum of the data points by the count of the data points, we obtain the new position of the centroid mu_k**
### Third step - update

* Move each cluster centroid to the mean of the points assigned to it
* Based on the set of labels, we recalculate each cluster centroid as the mean of all $x_i \text{ such that } y_i = k$ 

we do this until **centroids don't change anymore**, this is known as **convergence** of K-means

![](pictures/Pasted%20image%2020240209101228.png)

![](pictures/Pasted%20image%2020240209101315.png)

-----
# Limitations of K-means

* K-means if strongly limited by how the initial k is sampled or chosen
* It's not consistent. Solutions can change by changing k over the same set of points (even becoming exponential)
* Sensitive to scaling and outliers

-----
# K-means as a loss minimization problem

We can define a **loss function** to better formalize the k-means algorithm

This is similar to PCA, as it uses the sum of squared distances method$$L(\mu, y; D) = \sum_{i=1}^{N} \| x_i - \mu_{y_i} \|_2^2 = \sum_{i=1}^{N} \min_{k \in K} \left( \| x_i - \mu_k \|_2^2 \right)$$where:
- L(μ,y;D): The loss function or cost function, measuring the sum of squared distances.
- D: The dataset of N points x_i
- N: The total number of data points.
- x_i: The i-th data point.
- μ_(y_i): The centroid of the cluster to which the i-th data point x_i is assigned. 
	- Here, y_i represents the cluster index to which x_i is assigned.
- ∥⋅∥_2: The Euclidean norm (distance).
- μ_k: The centroid of cluster k.
- K: The set of all clusters.

---------
# Convergence

**For any dataset D and any number of clusters K, the K-means algorithm converges (local optimum) in a finite number of iterations**, where convergence is measured by the loss ceasing the change of centroids

The goal is to show that the assignment and update step can never increase the value of the loss function
### Assumptions

**The possible assignments to y and µ can only take a finite number of values**

* y is a discrete value 
* µ is all possible means of a subset of data (**it is not infinite**)
* The loss L is lower bounded by zero by ℓ2 property

**Together, it means that L can only decrease a limited number of times before reaching its minimum value** (cannot decrease indefinitely)

![](pictures/Pasted%20image%2020250117104623.png)
The distance between x_i and its new centroid μ_b is less than or equal to the distance to its old centroid mu_a, by definition

Therefore, this step cannot increase the loss

![](pictures/Pasted%20image%2020250117104803.png)
The mean minimizes the sum of squared distances between the points and the centroid, reducing the loss function

Convergence is not guaranteed to be "fast", you may need either:
1. heuristic for selecting the initial random guess or 
2. select the best fit over multiple random initializations (instead of a single random sampling)

Or use **mini-batch k-means**

--------------
# Furthest-First Heuristic

**Idea**: Semi-random initialization by picking initial means as far from each other as possible

**Steps**:
1. Randomly select the first centroid
2. Iteratively select the next centroid as the point farthest from the nearest previously chosen centroid

![](pictures/Pasted%20image%2020250117110654.png)
- Since outliers are far away, they are likely to be selected early in the initialization process
- This results in some of the initial centroids being placed at outliers, which do not represent the main distribution of the data
![](pictures/Pasted%20image%2020250117110722.png)

--------
# K-means++

**K-means++** is an improved method for initializing the centroids in the K-means clustering algorithm

**The goal is to enhance the clustering performance by choosing initial centroids that are more spread out and diverse**

Sample randomly but **proportionally according to the distance between centroids**$$Pr[\mu_k = x_m] \propto min_{k<k’} ||x_m - \mu’_k ||_2^2$$![](pictures/Pasted%20image%2020250117111639.png)![](pictures/Pasted%20image%2020250117111813.png)
This ensures that points further from existing centroids are more likely to be chosen

Note that **randomness(K-means++) > randomness(Kmeans + Furthest-first)** because with Furthest-first we select at random only at the start; then all the rest is deterministic

With Kmeans++ at each cluster selection there is stochasticity involved

## Inverse Random Sampling

Inverse transform sampling is a method used to generate random samples from a probability distribution, used to select the next centroid based on the distances computed during the initialization process
### Steps

![](pictures/Pasted%20image%2020250117114355.png)
![](pictures/Pasted%20image%2020250117114405.png)

![](pictures/Pasted%20image%2020250117114635.png)

------------
# Choosing K

**Goal**: find a k that gives large gap between k-1-means and k-means cost function

A number of “information criteria” have been proposed to try to balance the goodness of fit (how well the model fits the data) with the complexity of the model, by "regularizing" K

![](pictures/Pasted%20image%2020250117115655.png)

### K-means Complexity 

Given:
- N: Number of data points.
- D: Number of dimensions.
- KK: Number of clusters.

**Initialization**: O(nd) One pass over data to select k centers, So O(ndk) time in total
**Lloyd’s method**: O(ndk) 
* Exponential # of rounds in the worst case (bad initialization)

Expected polynomial time in the smoothed analysis (non worst-case) model!

![](pictures/Pasted%20image%2020250117125207.png)
