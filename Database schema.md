# Database schema

Note : A button which allows for the creation of mentioned tables has been added to the project, in the development options.

A database schema, containing the structure of the tables used in MySQL is provided here. The database associated with the project was made with MySQL 8.0 and requires an already existing database.

1) Amount Table

--> create table amount(name char(30),password char(30), balance int);

2) History table

--> create table history(name char(30),DateofTransaction date,Credit int,Debit int,TotalBalance int);

The creation of these two tables are vital to the execution of the program. Without these, the program will not work.
Constructive criticism and any help are greatly appreciated.