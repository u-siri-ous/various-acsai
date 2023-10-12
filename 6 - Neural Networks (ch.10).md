No one really knows what happens inside the neuron, and that's an ongoing philosophical question

<u><b>Key Idea</b></u>: we can model more complicate behavior using the output from a neural network and feeding it in another (e.g., output in other perceptrons)

![[Pasted image 20231012142532.png]]
#### Exercise 1
Show that a perceptron can simulate a not gate (i.e., an inverter) 
Input multiplies with weight and adds bias
![[Pasted image 20231012143537.png]]
#### Exercise 2
Show that a perceptron can simulate an or gate
![[Pasted image 20231012143526.png]]

---------
## A more complicated planet

![[Pasted image 20231012143254.png]]

We can see that the MLP doesn't always do good, in this example we can see that the graph has two lines to classify, and we cannot find one that's precise enough
>*Happiness is not linear* 

![[Pasted image 20231012143731.png]]
* Line 1: 6x<sub>a</sub> + 10x<sub>b</sub> – 15 = 0
* Line 2: 10x<sub>a</sub> + 6x<sub>b</sub> – 15 = 0

We can set a **system of inequalities**, if both lines are $\geq$ 0 then "**happy**" else "**sad**", basically putting them in an and gate

This is perfectly valid, but it doesn't perform really well; **we need to combine more perceptrons**

![[Pasted image 20231012144925.png]]
The chosen weights simulate and gates, and we find a cleaner version of figure 10.9 below
![[Pasted image 20231012145420.png]]

------
### Architecture of a feed-forward NN

![[Pasted image 20231012152216.png]]

Properties:
1. All arcs are present from one layer to the next layer, and no other "backwards" arcs that jump more than two layers
2. Each one of the nodes use an **activation fcn**, and that is usually the same across all nodes 
3. Each arc has a weight
4. Each node outputs *f(input)* as a weighted sum of inputs from he previous layer, with *f* being the activation fcn
#### Exercise 
Prove that for any fcn $$f:[0,1]^n \rightarrow [0,1]$$
There exists a feedforward perceptrons (N) with *n* inputs such that $$f(x_1,...,x_n)=N(x_1,...,x_n) ~\forall(x_1,...,x_n)$$Remember that not and and are universal logic gates

-----
## Activation functions 

### ReLU
$$ \text{ReLU}(x) =
\begin{cases}
 0 & \text{if } x \leq 0 \\
 x & \text{if } x > 0
\end{cases} ~~~or~~~
Relu(z) = max(0, z)
$$
![[Pasted image 20231012154455.png]]
### Hyperbolic tan
$$ 

tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{1 - e^{-2x}}{1 + e^{-2x}}
$$
![[Pasted image 20231012154547.png]]

### SoftMax

$$
\sigma(z_i) = \frac{e^{z_{i}}}{\sum_{j=1}^K e^{z_{j}}} \ \ \ for\ i=1,2,\dots,K 
$$