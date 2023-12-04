>*This was taken from [slides 5](obsidian://open?vault=various-acsai&file=slides%2F05%20-%20pumping%20lemma.pdf) and Sipser book page 102 of pdf*
## THM: Pumping lemma

Given a regular language A, then there exists a *pumping length p* s.t.:
* If *s* is any string in *A* of length at least *p*, it can be divided in **three pieces *s = xyz***, satisfying the conditions:
	1. for each $i \geq 0, \ xy^iz \in A$ 
	2. $|y| > 0 \ \text{or} \ y \neq \epsilon$
	3. $|xy| \leq p$
	where:
	1. the notation |s| represents the length of the string 
	2. $y^i$ represents i copies of y concatenated together, so $y^0 = \epsilon$
	3. x or z might be $\epsilon$
## Proof idea

