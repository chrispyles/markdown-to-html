# Markdown to HTML Converter

This is a converter from Markdown to HTML with advanced support for Markdown tables and GFM syntax highlighting. This package relies on `markdown2` for converting basic Markdown to HTML and `pygments` to support code to HTML conversion for syntax highlighting. The default (and, currently, only) theme for this package is Monokai.

You can find a sample of a site generated from this package at [https://mcautograder.chrispyles.io](https://mcautograder.chrispyles.io).

## Installation

The converter is installed using pip:

```
pip install md2html
```

## Changelog

**v1.2:**

* Added YAML syntax highlighting

**v1.1:**

* Added docstrings for documentation
* Moved some utils out of `md2html/converter.py`

**v1.0:**

* Changed to Boostrap CSS

**v0.1:**

* Initial release

### Help

If you have any problems with `md2html`, please open an issue on this projects [Github](https://github.com/chrispyles/markdown-to-html).