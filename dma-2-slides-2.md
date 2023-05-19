## [The Entity Relationship Model (ER)](https://www.javatpoint.com/dbms-er-model-concept), we 

This model is used to identify the data elements and a relationship for a specified system via an entity-relationship diagram:

### Entity type and set

- **Entities** &rarr; An entity is a "thing", and object, person or place
  - Strong entities have key values and does not depend on other entitites and are uniquely identified
  - Weak entities are the ones that can have an undefined key attribute and are identified by strong entities
- **Attributes** &rarr; Attributes are properties that define the entity type (e.g. for the entity dog, the attribute breed)
  - The key attribute uniquely identies each entity in the entity set

![image](https://media.geeksforgeeks.org/wp-content/uploads/20230428115454/Introduction-to-ER-Model-2.webp)
> Symbols used in ER models

### Relationship type and set

The relatioship represents *how* two variables are associated

The number of times an entity of an entity set participates in a relationship set is known as **cardinality**

- **1-to-1** 
- **1-to-many** 
- **Many-to-1**
- **Many-to-Many**

![image](https://media.geeksforgeeks.org/wp-content/uploads/20230428090323/Introduction-to-ER-Model-1.webp)
> Components of ER models

### Participation constraint

- **Total Participation** &rarr; Each entity in the entity set must participate in the relationship. Total participation is shown by a double line in the ER diagram

- **Partial Participation** &rarr; The entity in the entity set may or may NOT participate in the relationship 

### Identifiers 

Identifiers (or keys) consist of one or more attributes which identify uniquely instances of an entity

- If formed by one or more attributes, er talk about **internal identifier**
- If we go out of the scope of the entity, we talk about **external identifiers**

