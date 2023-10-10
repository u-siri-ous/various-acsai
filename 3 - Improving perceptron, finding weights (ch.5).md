**<u><b>Q</b></u>: Given a perceptron, how do we make a better one?

Let's take this via a simpler example:

**Given a perceptron <u><b>and</b></u> a point, find a better perceptron wrt the point**

#### EXAMPLE:

![Pasted image 20231003143527](../pictures/Pasted%20image%2020231003143527.png)

**Pseudocode for the perceptron trick (geometric)**:
* Case 1: If the point is correctly classified, leave the line as it is. 
* Case 2: If the point is incorrectly classified, move the line a little closer to the point.

**Pseudocode for the perceptron trick (algebraic)**:
* Case 1: If the point is correctly classified, leave the classifier as it is. 
* Case 2: If the point is incorrectly classified, that means it produces a positive error. 
		**Adjust the weights and the bias a small amount so that this error slightly decreases**
		This may be done a few times (fine-tuning)

#### EXAMPLE - Perceptron trick on a bad classifier:

Weights:
* Aack   a = 1
* Beep   b = 2
* Bias     c = -4
Prediction:
<b>ŷ = step(x<sub>aack</sub> - 2x<sub>beep</sub> - c)</b>
Sentence: “Beep aack aack beep beep beep beep." $\rightarrow$ (2, 5)
Label: **Sad(0)**

The score is 1 · x<sub>aack</sub> + 2 · x<sub>beep</sub> – 4 = 1 · 2 + 2 · 5 – 4 = 8, and the prediction is ŷ = step(8) = 1
The sentence should have had a negative score, to be classified as sad. However, the classifier gave it a score of 8, which is positive. We need to decrease this score, and thus we <u>decrease</u> the weights.

In this case, we see that the "beeps" have a stronger error wrt "aacks", let’s decrease the weight of each word by the <u>learning rate</u> times the number of times the word appears in the sentence. 
In other words: 
* The word aack appears **twice**, so we’ll reduce its weight by **two times the learning rate**, or 0.02. 
   We obtain a new weight a' = 1 – 2 · 0.01 = 0.98
* The word beep appears **five times**, so we’ll reduce its weight by **five times the learning rate**, or 0.05. 
   We obtain a new weight b' = 2 – 5 · 0.01 = 1.95
* The bias adds to the score only once, so we reduce the bias by the learning rate, or 0.01. 
   We obtain a new bias c' = –4 – 0.01 = –4.01

**Improved classifier 1** 

Weights: 
* Aack: a' = 0.98 
* Beep: b' = 1.95 
* Bias: c' = –4.01 
Prediction: <b>ŷ = step(0.98<sub>aack</sub> - 1.95x<sub>beep</sub> - 4.01)</b>
---------
Sentence 2: “Aack aack.” 
Label: Happy

The prediction for this sentence would be step(-2) = 0, misclassifying it as **sad(0)**, so in order to classify this sentence as happy, we need the classifier to give it a positive score. 
**The perceptron trick will increase this score of –2 by increasing the weights of the words and the bias**, according to occurences of the words times the learning rate.

a' = a + 2(0.01)
b' = b
c' = c + 0.01 = 3.99

-----
## Pseudocode for the perceptron trick 
Inputs: 
* A perceptron with weights a, b, and bias c 
* A point with coordinates (x<sub>1</sub>, x<sub>2</sub>) and label y 
* A small positive value $\eta$ (the learning rate) 
Output: 
* A perceptron with new weights a', b', and bias c' 
Procedure: 
* The prediction the perceptron makes at the point is ŷ = step(ax<sub>1</sub> + bx<sub>2</sub> + c). 
	* **Case 1**: If ŷ = y: **Return the original perceptron with weights a, b, and bias c** . 
	* **Case 2**: If ŷ = 1 and y = 0: **Return the perceptron with the following weights and bias**:
		* a' = a – $\eta$ x<sub>1</sub> 
		* b' = b – $\eta$ x<sub>2</sub> 
		* c' = c – $\eta$ x<sub>1</sub> 
	* **Case 3**: If ŷ = 0 and y = 1:  **Return the perceptron with the following weights and bias**:
		* a' = a + $\eta$ x<sub>1</sub> 
		* b' = b – $\eta$ x<sub>2</sub>  
		* c' = c + $\eta$ x<sub>1</sub>  
		
> NOTE: a slicker way to do this would be
> Procedure: 
> 	The prediction the perceptron makes at the point is ŷ = step(ax<sub>1</sub> + bx<sub>2</sub> + c). 
> 	Return the perceptron with the following weights and bias: –
> 		a' = a + $\eta$ (y – ŷ) x<sub>1</sub> 
> 		b' = b + $\eta$ (y – ŷ) x<sub>2</sub>  
> 		c' = c + $\eta$ (y – ŷ)
 
If the perceptron correctly classifies the point, the output perceptron is the same as the input, and both of them produce an error of 0. 
If the perceptron misclassifies the point, the output perceptron produces a smaller error than the input perceptron.

**We'll just pick random points for the time being**, we basically do the perceptron trick many times to get the perceptron algorithm. 

This involves the notion of **early stopping**, for efficiency purposes, and the notion of **epochs**, which are the times you apply the perceptron trick
