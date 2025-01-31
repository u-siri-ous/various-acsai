The mixture of gaussians helps us in cases where data cannot be explained by a single gaussian (think of multiple clusters instead of only one)

**The objective is to find the underlying distribution of our data**, or a good enough approximation like in MLE

![[../pictures/Pasted image 20250130152810.png]]

![[../pictures/Pasted image 20250130152915.png]]

GMM introduces a probabilistic approach to clustering, by modeling data points as a mixture of multiple gaussian distributions (think of it as a softer assignment wrt kmeans)

![[../pictures/Pasted image 20250130154004.png]]

-------------
# Interpretation as a Generative model

![[../pictures/Pasted image 20250130154816.png]]

The marginalization over the modes means summing the contributions of each Gaussian component to obtain the total density

A possible algorithm is:

1. sample which Gaussian $\hat{k}$ by inverse transform sampling on the mixing coefficients $\pi=[0.5, 0.3, 0.2]$
	1. Calculate the Cumulative distribution fcn
	2. Generate a random number uniformly distributed between 0 and 1
	3. Determine where it falls (which gaussian to select)
2. Once you know $\hat{k}$, then select the params of the appropriate gaussian and sample $x\sim\mathcal{N}_{\hat{k}}(\mu,\Sigma)$

![[../pictures/Pasted image 20250130160902.png]]

These are basically the same thing

In reality, we need to answer the question
#### From which Gaussian is this point sampled from?

-------
# How to fit a MoG

![[../pictures/Pasted image 20250130161846.png]]

There can be three situations:

- **Unlabeled data, known parameters**
    - In the first scenario, we consider two Gaussians and do not know which Gaussian generated a single data point.
        
    - **Using the probability density function (pdf) of each Gaussian, we can estimate which sample is more likely to have come from which Gaussian** (method of responsibilities)
	    ![[../pictures/Pasted image 20250130162425.png|300]]
	    * k: Refers to the index of a single Gaussian component within the mixture model.
	    * l: Refers to the index used to sum over all Gaussian components in the mixture. 

- **Labeled data, unknown parameters**
    - In the second scenario, we know which Gaussian each data point comes from, but we do not know the parameters of the Gaussians.
        
    - **We find these parameters using Maximum Likelihood (ML) estimation** on the two sets of data.
        
- **Unlabeled data, unknown parameters**
    - We use an iterative method called the **Expectation Maximization (EM) algorithm** to estimate the parameters.

### Summary

- **Singularities**: Prevented by regularization to avoid overfitting to single points.
- **Identifiability**: Addressed by ordering constraints to ensure unique parameter solutions.
- **No Closed-Form Solution**: Handled by iterative algorithms like EM for parameter estimation.

-----------

# Expectation Maximization (EM)

EM is an **elegant and powerful method for finding maximum likelihood solutions for models with latent variables** in an iterative way

A latent variable is an unobserved variable (in the case of GMM - the component/Gaussian that generated a given datapoint)

## Step 1 - Expectation

We assume we have a good initialization/version of the weights (same problem of initialization has K-means)

To adjust the parameters, we must first solve the inference problem. **Which Gaussian generated each data point?**

Compute the **posterior probability that each Gaussian generates each data point** (as this is unknown to us) - known as the **responsibility (that component $k$ takes for ‘explaining’ the observation x)**

![](pictures/Pasted%20image%2020250130164425.png)

For a data point, $\hat \gamma_{ik}$ is $1\times K$ i.e. `[0.8, 0.1, 0.1]` for 3 Gaussians:
* It means that 80% of the data is explained by 1st Gaussian.
* It means that 10% of the data is explained by 2nd Gaussian.
* It means that 10% of the data is explained by 3rd Gaussian.
## Step 2 - Maximization

**Assuming that the data really was generated this way, change the parameters of each Gaussian to maximize the probability that it would generate the data it is currently responsible for**

Each Gaussian gets a certain amount of posterior probability for each data point

At the optimum we shall satisfy $$\frac{\partial \ln p(\mathbf{X} \mid \pi, \mu, \Sigma)}{\partial \Theta}=0$$We can derive closed-form updates for all parameters **in this step only**

![](pictures/Pasted%20image%2020250130165058.png)

This means the optimal mixing proportion to use (given these posterior probabilities) is just the **fraction of the data that the Gaussian gets responsibility for.**

In the end, in each M step we have Γ (responsibility matrix N X K) marginalized over N in the numerator, and in the denominator we always have Γ but marginalized over Nk (the denominator is normalized)

This is the part where we "move the parameters" by modifying them and thus (hopefully) increasing the log-likelihood.
## Step 3 - Evaluate log likelihood and iterate until convergence

![](pictures/Pasted%20image%2020250130170441.png)
where:![](pictures/Pasted%20image%2020250130170503.png)

----------
# Summary 


![](pictures/Pasted%20image%2020250130170812.png)

--------------------
# Covariance types

**GMM** can have assumptions even on the shape of the Gaussian based on the covariance matrix.

**Remember:**

- $\mu$ indicates where to place the Gaussian (acts as a translation in space);
- $\Sigma$ instead models the shape of each Gaussian

$\Sigma$ types:

- `full`: **each component** has its own general covariance matrix **(more parameters)**
- `tied`: **all components** share the same general covariance matrix.
- `diag` **each component** has its own diagonal covariance matrix.
- `spherical`: **each component** has its own single variance. **(less params)**
### Note: It is common to decorrelate the data with PCA so that then you can assume a diagonal matrix (less params!)

--------
# How many Gaussians? (similar to K-means)

- The fact that **GMM is a generative model gives us a natural means of determining the optimal number of components for a given dataset.**

- A generative model is inherently a probability distribution for the dataset, and so we can simply evaluate the likelihood of the data under the model, using cross-validation to avoid over-fitting.

- Another means of correcting for over-fitting is to adjust the model likelihoods using **some analytic criterion such as the Akaike information criterion (AIC) or the Bayesian information criterion (BIC).**



