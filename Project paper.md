# Data Management and Analysis - Unit 2

## Team : Gai-Ramil-Sannino

## Description / Abstract

The project was to design a car rental company database, using MySQL or PostgreSQL.
This paper will present each table with a description of attributes and given and user-defined constraints. The aim of the project was to represent a single company in a concise, yet complete way, but also simple to use and to query on.
The resulting database system provides a robust platform for the car rental company to streamline its processes via a decomposition in multiple, linked, tables to keep control of billing, reservations and number of active customers, with a system to balance the type of car with the driver.

---------------

## Database Design

This section contains a description of all the tables, with **primary** and <u>foreign keys</u>, as well as the designed ER model and relational schema for the database

### Customer

1. **user_id**: INTEGER, stores the unique identifier for each customer
2. first_name: VARCHAR(50), stores the name of the customer
3. last_name: VARCHAR(50), stores the surname of the customer
4. nationality: VARCHAR(50), stores the nationality of the customer, this field is usually requested by companies to ensure the validity of the driver's license
5. email: VARCHAR(50), stores the email of the customer
6. telephone: VARCHAR(20), stores the telephone number of the customer

The decision was to let the company have at least one way to contact the customer, so not both of the contact methods are mandatory

### Reservation

1. **reservation_number**: INTEGER, uniquely stores the reservation number for a customer
2. date_reservation: DATE, date in which the reservation was requested. The decision was to limit dates from year 2020 to year 2023.
3. <u>customer_id</u>: INTEGER, foreign key $\rightarrow$ CUSTOMER.user_id
4. type_reservation: VARCHAR(50), the type of reservation requested, between:
	* Standard
	* Corporate
	* Elite
5. insurance_type: VARCHAR(50), the type of insurance that the company will grant to the customer, based on age/experience driving, between:
	* Null
	* Partial
	* Full
6. <u>car_id</u>: INTEGER, foreign key $\rightarrow$ CAR.plate

### Classification

1. **id_type**: VARCHAR(50), identifies the specific type of car requested, between:
	* City Car
	* SUV
	* Luxury
2. cost_day: INTEGER, the cost per day for each category of car, on which the calculation of the cost of the whole reservation will be based on

### Car

1. **plate**: INTEGER, identifier of the car plate, coded in a 4 digit number
2. model: VARCHAR(50), the model of the car
3. brand: VARCHAR(50), the brand of the car
4. engine: VARCHAR(50), the engine of the car
5. <u>type_car</u>: VARCHAR(50), foreign key $\rightarrow$ CLASSIFICATION.id_type

### Trip

1. <u><b>res_id</b></u>: 
	 * INTEGER, foreign key $\rightarrow$ RESERVATION.reservation_number
	 * Also Primary Key (see both <u>underlined</u> and **bold** font)
2. km: INTEGER, number of kilometers driven during the trip
3. days_trip: INTEGER, number of days of the trip, pivotal to calculate the cost of the whole reservation
4. <u>car_id</u>: INTEGER, foreign key $\rightarrow$ CAR.plate

--------------

## Database implementation

The chosen RDBMS was pgadmin4 with the help of the query tool to populate the aforementioned tables.

Data was generated and tweaked and cleaned by the group, the decision was to start with 50 customers for this company.

Below, the SQLs for the tables and the dataset(s) are included. (a questo punto metterei i codici e i datasets, almeno nella forma di come sono fatti, non c'è molto da dire)

--------------------

### Annex, paper structure

Abstract: This paper presents the design and implementation of a comprehensive database system for a car rental company. The objective of the project is to develop an efficient and reliable database solution to manage various aspects of the company's operations, including customer information, vehicle inventory, reservations, and billing. The paper outlines the database design process, describes the key components of the system, and discusses the challenges encountered during the implementation. The resulting database system provides a robust platform for the car rental company to streamline its processes, enhance customer experience, and improve overall operational efficiency.

1. Database Design
	- Conceptual data modeling using entity-relationship diagrams (ERDs) (okay, prima delle descrizioni delle tables, da mettere)
	- Translation of ERDs into a relational schema (okay, come prima, da mettere)
	- Normalization process to ensure data integrity (pisciata)
	- Design of tables, relationships, and constraints (fatto, mancano i constraint/check/trigger se li facciamo, e li farei)

1. Database Implementation
	*  Selection of a database management system (DBMS) (okay, non so che altro dire su pgadmin)
	- Creation of the database schema (ci sono tutte le cose sopra)
	- Implementation of tables, views, and stored procedures (rido male non abbiamo fatto nulla di questo)
	- Populating the database with sample data (scritto tutto)
	- SQL codes and datasets ()
