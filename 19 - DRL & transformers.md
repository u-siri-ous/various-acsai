## Conjecture 1

Let G be a connected graph with at least n >= 3 vertices with a matching number $\mu$ and largest eigenvalue $\lambda_1$ , then  $$\lambda_1 + \mu \geq \sqrt{n-1} + 1$$$\mu$ represents max number of pairwise disjoint edges

Known to be false with n = 600

--------
# Deep cross-entropy method
For this approach, n is fixed by the architecture of the NN. Let's take n=19:

(foto oriana)

let's order the pairs lexicographically (i.e. {1,2}, {1,3}, {1,4}, ..., {18,19})

(foto nn oriana)

Given which of the first k edges, N gives the probability P(k+1) that the k+1 st edge is in the graph, put it in the graph and repeat until k=19 choose 2
## Score fcn
Evaluate how good an example is by minimizing the score fcn. For conj. 1 the score fcn is $$\text{score function} = \lambda_1 + \mu $$The goal is to find a graph with score $\lt \sqrt{n-1} +1$ 

Say we want to minimize the score:

Use a NN to generate a set of graphs (foto oriana)

----------------
# Transformers
(foto oriana)

Introduced in a paper called "Attention is all you need" 
## Embeddings
Represent words as numbers or vector (we've seen Word2Vec)

(foto oriana)

look up n-grams in nlp
## Multihead attention
We use more than one embedding, but it takes a lot of computational power. We will modify the embeddings in many ways (data augmentation via linear transformaions)
A linear transformation is a combination of rotation, stretches and shears

(metti foto oriana)

(finisci con foto oriana)

