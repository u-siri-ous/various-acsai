## Knowledge-based Agents

The **knowledge base** in the primary component of knowledge-based agents

A KB is a set of **sentences**, each expressed in a **knowledge representation language**, with sentences that are primary and not derived from others called **axioms**

Each time the agent is called, it performs three , in two operations **TELL** and **ASK**:

1. **TELL** the KB what it perceives
2. **ASK** the KB what action should be performed
3. **TELL** the KB what action was chosen and executes it

Both operations may involve *deriving new sentences from old ones*

-------------------

## Logic - Operators and definitions

1. **Syntax** $\rightarrow$ the grammar
2. **Semantics** $\rightarrow$ the meaning that defines the **truth**
3. **Deductive system** $\rightarrow$ derive consequences from statements

##### Truth, Satisfaction

The semantics define the **truth** in the possible world

If a statement is true in a model, we say that the model *satisfies* the statement

##### Entailment (⊨)

*A sentence follows logically from another sentence* $\rightarrow$ **α ⊨ β**

Formally,
<center><b>α entails β iff, in every model in which α is true, β is also true</b></center>

<center><b>α ⊨ β ↔ M(α) ⊆ M(β)</b></center>

Where M(X) is the set of all models of X

![[Pasted image 20230526103308.png]]
In this example, **we can say that KB entails $\alpha$<sub>1</sub> $\rightarrow$ in every model in which KB is true, α<sub>1</sub> is also true

Conversely, **we can't say that KB entails $\alpha$<sub>2</sub> $\rightarrow$ in some models in which KB is true, α<sub>2</sub> is false

**Entailment** is like the needle being in the haystack; **inference** is like finding it

##### Soundness and completeness - the basics

An inference algorithm:

* is called **sound or truth-preserving** if it derives only entailed sentences
* is **complete** if it can derive any sentence that is entailed

![[Pasted image 20230526104025.png]]

-------------

## Propositional logic

Propositional logic (PL) deals with **propositions** (aka sentences or statements)

### Syntax

![[Pasted image 20230526105706.png]]

Operators have an order: 
1. ¬
2. ∧
3. ∨
4. ⇒
5. ⇔

Atomic sentences (**literals**) consist of a single proposition symbol, while complex sentences use the aforementioned logical connectives and parentheses

------------

### Semantics

The semantics for propositional logic must specify how to compute the truth value of *any* sentence, given a model

Atomic sentences are easy: 

* *True* is true in every model and *False* is false in every model
* The truth value of every other proposition symbol must be specified directly in the model

For complex sentences, we follow this **truth table**:

![[Pasted image 20230526111622.png]]

Other logic gates may be used as well

#### Interpretation and Valuation

![[Pasted image 20230526112406.png]]

![[Pasted image 20230526112633.png]]

#### Example of applied PL

![[Pasted image 20230526112848.png]]