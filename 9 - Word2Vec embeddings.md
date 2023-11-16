The goal is to represent each word in the English language by a vector in $\mathbb{R}^d$, where *d* is a *hyperparameter* 
Conversely, *parameters* are learned during training (e.g. weights) 
#### Example

{Humans} $\rightarrow \mathbb{R}^5$, using this on Personality tests we get

{Bob} $\mapsto$ (Openness, Agreeableness, Negative Emotionality, Extraversion, Conscientousness)
### Using Natural Language

171146 words in English, we use a vector of word counts 
**One-Hot Encoding has the disadvantage of the lack of semantic meaning and an high dimensionality**

Word2Vec maps each word *x* to a vector $V(x) \in \mathbb{R}^d$ such that:
1. if *x* and *y* have similar meanings, then $||V(x)-V(y)||$ is small, as *d* is small
2. if two words have opposite meanings then $||V(x)+V(y)||$ is small (i.e. $V(x) \approx -V(y)$)
3. some relations between words are also preserved (i.e. analogies)
	$V(queen) - V(woman) + V(man) \approx V(king)$
## Cosine Similarity

Let $a,b \in \mathbb{R}^d$, we define cosine similarity as $$S_c(a,b)=cos(\theta)$$where $\theta$ is the angle between a and b
This can be rewritten as $$\frac{a \cdot b}{||a||~||b||} = \frac{\sum_{i=1}^d a_i~b_i}{\sqrt{\sum_{i=1}^d a_i^2}\sqrt{\sum_{i=1}^d b_i^2}}$$
* $S_c(a,b) \approx 1$ indicates that the words are similar (e.g., good, better)
* $S_c(a,b) \approx -1$ indicates that the words are opposite (e.g., good, evil)
* $S_c(a,b) \approx 0$ indicates that the words are not correlated 
### Finding Word2Vec embedding

* Use a feedforward NN to solve a problem we do not care about which is the following

**Given 2 words x and y, how likely is it that x and y appear close to each other in a text?**

Words come with context, which is crucial for their interpretation
We can generate data by sliding a window across text

Example:
“The world is indeed full of peril, and in it there are many dark places; but still there is much that is fair, and though in all lands love is now mingled with grief, it grows perhaps the greater.”

We can make a (window size 2 words before and after "word" entry)

| Word    | Context                  |
|---------|--------------------------|
| is      | The, world, indeed, full |
| indeed  | world, is, full, of      |
| ...     | ...                      |
| perhaps | it, grows, the, greater  |

## Skipgram vs Cbow (continuous-bag-of-words)

Given a word, guess the context vs given the context, guess the word

<u>Let's use skipgram</u>

![[photo_2023-10-31_16-28-00.jpg]]

![[photo_2023-10-31_16-27-51.jpg]]