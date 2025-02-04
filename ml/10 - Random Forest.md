A **Random Forest** is an ensemble learning method used for classification, regression, and other tasks

It operates by constructing multiple decision trees during training and outputting the class (classification) or average prediction (regression) of the individual trees
# Ensemble methods

Ensemble methods aim to mitigate **overfitting** of decision trees

Each tree is trained on a random subset (**bootstrap sample**) of the data and features, this randomness helps to ensure that the trees are not correlated and reduces the risk of overfitting

1. Train different classifiers $h(\cdot)_{{D}_j}$ on **$M$ different datasets** $\{{D}_1,\ldots,{D}_m\}$ still sampled from the same generative process $\underbrace{\{x_i,y_i\}_{i=1}^N}_{\text{known}} \sim \underbrace{\mathcal{\mathcal{D}}}_{\text{unknown}}$
2. Average the results of different classifiers (**bootstrap aggregation** aka **bagging**): $$
h({x}) = \frac{1}{M}\sum_{j=1}^M h({x})_{{D}_j}
$$![](pictures/Pasted%20image%2020250204132227.png)

!! Allowing repetition in picking the samples is crucial (later why)
# From Decision Trees to Random Forest

![](pictures/Pasted%20image%2020250204133108.png)

If you have a dataset with D=100 features, setting K=10 means that at each split, the decision tree will consider only 10 randomly selected features out of the 100 (that's why K << D)

The number of features becomes **fixed** and $= \sqrt{D}$, but we need to tune for M (the number of trees)

**Features that appear near the top of the decision tree influence the final prediction for a larger portion of the input samples** (a split at the top affects more samples and is more important in the outcome) ⇾ by looking at how many samples (data points) are affected by a particular feature, we can get an idea of **how important that feature is in making predictions**

**When you average the predictive performance estimates from multiple, randomly created decision trees, it reduces the variability of those estimates** → **helps to identify the most important features**!! Known as:
### MDI - Mean Decrease in Impurity

![](pictures/Pasted%20image%2020250204140807.png)

--------

**What about the part of the dataset that doesn't get sampled?** It's called the Out-Of-Bag Dataset (OOB Dataset) 
# Out-Of-Bag Evaluation

The key idea is that the data points that were not used in the construction of a particular tree can be used as a **validation set for that tree**, without the need for a separate validation set (unbiased validation)

Each sample in the dataset is used as an OOB sample for several trees in the Random Forest → each OOB sample will have predictions from multiple trees

* For classification tasks, determine the final prediction by majority voting among the OOB predictions for each sample
- For regression tasks, compute the final prediction by averaging the OOB predictions for each sample

The OOB error rate is calculated by comparing the OOB predictions with the actual values of the OOB samples

* For classification tasks, the OOB error rate is the proportion of OOB samples that were misclassified.
- For regression tasks, the OOB error rate is typically measured by the mean squared error (MSE) or mean absolute error (MAE) between the OOB predictions and the actual values.

This provides an estimate of the model's **generalization error**, which indicates how well the model is likely to perform on unseen data → train error - test/valid error
### OOB Evaluation:

- Removes **the need for a validation set**
- It gives you a **quick way to estimate the number of ensembles**
- A quick good hint of how the forest **generalization error** could be (without doing K-fold cross-validation)









