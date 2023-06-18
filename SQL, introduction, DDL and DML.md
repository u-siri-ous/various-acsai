SQL comprehends:

* **Data Definition Language** (DDL): database schema and data description 
* **Data Manipulation Language** (DML): used for storing, querying, modifying and deleting data
* **Data Control Language** (DCL): deals with the management of permissions, rights and other forms of database control 
* **Transactions Control Language** (TCL): deals with the management of transactions

![](pictures/Pasted%20image%2020230610142333.png)

SQL constraints are used to specify rules for the data in a table, the following are used:

* **NOT NULL**: Ensures that a column cannot have a NULL value 
* **UNIQUE**: Ensures that all values in a column are different 
* **PRIMARY KEY**: A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table 
* **FOREIGN KEY**: Prevents actions that would destroy links between tables 
* **CHECK**: Ensures that the values in a column satisfies a specific condition 
* **DEFAULT**: Sets a default value for a column if no value is specified 
* **CREATE INDEX**: Used to create and retrieve data from the database very quickly

------------

DML statements are used to work with the data in tables:

* **INSERT**
	* INSERT INTO table_name (column1, column2, column3, ...) 
	* VALUES (value1, value2, value3, ...);
* **UPDATE**
	* UPDATE table_name 
	* SET column1 = value1, column2 = value2, ... | SELECT | null | default 
	* WHERE condition;
* **DELETE**
	* DELETE FROM table_name WHERE condition;
* **SELECT**
	* SELECT column1, column2,…, columnN 
	* FROM table_name1, table_name2,…,table_nameN 
	* WHERE condition; and/or ORDER BY column1 ASC|DESC,…, columnN ASC|DESC;

	* SELECT AGGR_OPER (* | [ distinct | all ]) column1, …, columnN 
	* FROM table_name1, table_name2,…,table_nameN 
	* WHERE condition
	
The aggregates operators are: 

* count (Attribute List) 
* sum (Attribute List) 
* avg (Attribute List) 
* min (Attribute List) 
* max (Attribute List)

These are used through the HAVING clause:

* SELECT column(s)\_name_1 
* FROM table(s)_name 
* WHERE condition 
* GROUP BY column(s)\_name_2 
* HAVING condition;

### JOIN

SELECT AttributeList 
FROM table1
INNER/LEFT/RIGHT/FULL OUTER JOIN table2
ON table JoinCondition 
[WHERE Condition]

![](pictures/Pasted%20image%2020230612101127.png)

---------

### Order of execution of commands

1. FROM / JOIN
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. DISTINCT
7. ORDER BY
8. LIMIT / OFFSET