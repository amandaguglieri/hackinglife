---
title: SQL injection
author: amandaguglieri
draft: false
TableOfContents: true
tags: pentesting,web 
---

SQL stands for Structure Query Language.

SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database:

+ to view data.
+ to retrieve it.
+ to modify it.
+ to delete it.
+ to compromise the infraestructure with what is known for instance as a denial of service attack.


A detailed Cheat sheet with manual union and blind attacks can be found in the [SQLi Cheat sheet](sqli.md).

## Examples

1. [Retrieving hidden data](#data)
2. [Subverting application logic](#logic)
3. [UNION attacks](#union)
4. [Examining the database](#database)
5. [Blind SQL injection](#blind)



### Retrieving hidden data<a name="data"></a>

Examples at a shopping application 

| Request URL | SQL Query | Explained |
| --- | --------- | ----------|
| http://insecure-website.com/products?category=Gifts | SELECT * FROM products WHERE category='Gift' AND release=1 | Restriction "released" is being used to hide products that are not released. Unreleased products will be presumably released=0 |
| http://insecure-website.com/products?category=Gifts'-- | SELECT * FROM products WHERE category='Gift'--' AND released=1 | Explained: Double dash sequence -- is a comment indicator in SQL which means that the rest of the query is interpretated as a comment. The application will display all the products in a category, being released or not. | 
| https://insecure-website.com/products?category=Gifts'+OR+1=1-- | SELECT * FROM products WHERE category='Gifts' OR 1=1--' AND released=1 | This will return all items where category is Gifts, or 1=1. Since 1=1 is always true, the query will return all items. | 


### Subverting application logic<a name="logic"></a>

| Request URL | SQL Query | Explained |
| ----------- | --------- | --------- |
| Login  |  SELECT * FROM users WHERE username="admin" AND password="lalalala" | Login process, probably with a POST method |
| Login: Adding admin'-- in the username and '' in the password field | SELECT * FROM users where username="admin'-- AND password='' | This query returns the user whose name is admin and succesfully logs the attacker as that user. |


### UNION attacks<a name="union"></a>

In cases where the results of a SQL query are returned within the application responses, an attacker may try to retrieve data from others tables using the keyword UNION. They also can examine the existing database.



## Clasification

SQLi (for SQL injection) typically falls under three categories.


### 1. In-band SQLi / or Classic SQL injection

Attacks are sent from the same channel in which results are collected.


#### Error-based SQLi

The attacker performs actions that cause the database to produce error messages. The attacker can potentially use the data provided by these error messages to gather information about the structure of the database.


#### Union-based SQLi

This technique uses the UNION SQL operator.


### 2. Inferential (Blind) SQLi

The attacker sends data payloads to the server and observes the response and behaviour of the server to learn more about its structure. This method is called SQLi because the data is not transferred from the website database to the attacker.

Blind SQL injection relies on the response and behavioral pattern of the server to they are tipically slower to execute but may be just harmful.

#### Boolean-based (content-based) Blind SQLi

Inferential SQL injection technique that relies on sending a SQL query to the database which forces the application to return a different result depending on whether the query returns a TRUE or FLASE result.


#### Time-Based Blind SQLi

If you don't get a TRUE or FALSE response, sometimes you may infere if it is TRUE or FALSE based on time of response. Time-based SQL injection is a inferential SQL injection technique that relies on sending a SQL query to the database, which forces the database to wait for a specified amount of time (in seconds) before responding. The response time will indicate to the attacker whether the result of the query is TRUE or FALSE.


### 3. Out-of.Band SQLi

It's used when an attacjer is unabled to use the same channel to launch the attack and gather results. Out-of-band SQLi techniques would rely on the database server's ability to maje DNS or HTTP request to deliver data to an attacker.

Such is the case of Microsoft SQL Server's xp_dirtree command, which can be used to make DNS request to a server that an attacker controls, as well as Oracle Database's UTL_HTTP package, which can be used to send HTTP requests from SQL and PL/SQL ti a server that an attacker controls.


## Cheat sheet

A detailed Cheat sheet with manual union and blind attacks can be found in the [SQLi Cheat sheet](sqli.md).

## DUAL

The DUAL is a special one row, one column table present by default in all Oracle databases. The owner of DUAL is SYS, but DUAL can be accessed by every user. This is a possible payload for SQLi:

```
'+UNION+SELECT+NULL+FROM+dual--
```

Oracle syntax requires the use of FROM, but some queries don't requires any table. For these case we use DUAL. Also Oracle doesn't allow the queries that employ information_schema.tables.
