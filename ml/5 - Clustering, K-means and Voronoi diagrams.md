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

Assign each datapoint to the closest cluster centroid $$y_i = argmin_k||x_i + \mu_j||^2_2$$and update centroids $$\mu_k \leftarrow \frac{\sum_{i=1}^n 1\{y_i=k\}x_i}{\sum_{i=1}^n 1\{y_i=k\}}$$where $1\{y_i = k\}$ is the **indicator function** defined as 
$$1\{y_i = k\} = \begin{cases}
1 & \text{ if } y_i = k \\
0 & \text{ if } y_1 \neq k
\end{cases}$$this expresses that we have to consider the point when calculating mean iff the label corresponds to the current centroid
### Third step - update

* Move each cluster centroid to the mean of the points assigned to it
* Based on the set of labels, we recalculate each cluster centroid as the mean of all $x_i \text{ such that } y_i = k$ 

we do this until **centroids don't change anymore**, this is known as **convergence** of K-means

![](pictures/Pasted%20image%2020240209101228.png)

![](pictures/Pasted%20image%2020240209101315.png)

-----
# Limitations of K-means

* K-means if strongly limited by how the initial k is sampled or chosen
* It's not consistent. Solutions can change by changing k over the same set of points
* Sensitive to scaling and outliers

-----
# K-means as a loss minimization technique

## Distortion function


