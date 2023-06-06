FOL is another way of knowledge representation in AI

It adds to Propositional logic:

* **Terms**
* **Objects**
* **Relations**
* **Functions**

### Syntax 

#### Components

* **Constants**
* **Variables**
	* Free = it occurs **outside** the scope of a quantifier
	* Bound = it occurs **within** the scope of a quantifier
* **Predicates**
	* Unary = property
	* *n*-ary = relationship, written as ***P/n***
* **Quantifiers**
	* Universal $\forall$ (implication)
	* Existential $\exists$ , $\nexists$ , !$\exists$ (conjunction)
* **Functions**
* **Connectives and operators**

**OPERATOR PRECEDENCE :** 
1. ¬
2. =
3. ∧
4. ∨
5. ⇒
6. ⇔

![Pasted image 20230604094245](../pictures/Pasted%20image%2020230604094245.png)

--------------

#### Sentences and statements

The most basic sentence is **the atomic sentence**, in the form:

<center><b>Predicate (term<sub>1</sub>, term<sub>2</sub>, ... , term<sub>n</sub>)</b></center>

Like in PL, the combination of atomic sentences using connectives are **complex sentences**

FOL sentences and statements are made of two parts:

* **Subject**, the main part / variable 
* **Predicate**, the relation that binds two atoms together

Examples : 

**All men drink coffee** is translated in **∀x man(x) ⇒ drink (x, coffee)** 

It will read as *For all x where x is a man who drinks coffee*

**Some dogs are brown** is translated in **∃x: dogs(x) ∧ brown(x)**

It will read as *There exist some x where x is a dog and is brown*


![Pasted image 20230604093048](../pictures/Pasted%20image%2020230604093048.png)

---------------

### Semantics

![Pasted image 20230604093942](../pictures/Pasted%20image%2020230604093942.png)

#### Interpretation function

Given a domain $\Delta$ and a set of constant, function and predicate symbols, we define the **interpretation, I**, as a mapping of:

* Every constant *c* to an **element** I(c) $\in$ $\Delta$ 
* Every function symbol *f/n* to a **function** I(f) : Δ<sup>n</sup> $\rightarrow$ $\Delta$
* Every predicate symbol *P/m* to a **relation** I(P) $\subseteq$ Δ<sup>m</sup>

**The pair (Δ, I) is a structure S for the alphabet**

![Pasted image 20230604095544](../pictures/Pasted%20image%2020230604095544.png)

Finally, given a structure, a variable assignment and formulae, the **evaluation of a formula** is done using **atomic formulae**

##### Summary on evaluation
![Pasted image 20230604095833](../pictures/Pasted%20image%2020230604095833.png)

A formula is:

* **ground** if it does not contain any variable
* **closed** (or a sentence) if it does not contain any free variables
* **open** if it contains **at least on**e free variable
* **clean** if:
	* $\forall$ x, x is either always free or always bound
	* every two occurrences of quantifiers bind different variables

**Every formula can be "cleansed" by means of renaming**, the uniform replacement of all occurrences of a variable x bound by the same occurrence of a quantifier in a formula φ with a variable not occurring in φ is called a renaming of x in φ

todo: exercises



