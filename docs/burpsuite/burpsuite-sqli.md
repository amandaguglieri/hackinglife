---
title: BurpSuite Labs - SQL injection
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, burpsuite, xss
---

# BurpSuite Labs - SQL injection

## SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

### Enuntiation

This lab contains an [SQL injection](https://portswigger.net/web-security/sql-injection) vulnerability in the product category filter. When the user selects a category, the application carries out an SQL query like the following:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

To solve the lab, perform an SQL injection attack that causes the application to display details of all products in any category, both released and unreleased.

### Solution

Filter by one of the categories and, in the URL, instead of that categorry, after the "=" add:

```
' OR '1'='1
```



## SQL injection vulnerability allowing login bypass

### Enuntiation

This lab contains an [SQL injection](https://portswigger.net/web-security/sql-injection) vulnerability in the login function.

To solve the lab, perform an SQL injection attack that logs in to the application as the `administrator` user.

### Solution

In the login page, add to username:

```
administrator'--
```

In password it doesn't matter what you write.
