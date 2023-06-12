### [The Entity Relationship Model (ER)](https://www.javatpoint.com/dbms-er-model-concept)

This model is used to identify the data elements and a relationship for a specified system via an entity-relationship diagram:

### Entity type and set

**Entities** $\rightarrow$ An entity is a "thing", and object, person or place
  - Strong entities have key values and does not depend on other entitites and are uniquely identified
  - Weak entities are the ones that can have an undefined key attribute and are identified by strong entities
**Attributes** $\rightarrow$ Attributes are properties that define the entity type (e.g. for the entity dog, the attribute breed)
  - The key attribute uniquely identies each entity in the entity set

![Pasted image 20230526170314.png](pictures/Pasted%20image%2020230526170314.png)

> Symbols used in ER models

![Pasted image 20230608192040](pictures/Pasted%20image%2020230608192040.png)

### Relationship type and set

The relationship represents *how* two variables are associated

The number of times an entity of an entity set participates in a relationship set is known as **cardinality**

- **1-to-1** 
- **1-to-many** 
- **Many-to-1**
- **Many-to-Many**

![Pasted image 20230526170337.png](pictures/Pasted%20image%2020230526170337.png)
> Components of ER models

### Participation constraint

- **Total Participation** $\rightarrow$ Each entity in the entity set must participate in the relationship. Total participation is shown by a double line in the ER diagram

- **Partial Participation** $\rightarrow$ The entity in the entity set may or may NOT participate in the relationship 

### Identifiers 

Identifiers (or keys) consist of one or more attributes which identify uniquely instances of an entity

- If formed by one or more attributes, of the entity, we talk about **internal identifier**
- If we go out of the scope of the entity, we talk about **external identifiers**

### Generalizations

These are logical links between a *parent* entity, which is more general, and a *child* entity, with the following properties:

- Every instance of a child entity is also an instance of the parent entity, and has at most **one** parent
- Every property of the parent entity (attribute, identifier, relationship or other generalization) is also a property of a child entity $\rightarrow$ *inheritance*
- A generalization is *total* if every instance of the parent entity is also an instance of one of its children, otherwise it is *partial*
- A generalization is *exclusive* if every instance of the parent entity is **at most** an instance of one of the children, otherwise it is *overlapping*
