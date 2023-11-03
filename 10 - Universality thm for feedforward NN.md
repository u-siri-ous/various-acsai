>*based off of ch. 4 of NN and DL - Michael Nielsen*

**THM:** for every boolean fcn $$f(x_1,...,x_n) : \{0,1\}^n \rightarrow \{0,1\}^m$$there exists a feedforward NN *N* **with perceptron neuron**s such that $$f(x_1,...,x_n) = N(x_1,...,x_n)~~~~\forall x_1,...,x_n$$
## Universality thm

For every continuous fcn $f:[0,1]^n \rightarrow (0,1)^m$ and every $\epsilon > 0,~\exists$ a feedforward NN *N* **with sigmoid neurons** such that $$|N(x_1,...,x_n) - f(x_1,...,x_n)| < \epsilon~~~~\forall x_1,...,x_n \in[0,1]^n$$Moreover, N can be chosen to have only one hidden layer (i.e. DNN are not necessary)
### Proof - built geometrically

Let's do the proof for n=1 and m=1 (i.e. one input and one output), we aim to approximate the curve

(foto oriana)

$\sigma(wx+b)$ is an approximation of a shifted step fcn, the "jump" occurs at $x = -\frac{b}{w}$ (-b over w)
#### Bump fcn

(foto oriana 2)



 


