The **perceptron** is similar to a **linear regression model**, as it uses a linear combination of the feature vector and the weights to make a prediction. 

We use binary sentiment analysis to make an example, i.e. defining two sentiments, namely *happy* and *sad*, the aim is to **find the line that splits the plane in a *happy* and a *sad* region**, learning to do so from a pre-existing dataset, in this case, words.

We define *happy* words to have a +ve score, while *negative* words have a -ve score and *neutral* words have a score of zero. 
To train the model, 
* we need a dataset containing sentences along with their **labels**
* at first, scores are random, and they get better with each prediction i.e. iterating over the dataset multiple times, and 

The training stage is successful implementing an **error function**, and we aim to minimize this function via various methods, one we'll see is gradient descent.

-----------

This is applicable to human language to an extent, so we'll use the example of the alien planet in which we have to learn the language.

![Pasted image 20231002175934](Pasted%20image%2020231002175934.png)

## Sentiment analysis classifier - example 1

This classifier basically counts the occurrences of the two words to determine if the sentence is *happy* or *sad*.

Given a sentence, assign the following scores to the words: 
* Scores: 
	* Aack: 1 point 
	* Beep: –1 points 
* Rule: 
	* Calculate the score of the sentence by adding the scores of all the words on it as follows:
		* If the score is positive or zero, predict that the sentence is happy. 
		* If the score is negative, predict that the sentence is sad.

Sentence  | Aack | Beep | Mood
----------|------|------|--
Aack aack aack!  | 3 | 0 | Happy
Beep beep!  | 0 | 2 | Sad
Aack beep aack! | 2 | 1 | Happy
Aack beep beep beep! | 1 | 3 | Sad

![Pasted image 20231002180845](Pasted%20image%2020231002180845.png)

In this case, the equation of the line is the bisector of the first quadrant, as the alien that says nothing (i.e. says zero words) is considered happy.
The happy zone is the zone in which the number of appearances of aack is greater than or equal to the number of appearances of beep, and the sad zone is the zone in which the number of appearances of aack is less than that of beep.

----------
## Sentiment analysis classifier - example 2

![Pasted image 20231002182015](Pasted%20image%2020231002182015.png)
In this example, the occurences of the words are much more sparse and uneven than before.
The trick is to always find a pattern, in this case, we can see that **every alien that says 4 or more words is happy and the others are sad**, and **there aren't words that indicate a negative score, per se**.

Now assign:
* Scores: 
	* Crack: one point 
	* Doink: one point
* Rule: 
	* Calculate the score of the sentence by adding the scores of all the words on it: 
		~~* If the score is four or more, predict that the sentence is happy.~~ 
		~~* If the score is three or less, predict that the sentence is sad.~~ 
	
		*To make it simpler and to avoid ambiguity, let’s slightly change the rule by using a cutoff of 3.5
		* If the score is 3.5 or more, predict that the sentence is happy. 
		* If the score is less than 3.5, predict that the sentence is sad.

![Pasted image 20231002182451](Pasted%20image%2020231002182451.png)

**Positive zone**: the area on the plane for which x<sub>crack</sub> + x<sub>doink</sub> – 3.5 $\geq$ 0 
**Negative zone**: the area on the plane for which x<sub>crack</sub> + x<sub>doink</sub> – 3.5 < 0

----------
## The *error* function

It's impossible to get a perfect classifier, it can sometimes misclassify points.

Recall that the general form of the perceptron classifier is:
<b><center>ax<sub>1</sub> + bx<sub>2</sub> + c = 0</center></b>
where:
* a is the score of the word 1, 
* b the score of the word 2, and 
* c is the bias

>If we wanted to have the same line, except with the positive and negative regions *flipped*, we would consider the equation - ax<sub>1</sub> - bx<sub>2</sub> - c = 0

In general:
* **Positive zone**: the area on the plane for which <b>ax<sub>1</sub> + bx<sub>2</sub> + c 
</b>$\geq$ 0 
* **Negative zone**: the area on the plane for which <b>ax<sub>1</sub> + bx<sub>2</sub> + c 
</b>< 0

![Pasted image 20231002214754](Pasted%20image%2020231002214754.png)

<u><b>Q:</b></u> How to evaluate the <u>accuracy</u> of the model


----------
## Activation functions - The step function

The function that returns a 1 if the output is nonnegative and a 0 if the output is negative. 
In other words, if the input is x, then:
$$ \text{step}(x) =
\begin{cases}
 1 & \text{if } x \geq 0 \\
 0 & \text{if } x \lt 0
\end{cases}
$$
This is used to **encode** the positive and the negative part of the plane (or happy and sad etc...), it turns the score into a **prediction**.

Generally, the prediction can be thought as:

<center><b>ŷ= step(ax<sub>var1</sub> + bx<sub>var2</sub> + cx<sub>var3</sub>  + d)</b></center>

where:
* a, b, c, ..., z are the **weights**
* the last term is the **bias**

of course, the plane has as many dimensions are there are variables/words.

## Sentimental analysis classifier - example 3

p 140 grokking ml


