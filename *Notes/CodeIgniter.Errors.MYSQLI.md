---
title: CodeIgniter.Errors.MYSQLI
date: 2023-10-26
tags:
  - MySQL
  - CodeIgniter
---

---

# undefined constant MYSQLI_STORE_RESULT (CodeIgniter)

```php
CRITICAL - 2023-01-22 16:32:47 --> Undefined constant "CodeIgniter\Database\MySQLi\MYSQLI_STORE_RESULT"
```

## Fix

1. Edit `/etc/php/php.ini`
2. Find `extension=mysqli` and `extension=pdo_mysql` then uncomment.

---

# Error connecting to the database: No such file or directory

```php
ERROR --> Error connecting to the database: No such file or directory
CRITICAL --> Unable to connect to the database.
Main connection [MySQLi]: No such file or directory
```

## Fix

1. Edit `/etc/php/php.ini`
2. Find `pdo_mysql.default_socket` and set its value to `/var/mysql/mysql.sock`
