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

By default, mongo uses [ TCP ports 27017-27018](27017-27018-mongodb.md). 

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

# Find in city collection all cities that matches the criteria (= MA) and return the count
db.city.find({"city":"MA"}).count() 

# How many cities of state “Indiana” have population greater than 15000 in collection “city” in database “city”?
db.city.find({$and:[{"state":"IN"}, {"pop":{$gt:15000}}]}).count()


####################
# Operators
####################
# Greater than: $gt
db.city.find({"population":{$gt:150000}}).count() 

# And operator: $and
db.city.find({$and:[{population:{$gt:150000}},{"state":"FLORIDA"}]})

# Or operator: $or
db.city.find({$or:[{population:{$lt:1000}},{"state":"FLORIDA"}]})

# Not equal operator: $ne
# equal operator: $e

# Additionally, you can use regex: Cities that starts with HA: 
db.city.find({"city":{$regex:"^HA.*"}})

# What is the name of 101st city in collection “city” when sorted in ascending order according to “city” in database “city”?
db.city.find().sort({"city":1}).skip(100).limit(1)

#####################
# Operations
#####################
# Perform an average on an aggregate of documents
db.city.aggregate({"$group":{"_id":null, avg:{$avg:{"$population"}} }})


# We can dump the contents of the documents present in the flag collection by using the db.collection.find() command. Let's replace the collection name flag in the command and also use pretty() in order to receive the output in a beautified format.
```

