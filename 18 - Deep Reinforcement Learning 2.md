[Bellman Equation](https://www.youtube.com/watch?app=desktop&v=14BfO5lMiuk) $$V(s)=max_a(R(s,a)+\gamma V(s'))$$where:
* $\gamma$ is the discount factor

Solving it requires repeated sampling
## Deterministic vs Stochastic policies
### Deterministic
When at a given state, it tells you what state to move to and depends on what state you're in
### Stochastic
Given a state there is a probability distribution on the set of actions available, and we move according to this probability distribution
## Value network
The idea is to let a NN compute the value for each square in the grid (example grid with positive reinforcements) 

To train it we need
