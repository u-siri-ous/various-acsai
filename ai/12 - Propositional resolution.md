### NNF - Negation normal form

Every propositional formula is equivalent to a formula where:
* **negation** appears only in front of propositional symbols
* there aren't biconditionals and implications

![Pasted image 20230529163744](../pictures/Pasted%20image%2020230529163744.png)

----------

### Propositional resolution, definition and properties
(http://www.inf.u-szeged.hu/~ihegedus/teach/resolution.pdf)

Let a literal be an atomic sentence:
* A **clause** is a disjunction of literals
* The order of literals is irrelevant
* Multiple literals can be merged $\rightarrow$ representation as a finite **set**

![Pasted image 20230529164635](../pictures/Pasted%20image%2020230529164635.png)

* We use factoring to remove copies of literals in clauses
* You can resolve only one pair of complementary literals at a time
* Resolving two singleton clauses leads to the empty clause $\rightarrow$ **we found a contradiction**

--------------

### CNF - Conjunctive Normal Form

![Pasted image 20230529170625](../pictures/Pasted%20image%2020230529170625.png)

----------------

### Algo and Example

![Pasted image 20230529171355](../pictures/Pasted%20image%2020230529171355.png)

![Pasted image 20230529171448](../pictures/Pasted%20image%2020230529171448.png)

We resolved "parts" of the CNF pairwise, with one **resolvent** at a time:
e.g., <font color="#00b050"><font color="#2DC26B">&#172 p<sub>2,1</sub> </font></font>$\vee$ <font color="#ff0000">b<sub>1,1</sub></font> resolving with <font color="#ff0000">&#172 b<sub>1,1</sub></font> $\vee$ p<sub>1,2</sub> $\vee$ <font color="#2DC26B">p<sub>2,1</sub></font> :
1. <font color="#00b050">resolvent</font> = $\neg$ b<sub>1,1</sub> $\vee$ p<sub>1,2</sub> $\vee$ b<sub>1,1</sub> 
	* we have removed <font color="#00b050">p<sub>2,1</sub></font> as it was affirmed and negated
2. <font color="#ff0000">resolvent</font> = $\neg$ p<sub>2,1</sub> $\vee$ p<sub>1,2</sub> $\vee$ p<sub>2,1</sub> 
	* we have removed <font color="#ff0000">b<sub>1,1</sub></font> as it was affirmed and negated