---
Title: emacs
author: amandaguglieri
draft: false
TableOfContents: true
---

## Syntax

Before starting, it is convenient to consider the syntax we'll be using:


```
C-<char> 
We'll keep press CTRL key and at the same time a character.

M-<char>
We'll keep press ALT key and at the same time a character.

ESC <char>
We'll press ESC key, and after that we'll press the character.

C <char>
We'll press CTRL key, and after that we'll press the character.

M <char>
We'll press ALT key, and after that we'll press the character.
```

## Basic commands

**Disclaimer**: when creating this cheat sheet, I've realized that I'm totally in love with emacs, meaning this article is full of bias comments. Neutrality is overrated.


### Session and process management

```
 # Close session. It will ask if you want to save the buffers.
C-x C-c

# Cancel a running process.
C-g

# Remove all open windows and expand the windows that contains the active cursor position 
C-x 1

```

### Cursor Movement 

A difference with vim or neovim editor, "cursor mode" and "insert mode" go together in emacs, meaning you will be able to insert any character from whenever the cursor is without having to switch from one mode to another. 

There is also a small but big difference. Emacs includes a blank character at the end of the line. This alone can sound very vague, but it allows you to move in a more natural and human way from the beginning of one line to the end of the previous one. Just this silly feature makes me love more emacs than vim (#sorryVimDudes). 


```
# Go to previous line.
C-p

# Go to next line.
C-n

# Move cursor position one character forwards.
C-f

# Move cursos position one character backwards.
C-b

# Go to the beginning of the line.
C-a

# Go to the end of the line.
C-e

# Go to the beginning of the sentence.
M-a

# Go to the end of the sentence.
M-e

# Go to the beginning of the file.
M-<

# Go to the end of the file.
M->
```
 
### Deleting


```
# Remove following word
M-d

# Remove previous word
M-DEL

# Remove from the cursor position to the end of the line
C-k

# Remove from the cursor position to the end of the sentence
M-k

# Select from here to the position where you've moved the cursor. 
C-Space
DEL
```

### Clipboard

Another cool functionality in emacs is that clipboard has history. If having a blank character at the end of the line wasn't not enough for just falling in love with emacs, now you cannot make excuses. The ability to navigate through the history of yanked code turns emacs into exactly what you have dreaming with.

```
# Browse the clipboard to older yanked text. 
M-y
```

### Undo

```
# Three ways to undo an action text related (non cursor position related).
C-/
C-_
C-x u
```

### Buffers

Also, browsing your buffers in emacs is insanely easy. One more reason to love emacs.

The emacs autosaved file has this syntax:

```
#nameOfAutosavedFile;
```

```
# List your buffers.
C-b

# Get rid of the list with all buffers.
C-x 1

# Go to an specific buffer (normally all of them are wrapped up between * *).
C-x b <nameOfBuffer>

# Enter in a minibuffer
M-x

# Get out of a minibuffer (in this case C-g doesn't work).
ESC ESC ESC
```

### File management

```
# Save in bulk. It will ask if you want to save your buffers one by one.
C-x s

# To recover a file:
# Open the non saved file with
emacs nameOfNonSavedFileç
M-x recover-file RETURN
Yes ENTER
```

### Modes

```
# Change to fundamental mode.
M-x fundamental-mode

# Change to text mode.
M-x text-mode

# Activate or deactivate autofill mode.
M-x auto-fill-mode RETURN
```

### Search

```
# Search for an expression forwards.
C-s

# Search for an expression backwards.
C-r
```

### Windows management

Only a few things can compete with the beauty of [i3 windows manager](i3.md), and in my opinion emacs is not as neat and direct as i3, but still, emacs is not exactly a windows management tool but it manages its windows in a quite easy way:

```
# Divide vertically current window in two.
C-x 2

# Divide horizontally current window in two.
C-x 3

# Move cursor position to the other window.
C-x o

# Open a file in a different window below.
C-x 4 C-f nameOfFile

# Create a new and independent window.
M-x make-frame

# Remove/close the window.
M-x delete-frame
```

### Help

```
# Show documentation about a command.
C-h k command

# Describe a command.
C-h x command

# Open available manuals.
C-h i
```
