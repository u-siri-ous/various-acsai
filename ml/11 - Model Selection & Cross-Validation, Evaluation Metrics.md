# Fitting errors - Bias & Variance Error proof

The generalization error can be decomposed in three main parts:
1. Bias error → Underfit
2. Variance error → Overfit
3. Noise in data → cannot be controlled

![[../pictures/Pasted image 20250205102337.png]]
![[../pictures/Pasted image 20250205102552.png]]

in second to last step rule is applied to E(eps^2) = V(eps) + E(eps)^2
this is equal to tau^2 by definition

In the last step, we consider f(x*) as constant because it's the true value at point x*, while fn(x*) is the estimate (so NOT the true value)

![[../pictures/Pasted image 20250205103810.png]]

----------------
# From the definition of SL to Bayes optimal classifier

The Bayes optimal classifier represents the theoretical best possible classifier for a given problem, based on the true underlying probability distribution of the data

It achieves the lowest possible error rate, also known as the Bayes error rate

![[../pictures/Pasted image 20250205103956.png]]
![[../pictures/Pasted image 20250205104015.png]]

In this way, **bias and variance errors go to 0** → we rely on the true distribution D!!
# Learning and validation

In order to learn, **we need to lower the cost/loss fcn BOTH in test and train** → reduce error over the training set$$\mathcal{L}(\underbrace{\hat{y}}_\text{predicted}, \underbrace{y}_\text{ground truth})\quad \text{where}\quad \hat{y}=h_{\theta}(\mathbf{x}) $$so **we want to do well on unseen samples** → **lower the generalization error**
## Single Held out split - Train on train, test on test

![[../pictures/Pasted image 20250205104934.png]]

![[../pictures/Pasted image 20250205105113.png]]

When you repeatedly tune your model and validate it on the same validation set, **you risk overfitting to the validation set**

This means that your model starts to perform exceptionally well on the validation set, but its performance on new, unseen data (like a test set or real-world data) might actually be worse

![[../pictures/Pasted image 20250205105931.png]]

**A solution to this is cross-validation**
## Nested cross-validation - reprise on k-fold CV

![[../pictures/Pasted image 20250205110212.png]]

**Which value for K?** → For larger $K$, the **error estimation tends to be more accurate**, but computation time will be greater

Typical choices for `K` are `2, 5, 10`

**What if we have so little data that even K-fold won't work?**
## Leave-One-Out (LOO) Cross-Validation

A type of k-fold cross-validation where the number of folds equals the number of data points → $K = N$

It performs **single data point validation**, thus the model is trained and tested $N$ times

![[../pictures/Pasted image 20250205113843.png]]

It often overfits to data and is more computationally expensive than k-fold CV

![[../pictures/Pasted image 20250205114053.png]]

----------
# What happens after Cross-Validation?

After running cross validation, you have **2 choices.**

1. You can either select **one of the K trained models as your final model** to make predictions

2. You can train a **new model on all the data, using the hyperparameters selected by cross-validation.**

_2. is generally preferred to 1_

![[../pictures/Pasted image 20250205114757.png]]
![[../pictures/Pasted image 20250205114801.png]]
### CV works if the data is sampled i.i.d. from same distribution!!

This hypothesis is used a lot in ML, but reality is often disappointing

![[../pictures/Pasted image 20250205115232.png]]
![[../pictures/Pasted image 20250205115156.png]]

-------------------
# Hyperparameter tuning of an estimator

Hyperparameters are parameters that are not directly learnt within estimators → **not derived from data**
## General form of HP search

A search of HP consists of:

- an estimator **(example: Decision Tree)**
- a parameter space; **($k \in [1,3,5,7,11]$ )**
- a method for searching or sampling candidates; **(exhaustive grid search)**
- a cross-validation scheme; **(10-fold CV)**
- a score function **(accuracy)**

### What happens if we have to chose/validate 2 hyper-params?

![[../pictures/Pasted image 20250205120243.png]]
### Introduce MID as hyperparameter

![[../pictures/Pasted image 20250205120409.png]]
To answer this:

- You have 3 values for tree depth (1, 2, 3).
- You have 2 values for minimum impurity decrease (0.01, 0.1).

So, the total number of hyperparameter combinations is: $$3 \text{ (depth values)} \times 2 \text{ (impurity values)} = 6 \text{ combinations}$$For each combination, you perform 10-fold cross-validation, so the total number of models trained is: $$6 \text{ (combinations)} \times 10 \text{ (folds)} = 60 \text{ models}$$So, you train 60 models in total

# Methods for searching

1. **Exhaustive Grid Search** (brute force all the HP in CV given predefined ranges) → **Mostly used**
2. **Randomized Parameter Optimization** (distribution over parameters $\rightarrow$ sample; sample size or budget)
3. **Searching for optimal parameters with successive halving** → tournament among candidates parameter
## Grid Search

![[../pictures/Pasted image 20250205121245.png]]

## Randomized Parameter Optimization

Randomized search allows you to set a **budget** **independent of the number of parameters and possible values**

This means **you can control how many combinations you want to test, regardless of how many different hyperparameters or values you have**

Randomized search can handle extra parameters gracefully without wasting resources on non-influential ones

## Successive Halving

**Idea:** Successive halving (SH) is like a **tournament among candidate parameter combinations**

**SH is an iterative selection process where all candidates (the parameter combinations) are evaluated with a small amount of resources at the first iteration**

**Only some of these candidates** (usually half) **are selected for the next iteration, which will be allocated more resources**

For parameter tuning, the resource is typically the `number of training samples`, but it can also be an arbitrary numeric parameter such as `n_estimators` in a random forest

![[../pictures/Pasted image 20250205143543.png]]
![[../pictures/Pasted image 20250205143706.png]]

-----------------
# Evaluation Metrics

Means to quantify the gap between desired performance and current performance, in order to evaluate how well the model is performing along with the cost fcn

![[../pictures/Pasted image 20250205144147.png]]

# Confusion matrix, accuracy, precision & recall
## Confusion matrix

The matrix mentioned below is called the **confusion matrix**

It provides a summary of the prediction results on a classification problem and allows you to see how well your model performed in terms of correctly and incorrectly classified instances for each class
### Components of a Confusion Matrix:

1. **True Positives (TP)**: The number of instances correctly predicted as the positive class.
2. **True Negatives (TN)**: The number of instances correctly predicted as the negative class.
3. **False Positives (FP)**: The number of instances incorrectly predicted as the positive class (also known as **Type I error**).
4. **False Negatives (FN)**: The number of instances incorrectly predicted as the negative class (also known as **Type II error**).

The aim is to have a **diagonal confusion matrix** → every point classified correctly

**Changing the confusion matrix by changing the threshold of tp and tn changes the metrics!!!**

![[../pictures/Pasted image 20250205150332.png]]

## Accuracy

![[color is ground truth while positioning is prediction|[../pictures/Pasted image 20250205144243.png]]

Accuracy is basically how many got labeled right, over total number of samples
## Precision

Precision tells us the ratio of true positives among all **predicted positives** (so also false positives, actually negatives) → quality of positive predictions

![[../pictures/Pasted image 20250205145350.png]]
## Positive Recall 

Positive Recall (aka **sensitivity**) tells us the true positive rate over all the positives → so, all correctly predicted positives + **incorrectly** predicted negative (actually positives)

**This is often called RECALL, and the only one considered in evaluation**

![[../pictures/Pasted image 20250205145704.png]]
## Negative Recall (with better picture)

Negative recall (aka **specificity**) tells us the true negative rate

![[../pictures/Pasted image 20250205150243.png]]

![[../pictures/Pasted image 20250205150156.png]]
## F1 score

The F1 score is a cohesive measure of performance useful for imbalanced datasets

![[../pictures/Pasted image 20250205150539.png]]

-----------
# ROC & AUC

ROC is the Receiver Operating Characteristic curve

Used to plot the balance of **true positive rate** (recall) against the **false positive rate** at various threshold settings

AUC or Area Under ROC is a single scalar, ranging from 0 to 1:

- **AUC = 1**: Perfect model with no false positives or false negatives.
- **AUC = 0.5**: Random classifier with no discrimination power → aka **chance level**
- **AUC < 0.5**: Worse than random, indicating the model is misclassifying more than classifying correctly.

![[../pictures/Pasted image 20250205151559.png|450]]

---------------
# Precision-Recall Curve

This also helps for when classes are imbalanced

![](pictures/Pasted%20image%2020250205152121.png)
### Interpretation:

- **High Precision, Low Recall**: Indicates that the model is making few mistakes but missing many positives
- **High Recall, Low Precision**: Indicates that the model is identifying most positives but with many false positives.
- **Balanced Precision and Recall**: Indicates an optimal trade-off where both precision and recall are reasonably high

------------
![](pictures/Pasted%20image%2020250205153152.png)











