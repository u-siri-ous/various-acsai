Imagine you're lost on a foggy mountain, **how do you get down from the mountain?** 
**Take small steps in the direction of steepest descent, and repeat**

![[Pasted image 20231010152311.png]]

Let f(x<sub>1</sub>,...,x<sub>n</sub>) be a *smooth* function, the **gradient** of f is denoted as $\nabla$f and it's the **vector of partial derivatives**:
![[Pasted image 20231010152520.png]]
The gradient is aka as the direction of steepest ascent, with its negative being the direction of steepest descent

<b><u>Theorem</u></b>: if f is differentiable on a neighborhood around the point p, then the direction of steepest descent at p is $$-\nabla f(p)$$
This gives us a method to **minimize** functions

Input:
* function *f*
* learning rate *l*
* number of epochs *N*

Process: 
* Pick a random point p<sub>0</sub> 
* For i = 0, …, *N* – 1: 
	* Calculate the gradient ∇f(p<sub>i</sub>) 
	* Pick the point p<sub>i+1</sub> = p<sub>i</sub> – *l* ∇f(p<sub>i</sub>) 
	* End with the point p<sub>n</sub>
![[Pasted image 20231010153913.png]]

## Training perceptrons via gradient descent

Suppose we are given a standard perceptron ax<sub>1</sub> + bx<sub>2</sub> + c = 0 and we want to perform the perceptron trick on p = (p<sub>1</sub>, p<sub>2</sub>)
Recall that ŷ= step(ap<sub>1</sub> + bp<sub>2</sub> + c), let PE be the perceptron error function

PE(a, b, c, p<sub>1</sub>, p<sub>2</sub>, y) = 0 if y = ŷ 
PE = |ap<sub>1</sub> + bp<sub>2</sub> + c| if y $\neq$ ŷ

PE = y ReLU(-ap<sub>1</sub> - bp<sub>2</sub> - c) + (1-y) ReLU(ap<sub>1</sub> + bp<sub>2</sub> + c)

Suppose:
* y = ŷ = 0, then PE = 0
* y = ŷ = 1, then PE = 0 (the ReLU is 0 for whatever negative number)
* y = 1, ŷ = 0 then PE = |ap<sub>1</sub> + bp<sub>2</sub> + c|
* y = 0, ŷ = 1 then PE = |ap<sub>1</sub> + bp<sub>2</sub> + c|

The derivative of the ReLU is the step function

--------
## Activation functions - ReLU

### todo

----------
Gradient descent is applied when a,b and c are variables

![[Pasted image 20231010163005.png]]

These three together constitute the gradient of PE

![[Pasted image 20231010164429.png]]

By gradient descent, we update (a, b, c) by $$(a', b', c') = (a, b, c)\nabla PE (p_1,p_2)l$$
This is exactly the same update rule for the perceptron trick
## Exercise 

Prove that the logistic trick is just gradient descent (need quotient rule)