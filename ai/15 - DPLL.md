![Pasted image 20230530124655](../pictures/Pasted%20image%2020230530124655.png)

DPLL takes as input a sentence in conjunctive normal form, i.e., a set of clauses:

* DPLL detects if the sentence must be true or false, even with partially completed model
	* **A clause is true if *any* literal is true**, even if the other literals do not yet have truth values
	* Similarly, a **sentence is false if any clause is false**, which occurs when ***each* of its literals is false**
![Pasted image 20230531201002](../pictures/Pasted%20image%2020230531201002.png)
* It uses **pure symbol heuristic**
	* A pure symbol is a symbol that always appears with the same “sign” in all clauses (negated or affirmed/true or false)
	* During the run, if a pure literal *l* occurs then extend the partial interpretation with *l*
* It uses **unit clause heuristic**
	* In DPLL, unit clauses are the ones with only a literal *and* the ones in which all literals but one are assigned false
	* During the run, if a unit clause occurs then extend the partial interpretation with its literal
* It can use **max-degree heuristic**
	* Choosing the symbol which appears the most as first to propagate
	* Combined with pure literal heuristic, if possible

![Pasted image 20230531201031](../pictures/Pasted%20image%2020230531201031.png)

-----------

DPLL uses backtracking like CSPs, for example, below, $\phi$ is **not satisfiable**

![Pasted image 20230601130351](../pictures/Pasted%20image%2020230601130351.png)

It runs until we find at least **one** interpretation that satisfies all the clauses, if it exists