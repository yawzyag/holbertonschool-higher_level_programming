# Object-relational mappers (ORMs)

![database-python](https://miro.medium.com/max/1050/0*UkOqM_a_agYwUOoV)

[Reference](https://www.fullstackpython.com/object-relational-mappers-orms.html)

---
An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational databases tables into objects that are more commonly used in application code.

## Why are ORMs useful

ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. Developers can use the programming language they are comfortable with to work with a database instead of writing SQL statements or stored procedures.

The ability to write Python code instead of SQL can speed up web application development, especially at the beginning of a project. The potential development speed boost comes from not having to switch from Python code into writing declarative paradigm SQL statements. While some software developers may not mind switching back and forth between languages, it's typically easier to knock out a prototype or start a web application using a single programming language.

ORMs also make it theoretically possible to switch an application between various relational databases. For example, a developer could use  SQLite  for local development and MySQL  in production. A production application could be switched from MySQL to  PostgreSQL  with minimal code modifications.

In practice however, it's best to use the same database for local development as is used in production. Otherwise unexpected errors could hit in production that were not seen in a local development environment. Also, it's rare that a project would switch from one database in production to another one unless there was a pressing reason.

### Do I have to use an ORM for my web application

Python ORM libraries are not required for accessing relational databases. In fact, the low-level access is typically provided by another library called a database connector, such as psycopg (for PostgreSQL) or MySQL-python (for MySQL). Take a look at the table below which shows how ORMs can work with different web frameworks and connectors and relational databases.

---
