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
