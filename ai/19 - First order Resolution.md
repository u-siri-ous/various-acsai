Defined similarly as [propositional resolution](12,13%20-%20Propositional%20resolution,%20definitions,%20soundness%20and%20completeness.md), 

![Pasted image 20230605153333](../pictures/Pasted%20image%2020230605153333.png)

### Unification

Two atomic formulae $\zeta$, $\xi$ **unify** if $\exists$ a substitution $\sigma$( { x<sub>1</sub>/g<sub>1</sub>, ... , x<sub>n</sub>/g<sub>n</sub> }, { $\zeta$, $\xi$ } ) that makes them **syntactically equal**

A unifier is **more general** than another if it can be obtained from the first one

![Pasted image 20230605153852](../pictures/Pasted%20image%2020230605153852.png)

We can only substitute **variables** with anything, not constants nor functions!

### The whole story

![Pasted image 20230605154535](../pictures/Pasted%20image%2020230605154535.png)