### Definitions

![](pictures/Pasted%20image%2020230530165518.png)

* **Domain** $\rightarrow$ set of valid values for an attribute
* **Relation** $\rightarrow$ a "link" between tables based on values
* **Database** $\rightarrow$ set of relations

-------------

### Intra-relational Constraints 

1. **Record**
	* Constraint on individual *n*-uple
2. **Value**
	* Constraint on single value
3. **Integrity**
	* Functions on individual *n*-uples 

----------

### Keys

A key is a set of attributes which uniquely identify the records of a relation

* **Superkey** $\rightarrow$ A key is a superkey if it does not contain two distinct records t1 and t2 with t1[K]=t2[K]
* **Candidate key** $\rightarrow$ minimal superkey
* **Primary key** $\rightarrow$ A key that does not allow NULL as value

![](pictures/Pasted%20image%2020230530175836.png)

-------

### Inter-relational Constraints

Links between different relations are expressed by common values in replicated attributes

* **Foreign key** $\rightarrow$ links information between different tables through common values and forces them to appear as primary key values in referenced relation

An update or delete operation on a relation can cause inconsistencies, so, in that case:

* Do not allow the operation 
* Cascade elimination 
* Insert NULL Values