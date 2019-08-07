########################################################
##### Markdown to HTML Converter for Documentation #####
#####                by Chris Pyles                #####
########################################################

import markdown2 as md
import sys
import glob
import re

html_head = """
<!DOCTYPE html>
<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=Poppins:400,400i,600,700|Roboto:400,400i,700&display=swap" rel="stylesheet">
	<style type="text/css">

		h1, h2, h3, h4, h5, h6 {
			font-family: 'Roboto', sans-serif;
			font-weight: 600;
		}

		h1, h2 {
			letter-spacing: 1px;
		}

		h1 {
			font-size: 30pt;
		}

		h2 {
			font-size: 20pt;
		}

		h3 {
			font-size: 14pt;
		}

		p, ul, th, td {
			font-family: 'Roboto', sans-serif;
			font-size: 12pt;
		}

		th, td {
			border-top: 1px solid black;
			border-left: 1px solid black;
			text-align: center;
			padding: 5px 2px;
		}

		th {
			font-weight: 600;
		}

		div {
			width: 65%;
			margin: 0 auto;
		}

		table {
			width: 75%;
			margin: 0 auto;
			border-right: 1px solid black;
			border-bottom: 1px solid black;
			border-spacing: 0;
			table-layout: fixed;
		}

		p.code {
			width: 95%;
			margin: 10px auto;
			padding: 10px;
			background-color: rgb(222, 222, 222);
		}

	</style>
</head>
<body><div>
"""

html_end = """
</div></body>
</html>
"""

table_regex = r"\<p\>\|(.*\|)+\n\|(\-+\|)+\n(\|.*\|\n)*\|.*\|\<\/p\>"
code_regex = r"\<p\>\<code\>"

def add_code_class(code):
	return re.sub(code_regex, """<p class="code"><code>""", code)

def replace_table(table):
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


if len(sys.argv) == 1:
	print("Please enter a filename.")
elif len(sys.argv) == 2 and "*" in sys.argv[1]:
	file_names = glob.glob(sys.argv[1])
else:
	file_names = sys.argv[1:]

	for file_name in file_names:
		markdowner = md.Markdown()

		with open(file_name) as f:
			html = markdowner.convert(f.read())

		match = re.search(table_regex, html)
		while match != None:
			html = re.sub(table_regex, replace_table(match[0]), html)
			match = re.search(table_regex, html)

		match = re.search(code_regex, html)
		while match != None:
			html = add_code_class(html)
			match = re.search(code_regex, html)

		with open(file_name[:-2] + "html", "w+") as f:
			f.write(html_head + html + html_end)