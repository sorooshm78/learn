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
