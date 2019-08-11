# Markdown to HTML Converter

This is a converter from Markdown to HTML with advanced support for Markdown tables and GFM syntax highlighting. This package relies on `markdown2` for converting basic Markdown to HTML and `pygments` to support code to HTML conversion for syntax highlighting. The default (and, currently, only) theme for this package is Monokai.

You can find a sample of a site generated from this package at [https://mcautograder.cpyles.com](https://mcautograder.cpyles.com).

## Installation

The recommended method for installing this package is to add it as a submodule to the repo containing your Markdown files:

```bash
git submodule add https://github.com/chrispyles/markdown-to-html
```

Then, when running the converter, the only changes to the syntax below would be prepending the folder name to the file path:

```bash
python3 markdown-to-html/converter.py ...
```

## Usage

This package is relies on the executable file `converter.py` and is meant to be run from the command line. Once you're in the directory which contains this file, the command line usage is

```bash
python3 converter.py ...
```

Here is the help entry for this file:

```bash
usage: converter.py [-h] [-s SITE] [-n NAV] ...

convert Markdown to HTML

positional arguments:
  files                 files to be converted to HTML

optional arguments:
  -h, --help            show this help message and exit
  -s SITE, --site-info SITE
                        add metadata to the HTML files
  -n NAV, --nav NAV     add a YAML file to use for navigation menu
```

Running the converter will place HTML files in the same directory as your Markdown files, with the `.md` extension replaced with `.html`.

### Page Metadata

If you would like to add metadata to your page, including a navigation menu, do so by creating a YAML file containing this metadata and passing the file path to the `-s` flag, e.g.

```bash
python3 converter.py -s meta.yml ...
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
      url: HTML file url
    - title: ...
      url: ...
    ...
```

Currently, the `title` must be set if you use this option. The converter does not yet support navigation submenus, so all links will be rendered as

* [Link 1]()
* [Link 2]()
* [Link 3]()
* etc.

### Navigation Menu

The converter also supports adding only a navigation menu without page metadata. To do this, pass a YAML file to the `-n` flag. It should have the following structure:

```yaml
nav_title: navigation menu title
links:
  - title: link name
    url: HTML file url
  - title: ...
    url: ...
  ...
```
