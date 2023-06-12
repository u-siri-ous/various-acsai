A nested query is a SELECT statement that is typically enclosed in parentheses, and embedded within a primary SELECT, INSERT, or DELETE operation 

In the WHERE clause there can be expressions in which the value of an attribute is compared with the result of another query, and it will return only one value

SELECT 
FROM 
WHERE (Attribute expr SELECT FROM WHERE)

### ANY/ALL

**ANY**: the condition is satisfied if the comparison between the attribute value and at least one of the values returned from the nested query is true for one row

**ALL**: the condition is satisfied if the comparison between the attribute value and all the values returned from the nested query is true for all rows

SELECT column_name(s) 
FROM table_name 
WHERE column_name | operator 
ANY/ALL (SELECT column_name FROM table_name WHERE condition);

### IN

The IN operator allows to specify multiple values in a WHERE clause, shorthand OR cascade

SELECT ListAttributes 
FROM ExternalTable 
WHERE Value/s IN 
SELECT ListAttributes2 FROM InnerTable WHERE Condition

### EXISTS

It's used to test existence of any record in a subquery

SELECT ListAttributes 
FROM ExternalTable 
WHERE EXISTS 
SELECT ListAttributes2 FROM InnerTable WHERE Condition

------------

## VIEWS

A view is a virtual table based on the result-set of an SQL statement

The fields in a view are fields from one or more real tables in the database

CREATE VIEW view_name (namecolum1, namecolum2,…) AS 
SELECT column1, column2, ... 
FROM table_name 
WHERE condition;

---------

![](pictures/Pasted%20image%2020230612105751.png)