---
title: mkdocs Material theme
author: amandaguglieri
draft: false
TableOfContents: true
---

# mkdocs Material theme


## Adminition extension

The following code will be reflected  in the document as the chart below

```
!!! note "title"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod 
    nulla. 

```


!!! note "title"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et  euismod nulla.
    

### Basic syntax

Admonitions follow a simple syntax: a block starts with `!!!`, followed by a single keyword used as a [type qualifier](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types). The content of the block follows on the next line, indented by four spaces

```
!!! <typeofchart> "title"
```

When [Details](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#details) is enabled and an admonition block is started with `???` instead of `!!!`, the admonition is rendered as a collapsible block with a small toggle on the right side.

These are the type qualifier:  [`note`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:note)
[`abstract`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:abstract)
[`info`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:info)
[`tip`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:tip)
[`success`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:success)
[`question`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:question)
[`warning`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:warning)
[`failure`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:failure)
[`danger`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:danger)
[`bug`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:bug)
[`example`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:example)
[`quote`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#type:quote)
