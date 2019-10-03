########################################################
##### Markdown to HTML Converter for Documentation #####
#####                by Chris Pyles                #####
########################################################

import markdown2 as md
import sys
# import glob
import re
import argparse
import yaml
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from .pygments_style import Monokai

# import executables from this directory
from .converter_html import *
from .syntax_highlighting import *
from .meta import *

def main(namespace):
	"""
	Converts Markdown to HTML
	"""

	assert namespace["nav"] != None or namespace["site"] != None, "You must define navigation or site metadata."

	has_meta = namespace["site"] != None

	# create HTML segment of metadata
	if has_meta:
		new_head = create_meta(namespace["site"])

	# create HTML segment for navigation menu
	if has_meta:
		nav_html = create_nav(meta = namespace["site"])
	else:
		nav_html = create_nav(path = namespace["nav"])

	# define regexes for replacing MD and adding sections
	div_regex = r"\<div class=\"container\" id=\"body\"\>\n\<\/div\>"
	table_regex = r"\<p\>\|(.*\|)+\n\|(\-+\|)+\n(\|.*\|\n)*\|.*\|\<\/p\>"
	code_regex = r"\<p\>(\<code\>|\`{3})(.*\n)*?(\<\/code\>|\`{3})\<\/p\>"
	head_regex = r"\<head\>\n\t\<!-- \<link"
	# nav_regex = r"\<body\>\<nav"

	# utils for replacing regexes above with new HTML code
	def add_in_head(html):
		"""
		Substitues head_regex for new head metadata

		Args:

		* `html` (`str`): Original HTML

		Returns:

		* `str`. HTML with new head element
		"""
		return re.sub(head_regex, new_head, html)

	def sub_in_html(html_template, html):
		"""
		Substitutes an empty `<div></div>` in template for the converted HTML

		Args:

		* `html_template` (`str`): The template HTML
		* `html` (`html`): New HTML to go inside the `div` tags

		Returns:

		* `str`. Substituted HTML
		"""
		return re.sub(div_regex, html, html_template)

	def add_in_nav_html(html):
		"""
		Adds in navigation menu

		Args:

		* `html` (`str`): Original HTML into which navbar should be placed

		Returns:

		* `str`. The HTML with navbar added
		"""
		return re.sub(r"\<body\>\<div class=\"container\" id=\"body\"\>", nav_html, html)

	def add_code_class(markdown):
		"""
		Uses pygments to add syntax highlighting to code

		Args:

		* `markdown` (`str`): Markdown text

		Returns:

		* `str`. Markdown with block code substituted for HTML with pygments syntax highlighting
		"""
		return run_lexer(markdown)

	def replace_table(table):
		"""
		Generates HTML tables from MD tables

		Args:

		* `table` (`str`): Markdown table

		Returns:

		* `str`. Table in HTML format
		"""
		html = "<table class=\"table\"><tr><th scope=\"col\">"
		table = table[3:-4]
		lines = table.split("\n")
		headers = lines[0][2:-2].split(" | ")
		for h in headers:
		    html += h + "</th><th scope=\"col\">"
		html = html[:-16]
		html += "</tr><tr>"
		for line in lines[2:]:
		    data = line[2:-2].split(" | ")
		    html += "<td>"
		    for d in data:
		        html += d + "</td><td>"
		    html = html[:-4]
		    html += "</tr><tr>"
		html = html[:-4]
		html += "</table>"
		return html

	# # * wildcard
	# if len(sys.argv) == 4 and "*" in sys.argv[3]:
	# 	file_names = glob.glob(sys.argv[3])
	# else:
	file_names = namespace["files"]

	for file_name in file_names:
		markdowner = md.Markdown()

		# get MD contents for syntax highlighting
		with open(file_name) as f:
			file_md = f.read()

		# get HTML for MD code
		code_html = []
		match = re.search(md_code_regex, file_md)
		while match != None:
			code = match[0]
			code = add_code_class(code)
			code_html += [code]
			file_md = re.sub(md_code_regex, "", file_md, count=1)
			match = re.search(md_code_regex, file_md)

		# open the MD file and convert to HTML
		with open(file_name) as f:
			html = "<div class=\"container\" id=\"body\">\n" + markdowner.convert(f.read())

		# replace MD tables with HTML tables
		match = re.search(table_regex, html)
		while match != None:
			html = re.sub(table_regex, replace_table(match[0]), html)
			match = re.search(table_regex, html)

		# add back in the code with syntax highlighting
		for code in code_html:
			html = re.sub(code_regex, code, html, count=1)

		html += "\n</div>"

		# substitute in new HTML
		html = sub_in_html(html_template, html)

		# add in navigation menu
		html = add_in_nav_html(html)

		# add in metadata
		if has_meta:
			html = add_in_head(html)

		# write the HTML file
		with open(file_name[:-2] + "html", "w+") as f:
			f.write(html)