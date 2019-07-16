# MySQL

![mysql](https://dinfratechsource.files.wordpress.com/2018/12/MySQLimage1.jpg?w=944&h=531&zoom=2)
reference(https://www.tutorialspoint.com/mysql/)

MySQL is the most popular Open Source Relational SQL Database Management System. MySQL is one of the best RDBMS being used for developing various web-based software applications. MySQL is developed, marketed and supported by MySQL AB, which is a Swedish company. This tutorial will give you a quick start to MySQL and make you comfortable with MySQL programming.

-----

# What is a Database?
A database is a separate application that stores a collection of data. Each database has one or more distinct APIs for creating, accessing, managing, searching and replicating the data it holds.

Other kinds of data stores can also be used, such as files on the file system or large hash tables in memory but data fetching and writing would not be so fast and easy with those type of systems.

-----

##  MySQL Database

MySQL is a fast, easy-to-use RDBMS being used for many small and big businesses. MySQL is developed, marketed and supported by MySQL AB, which is a Swedish company. MySQL is becoming so popular because of many good reasons

-----

## Administrative MySQL Command

Here is the list of the important MySQL commands, which you will use time to time to work with MySQL database −

* USE Databasename − This will be used to select a database in the MySQL workarea.

* SHOW DATABASES − Lists out the databases that are accessible by the MySQL DBMS.

* SHOW TABLES − Shows the tables in the database once a database has been selected with the use command.

* SHOW COLUMNS FROM tablename: Shows the attributes, types of attributes, key information, whether NULL is permitted, defaults, and other information for a table.

* SHOW INDEX FROM tablename − Presents the details of all indexes on the table, including the PRIMARY KEY.

* SHOW TABLE STATUS LIKE tablename\G − Reports details of the MySQL DBMS performance and statistics.

-----
# CREATE MYSQL DATABASES AND USERS

To create MySQL database and users, follow these steps:

At the command line, log in to MySQL as the root user:

    mysql -u root -p

Type the MySQL root password, and then press Enter.
To create a database user, type the following command. Replace username with the user you want to create, and replace password with the user's password:

    GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';

This command grants the user all permissions. However, you can grant specific permissions to maintain precise control over database access. For example, to explicitly grant the SELECT permission, you would use the following command:

    GRANT SELECT ON *.* TO 'username'@'localhost';

Type \q to exit the mysql program.
To log in to MySQL as the user you just created, type the following command. Replace username with the name of the user you created in step 3:

    mysql -u username -p
    
Type the user's password, and then press Enter.
To create a database, type the following command. Replace dbname with the name of the database that you want to create:

    CREATE DATABASE dbname;
    
To work with the new database, type the following command. Replace dbname with the name of the database you created in step 7:

    USE dbname;
    
You can now work with the database. For example, the following commands demonstrate how to create a basic table named example, and how to insert some data into it:

    CREATE TABLE example ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
    INSERT INTO example ( id, name ) VALUES ( null, 'Sample data' );
