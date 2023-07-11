```
$psql
failed: FATAL:  role "sm" does not exist
```

Swich to postgres user 
```
sudo su postgres
```
Then
```
psql
```

## Help
```
Type:  
    \copyright for distribution terms
    \h for help with SQL commands
    \? for help with psql commands
    \g or terminate with semicolon to execute query
    \q to quit
```

## Conninfo
```
\conninfo 
    display information about current connection
```

```
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```

## List database
```
\l
    list databases
        * postgres
        * template0 
        * template1 
```
### Template1
template1 is the one used by default. You can alter / add / remove objects there to affect every newly created DB. CREATE DATABASE basically makes a copy of it on the file level (very fast) to create a new instance.

### Template0
template0 starts out being the same and should never be changed - to provide a virgin template with original settings.
template0 contains the same data as template1. We could think of this template database as a fallback if anything irreversible happens to template1. As such, this template database should never be modified in any way as soon as the database cluster has been initialized. To create a database with template0 as the template database
```
CREATE DATABASE new_db_name TEMPLATE template0;
```

### Custom Template Databases
To create a new database with this template
```
CREATE DATABASE new_db_name TEMPLATE template_db_name;
```

### Create database
```
create database <database_name>;
```
### Connect to another database
```
-d, --dbname=DBNAME      database name to connect to (default: "postgres")
```
Example
```
psql -d <db_name>
```

```
\c <db_name>
```

### Show table
```
\d
```
or
```
\d <tablename>
```

## Create User
CREATE ROLE adds a new role to a PostgreSQL database cluster. A role is an entity that can own database objects and have database privileges; a role can be considered a “user”, a “group”, or both depending on how it is used.
```
CREATE ROLE name [ [ WITH ] option [ ... ] ]
where option can be:

    | SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | REPLICATION | NOREPLICATION
    | BYPASSRLS | NOBYPASSRLS
    | CONNECTION LIMIT connlimit
    | [ ENCRYPTED ] PASSWORD 'password' | PASSWORD NULL
    | VALID UNTIL 'timestamp'
    | IN ROLE role_name [, ...]
    | IN GROUP role_name [, ...]
    | ROLE role_name [, ...]
    | ADMIN role_name [, ...]
    | USER role_name [, ...]
    | SYSID uid
```

### List Rols
```
\du[S+] [PATTERN]      list roles
```

```
CREATE ROLE -> create role
DROP ROLE -> delete role
ALTER ROLE -> change role
```

```
CREATE ROLL <user> LOGIN 
# same
CRETAE USER <user>
```

```
ALTER GROUP <group> ADD USER <user>
ALTER GROUP <group> DROP USER <user>
```

```
GRANT <permission_type> ON <table_name> TO <role_name>;
```

Introduction to PostgreSQL group roles

It is easier to manage roles as a group so that you can grant or revoke privileges from a group as a whole instead of doing it on an individual role.

Typically, you create a role that represents a group and then grants membership in the group role to individual roles.

By convention, a group role does not have the LOGIN privilege. It means that you will not be able to use the group role to log in to PostgreSQL.

To create a group role, you use the CREATE ROLE statement as follows:

```
CREATE ROLE group_role_name;
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)
```

For example, the following statement creates a group role sales:

```
CREATE ROLE sales;
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)
```

When you use the \du command in the psql tool, you will see that the group roles are listed together with user roles:

```
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 alice     |                                                            | {}
 api       | 1000 connections                                           | {}
 bob       | Cannot login                                               | {}
 dba       | Create DB                                                  | {}
 john      | Superuser                                                  | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 sales     | Cannot login                                               | {}
Code language: Shell Session (shell)
```

To add a role to a group role, you use the following form of the GRANT statement:

```
GRANT group_role to user_role;
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)
```

For example, the following statement adds the role alice to the group role sales:

```
GRANT sales TO alice;
Code language: SQL (Structured Query Language) (sql)
```

If you run the \du command again, you will see that alice now is a member of sales:

```
\du
Code language: Shell Session (shell)

                                 List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 alice     |                                                            | {sales}
 api       | 1000 connections                                           | {}
 bob       | Cannot login                                               | {}
 dba       | Create DB                                                  | {}
 john      | Superuser                                                  | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 sales     | Cannot login                                               | {}
Code language: Shell Session (shell)
```
To remove a user role from a group role, you use REVOKE statement:

```
REVOKE group_role FROM user_role;
```

For example, the following statement uses the REVOKE statement to remove the role alice from the group role sales:

```
REVOKE sales FROM alice;
```

Notice that PostgreSQL does not allow you to have circular membership loops, in which a role is the member of another role and vice versa.

## System Catalogs
Look dont touch

### pg_database
The catalog pg_database stores information about the available databases. Databases are created with the CREATE DATABASE command

### pg_tables
The view pg_tables provides access to useful information about each table in the databas

### pg_authid
The catalog pg_authid contains information about database authorization identifiers (roles). A role subsumes the concepts of “users” and “groups”. A user is essentially just a role with the rolcanlogin flag set. Any role (with or without rolcanlogin) can have other roles as members; see pg_auth_members.

Since this catalog contains passwords, it must not be publicly readable. pg_roles is a publicly readable view on pg_authid that blanks out the password field.


### pg_roles
The view pg_roles provides access to information about database roles. This is simply a publicly readable view of pg_authid that blanks out the password field. 


## Access Control
Postgres provides mechanisms to allow users to limit the access to their data that is provided to other users.

Database superusers
Database super-users (i.e., users who have pg_user.usesuper set) silently bypass all of the access controls described below with two exceptions: manual system catalog updates are not permitted if the user does not have pg_user.usecatupd set, and destruction of system catalogs (or modification of their schemas) is never allowed.

Access Privilege
The use of access privilege to limit reading, writing and setting of rules on classes is covered in grant/revoke(l).

Class removal and schema modification
Commands that destroy or modify the structure of an existing class, such as alter, drop table, and drop index, only operate for the owner of the class. As mentioned above, these operations are never permitted on system catalogs.


### Privileges
When an object (table, function, etc.) is created, an owner is immediately assigned, typically the role that executed the creation declaration is considered the owner. The default state of a newly created object is that only the owner can interact with it. Therefore to share or allow other roles access to the object it is necessary to grant privileges. 

The permissions relevant to a particular object change based on the type of item, and the power to alter default privileges or destroy an entity is intrinsic to being the possessor of the object. This right cannot be given or withdrawn in and of itself. On the other hand, just like any other privilege, you can pass down the right to own anything through the role members.

There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, USAGE, SET and ALTER SYSTEM.

Privileges can be inherited by roles using INHERIT to attribute automatically gain privileges of roles of which they are members. 

```
grant <acceess> on <table> to <user>;
grant SELECT on users to alice;
```

```
revoke <acceess> on <table> from <user>;
revoke SELECT on users from alice;
```


### The available privileges are:
SELECT
Allows SELECT from any column, or specific column(s), of a table, view, materialized view, or other table-like object. Also allows use of COPY TO. This privilege is also needed to reference existing column values in UPDATE, DELETE, or MERGE. For sequences, this privilege also allows use of the currval function. For large objects, this privilege allows the object to be read.

INSERT
Allows INSERT of a new row into a table, view, etc. Can be granted on specific column(s), in which case only those columns may be assigned to in the INSERT command (other columns will therefore receive default values). Also allows use of COPY FROM.

UPDATE
Allows UPDATE of any column, or specific column(s), of a table, view, etc. (In practice, any nontrivial UPDATE command will require SELECT privilege as well, since it must reference table columns to determine which rows to update, and/or to compute new values for columns.) SELECT ... FOR UPDATE and SELECT ... FOR SHARE also require this privilege on at least one column, in addition to the SELECT privilege. For sequences, this privilege allows use of the nextval and setval functions. For large objects, this privilege allows writing or truncating the object.

DELETE
Allows DELETE of a row from a table, view, etc. (In practice, any nontrivial DELETE command will require SELECT privilege as well, since it must reference table columns to determine which rows to delete.)

## PostgreSQL Function
PostgreSQL functions, also known as Stored Procedures, allow you to carry out operations that would normally take several queries and round trips in a single function within the database. Functions allow database reuse as other applications can interact directly with your stored procedures instead of a middle-tier or duplicating code.

Functions can be created in a language of your choice like SQL, PL/pgSQL, C, Python, etc.
Syntax

The basic syntax to create a function is as follows −
```
CREATE [OR REPLACE] FUNCTION function_name (arguments) 
RETURNS return_datatype AS $variable_name$
   DECLARE
      declaration;
      [...]
   BEGIN
      < function_body >
      [...]
      RETURN { variable_name | value }
   END; LANGUAGE plpgsql;
```

Where,
* function-name specifies the name of the function.

* [OR REPLACE] option allows modifying an existing function.

* The function must contain a return statement.

* RETURN clause specifies that data type you are going to return from the function. The return_datatype can be a base, composite, or domain type, or can reference the type of a table column.

* function-body contains the executable part.

* The AS keyword is used for creating a standalone function.

* plpgsql is the name of the language that the function is implemented in. Here, we use this option for PostgreSQL, it Can be SQL, C, internal, or the name of a user-defined procedural language. For backward compatibility, the name can be enclosed by single quotes.

Example

The following example illustrates creating and calling a standalone function. This function returns the total number of records in the COMPANY table. We will use the COMPANY table, which has the following records −

```
testdb# select * from COMPANY;
 id | name  | age | address   | salary
----+-------+-----+-----------+--------
  1 | Paul  |  32 | California|  20000
  2 | Allen |  25 | Texas     |  15000
  3 | Teddy |  23 | Norway    |  20000
  4 | Mark  |  25 | Rich-Mond |  65000
  5 | David |  27 | Texas     |  85000
  6 | Kim   |  22 | South-Hall|  45000
  7 | James |  24 | Houston   |  10000
(7 rows)
```

Function totalRecords() is as follows −

```
CREATE OR REPLACE FUNCTION totalRecords ()
RETURNS integer AS $total$
declare
	total integer;
BEGIN
   SELECT count(*) into total FROM COMPANY;
   RETURN total;
END;
$total$ LANGUAGE plpgsql;
```

When the above query is executed, the result would be −

```
testdb# CREATE FUNCTION
```

Now, let us execute a call to this function and check the records in the COMPANY table

```
testdb=# select totalRecords();
```

When the above query is executed, the result would be −

```
 totalrecords
--------------
      7
(1 row)
```

## CREATE RULE
```
CREATE [ OR REPLACE ] RULE name AS ON event
    TO table_name [ WHERE condition ]
    DO [ ALSO | INSTEAD ] { NOTHING | command | ( command ; command ... ) }

where event can be one of:

    SELECT | INSERT | UPDATE | DELETE
```
CREATE RULE defines a new rule applying to a specified table or view. CREATE OR REPLACE RULE will either create a new rule, or replace an existing rule of the same name for the same table.

The PostgreSQL rule system allows one to define an alternative action to be performed on insertions, updates, or deletions in database tables. Roughly speaking, a rule causes additional commands to be executed when a given command on a given table is executed. Alternatively, an INSTEAD rule can replace a given command by another, or cause a command not to be executed at all. Rules are used to implement SQL views as well. It is important to realize that a rule is really a command transformation mechanism, or command macro. The transformation happens before the execution of the command starts. If you actually want an operation that fires independently for each physical row, you probably want to use a trigger, not a rule.


### Example
```
CREATE OR REPLACE RULE add_user
AS ON INSERT
TO users
WHERE NEW.email ilike 'a%'
DO ALSO INSERT INTO a_users(id, email) VALUES (NEW.id, NEW.email)
```
define rule on event insert on table users if email start with a also insert in users table , insert in table a_users

-----

```
CREATE OR REPLACE RULE add_user
AS ON INSERT
TO users
WHERE NEW.email ilike 'a%'
DO INSTEAD INSERT INTO a_users(id, email) VALUES (NEW.id, NEW.email)
```
like above but not run two command and just do rule command

## CREATE TRIGGER
```
CREATE [ OR REPLACE ] [ CONSTRAINT ] TRIGGER name { BEFORE | AFTER | INSTEAD OF } { event [ OR ... ] }
    ON table_name
    [ FROM referenced_table_name ]
    [ NOT DEFERRABLE | [ DEFERRABLE ] [ INITIALLY IMMEDIATE | INITIALLY DEFERRED ] ]
    [ REFERENCING { { OLD | NEW } TABLE [ AS ] transition_relation_name } [ ... ] ]
    [ FOR [ EACH ] { ROW | STATEMENT } ]
    [ WHEN ( condition ) ]
    EXECUTE { FUNCTION | PROCEDURE } function_name ( arguments )

where event can be one of:

    INSERT
    UPDATE [ OF column_name [, ... ] ]
    DELETE
    TRUNCATE
```
CREATE TRIGGER creates a new trigger. CREATE OR REPLACE TRIGGER will either create a new trigger, or replace an existing trigger. The trigger will be associated with the specified table, view, or foreign table and will execute the specified function function_name when certain operations are performed on that table.

To replace the current definition of an existing trigger, use CREATE OR REPLACE TRIGGER, specifying the existing trigger's name and parent table. All other properties are replaced.

The trigger can be specified to fire before the operation is attempted on a row (before constraints are checked and the INSERT, UPDATE, or DELETE is attempted); or after the operation has completed (after constraints are checked and the INSERT, UPDATE, or DELETE has completed); or instead of the operation (in the case of inserts, updates or deletes on a view). If the trigger fires before or instead of the event, the trigger can skip the operation for the current row, or change the row being inserted (for INSERT and UPDATE operations only). If the trigger fires after the event, all changes, including the effects of other triggers, are “visible” to the trigger.

A trigger that is marked FOR EACH ROW is called once for every row that the operation modifies. For example, a DELETE that affects 10 rows will cause any ON DELETE triggers on the target relation to be called 10 separate times, once for each deleted row. In contrast, a trigger that is marked FOR EACH STATEMENT only executes once for any given operation, regardless of how many rows it modifies (in particular, an operation that modifies zero rows will still result in the execution of any applicable FOR EACH STATEMENT triggers).

Triggers that are specified to fire INSTEAD OF the trigger event must be marked FOR EACH ROW, and can only be defined on views. BEFORE and AFTER triggers on a view must be marked as FOR EACH STATEMENT.

## Transactions
Transactions are a fundamental concept of all database systems. The essential point of a transaction is that it bundles multiple steps into a single, all-or-nothing operation. The intermediate states between the steps are not visible to other concurrent transactions, and if some failure occurs that prevents the transaction from completing, then none of the steps affect the database at all.

For example, consider a bank database that contains balances for various customer accounts, as well as total deposit balances for branches. Suppose that we want to record a payment of $100.00 from Alice's account to Bob's account. Simplifying outrageously, the SQL commands for this might look like:

```
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
UPDATE branches SET balance = balance - 100.00
    WHERE name = (SELECT branch_name FROM accounts WHERE name = 'Alice');
UPDATE accounts SET balance = balance + 100.00
    WHERE name = 'Bob';
UPDATE branches SET balance = balance + 100.00
    WHERE name = (SELECT branch_name FROM accounts WHERE name = 'Bob');
```

The details of these commands are not important here; the important point is that there are several separate updates involved to accomplish this rather simple operation. Our bank's officers will want to be assured that either all these updates happen, or none of them happen. It would certainly not do for a system failure to result in Bob receiving $100.00 that was not debited from Alice. Nor would Alice long remain a happy customer if she was debited without Bob being credited. We need a guarantee that if something goes wrong partway through the operation, none of the steps executed so far will take effect. Grouping the updates into a transaction gives us this guarantee. A transaction is said to be atomic: from the point of view of other transactions, it either happens completely or not at all.

We also want a guarantee that once a transaction is completed and acknowledged by the database system, it has indeed been permanently recorded and won't be lost even if a crash ensues shortly thereafter. For example, if we are recording a cash withdrawal by Bob, we do not want any chance that the debit to his account will disappear in a crash just after he walks out the bank door. A transactional database guarantees that all the updates made by a transaction are logged in permanent storage (i.e., on disk) before the transaction is reported complete.

Another important property of transactional databases is closely related to the notion of atomic updates: when multiple transactions are running concurrently, each one should not be able to see the incomplete changes made by others. For example, if one transaction is busy totalling all the branch balances, it would not do for it to include the debit from Alice's branch but not the credit to Bob's branch, nor vice versa. So transactions must be all-or-nothing not only in terms of their permanent effect on the database, but also in terms of their visibility as they happen. The updates made so far by an open transaction are invisible to other transactions until the transaction completes, whereupon all the updates become visible simultaneously.

In PostgreSQL, a transaction is set up by surrounding the SQL commands of the transaction with BEGIN and COMMIT commands. So our banking transaction would actually look like:

```
BEGIN;
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
-- etc etc
COMMIT;
```

If, partway through the transaction, we decide we do not want to commit (perhaps we just noticed that Alice's balance went negative), we can issue the command ROLLBACK instead of COMMIT, and all our updates so far will be canceled.

PostgreSQL actually treats every SQL statement as being executed within a transaction. If you do not issue a BEGIN command, then each individual statement has an implicit BEGIN and (if successful) COMMIT wrapped around it. A group of statements surrounded by BEGIN and COMMIT is sometimes called a transaction block.

## CREATE INDEX
```
CREATE [ UNIQUE ] INDEX [ CONCURRENTLY ] [ [ IF NOT EXISTS ] name ] ON [ ONLY ] table_name [ USING method ]
    ( { column_name | ( expression ) } [ COLLATE collation ] [ opclass [ ( opclass_parameter = value [, ... ] ) ] ] [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] )
    [ INCLUDE ( column_name [, ...] ) ]
    [ NULLS [ NOT ] DISTINCT ]
    [ WITH ( storage_parameter [= value] [, ... ] ) ]
    [ TABLESPACE tablespace_name ]
    [ WHERE predicate ]
```
![index](https://dataschool.com/assets/images/sql-optimization/how_to_index/Index_pointsTo_table.png)

## Backup and Restore

for backup
```
pg_dump -U <user> <database_name> > <filename>
pg_dump -U <user> <database_name> -f <filename>
```
diffrent format 
```
pg_dump -U <user> <database_name> -f <filename> -Fc #(binary format)
pg_dump -U <user> <database_name> -f <filename> -Fd #(directory)
pg_dump -U <user> <database_name> -f <filename> -Ft #(tar format) 
```

for restore 
```
\i <backup_filename> # just for sql file
or
pg_restore -U <user> -C # create  <backup_filename> -d <database_name> <filename]]]>
```

## Aggregate Functions
Aggregate functions compute a single result from a set of input values. The built-in aggregate functions

### avg(expression)
the average (arithmetic mean) of all input values
```
SELECT AVG(price) FROM products
```

### min(expression)
minimum value of expression across all input values
```
SELECT MIN(price) FROM products
```

### sum(expression)
sum of expression across all input values
```
SELECT SUM(price) FROM products
```

### count(*)
number of input rows
```
SELECT COUNT(price) FROM products
```

## Window Functions

A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. However, window functions do not cause rows to become grouped into a single output row like non-window aggregate calls would. Instead, the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

Here is an example that shows how to compare each employee's salary with the average salary in his or her department:
```
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;
```
```
  depname  | empno | salary |          avg
-----------+-------+--------+-----------------------
 develop   |    11 |   5200 | 5020.0000000000000000
 develop   |     7 |   4200 | 5020.0000000000000000
 develop   |     9 |   4500 | 5020.0000000000000000
 develop   |     8 |   6000 | 5020.0000000000000000
 develop   |    10 |   5200 | 5020.0000000000000000
 personnel |     5 |   3500 | 3700.0000000000000000
 personnel |     2 |   3900 | 3700.0000000000000000
 sales     |     3 |   4800 | 4866.6666666666666667
 sales     |     1 |   5000 | 4866.6666666666666667
 sales     |     4 |   4800 | 4866.6666666666666667
(10 rows)
```

### row_number ()
Returns the number of the current row within its partition, counting from 1.

### rank ()
Returns the rank of the current row, with gaps; that is, the row_number of the first row in its peer group.


## CREATE VIEW

CREATE VIEW — define a new view
```
CREATE [ OR REPLACE ] [ TEMP | TEMPORARY ] [ RECURSIVE ] VIEW name [ ( column_name [, ...] ) ]
    [ WITH ( view_option_name [= view_option_value] [, ... ] ) ]
    AS query
    [ WITH [ CASCADED | LOCAL ] CHECK OPTION ]
```

Usage
```
SELECT * FROM <view_name>
```

CREATE VIEW defines a view of a query. The view is not physically materialized. Instead, the query is run every time the view is referenced in a query.

CREATE OR REPLACE VIEW is similar, but if a view of the same name already exists, it is replaced. The new query must generate the same columns that were generated by the existing view query (that is, the same column names in the same order and with the same data types), but it may add additional columns to the end of the list. The calculations giving rise to the output columns may be completely different.

If a schema name is given (for example, CREATE VIEW myschema.myview ...) then the view is created in the specified schema. Otherwise it is created in the current schema. Temporary views exist in a special schema, so a schema name cannot be given when creating a temporary view. The name of the view must be distinct from the name of any other relation (table, sequence, index, view, materialized view, or foreign table) in the same schema.

