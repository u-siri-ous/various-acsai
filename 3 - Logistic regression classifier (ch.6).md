The logistic regression classifier takes over the *binary* classification of perceptron, as it can predict more variations in the same dataset, and outputs probabilities.

For example, going back to the previous lecture, in which we analysed phrases. It only took into account the fact of them being strictly happy or sad, but natural language has *nuances* to it, so naturally, sentences can be various kinds of happy and sad.

**We need a smoother, real valued way to classify points**

The goal of the logistic classifier is to assign scores as close as possible to the label of the points

The logistic classifier, in contrast with the perceptron classifier, doesn’t give definite answers

Input:
* Set of points labelled as happy = 1 and sad = 0
Task:
* Build a classifier that predicts the <u>probability</u> that a future point is happy or sad

## Activation Functions - The Sigmoid
The Sigmoid is the activation function of the logistic regression model, and it's defined as follows:
$$\sigma(x) = \frac{1}{1+e^{-x}} $$
and:
$$
\lim_{x\to\infty} \sigma(x) = 1
$$
$$
\lim_{x\to-\infty} \sigma(x) = 0
$$

![Pasted image 20231003162237](../pictures/Pasted%20image%2020231003162237.png)

It's real valued and continuous, so the error **won't ever** be 0 or one, but a float number.

---------
### Logistic Classifier 1

![Pasted image 20231003162302](../pictures/Pasted%20image%2020231003162302.png)

Logistic Classifier 1:
* Weight of Aack: a = 1 
* Weight of Beep: b = 2 
* Bias: c = –4
Prediction (in this specific case): 
$$\text
ŷ = \sigma(1 * x_a + 2 * x_b -4)
$$
Sentence 1: ŷ = σ(3 + 2 · 2 – 4) = s(3) = 0.953. 
Sentence 2: ŷ = σ(1 + 2 · 2 – 4) = s(1) = 0.731. 
Sentence 3: ŷ = σ(0 + 2 · 1 – 4) = s(–2) = 0.119. 
Sentence 4: ŷ = σ(2 + 2 · 0 – 4) = s(–2) = 0.119.

-----
## Error functions in logistic regression

We want the error functions to have a good error function. Some properties follow:
1. If a point is correctly classified, the error is a small number. 
2. If a point is incorrectly classified, the error is a large number. 
3. **The error of a classifier for a set of points is the sum (or average) of the errors at all the points**.

Types of error function:
1. Absolute error - the absolute value of the difference between the prediction and the label
$$ |ŷ-y|$$
2. Square error - is the square of the difference between the prediction and the label
$$(ŷ-y)^2$$
Both of these are always [0,1], so not useful as we want to be more precise with real values

### The log loss function

This function uses probabilities to define the error function, answering this question:
<center><b>What is the probability that the prediction is correct?</b></center>

Given that ŷ is the probability that a sentence is happy, **1 - ŷ is the probability that the sentence is sad**:
1. If y = 1 (happy)
    Then P(prediction correct) = ŷ
2. If y = 0 (sad)
	Then P(prediction correct) = 1 - ŷ

We can say that:
$$P\text
{(all predictions are correct) = }
$$
$$
{
ln\biggl(\prod_{i=1}^n~P(\text{prediction~i~is~correct})\biggr)  = \sum_{i=1}^nln(P (\text{prediction i is correct}))
}
$$
We use log as it has the following property:
$$log(ab) = log(a) + log(b)$$
So we use it to transform the product in a sum

--------
### Logistic Classifier 1 - logloss

![Pasted image 20231003162302](../pictures/Pasted%20image%2020231003162302.png)

Logistic Classifier 1:
* Weight of Aack: a = 1 
* Weight of Beep: b = 2 
* Bias: c = –4
Prediction (in this specific case): 
* Sentence 1: ŷ = σ(3 + 2 · 2 – 4) = s(3) = 0.953
* Sentence 2: ŷ = σ(1 + 2 · 2 – 4) = s(1) = 0.731 
* Sentence 3: ŷ = σ(0 + 2 · 1 – 4) = s(–2) = 0.119 
* Sentence 4: ŷ = σ(2 + 2 · 0 – 4) = s(–2) = 0.119

REM: the predictions are interpreted as probabilities

* Point 1: 
	* Label = 0 (sad) 
	* Prediction (probability of being happy) = 0.953 
	* Probability that prediction is correct: 1 – 0.953 = 0.047 
* Point 2: 
	* Label = 1 (happy) 
	* Prediction (probability of being happy) = 0.731 
	* Probability that prediction is correct: 0.731 
* Point 3: 
	* Label = 1 (happy) 
	* Prediction (probability of being happy) = 0.119 
	* Probability that prediction is correct: 0.119 
* Point 4: 
	* Label = 0 (sad) 
	* Prediction (probability of being happy) = 0.119 
	* Probability that prediction is correct: 1 – 0.119 = 0.881

We now need the probability that all four of them are correct; assuming independence we simply multiply the above probabilities and that equals 0.004. This is almost what we want.

Let's calculate logloss on sentences this way:
$$\text {logloss = -ln(probability prediction is correct) or} 
$$
$$\text {-ln(|ŷ-y|) or}$$
$$\text{-y ln(ŷ) - (1-y) ln(1-ŷ)}$$
![Pasted image 20231005143121](../pictures/Pasted%20image%2020231005143121.png)![Pasted image 20231005143310](../pictures/Pasted%20image%2020231005143310.png)

**logloss of the entire dataset is the sum of the logloss at each point**

------
### Comparing classifiers using logloss

Logistic Classifier 1: (blue)
* Weight of Aack: a = 1 
* Weight of Beep: b = 2 
* Bias: c = –4

Logistic Classifier 2: (violet)
* Weight of Aack: a = –1 
* Weight of Beep: b = 1 
* Bias: c = 0

![Pasted image 20231005144539](../pictures/Pasted%20image%2020231005144539.png)

Classifier 2 looks better, let's check with logloss

![Pasted image 20231005144728](../pictures/Pasted%20image%2020231005144728.png)

* Point 1: y = 0, yˆ = 0.269: l
	* log loss = ln(1 – 0.269) = 0.313 
* Point 2: y = 1, yˆ = 0.73: 
	* log loss = ln(0.721) = 0.313 
* Point 3: y = 1, yˆ = 0.73: 
	* log loss = ln(0.731) = 0.313 
* Point 4: y = 0, yˆ = 0.119: 
	* log loss = ln(1 – 0.119) = 0.127 

The total log loss for the dataset is the sum of these four, which is **1.067**
Notice that this is much smaller than 5.616, confirming that classifier 2 is indeed much better than classifier 1