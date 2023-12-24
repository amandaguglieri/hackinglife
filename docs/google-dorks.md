---
title: Google dorks
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanning
  - osint 
  - dorking
---

# Google Dorks

Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using.   

This is an awesome database with more than 7K googledork entries: [https://www.exploit-db.com/google-hacking-database](https://www.exploit-db.com/google-hacking-database).

| Google Dorking Query | Expected results |
|------------------------------- | ---------------------- |
| intitle:"api" site: "example.com" |  Finds all publicly available API related content in a given hostname. Another cool example for API versions:  inurl:"/api/v1" site: "example.com" |
| intitle:"json" site: "example.com" |  Many APIs use json, so this might be a cool filter |
| inurl:"/wp-son/wp/v2/users" |  Finds all publicly available WordPress API user directories. |
| intitle:"index.of" intext:"api.txt" | Finds publicly available API key files. |
|  inurl:"/api/v1" intext:"index of /" | Finds potentially interesting API directories. |
| intitle:"index of" api_key OR "api key" OR apiKey -pool | This is one of my favorite queries. It lists potentially exposed API keys. |


