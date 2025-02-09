# Linear Regression - basics of LA

Basically, fit a line (or hyperplane) to data

How?

![](pictures/Pasted%20image%2020250205170800.png)
![](pictures/Pasted%20image%2020250205172214.png)

The vector belongs to $\mathbb{R}^{d+1}$ because of the term $\theta_0$ which is aka the **intercept** (literally, the point in which the y axis is crossed if d = 2)

This is also known as **bias**, as it's not feature-dependent and just moves out fcn up and down

# Loss function and how to minimize it

![](pictures/Pasted%20image%2020250205172150.png)

To minimize it, we take the argmin to output the value of theta that minimizes f_theta

![](pictures/Pasted%20image%2020250205172353.png)

expanding the terms it results in:![](pictures/Pasted%20image%2020250205172712.png)

![](pictures/Pasted%20image%2020250205173322.png)
![](pictures/Pasted%20image%2020250205173523.png)

We use this to **find the best fitting line/plane** to a set of data points, minimizing the sum of the squared differences (errors) between the observed values and the values predicted by the model (aka residual)

----------
# Probabilistic Interpretation

![](pictures/Pasted%20image%2020250205174540.png)
![](pictures/Pasted%20image%2020250205174655.png)
This notation means that $y_i$ is normally distributed with mean $\theta^T x_i$ and variance $\sigma^2$

It's describing the distribution of $y_i$ conditionally on $x_i$ and $\theta$

## Estimate $\theta$ with MLE

For a single training point:$$

p\left(y_i \mid x_i ; \theta\right) \doteq L({\theta};{x}_i,y_i) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(y_i-\theta^{T} x_i\right)^{2}}{2 \sigma^{2}}\right)

$$For multiple training point $\{x_i,y_i\}$, given IID assumptions on $\epsilon$, the conditional distribution of y given x follows a specific pattern → Gaussian $$

\begin{aligned}

L(\theta) &=\prod_{i=1}^{n} p\left(y^{(i)} \mid x^{(i)} ; \theta\right) \\

&=\prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(y^{(i)}-\theta^{T} x^{(i)}\right)^{2}}{2 \sigma^{2}}\right)

\end{aligned}

$$This represents the joint probability of observing all the data points given the model parameters θ

**Maximizing the MLE is the same as minimizing the squared loss, given the Gaussian assumption**

![](pictures/Pasted%20image%2020250205180521.png)$$\begin{align}
&\arg\max_{{\theta}} n \log \frac{1}{\sqrt{2 \pi} \sigma}-\frac{1}{\sigma^{2}} \cdot \frac{1}{2} \sum^{n}\left(y^{(i)}-\theta^{T} x^{(i)}\right)^{2} \rightarrow \\
&\arg\min_{{\theta}} \frac{1}{2} \sum_{i=1}^{n}\left(y^{(i)}-\theta^{T} x^{(i)}\right)^{2} 
\end{align}$$The reason we choose to minimize the loss rather than maximize the MLE (Maximum Likelihood Estimation) is that we don't have σ\sigma (the standard deviation), but only x and y

**Therefore, we don't have the means to develop the MLE equation**

------------------
# Gradient Descent

### Idea: make a little step so that locally after each step the cost is lower than before

Input: Training set $\{{x}_i,y_i\}$, learning rate $\gamma$, a small value in $\{0.1,\ldots,\texttt{1e-6}\}$

1. **Initialization - Very Important if the function is not strictly convex** as minimum is not guaranteed to be unique
	* Set $\theta$ to all zeros or random initialization from a distribution.$${\theta} \doteq {0}^T$$
2. Repeat until **convergence**:
	* Compute the gradient of the loss wrt the parameters ${\theta}$ given **all the training set**
	* Take a small step in the opposite direction of steepest ascent **(so the steepest descent).$${\theta} \leftarrow  {\theta} -\gamma {\nabla}_{{\theta}}\mathcal{J}({\theta};{x},y)$$
3. When convergence is reached, your final estimate is in ${\theta}$
## Convergence

1. **Validation Loss/Metric**: 
	When the validation loss stops improving for a certain number of iterations, training is stopped to prevent overfitting
	This is known as **early stopping**
	
2. **Loss function stability**:
	If the absolute difference between the loss at two consecutive iterations is very small, it indicates that the model is no longer improving significantly$$\left| \mathcal{J}(\theta; \mathbf{x}, \mathbf{y})_t - \mathcal{J}(\theta; \mathbf{x}, \mathbf{y})_{t-1} \right|$$
3. **No variations in the parameters**
	If the parameters do not change significantly, it suggests that the model is converging to a stable solution $$\mid\mid {\theta}_{t} - {\theta}_{t-1}   \mid\mid $$
4. **Gradient norm goes to 0**
	This indicates that the optimization algorithm has reached a point where the slope of the loss function is flat, signifying a local minimum $$\mid\mid {\nabla}_{{\theta}}\mathcal{J}({\theta};{x},y)   \mid\mid \rightarrow 0 $$
![](pictures/Pasted%20image%2020250205185209.png)

-----------
# Stochastic Gradient Descent (SGD)

![](pictures/Pasted%20image%2020250205185509.png)
(samples are one or a few taken uniformly, << n)

This is generally faster than normal gradient descent and achieves convergence faster, allowing for more epochs




















