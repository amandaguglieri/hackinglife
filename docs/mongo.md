---
title: Mongo
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - database
  - NoSQL
---
# Mongo

## To connect to a MongoDB

By default mongo does not require password. Admin is a common mongo database default admin user.

```bash
mongo $ip
mongo <HOST>:<PORT>
mongo <HOST>:<PORT>/<DB>
mongo <database> -u <username> -p '<password>'
```


A collection is a group of documents in the database.


## Basic usage


```mongo
# Enter in mongodb application
mongo

# See help
help

# Display databases
show dbs

# Select a database
use <db>

# Display collections in a database
show collections

# Dump a collection
db.<collection>.find()

# Return the number of records of the collection
db.<collection>.count() 

# Find in current db the username admin
db.current.find({"username":"admin"}) 

# We can dump the contents of the documents present in the flag collection by using the db.collection.find() command. Let's replace the collection name flag in the command and also use pretty() in order to receive the output in a beautified format.

```

