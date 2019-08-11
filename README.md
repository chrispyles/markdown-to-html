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
