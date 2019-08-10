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

code_css = HtmlFormatter().get_style_defs("")

html_template = """
<!DOCTYPE html>
<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=Poppins:400,400i,600,700|Roboto:400,400i,700&display=swap" rel="stylesheet">
	<style type="text/css">

		h1, h2, h3, h4, h5, h6 {{
			font-family: 'Roboto', sans-serif;
			font-weight: 600;
		}}

		h1, h2 {{
			letter-spacing: 1px;
		}}

		h1 {{
			font-size: 30pt;
		}}

		h2 {{
			font-size: 20pt;
		}}

		h3 {{
			font-size: 14pt;
		}}

		p, ul, th, td {{
			font-family: 'Roboto', sans-serif;
			font-size: 12pt;
		}}

		th, td {{
			border-top: 1px solid black;
			border-left: 1px solid black;
			text-align: center;
			padding: 5px 2px;
		}}

		th {{
			font-weight: 600;
		}}

		div {{
			width: 65%;
			margin: 0 auto;
		}}

		table {{
			width: 75%;
			margin: 0 auto;
			border-right: 1px solid black;
			border-bottom: 1px solid black;
			border-spacing: 0;
			table-layout: fixed;
		}}

		p.code {{
			width: 95%;
			margin: 10px auto;
			padding: 10px;
			background-color: rgba(222, 222, 222, 0.5);
		}}

		nav {{
			position: fixed;
			width: 30%;
			padding-left: 5px;
		}}

		/* Resize div for Pygments. */
		div.highlight {{
			font-size: 12pt;
			width: 95%;
			margin: 10px auto;
			padding: 10px;
			background-color: rgba(222, 222, 222, 0.5);
		}}

		pre {{
			margin: 0;
		}}

		/* Below is imported the style from Pygments. */

		{}

	</style>
</head>
<body><div>
</div></body>
</html>
""".format(code_css)

# create CLI argument parser and extract arguments
parser = argparse.ArgumentParser(description="convert Markdown to HTML")
parser.add_argument("-s", "--site-info", dest="site", help="add metadata to the HTML files")
parser.add_argument("-n", "--nav", dest="nav", help="add a YAML file to use for navigation menu")
parser.add_argument(dest="files", nargs=argparse.REMAINDER, help="files to be converted to HTML")
namespace = vars(parser.parse_args())

# determine whether or not navigation menu & metadata need to be added
has_nav = "nav" in namespace or "site" in namespace
has_meta = "site" in namespace

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

	nav_html = "<body><nav>\n<h3>" + nav["nav_title"] + "</h3>\n<ul>\n"

	for link in nav["links"]:
		nav_html += "<li><a href=\"" + link["url"] + "\">" + link["title"] + "</a></li>\n"

	nav_html += "</nav><div>\n"

# define regexes for replacing MD and adding sections
div_regex = r"\<div\>\n\<\/div\>"
table_regex = r"\<p\>\|(.*\|)+\n\|(\-+\|)+\n(\|.*\|\n)*\|.*\|\<\/p\>"
code_regex = r"\<p\>\<code\>(.*\n)*?\<\/code\>\<\/p\>"
head_regex = r"\<head\>\n\t\<link"

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
	return re.sub(r"\<body\>\<div\>", nav_html, html)

def add_code_class(html):
	"""
	Adds HTML class "code" to all block code paragraphs
	"""
	code = re.search(code_regex, html)[0]
	new_code = code[10:-11]
	new_code = highlight(new_code, PythonLexer(), HtmlFormatter())
	return re.sub(code_regex, new_code, html, count=1)

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

	# * wildcard found
	elif len(sys.argv) == 2 and "*" in sys.argv[1]:
		file_names = glob.glob(sys.argv[1])

	# use the CLI args as filenames
	else:
		file_names = sys.argv[1:]

	# construct the HTML stirng
	for file_name in file_names:
		markdowner = md.Markdown()

		with open(file_name) as f:
			html = "<div>" + markdowner.convert(f.read())

		# replace MD tables with HTML tables
		match = re.search(table_regex, html)
		while match != None:
			html = re.sub(table_regex, replace_table(match[0]), html)
			match = re.search(table_regex, html)

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
			f.write(html_head + html + html_end)

# construct HTML with nav
else:
	# * wildcard
	if len(sys.argv) == 4 and "*" in sys.argv[3]:
		file_names = glob.glob(sys.argv[3])
	else:
		file_names = sys.argv[3:]

	for file_name in file_names:
		markdowner = md.Markdown()

		with open(file_name) as f:
			html = "<div>\n" + markdowner.convert(f.read())

		# replace MD tables with HTML tables
		match = re.search(table_regex, html)
		while match != None:
			html = re.sub(table_regex, replace_table(match[0]), html)
			match = re.search(table_regex, html)

		# change block code to have HTML class "code"
		match = re.search(code_regex, html)
		while match != None:
			html = add_code_class(html)
			match = re.search(code_regex, html)

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