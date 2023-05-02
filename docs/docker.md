---
title: docker
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - docker
---

# docker 


## Installation

To make sure that I have docker engine, docker compose and nginx installed.

```bash
sudo apt install docker docker-compose nginx
```

Depending on the image you are going to compose you will need nginx or other dependencies. 

## Basic commands

```bash
# show all processes 
docker ps -a

# Actions on dockerInstance/PID/part of id if unique: restart, stop, start, status
sudo docker <restart/stop/start/status> <nameOfDockerInstance/PID/partOfIDifUnique>

# Create the first docker instance: Hello, world! It gets the setting from docker.hub
sudo docker run hello-world
# run: build and deploy an instance
# by default, docker saves everything in /var/lib/docker

# Execute commands in an already running docker instance. You can execute a terminal or a command. 
sudo docker run -it <image> <echo lala / bf bash>
# image: for instance, debian
# <echo lala or bf bash>: command echo lala. Or terminal in bash




```
