---
title: Mastering Regular Expressions - Regex
author: amandaguglieri
draft: false
TableOfContents: true
---
# Mastering Regular Expressions - Regex

The implementation system of regex functionality is often called "regular expression engine". Basically a regex engine tries to match the pattern to the given string. There are two main types of regex engines: DFA and NFA, also referred to as text-directed and regex-directed engines. 

![Types of regex engines](img/regex_00.png)
h you can build complex patterns that can match a wide range of combinations.

| Metacharacter | Description                                   |
| ------------- | --------------------------------------------- |
| .             | Any single character                          |
| ^             | Match the beginning of a line                 |
| $             | Match the end of a line                       |
| a\|b          | Match either a or b                           |
| \d            | any digit                                     |
| \D            | Any non-digit character                       |
| \w            | Any word character                            |
| \W            | Any non-word character                        |
| \s            | matches any whitespace character              |
| \S            | Match any non-whitespace character            |
| \b            | Matches a word boundary                       |
| \B            | Match must not occur on a \b boundary.        |
| [\b]          | Backspace character                           |
| \xYY          | Match hex character YY                        |
| \ddd          | Octal character ddd                           |
| `[]`          | Start/close a charaters class                 |
| `()`          | Start/close a characters group                |
| `\`           | Escape special characters                     |
| \|            | It means OR                                   |
| `{}`          | Start/close repetitions of a characters class |

Quantifiers

| Regex Quantifier | Description                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| +                | + indicates that the previous character must occur at least one or more times.                                     |
| ?                | ? indicates that the preceding character is optional. It means the preceding character can occur zero or one time. |
| *                | Matches zero or more of the preceding character.                                                                   |
| {n}              | Matches exactly n occurrences of the preceding character.                                                          |
| {n,}             | Matches n or more occurrences of the preceding character.                                                          |
| {n,m}            | Matches between n and m occurrences of the preceding element                                                       |

The followings are common examples of character classes:

- `[abc]` - matches any one character that is either 'a', 'b', or 'c'.
- `[a-z]` - matches any one lowercase letter from 'a' to 'z'.
- `[A-Z]` - matches any one upper case letter from 'A' to 'Z'.
- `[0-9]` - matches any one digit from '0' to '9'. Optionaly, use \d metacharacter.
- `[^abc]` - matches any one character that is not 'a', 'b', or 'c'.
- `[\w]` - matches any one-word character, including letters, digits, and underscore.
- `[\s]` - matches any whitespace character, including space, tab, and newline.
- `[^a-z]` - matches any one character that is not a lowercase letter from 'a' to 'z'.

In regex, any subpattern enclosed within the parentheses () is considered a group. For example, `(xyz)` creates a group that matches the exact sequence "xyz".



| Non-printing character | Description                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| \0                     | NULL Byte. In many programming language marks the end of a string                                      |
| \b                     | Within a character class represent the backspace character, while outside `\b` matches a word boundary |
| \t                     | Tab key.                                                                                               |
| \n                     | New line                                                                                               |
| \v                     | Vertical tabulation                                                                                    |
| \f                     | Form feed                                                                                              |
| \r                     | In HTTP the `\r\n` sequence is used as the end-of-line marker                                          |
| \e                     | Escape character                                                                                       |


### Unicode

Regular expression flavors that work with Unicode use specific meta-sequences to match code points:

```
# `\u`+code-point 

code-point is the hexadecimal number of the character to match 
`\u2603`

# `\x`{code-point} in the PCRE library in Apache and PHP
{code-point} is the hexadecimal number of the character to match 
`\x{2603}`

```

