>*Taken from Sipser pdf page 91, and [these slides](obsidian://open?vault=various-acsai&file=slides%2F03%20-%20regular%20expressions.pdf)*

## THM: **If a language is described by a regexp, it is regular**

## Proof

We aim to convert regexp *R* into an *NFA*, both recognizing language *A*
NFAs are used because they are simpler and they don't need exiting arrows for every symbol in the alphabet

Remembering the **formal definition** of a regexp:
![[Pasted image 20231103100714.png]]

We consider the 6 aforementioned cases

1. R = $a$ for some $a \in \Sigma$, then L(R) = $a$, and the NFA will have an accepting state corresponding to the input $a$
2. R = $\epsilon$, the NFA will accept right away as L(R) = $\epsilon$ (i.e. it has $\delta(r,b) = \emptyset$ for any r and $b \in \Sigma$, and $q_0 \in F$)
3. R = $\emptyset$, the NFA has no accepting states as L(R) = $\emptyset$ (i.e. it has $\delta(r,b) = \emptyset$ for any r and $b \in \Sigma$, and $F = \emptyset$)
for cases 4, 5 and 6, we go back to the proof of [closure under star, concatenation and union for regular languages](obsidian://open?vault=various-acsai&file=notes%20%26%20proofs%2F18%2C%2024%2F02%20-%20Closure%20of%20RL%20under%20star%2C%20concatenation%20and%20union)

![[Pasted image 20231103104115.png]]

