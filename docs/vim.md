---
title: Vim - A text editor
author: amandaguglieri
draft: false
TableOfContents: true
---

# Vim - A text editor

### Open a file

To edit a new file. 

```bash
nvim <file>
```

Open a file in a recovery mode:

```bash
nvim -r <file>
```

### Go to INSERT mode

To enter into edit mode, press Supr twice and start writting

+ a : Cursor after the character.
+ i : Cursor before the character.
+ A : Cursor at the end of the line.
+ I : Cursor at the beginning of the line.


To get out of INSERT mode, press ESC.

### Browsing the file in CURSOR mode

+ 2:  Go to line 2 of the file.
+ gg: Go to line 1 of the file.
+ G : Go to last line.
+ `<n>` G : Go to line n. 
+ 0 : Go to the beginning of line.
+ $ : Go to the end of line.

### Delete (cut) in CURSOR mode

There is no delete in CURSOR mode. What it does is to CUT the content. There is also no need to enter into the INSERT mode to remove some text. You can delete text in the CURSOR mode with these keys:

+ x : Cut character.
+ dd : Cut full line.
+ dw : Cut word.
+ d$ : Cut from the cursor position to the end of line.
+ d`<n>`w : Cut n words from cursor position. For instance, "d3w" cuts three words. 
+ d`<n>`d : Cut n lines from cursor position. For instance, "d4d" cuts four lines.
+ ciw : Cut word no matter cursor position. Also no matter it word was in parathesis or "".
+ yw: Copy word.
+ yy: Copy full line.

**Tip**: We can multiply any command to run multiple times by adding a number before it. For example, '4yw' would copy 4 words instead of one, and so on.


### Select text

To select a content in CURSOR mode you need to change to VISUAL mode. 

+ v : Changes from CURSOR mode to VISUAL mode.
+ V : Changes from CURSOR mode to VISUAL mode AND select the line where the cursor was.

Being in VISUAL mode you can:

+ Select lines with cursor position (Up and Down arrows).
+ w : Select a word.


### Replace in CURSOR mode

+ R : Insert the text you want and it replaces the existing one.

### Copy in CURSOR mode

To copy into the clip:

+ y : Copy selected content into the clip. 

### Paste in CURSOR mode

Everything you delete goes to the clip. To paste in CURSOR mode, press key:

+ p : Paste clip in the next line.
+ P : Paste clip in previous line.

### Insert a line in CURSOR mode

Press these keys:

+ o : Add a line under cursor position.
+ O : Add a line before cursor position.


### Undo and Redo changes in CURSOR mode

You can do and undo changes from CURSOR mode with these keys:

+ u : Undo changes.
+ r : Redo changes.

### Close a file

There were no modifications. Close it without save it:

```bash
# Press Esc key to enter CURSOR mode.
:q
# Hit ENTER
```

There were modifications but you don't want to save it:

```bash
# Press Esc key to enter CURSOR mode.
:q!
# Hit ENTER
```

### Save a file

To save the file and continue editing:

```bash
# Press Esc key to enter CURSOR mode.
:w
# Hit ENTER
```

To save the file and quit the editor:

```bash
# Press Esc key to enter CURSOR mode.
:wq!
# Hit ENTER
```

Also, you can:

```bash
# Press Esc key to enter CURSOR mode.
:x
# Hit ENTER
```

To save the file with a different name:

```bash
# Press ESC key to enter CURSOR mode.
:w <newFileName>
# Hit ENTER
```

### Browsing activities in the editor

Keys g+d: highlight the definition of a variable/function/... in the file.
Keys g+f: takes you to the definition of that variable/function/... in the file, even if it's a different file from the one we have open.
Our browsing activity will pile up in the VIM editor.

To switch between activities:

+ CTRL+o : Go back into the browsing activity.
+ CTRL+i : Go forward.


### Search in CURSOR mode

Search from cursor position with:

+ \expression : Search word expression.
+ n : Go to the next occurrence.
+ N : Go to previous occurrence.
+ ESC : Escape the search.

### Browsing from opening and closing tags

Move the cursor position from a closing parenthesis to the opening one:

+ % : Change position between opening or closing tags () [] " "

### Substitute in CURSOR mode

To change "expresion1" to "expresion2" for the first occurrence:

```bash
# Press ESC key to enter CURSOR mode.
:s/expression1/expression2
```

To change all occurrences of the line:

```bash
# Press ESC key to enter CURSOR mode.
:s/expression1/expression2/g
```

To change all occurrences in the document (not asking one by one):

```bash
# Press ESC key to enter CURSOR mode.
:s%/expression1/expression2/g
```

To change all occurrences in the document asking one by one:

```bash
# Press ESC key to enter CURSOR mode.
:s%/expression1/expression2/gc
```
