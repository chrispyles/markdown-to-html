# Usage

This package an executable that can be run from the command line:

```
md2html ...
```

Here is the help entry for this package:

```
usage: md2html [-h] [-s SITE] [-n NAV] ...

convert Markdown to HTML

positional arguments:
  files                 files to be converted to HTML

optional arguments:
  -h, --help            show this help message and exit
  -s SITE, --site-info SITE
                        add metadata to the HTML files
  -n NAV, --nav NAV     add a YAML file to use for navigation menu
```

Running the converter will place HTML files in the same directory as your Markdown files, with the `.md` extension replaced with `.html`. The HTML files come with CSS in a `style` tag in the `head`.

## Page Metadata

If you would like to add metadata to your page, including a navigation menu, do so by creating a YAML file containing this metadata and passing the file path to the `-s` flag, e.g.

```
md2html -s meta.yml ...
```

The structure of your YAML file should be:

```yaml
title: page title
author: page author
description: page description
navigation:
  nav_title: navigation menu title
  links:
    - title: link name
      url: HTML file path
    - title: ...
      url: ...
    ...
```

Currently, the `title` must be set if you use this option. The converter does not yet support navigation submenus, so all links will be rendered as

* [Link 1]()
* [Link 2]()
* [Link 3]()
* etc.

## Navigation Menu

The converter also supports adding only a navigation menu without page metadata. To do this, pass a YAML file to the `-n` flag. It should have the following structure:

```yaml
nav_title: navigation menu title
links:
  - title: link name
    url: HTML file path
  - title: ...
    url: ...
  ...
```