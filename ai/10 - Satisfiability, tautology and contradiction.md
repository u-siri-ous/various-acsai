#### Equivalence

Two sentences α and β are logically equivalent if they are true in the same set of models. We write this as:
<center><b>α ≡ β</b></center>

Moreover:

<center><b>α ≡ β iff α ⊨ β and β ⊨ α</b></center>

----------

#### Tautology - Validity

A formula is a tautology if it always evaluates to *True*, in such case, the formula is **valid**. We write:

<center><b>⊨ φ</b></center>

From our definition of [entailment](obsidian://open?vault=various-acsai&file=ai%2F09%20-%20Logic-based%20agents%2C%20Introduction%20to%20propositional%20logic), we can derive the **deduction theorem**: 

<center><b>For any sentences α and β, α ⊨ β iff the sentence (α ⇒ β) is valid</b></center>

------------------

#### Contradiction

A formula is a contradiction if it always evaluates to *False*, i.e. it's *unsatisfiable*. We write:

<center><b>⊭ φ</b></center>

------------

#### Satisfiability

A propositional formula is **satisfiable** iff it is satisfied by some interpretation, i.e. it's true in some model

Satisfiability can be checked by enumerating the possible models until one is found that satisfies the sentence

α is valid iff ¬α is unsatisfiable, from this we get:

<center><b>α ⊨ β iff the sentence (α ∧ ¬β) is unsatisfiable</b></center>

This is provable by contradiction

-----------

![[pictures/Pasted image 20230526151132.png]]