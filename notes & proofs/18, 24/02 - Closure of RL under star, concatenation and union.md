>*This was taken from 1.45, .47, .49 Sipser (p. 83 -> 87) and [these slides](obsidian://open?vault=various-acsai&file=slides%2F02%20-%20nondeterminism.pdf)*
## Closure under union

We have regular languages A1 and A2 and want to prove that A1 ∪ A2 is regular

The idea is to take two NFAs (to use ε-transitions), N1 and N2 for A1 and A2, and combine them into one new NFA, N

N must accept its input if ***either*** N1 or N2 accepts this input

We define a new set of states and a new transition function as follows:
1. The starting state $q_0$ is new, with ε-transitions that take the computation to N1 or N2
2. $Q_{N} = {q_0} ∪ Q_{1} ∪ Q_{2}$
3. $F_N = F_{1} \cup F_{2} \rightarrow$ N accepts if either N1 or N2 accept
4. Define $\delta | \text{ for any }q \in Q\text{ and any } a \in \Sigma \cup \epsilon$ $$\delta(q,a) =
\begin{cases}
 \delta_{1}(q,a) & q \in Q_{1} \\
 \delta_{2}(q,a) & q \in Q_{2} \\
 \{q_{01},q_{02}\} & q=q_0 \land a = \epsilon \\
 \emptyset & q=q_0 \land a \neq \epsilon
\end{cases}
$$![[Pasted image 20231031110754.png]]

## Closure under concatenation

We have regular languages A1 and A2 and want to prove that A1 ◦ A2 (or A1A2) is regular

In this case, we have that we need ε-transitions from the accepting states of N1 to N2, to construct the string in the order A1A2

We define a new set of states and a new transition function as follows:
1. The starting state $q_1$ is the same as N1
2. $Q_{N} = Q_{1} ∪ Q_{2}$
3. $F_N = F_{2} \rightarrow$ N accepts if N2 accepts
4. Define $\delta | \text{ for any }q \in Q\text{ and any } a \in \Sigma \cup \epsilon$ $$\delta(q,a) =
\begin{cases}
 \delta_{1}(q,a) & q \in Q_{1} \land q \notin F_{1}\\
 \delta_{1}(q,a) & q \in F_{1} \land a \neq \epsilon \\
 \delta_{1}(q,a) \cup \{q_{02}\} & q \in F_{1} \land a = \epsilon \\
 \delta_{2}(q,a) & q \in Q_2
\end{cases}
$$![[Pasted image 20231031111838.png]]

## Closure under star

In this case the operation yields an infinite set constructed recursively

The resulting NFA N will accept its input whenever it can be broken into several pieces and N1 accepts each piece

We can construct N like N1 with additional ε arrows returning to the start state from the accept states
This way, **when processing gets to the end of a piece that N1 accepts, the machine N has the option of jumping back to the start state to try to read another piece that N1 accepts**

Trivially, N must accept ε

We define a new set of states and a new transition function as follows:
1. We define a new accepting starting state $q_0$
2. $Q = \{q_0\} \cup Q_1$
3. $F_N = \{q_0\} \cup F_1 \rightarrow$ the accept states are the old accept states plus the new start state 
4. Define $\delta | \text{ for any }q \in Q\text{ and any } a \in \Sigma \cup \epsilon$ $$\delta(q,a) =
\begin{cases}
 \delta_{1}(q,a) & q \in Q_{1} \land q \notin F_{1}\\
 \delta_{1}(q,a) & q \in F_{1} \land a \neq \epsilon \\
 \delta_{1}(q,a) \cup \{q_{01}\} & q \in F_{1} \land a = \epsilon \\
 \{q_{01}\} & q = q_0 \land a = \epsilon \\
 \emptyset & q = q_0 \land a \neq \epsilon
\end{cases}
$$![[Pasted image 20231031112736.png]]