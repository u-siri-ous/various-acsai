# Introduction

SL is another learning paradigm dealing with labeled data, as opposed to UL

**The goal of supervised learning is to find relations and association between pairs of datapoints paired with a label**, and to find a fcn that will eventually be able to label data automatically

We want the difference between this fcn and the true label to be minimized as much as possible (with a loss fcn)
# Classification vs Regression

These are the two main tasks of SL

1. Regression → y is a continuous, real value
2. Classification → y is a categorical variable (either binary or multi class classification)
## Parametric models 

These models assume that the data follows a specific distribution, and they summarize the data with a fixed set of parameters

The number of parameters is fixed with respect to the training size. We try to "squeeze" the information of the training set into the parameters useful for the task at hand

An example is **linear regression** 
## Nonparametric models - Instance based learning

If non-parametric, then the way the model classifies/regresses a value is different and it is **NOT encoded** in some form of parameters, and they can grow with the training size

Non-parametric models assume that the data distribution cannot be defined in terms of such a finite set of parameters (assumed infinite dimensional)

---------------------
# Formalizing SL

3. The performance of the learning algo is measured on test data (unseen - unlabeled)
4. There should be a strong relationship between the data that our algorithm sees at training time and the data it sees at test time

In order to accomplish 1. we need to define a **loss fcn** which measures the **gap between the prediction and the ground truth**

This is decided based on the **task at hand** (i.e. there's no universal way to choose a loss fcn)

**A good loss fcn will decrease over time in both train and test data**

![](pictures/Pasted%20image%2020250202163723.png)

----------
# Probabilistic modeling of SL

The relationship between datapoints and labels can be seen as a probability distribution $\mathcal{D}$ over **input/output pairs** p(x, y) 

$\mathcal{D}$ is that it gives a high probability to reasonable (x, y) pairs, and a low probability to unreasonable (x, y) pairs

The distribution is assumed to be **random if D is unknown**

- An image X [H X W] dimensional that takes values `P=[0,1,2]`can be combined in $\mid P\mid^{(H\times W)}$ ways
- This is known as the sample space

Based on training data, we need to **induce** a function $f$ that maps new inputs $x$ to corresponding prediction $\hat{y}$, with the aim of reducing L in future samples taken from D

Formally, it’s **expected loss $\epsilon$ over $\mathcal{D}$ should be as small as possible**:
$$\epsilon \triangleq \mathbb{E}_{(x, y) \sim \mathcal{D}}[\mathcal{L}(y, f(x))]=\sum_{(x, y)} \underbrace{\mathcal{D}(x, y)}_{\text{weight/prob}} \underbrace{\mathcal{L}(y, f(x))}_{\text{function}}$$The expected loss is the average loss over **all** possible input-output pairs (x, y) drawn from the distribution D

>Think of D(x, y) as a weight assigned to each possible pair (x, y)
>The higher the weight, the more common that pair is in the distribution

**Expected loss represents the overall performance of the model across the entire distribution**

-------------
# Empirical Risk Minimization - ERM

![](pictures/Pasted%20image%2020250202170447.png)

* **ERM** **aims to find the model that minimizes the average loss across all training samples**, treating each sample with equal probability
	* This approach ensures **uniform treatment of data** and provides a practical way to train models in the **absence of prior knowledge about sample importance**
* ERM operates under the weak law of large numbers, which states that as the number of samples N increases, the empirical average (observed average) converges to the expected average (true average) ⇾ **approx vanishes as N goes to infinity**

>Note: If you take the weighted average instead, it is a way to saying this sample is more probable or put more emphasis on a sample instead of another

![](pictures/Pasted%20image%2020250202172304.png)
# Bias-Variance Tradeoff

The **bias error** is produced by weak assumptions in the learning algorithm
* **High bias** can cause an algorithm to **miss the relevant relations between features and target outputs** → Problem known as `underfitting`

The **variance** is an error produced by an **oversensitivity to small fluctuations in the training set**
* **High variance** can cause an algorithm to **model the random noise** in the training data, rather than the intended outputs → Problem known as `overfitting`

![](pictures/Pasted%20image%2020250202172637.png)

--------------
# k-Nearest Neighbors - KNN

KNN is a non-parametric model, with the inductive bias on unseen data by comparing it to the k-nearest neighbors

This is an improvement of the similar **nearest neighbors algo**
## Vanilla nearest Neighbors

1. Store the whole training set and labels at training time
2. Get a test example $\hat v$ at test time
3. Predict its label finding the training example $x$ **most similar** to $\hat v$
## Most Similar, how?

**The most similar point minimizes the distance between the points on a vector space** $$i^*=\arg\min_{i\in\mathcal{X}} d(x,\hat v).$$![](pictures/Pasted%20image%2020250202174818.png)
![](pictures/Pasted%20image%2020250202174943.png)

# Definition of KNN

![](pictures/Pasted%20image%2020250202175554.png)

![](pictures/Pasted%20image%2020250202175416.png)

![](pictures/Pasted%20image%2020250202175838.png)
The key to make KNN is to **choose the right distance metric**

For example:
- Euclidean distance treats each feature as **equally important** (each axis in the vector)
- However **some features (dimensions) may be much more discriminative than other features**, and **high ranges and outliers falsify the distance**

![](pictures/Pasted%20image%2020250202182916.png)
or
![](pictures/Pasted%20image%2020250202183029.png)
before feeding data to the algo (ma insomma usa standardscaler())

---------

![](pictures/Pasted%20image%2020250202183342.png)

![](pictures/Pasted%20image%2020250202183355.png)

------
# The impact of k

**Definition**: k is defined as a hyperparameter, that is, a parameter whose value controls the learning process and determines the value of the model parameters that the learning algorithm must learn

* k=1 → There is a risk of **overfitting** because we base our decisions on too little information. (NN)
* k≫1→ We might have good performance because we do not look only at the closest one but look around kk values (smooth out the result by imposing regularization).
	* With binary classification, it is better that kk is odd to avoid ties.
* k=∣D∣ → **Underfitting** because we take all the values at once and therefore do not minimally calculate the small variations but only the classes that represent the majority. (Best Constant Predictor)

**The sweetspot is to use cross-validation to choose k**, making it grow at a controlled rate with the general rule of thumb $$k < \sqrt{N}$$
### Steps to Use Cross-Validation to Choose k:

1. **Prepare Your Data**:
    - Split your dataset into features (X) and labels (y).
        
2. **Select a Range of** k **values**:
    - Decide on a range of k values to test (e.g., from 1 to 20).
        
3. **Perform k-Fold Cross-Validation**:
    1. Divide your data into j folds (e.g., 5 or 10 folds).
        
    2. For each k value:
        - Train the k-NN model using j−1 folds.
        - Validate the model on the remaining fold to tune k.
        - Calculate and store the accuracy (or another performance metric).
            
4. **Evaluate Performance**:
    - For each k value, compute the average performance across all folds.
        
5. **Select the Best** k:
    - Identify the k value with the highest average performance (accuracy, precision, etc.).

-----------

![](pictures/Pasted%20image%2020250202183552.png)

![](pictures/Pasted%20image%2020250202183610.png)


















