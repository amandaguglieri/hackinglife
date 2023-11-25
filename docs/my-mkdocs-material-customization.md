---
title: My mkdocs Material theme Customization
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



## Content tabs

Source: [https://squidfunk.github.io/mkdocs-material/reference/content-tabs/](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)

In mkdocs.yml:

```
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true 
```


Code in the document:

```
=== "Left"
	Content
  
=== "Center"
	Content
  
=== "Right"
	Content
```


How it is seen:

=== "Left"
	Content
  
=== "Center"
	Content
  
=== "Right"
	Content

## Data tables

Source: [https://squidfunk.github.io/mkdocs-material/reference/data-tables/#customization](https://squidfunk.github.io/mkdocs-material/reference/data-tables/#customization)

In mkdocs.yml:

```
 extra_javascript:
      - https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js
      - javascripts/tablesort.js
```

After applying the customization, data tables can be sorted by clicking on a
column-. This is code in the document

``` markdown title="Data table, columns sortable"
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | Fetch resource  |
| `PUT`       | Update resource |
| `DELETE`    | Delete resource |
```

This is how it is seen:

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | Fetch resource  |
| `PUT`       | Update resource |
| `DELETE`    | Delete resource |


## PDF button in every page

Most of the existing plugins offer a print-all-in-one-file solution, which is not my intended development.


#### mkdocs-pdf-export-plugin

[https://github.com/zhaoterryy/mkdocs-pdf-export-plugin](https://github.com/zhaoterryy/mkdocs-pdf-export-plugin)

Install and add to gh-deploy workflow:

```bash
pip install mkdocs-pdf-export-plugin
```


mkdocs.yml

```yaml
plugins:
    - search
    - pdf-export:
        verbose: true
        combined: false
        media_type: print
        enabled_if_env: ENABLE_PDF_EXPORT
```


/docs/css/extra.css

```css
@page {
    size: a4 portrait;
    margin: 25mm 10mm 25mm 10mm;
    counter-increment: page;
    font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
    white-space: pre;
    color: grey;
    @top-left {
        content: '© 2018 My Company';
    }
    @top-center {
        content: string(chapter);
    }
    @top-right {
        content: 'Page ' counter(page);
    }
}
```



## Resolving relative link issues when rendering

[https://octoprint.github.io/mkdocs-site-urls/](https://octoprint.github.io/mkdocs-site-urls/)


## Revision date


Install and add to gh-deploy workflow:

```bash
# Installs git revision date plugin globally
pip install mkdocs-git-revision-date-plugin
```


mkdocs.yml

```yaml
# Adding the git revision date plugin
plugins:
- search
- git-revision-date
```


