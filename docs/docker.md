---
title: docker
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - docker
---
# docker 

At the core of the Docker architecture lies a client-server model, where we have two primary components:

- The Docker daemon
- The Docker client

The Docker client acts as our interface for issuing commands and interacting with the Docker ecosystem, while the `Docker Daemon`, also known as the Docker server, is responsible for executing those commands and managing containers.


Think of a `Docker image` as a blueprint or a template for creating containers. A `Docker container` is an instance of a Docker image. It is a lightweight, isolated, and executable environment that runs applications. While `images` are immutable and `read-only`, `containers` are mutable and `can be modified` during runtime. However, any modifications made to a container's filesystem are not persisted unless explicitly saved as a new image or stored in a persistent volume.

[See Pentesting docker](cloud/containers/pentesting-docker.md).

## Installation

To make sure that I have docker engine, docker compose and nginx installed.

```bash
sudo apt install docker docker-compose nginx
```

Depending on the image you are going to compose you will need nginx or other dependencies. 

Another way, see [https://www.kali.org/docs/containers/installing-docker-on-kali/](https://www.kali.org/docs/containers/installing-docker-on-kali/)

```
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker --now
docker
sudo usermod -aG docker $USER
```


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
