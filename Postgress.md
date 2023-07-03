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

### Help
```
Type:  
    \copyright for distribution terms
    \h for help with SQL commands
    \? for help with psql commands
    \g or terminate with semicolon to execute query
    \q to quit
```

### Conninfo
```
\conninfo 
    display information about current connection
```

```
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```

### List database
```
\l
    list databases
        * postgres
        * template0 
        * template1 
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
psql -d <my_db>
```