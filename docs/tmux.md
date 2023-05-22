---
title: Tmux - A terminal multiplexer
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - terminal
  - shells
---

#  Tmux - A terminal multiplexer


## Installation


```bash
sudo apt install tmux -y
```


## Basic usage

start new:

```
tmux
```

start new with session name:

```
tmux new -s myname
```

attach:

```
tmux a  #  (or at, or attach)
```

attach to named:

```
tmux a -t myname
```

list sessions:

```
tmux ls
```

kill session:

```
tmux kill-session -t myname
```

Kill all the tmux sessions:

```
tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill
```

In tmux, hit the prefix `ctrl+b` (my modified prefix is ctrl+a) and then:

 [List all shortcuts](https://gist.github.com/MohamedAlaa/2961058#list-all-shortcuts)

