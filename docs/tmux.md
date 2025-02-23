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


##  Tmux Plugin Manager 

### Installation

 clone the [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) repo to our home directory:

```shell-session
 git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

Next, create a .tmux.conf file in the home directory.

```shell-session
touch .tmux.conf
```

The config file should have the following contents:

```
# Set TPM plugin path
set -g @plugin 'tmux-plugins/tpm'

# Example plugins (optional)
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'

# Initialize TPM
run '~/.tmux/plugins/tpm/tpm'

# Change normal binding 
bind-key p pipe-pane 'cat >> ~/tmux-session.log' \; display-message 'Logging started'
unbind P
bind-key P pipe-pane

# Set a limit
set -g history-limit 50000

```

Source the file:

```shell-session
tmux source ~/.tmux.conf 
```

### Basic usage

```
# Initiate a tmux
tmux

# Start logging the session. As I have modified the natural binding of the tool to avoid conflicts with my i3 windows manager, my shortcuts to enable logs are:
CTRL-B   P

# Now, when done, exit tmux
exit

# Logs are usually saved to 
cat ~/tmux-session.log

# A nice thing is that they accumulate


# Split vertically the terminal.
CTRL-B %

# Split horizontally the terminal
CTRL-B "

# Move from one pane to another
CTRL-B then arrow keys (`←`, `→`, `↑`, `↓`)

# Manually Clear History Inside a Pane
Ctrl + B, then :
# Then type:
clear-history
# and hit Enter.

# The default logging path is $HOME To change that, add set -g @logging-path "path" to .tmux.conf file
```


Finally, here are some additional plugins that we like:

- [tmux-sessionist](https://github.com/tmux-plugins/tmux-sessionist) - Gives us the ability to manipulate Tmux sessions from within a session: switching to another session, creating a new named session, killing a session without detaching Tmux, promote the current pane to a new session, and more.
    
- [tmux-pain-control](https://github.com/tmux-plugins/tmux-pain-control) - A plugin for controlling panes and providing more intuitive key bindings for moving around, resizing, and splitting panes.
    
- [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) - This extremely handy plugin allows us to restore our Tmux environment after our host restarts. Some features include restoring all sessions, windows, panes, and their order, restoring running programs in a pane, restoring Vim sessions, and more.

Check out the complete [tmux plugins list](https://github.com/tmux-plugins/list) to see if others would fit nicely into your workflow. For more on Tmux, check out this excellent [video](https://www.youtube.com/watch?v=Lqehvpe_djs) by Ippsec and this [cheat sheet](https://mavericknerd.github.io/knowledgebase/ippsec/tmux/) based on the video.