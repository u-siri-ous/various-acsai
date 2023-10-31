>*This was taken from 1.39 Sipser (p. 79) and from [these slides](obsidian://open?vault=various-acsai&file=slides%2F02%20-%20nondeterminism.pdf)*

***THM:*** **For every NFA *N* there exists a DFA *M* such that L(N) = L(M)**

***PROOF:***
We need to convert the NFA into a deterministic simulation of it

If k is the number of states of the NFA, it has 2<sup>k</sup> subsets of states
Each subset corresponds to one of the possibilities that the DFA must remember, so the DFA simulating the NFA will have 2<sup>k</sup> states

Let N be the NFA recognizing some language A, we construct a DFA M to recognize it

Things to keep in mind for proof: 
1. A DFA does not allow ε-transitions
2. Every input leads to one and only one state
3. Every state of M is a set of states of N
## The no ε-transition case

1. $Q' = P(Q) \rightarrow$ powerset of Q
2. $\delta'(R, a) = \bigcup_{~r\in R}~\delta(r,a) \rightarrow$ the union of the sets δ(r, a) for each possible r in R
						   When M reads a symbol *a* in state R, it shows where *a* takes each state in R
						   Because each state may go to a set of states, we take the union of all these sets
1. $q_0^′ = \{q_0\}$ 
2. $F^′ = \{R ∈ Q^′~|~\text{R contains an accept state of N}\}$ 

![[Pasted image 20231031100541.png]]
## The case with ε-transitions

For any state R of M, we define E(R) to be the collection of states that can be reached from members of R by going only along ε arrows, including the members of R themselves$$\forall~R ⊆ Q \text{ let E(R) = \{q | q can be reached from R by traveling along 0 or more ε arrows\} }$$ ![[Pasted image 20231031101421.png]]
This leads us to define the new transition function$$δ^′ (R, a) = \text{\{q ∈ Q | q ∈ E (δ(r, a)) for some r ∈ R\}}$$and the starting state $q_0^′ = \{E(q_0)\}$ 

At every step in the computation of M on an input, **it enters a state that corresponds to the subset of states that N could be in at that point**

![[Pasted image 20231031101511.png]] 

The start state is **E({1})** i.e. the set of states that are reachable from 1 by travelling along ε arrows, plus 1 itself
An ε arrow goes from 1 to 3, so **E({1}) = {1, 3}**

State {2} goes to {2,3} on input a because in N4, state 2 goes to both 2 and 3 on input a and we can’t go farther from 2 or 3 along ε arrows
State {2} goes to state {3} on input b because in N4, state 2 goes only to state 3 on input b and we can’t go farther from 3 along ε arrows
State {1} goes to ∅ on a because no a arrows exit it and it goes to {2} on b 

>Note that the procedure in Theorem 1.39 specifies that we follow the ε arrows after each input symbol is read
>An alternative procedure based on following the ε arrows before reading each input symbol works equally well, but that method is not illustrated in this example

State {3} goes to {1,3} on a because in N4, state 3 goes to 1 on a and 1 in turn goes to 3 with an ε arrow
State {3} on b goes to ∅
State {1,2} on a goes to {2,3} because 1 points at no states with a arrows, 2 points at both 2 and 3 with a arrows, and neither points anywhere with ε arrows
State {1,2} on b goes to {2,3} 