### Satisfiability, unsatisfiability, validity

A formula ψ is **satisfiable** if $\exists$ some structure S and some assignment α such that **(S, α) ⊨ ψ**

A formula ψ is **valid** if, $\forall$ structure S and assignment α, **(S, α) ⊨ ψ** $\rightarrow$ tautology

### Logical equivalences in FOL - $\exists$, $\forall$ 

![Pasted image 20230604105607](../pictures/Pasted%20image%2020230604105607.png)

### $\forall$ elimination

![Pasted image 20230604105801](../pictures/Pasted%20image%2020230604105801.png)

### Skolemization - $\exists$ elimination

![skolem](../pictures/skolem.png)

This is done via the **Skolem function** $\theta$, which takes variables in the scope of $\exists$ , i.e., bound by it, as parameters

----------------

### Propositionalization - from FOL to PL

The objective is to proceed as follows:

1. remove ∃’s by skolemization
2. omit ∀ as only the variables in the scope of ∀ remain

What remains resembles a formula in propositional logic! So:
1. turn formulae in CNF
2. apply inference mechanisms that are suitable for propositional logic

------------------

#### NNF in FOL

1. Occurrences of $\neg$ are only in front of atomic formulae, i.e., **push inwards**
2. There aren't any → and/or ↔

#### CNF in FOL

The same as PL, having a **quantifier-free formula**

-------------

### Prenex form

![Pasted image 20230604112140](../pictures/Pasted%20image%2020230604112140.png)

#### PCNF - Prenex CNF

![Pasted image 20230604112235](../pictures/Pasted%20image%2020230604112235.png)

#### General approach to PCNF

1. Eliminate → and ↔ 
2. Push negations in front of atomic formulae
3. Pull quantifiers out
4. Transform in CNF using distributivity of ∨ and ∧

##### Example

![Pasted image 20230605151942](../pictures/Pasted%20image%2020230605151942.png)

------------

### Clausal form

The universal closure of a formula φ(x<sub>1</sub>, ... , x<sub>n</sub>) with free variables x<sub>1</sub>, ... , x<sub>n</sub> is the sentence: 
<center><b>∀x<sub>1</sub> ... ∀x<sub>n</sub> (φ (x<sub>1</sub>, ... , x<sub>n</sub>))</b></center>
Process:

1. Get to PCNF
2. Skolemize all $\exists$
3. Remove all $\forall$
4. Write the formula as a **set of clauses**
5. Rename vars s.t. **no two clauses in clausal form share common variables**

