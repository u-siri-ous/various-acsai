>[Nice chapter on RBMs](https://studentweb.uvic.ca/~leizhao/Reading/chapter/06.pdf)
>[Video of lecture](https://www.youtube.com/watch?v=Fkw0_aAtwIw&pp=ugMICgJpdBABGAHKBRxyZXN0cmljdGVkIGJvbHR6bWFubiBtYWNoaW5l)

* Unsupervised Learning (unlabelled data)
* Generative stochastic model that learns a probability distribution over its set of inputs
* Was a candidate for the Netflix prize to predict user rating for films based on previous watched content

<u>Key Idea</u>: There might be hidden parameters that explain data from examples

| Alice  | Y | Y | N | Y | N | N | Y |
|--------|---|---|---|---|---|---|---|
| Bob    | N | N | Y | N | Y | Y | N |
| Carlos | Y | Y | N | Y | N | N | Y |

The hidden data is that there are a cat E and a dog D
The data could be explained from the fact that A & C like dogs while B likes cats

![[Pasted image 20231128143037.png]]

There are no arcs between hidden layer nodes and visible nodes; nodes and arcs are weighted (think of this like an energy fcn)

---------
### Terminology

A **scenario** is a subset of the nodes (visible and hidden) which are always 2<sup>k</sup>, where k is the number of nodes

The **score** of a scenario is defined as such: sum of weights of nodes in the scenario + sum of weights of edges with both ends in the scenario

The aim is to **turn the scores in probabilities**, for this we take the **softmax** $$\sigma(z_i) = \frac{e^{z_{i}}}{\sum_{j=1}^K e^{z_{j}}} \ \ \ for\ i=1,2,\dots,K$$In this case the equation is $$\sigma(score_i) = \frac{e^{score_{i}}}{\sum_{j=1}^K e^{score_{j}}}$$so it's e^score / sum of all e^score, scores are hopefully given

--------------

Each data point is a subset of the visible nodes = {A, B, C}

**A scenario extends a data point if** $X \subseteq \{A, B, C\}$ **if** $S \cap \{A, B, C\} = X$, so
\# of scenarios that extend a data point = $2^{\text{ \# of hidden nodes}}$
## Training a RBM

For each data point X:
Increase the probability of all scenarios that extend X and decrease the probability of all scenarios that do not extend X

**Increasing the probability of one scenario affects also other scenarios**

Example: Scenario ACD
learning rate = l = 0.1

Increase node weights of A,C,D by l
Increase edge weights of AD and CD by l (or of all connecting edges s.t. start and end are in the scenario)

Similarly if we want to decrease the probability of ACD we decrese the weights instead of increasing

Given a data point X, pick a random scenario S that extends X and update weights to increase the probability of S and pick a random scenario T that does **not** extend X and update weights to decrease the probability of T
### Gibbs sampling
![[Pasted image 20231128154508.png]]
![[Pasted image 20231128154322.png]]
![[Pasted image 20231128154412.png]]
![[Pasted image 20231128154356.png]]
### Independent sampling - picking a random scenario that extends a data point

Suppose X = {A, C}

*What is the probability of D given that AC occurred?* 
We use sigmoid to do this (why below)

Let H be a hidden node and X be a data point $$P(H | X) =\sigma \biggl(weight(H)+ \sum_{x \in X}  \ weight(xH) \biggr)$$xH are the edges touching the hidden node

We use this formula to compute a separate probability for each hidden node H, the chosen hidden node is random
### How to pick a completely random scenario

We will sample approximately (this problem is hard)

We take a random walk 
The length of the random walk is a hyperparameter 

Start with a random visible node X:
1. Generate a random subset X1 of hidden nodes using the formula (see above) 
2. Generate a random subset X2 of visible nodes using the formula (see above)
3. Repeat to obtain X0, X1, ... , Xp, where p = len(random walk)
	1. X_even are subsets of visible nodes and X_odd are subsets of hidden nodes
4. Output $X_{p-1} \cup X_p$

This generates a random scenario



