# Docs

**_function_ `converter.add_in_head(html)`**


Substitues head_regex for new head metadata

Args:

* `html` (`str`): Original HTML

Returns:

* `str`. HTML with new head element



**_function_ `converter.sub_in_html(html_template, html)`**


Substitutes an empty `<div></div>` in template for the converted HTML

Args:

* `html_template` (`str`): The template HTML
* `html` (`html`): New HTML to go inside the `div` tags

Returns:

* `str`. Substituted HTML



**_function_ `converter.add_in_nav_html(html)`**


Adds in navigation menu

Args:

* `html` (`str`): Original HTML into which navbar should be placed

Returns:

* `str`. The HTML with navbar added



**_function_ `converter.add_code_class(markdown)`**


Uses pygments to add syntax highlighting to code

Args:

* `markdown` (`str`): Markdown text

Returns:

* `str`. Markdown with block code substituted for HTML with pygments syntax highlighting



**_function_ `converter.replace_table(table)`**


Generates HTML tables from MD tables

Args:

* `table` (`str`): Markdown table

Returns:

* `str`. Table in HTML format



**_function_ `meta.create_meta(path)`**


Creates HTML metadata from information in YAML file located at PATH

Args:

* `path` (`str`): path to a YAML metadata file

Returns:

* `str`. The HTML head



**_function_ `meta.create_nav(path=None, meta=None)`**


Creates HTML navbar from YAML metadata at PATH or from existing dict META

Args:

* `path = None` (`str`): Location of nav YAML file
* `meta = None` (`dict`): Dictionary of site metadata with navigation info

Returns:

* `str`. The HTML nav element



---

**_class_ `pygments_style.Colors`**


Colors for Monokai color scheme



---

**_class_ `pygments_style.Monokai(Style)`**


Monokai theme for pygments



---

**_function_ `syntax_highlighting.get_syntax(code)`**


Gets the code syntax from Markdown code

Args:

* `code` (`str`): Markdown block code

Returns:

* `str`. The name of the language



**_function_ `syntax_highlighting.get_lexer(syntax)`**


Returns the pygments lexer for the specified language SYNTAX

Args:

* `syntax` (`str`): The language name

Returns:

* `pygments.RegexLexer`. The pygments lexer subclass for that language



**_function_ `syntax_highlighting.run_lexer(code)`**


Runs the lexer on the code in the Markdown, stripping out all backticks

Args:

* `code` (`str`): Markdown block code

Returns:

* `str`. HTML formatted code from pygments lexer


