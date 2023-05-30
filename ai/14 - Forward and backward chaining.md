### Clauses

* **Definite clause** $\rightarrow$ exactly one literal is positive
* **Goal clause** $\rightarrow$ all literals are negated
* **Fact** $\rightarrow$ a single positive literal
* **Horn clause** $\rightarrow$ at most one literal is positive (all definite clauses are Horn clauses)

![Pasted image 20230530121036](../pictures/Pasted%20image%2020230530121036.png)

-------

### Forward chaining - Data-directed reasoning

**Forward chaining determines if a single proposition is entailed by a KB of definite clauses**, if all the premises of an implication are known, then its conclusion is added to the set of known facts

It is essentially an application of modus ponens to extract more data from known facts, which implies soundness

![Pasted image 20230530122410](../pictures/Pasted%20image%2020230530122410.png)

#### AND-OR graph

![Pasted image 20230530122507](../pictures/Pasted%20image%2020230530122507.png)

[Solution to the exercise](https://youtu.be/CAsq7hm3sbI?t=331) 

-----------

### Backward chaining - Goal-directed reasoning

Backward chaining starts with a list of goals, or a hypothesis, and works backwards from the consequent to the antecedent to see if any data supports any of these consequents