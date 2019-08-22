########################################################
##### Markdown to HTML Converter for Documentation #####
#####                by Chris Pyles                #####
########################################################

import markdown2 as md
import sys
import glob
import re
import argparse
import yaml
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from .pygments_style import Monokai

# import executables from this directory
from .converter_html import *
import syntax_highlighting as sh

# create CLI argument parser and extract arguments
parser = argparse.ArgumentParser(description="convert Markdown to HTML")
parser.add_argument("-s", "--site-info", dest="site", help="add metadata to the HTML files")
parser.add_argument("-n", "--nav", dest="nav", help="add a YAML file to use for navigation menu")
parser.add_argument(dest="files", nargs=argparse.REMAINDER, help="files to be converted to HTML")
namespace = vars(parser.parse_args())

# determine whether or not navigation menu & metadata need to be added
has_nav = namespace["nav"] != None or namespace["site"] != None
has_meta = namespace["site"] != None

# create HTML segment of metadata
if has_meta:
	with open(namespace["site"]) as f:
		meta = yaml.safe_load(f)
	new_head = "<head>\n\t<title>{}</title>\n".format(meta["title"])
	if "description" in meta:
		new_head += "\t<meta name=\"description\" content=\"{}\">\n".format(meta["description"])
	if "author" in meta:
		new_head += "\t<meta name=\"author\" content=\"{}\">\n".format(meta["author"])
	new_head += "\t<link"

# create HTML segment for navigation menu
if has_nav:
	if has_meta:
		nav = meta["navigation"]
	else:
		with open(namespace["nav"]) as f:
			nav = yaml.safe_load(f)

	nav_html = "<body><nav>\n<h3 style=\"padding-left: 20px;\">" + nav["nav_title"] + "</h3>\n<ul class=\"nav\">\n"

	for link in nav["links"]:
		nav_html += "<li class=\"nav\"><a class=\"nav\" href=\"" + link["url"] + "\">" + link["title"] + "</a></li>\n"
		if link["url"] == "index.html":
			home_page_name = link["title"]

	nav_html += "</nav><div id=\"body\">\n"

# define regexes for replacing MD and adding sections
div_regex = r"\<div id=\"body\"\>\n\<\/div\>"
table_regex = r"\<p\>\|(.*\|)+\n\|(\-+\|)+\n(\|.*\|\n)*\|.*\|\<\/p\>"
code_regex = r"\<p\>\<code\>(.*\n)*?\<\/code\>\<\/p\>"
head_regex = r"\<head\>\n\t\<link"
nav_regex = r"\<body\>\<nav\>"

# utils for replacing regexes above with new HTML code
def add_in_head(html):
	"""
	Substitues head_regex for new head metadata
	"""
	return re.sub(head_regex, new_head, html)

def sub_in_html(html_template, html):
	"""
	Substitutes an empty <div></div> in template for the converted HTML
	"""
	return re.sub(div_regex, html, html_template)

def add_in_nav_html(html):
	"""
	Adds in navigation menu
	"""
	return re.sub(r"\<body\>\<div id=\"body\"\>", nav_html, html)

def add_code_class(markdown):
	"""
	Uses pygments to add syntax highlighting to code
	"""
	return sh.run_lexer(markdown)

def replace_table(table):
	"""
	Generates HTML tables from MD tables
	"""
	html = "<table><tr><th>"
	table = table[3:-4]
	lines = table.split("\n")
	headers = lines[0][2:-2].split(" | ")
	for h in headers:
	    html += h + "</th><th>"
	html = html[:-4]
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

# construct the HTML file if no nav
if not has_nav:

	# no CLI args given
	if len(sys.argv) == 1:
		print("Please enter a filename.")
		sys.exit()

	# * wildcard found
	elif len(sys.argv) == 2 and "*" in sys.argv[1]:
		file_names = glob.glob(sys.argv[1])

	# use the CLI args as filenames
	else:
		file_names = sys.argv[1:]

	# construct the HTML stirng
	for file_name in file_names:
		markdowner = md.Markdown()

		# get MD contents for syntax highlighting
		with open(file_name) as f:
			file_md = f.read()

		# get HTML for MD code
		code_html = []
		match = re.search(sh.code_regex, file_md)
		while match != None:
			code = match[0]
			code = add_code_class(code)
			code_html += [code]
			file_md = re.sub(sh.code_regex, "", file_md, count=1)
			match = re.search(sh.code_regex, file_md)

		# open the MD file and convert to HTML
		with open(file_name) as f:
			html = "<div id=\"body\">\n" + markdowner.convert(f.read())

		# replace MD tables with HTML tables
		match = re.search(table_regex, html)
		while match != None:
			html = re.sub(table_regex, replace_table(match[0]), html)
			match = re.search(table_regex, html)

		# add back in the code with syntax highlighting
		for code in code_html:
			html = re.sub(code_regex, code, html, count=1)

		# change block code to have HTML class "code"
		match = re.search(code_regex, html)
		while match != None:
			html = add_code_class(html)
			match = re.search(code_regex, html)

		html += "\n</div>"

		# substitute in new HTML
		html = sub_in_html(html_template, html)

		# write the HTML file
		with open(file_name[:-2] + "html", "w+") as f:
			f.write(html)

# construct HTML with nav
else:
	# * wildcard
	if len(sys.argv) == 4 and "*" in sys.argv[3]:
		file_names = glob.glob(sys.argv[3])
	else:
		file_names = sys.argv[3:]

	for file_name in file_names:
		markdowner = md.Markdown()

		# get MD contents for syntax highlighting
		with open(file_name) as f:
			file_md = f.read()

		# get HTML for MD code
		code_html = []
		match = re.search(sh.code_regex, file_md)
		while match != None:
			code = match[0]
			code = add_code_class(code)
			code_html += [code]
			file_md = re.sub(sh.code_regex, "", file_md, count=1)
			match = re.search(sh.code_regex, file_md)

		# open the MD file and convert to HTML
		with open(file_name) as f:
			html = "<div id=\"body\">\n" + markdowner.convert(f.read())

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

		# add in top div
		for link in nav["links"]:
			if link["url"][:-5] + ".md" == file_name:
				page_title = link["title"]
				page_url = link["url"][:-5]

		try:
			if page_url == "index":
				top_div = f"""<body>
				<div id="top">

				<table id="header"><tr><td style="border: none;">
				<p id="header" style="text-align: left;">
				{home_page_name}
				</p></td><td style="border: none;">
				<p id="header" style="text-align: right; margin-right: 38px; padding-left: 0;">
				{meta["title"]}
				</p></td></tr></table>

				</div>
				<nav>"""
			else:
				top_div = f"""<body>
				<div id="top">

				<table id="header"><tr><td style="border: none;">
				<p id="header" style="text-align: left;">
				<a class="nav" href="index.html">{home_page_name}</a> &nbsp;<span style="font-size: 9pt;">►</span>&nbsp; {page_title}
				</p></td><td style="border: none;">
				<p id="header" style="text-align: right; margin-right: 38px; padding-left: 0;">
				{meta["title"]}
				</p></td></tr></table>

				</div>
				<nav>"""

		except NameError:
			top_div = f"""<body>
			<div id="top"></div>
			<nav>"""

		html = re.sub(nav_regex, top_div, html)

		# write the HTML file
		with open(file_name[:-2] + "html", "w+") as f:
			f.write(html)