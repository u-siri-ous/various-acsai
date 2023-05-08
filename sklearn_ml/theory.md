### ML babyyyyy

Machine learning is centered around data, and a good dataset is essential for building successful projects. One of the most popular sources for finding datasets is **Kaggle**, which hosts a wide range of datasets that can be used for various purposes.

Both **Scikit-learn (sklearn)** and **PyTorch** are popular libraries used for machine learning tasks. 

Scikit-learn is used for traditional machine learning tasks such as classification, regression, and clustering.

PyTorch is primarily used for deep learning tasks. Both libraries provide a rich set of tools and algorithms that can help in building effective machine learning models.

----------------------------------------------------------------------------
### The Dataset

For a dataset to be effective, it should be heterogeneous, meaning it should contain a lot of intraclass variation and extra class variation

**Intraclass** variation refers to the different variations within a class, which in turn helps the model to learn the subtle differences between objects
>For example, if we're trying to classify cars, the dataset should contain different models, colors, and sizes of cars. This helps the model to understand the different features that distinguish one car from another

**Extraclass** variation refers to the diversity of classes that need to be classified, meaning that the dataset should contain classes that are as diverse as possible

>For instance, if we're trying to classify cars, then we should also include another class like bottles to make it extra class variation. This helps the model to learn the differences between objects in different classes and make more accurate classifications

A dataset has to be balanced in size and in variability

----------------------------------------------------------------------------
### Training a model - the basics

Training a machine learning model involves **teaching the algorithm to identify patterns in data** so that it can make accurate predictions or classifications on new data

There are two main types of machine learning: supervised learning and unsupervised learning

**Supervised learning** requires labeled data, where each input data has a corresponding output label, to teach the model to learn the mapping between the input and output data
It can be further divided into two categories: 
- *classification*, where the output is a discrete value that corresponds to a class or category
- *regression*, where the output is a continuous value, such as temperature

**Unsupervised learning**, on the other hand, involves providing the model with unlabeled data and allowing it to find patterns or groupings on its own. Clustering is a common unsupervised learning technique used to group similar data points together. Unsupervised learning is useful for exploratory data analysis and can help to identify hidden patterns in the data.

**Semi-supervised learning** is a hybrid approach that combines both supervised and unsupervised learning. It uses a small subset of labeled data to guide the learning process and improve the accuracy of the model, while the larger unlabeled dataset helps to identify new patterns or groupings in the data.

Supervised learning is generally more accurate than unsupervised learning because it has access to labeled data. However, *the availability of labeled data can be a limitation*

Unsupervised learning is more flexible and can be used in a wider range of applications, but it can be less precise than supervised learning

Semi-supervised learning can be a useful compromise between the two, as it combines the benefits of both approaches
